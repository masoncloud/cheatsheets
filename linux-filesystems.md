# Linux Filesystems

### Check inode usage per filesystem

    df -i

### Check if directory indexing is enabled (ext3+) (check for presence of dir_index)

    tune2fs -l /dev/xvdb5 |grep features
