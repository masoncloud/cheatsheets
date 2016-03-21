# DHCP

## ISC DHCP Server

### Install via apt

    sudo apt-get install isc-dhcp-server

### Specify interface to listen upon

    sudo sed -i 's/INTERFACES=""/INTERFACES="eth0"/' /etc/default/isc-dhcp-server

### Set domain name for dhcp in /etc/dhcp/dhcpd.conf

    option domain-name "sampledomain.com";

### Specify name servers for segment (for now, use public)

    option domain-name-servers 8.8.8.8,4.2.2.2;

### Sample entry in /etc/dhcp/dhcpd.conf

    subnet 192.168.1.0 netmask 255.255.255.0 {
        range 192.168.1.200 192.168.1.250;
        option subnet-mask 255.255.255.0;
        option broadcast-address 192.168.1.255;
        option routers 192.168.1.1;
        option domain-name-servers 8.8.8.8,4.2.2.1
    }

### Fixed entry sample

    host <some hostname> {
        hardware ethernet 00:00:00:a1:b2:c3;
        fixed-address 192.168.1.239;
    }

### To start/stop/restart

    sudo service isc-dhcp-server stop

### Specify default lease time

    default-lease-time 600;
    max-lease-time 7200;

### Make this dhcp server authoritative for the segment /etc/dhcp/dhcpd.conf

    authoritative

### Netboot image example:

Example mac: D0:50:ED:52:95:DE

    host nh-mgmt-pac-1 {
        filename "pxelinux.0";
        server-name "192.168.1.101";
        next-server 192.168.1.101;
        hardware ethernet D0:50:ED:52:95:DE;
        fixed-address 192.168.1.102;
    }
