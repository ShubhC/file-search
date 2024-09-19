# import the modules
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import psutil
import pickle
from pathlib import Path
from adapter.whoosh_adapter import WhooshAdapter
from search_plugins.search_plugin_instances import SearchPluginRepo
from classifier.classifier_instances import ClassifierRepo
from path_store import PathStore
import subprocess
import os


def restart_server():
    logging.info("Restarting the server...")
    subprocess.Popen(["pkill", "-f", "app.py"])
    subprocess.Popen(["python", "app.py"])


def update_search_plugin_repo(search_plugin_repo):
    with open("search_plugin_repo.pkl", "wb") as f:
        pickle.dump(search_plugin_repo, f)
    restart_server()


def update_index(event, event_type):

    indexing_done_flag = False

    classifier_repo = ClassifierRepo(indexing_done_flag)

    path_store = PathStore(indexing_done_flag)

    whoosh_adapter = WhooshAdapter(path_store, indexing_done_flag)

    search_plugin_repo = SearchPluginRepo(classifier_repo, path_store, whoosh_adapter)
    if event_type == "created":
        whoosh_adapter._update_index([Path(event.src_path)], None)
    elif event_type == "deleted":
        whoosh_adapter._update_index(None, [Path(event.src_path)])
        
    update_search_plugin_repo(search_plugin_repo)


class CustomEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        logging.info(f"Created: {event.src_path}")
        if "RECYCLE.BIN" not in event.src_path:
             update_index(event, "created")

    def on_modified(self, event):
        logging.info(f"Modified: {event.src_path}")

    def on_deleted(self, event):
        logging.info(f"Deleted: {event.src_path}")
        if "RECYCLE.BIN" not in event.src_path:
             update_index(event, "deleted")

    def on_moved(self, event):
        logging.info(f"Moved: {event.src_path}")


if __name__ == "__main__":
    # Set the format for logging info
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Set format for displaying path
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'

    # Initialize Observer
    observer = Observer()

    # Get all drive letters
    drives = [
        disk.device
        for disk in psutil.disk_partitions()
        if not disk.device.startswith("C")
    ]

    # Initialize logging event handler
    event_handler = CustomEventHandler()

    # Schedule observer for each drive
    for drive in drives:
        observer.schedule(event_handler, drive, recursive=True)

    # Start the observer
    observer.start()
    try:
        while True:
            # Set the thread sleep time
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
