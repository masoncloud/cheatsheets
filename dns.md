# DNS

## BIND

### Install BIND9

    sudo apt-get install bind9

### Set forwarders for Internet name resolution in /etc/bind/named.conf.options

    options {
        directory "/var/cache/bind/";
        forwarders {
            8.8.8.8;
            4.2.2.1;
        };
        dnssec-validation auto;
            auth-nxdomain no;    # conform to RFC1035
            listen-on-v6 { any; };
    };

### Make bind aware of zone file

    [/etc/bind/named.conf.local]
    
    zone "sampledomain.com" {
        type master;
        file "/var/lib/bind/db.sampledomain.com";
    };
    zone "0.55.168.192.in-addr.arpa" {
        type master;
        file "/var/lib/binb/db.sampledomain.com.inv";
    };

### Sample zone file

    $TTL    3600
    @       IN      SOA     ns1.sampledomain.com. dns.sampledomain.com. (
                    2015070501              ; Serial
                    3600                    ; Refresh
                    600                     ; Retry
                    86400                   ; Expire
                    600 )                   ; Negative Cache TTL
    ;
    @       IN      NS      ns1.sampledomain.com.
    ns1		IN	    A	    192.168.55.102
    host1   IN      A       192.168.55.101
    prv1            IN      CNAME   host1
    prv2            IN      CNAME   host.at.other.domain.

### Sample reverse zone file
 
    $TTL    3600
    @       IN      SOA     ns1.sampledomain.com. dns.sampledomain.com. (
                    201507050  1            ; Serial
                    3600                    ; Refresh
                    600                     ; Retry
                    86400                   ; Expire
                    600 )                   ; Negative Cache TTL
    ;
    @       IN      NS      ns1.sampledomain.com.
    101     IN      PTR     host1

### Testing examples

(sudo apt-get install dnsutils)

    # Lookup CNAME record for name at specific resolver
    dig -t CNAME ns1.sampledomain.com @8.8.8.8
