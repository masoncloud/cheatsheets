# TFTP

## tftpd-hpa


### Install tftpd-hpa

    sudo apt-get install tftpd-hpa

### Configure to serve in /etc/default/tftpd-hpa on all interfaces

    # /etc/default/tftpd-hpa
    TFTP_USERNAME="tftp"
    TFTP_DIRECTORY="/srv/tftp"
    TFTP_ADDRESS="0.0.0.0:69"
    TFTP_OPTIONS="--secure"

### Restart services, etc

    sudo service tftpd-hpa restart

### Placing boot images, etc:

    cd /srv/tftp
    sudo wget http://ftp.nl.debian.org/debian/dists/jessie/main/installer-amd64/current/images/netboot/netboot.tar.gz
    sudo tar zxf netboot.tar.gz 
    sudo rm netboot.tar.gz
