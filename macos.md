# MacOS

### Open URL with default browser from the command line

    open https://google.com

### Force child folders/files in a MacOS Windows file share to inherit parent permissions

    # If a rule for the user or group doesn't already exist, file_inherit,directory_inherit being the deviation from default
    sudo chmod +a "user:someuser user:sharedude allow list,add_file,search,add_subdirectory,delete_child,readattr,writeattr,readextattr,writeextattr,readsecurity,file_inherit,directory_inherit" /path/to/share
