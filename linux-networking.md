# Linux Networking

## Debian/Ubuntu

### Install VLAN support

    sudo apt-get install vlan
    
### Enable VLAN support

    sudo modprobe 8021q # Run-time
    echo 8021q | sudo tee -a /etc/modules
    
### Temporarily add VLAN

    sudo vconfig add eth0 101
    
### Temporarily set ip on vlan interface

    sudo ifconfig eth0.101 192.168.1.51/24
    
### Perm in /etc/network/interfaces example

    auto eth0.101
    iface eth0.101 inet static
        address ...
