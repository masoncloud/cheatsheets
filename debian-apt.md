# Debian APT

## Archive Mirror Example

### Install dependencies

    sudo apt-get install apt-mirror apache2

### Example mirror list

    [/etc/apt/mirror.list]
    deb-amd64 http://ftp.us.debian.org/debian jessie main main/debian-installer contrib non-free
    deb-src http://ftp.us.debian.org/debian jessie main contrib non-free
     
    deb http://ftp.us.debian.org/debian jessie-updates main contrib non-free
    deb-src http://ftp.us.debian.org/debian jessie-updates main contrib non-free
     
    deb-amd64 http://ftp.us.debian.org/debian sid main contrib non-free
    deb-src http://ftp.us.debian.org/debian sid main contrib non-free
     
    deb-amd64 http://ftp.us.debian.org/debian stretch main contrib non-free
    deb-src http://ftp.us.debian.org/debian stretch main contrib non-free
     
    deb-amd64 http://ftp.us.debian.org/debian testing main contrib non-free
    deb-src http://ftp.us.debian.org/debian testing main contrib non-free
     
    deb-amd64 http://ftp.us.debian.org/debian stable main contrib non-free
    deb-src http://ftp.us.debian.org/debian stable main contrib non-free
     
    deb-amd64 http://ftp.us.debian.org/debian unstable main contrib non-free
    deb-src http://ftp.us.debian.org/debian unstable main contrib non-free
     
    clean http://ftp.us.debian.org/debian

### Mirror the mirrors 

    sudo apt-mirror /etc/apt/mirror.list

### Make available to default Apache site

    ln -s /var/spool/apt-mirror/mirror/ftp.us.debian.org/debian /var/www/html/debian

### Cron to mirror

    /usr/bin/apt-mirror /etc/apt/mirror.list > /var/spool/apt-mirror/var/cron.log

### Cleaning up data no longer needed 

    /var/spool/apt-mirror/var/clean.sh

### Finally, in /etc/apt/sources.list, add your repo hostname

    deb http://<mirror_hostname>/debian/ jessie main
    deb-src http://<mirror_hostname>/debian/ jessie main
    
    deb http://<mirror_hostname>/debian/ jessie-updates main
    deb-src http://<mirror_hostname>/debian/ jessie-updates main
    
### Determine which package owns a given file

    dpkg-query -S <path/filename>


### Tuts

* http://www.pendrivelinux.com/how-to-set-up-your-own-debian-linux-mirror/
* http://kaivanov.blogspot.com/2013/11/creating-official-debian-mirror-with.html
* https://www.howtoforge.com/local_debian_ubuntu_mirror
