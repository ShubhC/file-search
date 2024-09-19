from datetime import datetime
import time

def convert_bytes(file_size_bytes):
    """
        converts bytes to MB.... GB... etc
    """
    for x in ['B', 'KB', 'MB', 'GB', 'TB']:
        if file_size_bytes < 1024.0:
            return "%3.1f %s" % (file_size_bytes, x)
        file_size_bytes /= 1024.0

def convert_time_format(time_string):
    # Convert the time string to a struct_time object
    time_struct = time.strptime(time_string, "%a %b %d %H:%M:%S %Y")

    # Convert the struct_time object to a datetime object
    time_datetime = datetime.fromtimestamp(time.mktime(time_struct))

    # Format the datetime object to the desired format
    formatted_time = time_datetime.strftime("%d %b %Y, %I:%M %p")

    return formatted_time
    
