def convert_bytes(file_size_bytes):
    """
        converts bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if file_size_bytes < 1024.0:
            return "%3.1f %s" % (file_size_bytes, x)
        file_size_bytes /= 1024.0
    
