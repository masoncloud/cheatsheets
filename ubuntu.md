# Ubuntu

## User Administration

### Adding a new user, granting sudo, and setting password

    NEWUSER=someuser
    sudo useradd -m -s /bin/bash $NEWUSER
    sudo usermod -a -G sudo $NEWUSER
    sudo passwd $NEWUSER

### Allow group to run sudo without providing password

Open up sudoers configuration via `sudo visudo`. For a given group, consider the following directive which uses the `admin` group as an example:

    %admin  ALL=(ALL) NOPASSWD:ALL


## System

### Determine number of processors/cores/sockets on a system

Keep in mind:

 * **CPU**    The logical CPU number of a CPU as used by the Linux kernel.
 * **CORE**   The logical core number. A core can contain several CPUs.
 * **SOCKET** The logical socket number. A socket can contain several cores.
 
        # Pick your poison
        nproc
        lscpu
        cat /proc/cpuinfo
        getconf _NPROCESSORS_ONLN
        
### Determine release version

    lsb_release -a

