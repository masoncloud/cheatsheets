# CalDAV

## Server Software

Some available projects. 

 * [OwnCloud](https://owncloud.org/) (PHP) [GitHub](https://github.com/owncloud/core)
 * [DAViCal](http://www.davical.org/) (PHP) [GitHub](https://github.com/DAViCal/davical)
 * [Baïkal](http://baikal-server.com/) (PHP, SabreDAV) [GitHub](https://github.com/jeromeschneider/Baikal)
 * [SabreDAV](http://sabre.io/) (PHP) [GitHub](https://github.com/fruux/sabre-dav)

 
### Up and Running on Baikal/Apache in 15 Minutes or so

The below procedure will get a fresh Deb/Ub install up and running as a Baikal CalDAV server. Replace all instances of cal.domain.com with your own hostname. 

1. Get your software
    
        sudo apt-get update
        sudo apt-get install apache2 php5 php5-sqlite sqlite3 unzip
        sudo a2enmod ssl
        sudo a2enmod rewrite
        cd /var/www
        sudo wget http://baikal-server.com/get/baikal-regular-0.2.7.tgz
        sudo tar -xvzf baikal-regular-0.2.7.tgz
        sudo rm baikal-regular-0.2.7.tgz
        sudo mv baikal-regular cal.domain.com
        sudo chown -R www-data:www-data cal.domain.com
        sudo cp /var/www/cal.domain.com/Specific/virtualhosts/baikal.apache2 /etc/apache2/sites-available/cal.domain.com.conf
        sudo sed -i "s/dav.mydomain.com/cal.domain.com/g" /etc/apache2/sites-available/cal.domain.com.conf

2. Setup your certificates. Personally, I'm a fan of the $9 certs at namecheap.com. If you have your own CA, or solution, feel free to skip ahead. 
    1. Generate a CSR.

            sudo mkdir /etc/apache2/ssl
            openssl req -new -newkey rsa:2048 -nodes -keyout /etc/apache2/ssl/cal.domain.com.key -out /etc/apache2/ssl/cal.domain.com.csr
            cat /etc/apache2/ssl/cal.domain.com.csr
    
    2. Use the CSR to obtain a cert. Once you have it, upload it from your local machine.
    
            scp ~/Downloads/cal_domain_com.zip ubuntu@cal.domain.com:/home/ubuntu/cal_domain_com.zip
    
    3. Back on the server, move it in to the SSL dir and unpack it.
    
            sudo mv /home/ubuntu/cal_domain_com.zip /etc/apache2/ssl/
            cd /etc/apache2/ssl/
            sudo unzip cal_domain_com.zip

3. Next we'll create an apache site configure for secure requests. Open up a config file `sudo vi /etc/apache2/sites-available/cal.domain.com-ssl.conf` and place the following in. Be sure to double check cal.domain.com has been replaced with your own domain.
        
        <IfModule mod_ssl.c>
            <VirtualHost _default_:443>
                ServerAdmin webmaster@cal.domain.com
        
                DocumentRoot /var/www/cal.domain.com/html
                ServerName cal.domain.com
        
                    RewriteEngine On
                    RewriteRule /.well-known/carddav /card.php [R,L]
                    RewriteRule /.well-known/caldav /cal.php [R,L]
        
                <Directory "/var/www/cal.domain.com/html">
                    Options None
                    Options +FollowSymlinks
                    AllowOverride All
                </Directory>
        
                ErrorLog ${APACHE_LOG_DIR}/error.log
                CustomLog ${APACHE_LOG_DIR}/access.log combined
        
                SSLEngine on
        
                SSLCertificateFile    /etc/apache2/ssl/cal_domain_com.crt
                SSLCertificateKeyFile /etc/apache2/ssl/cal.domain.com.key
                SSLCACertificateFile  /etc/apache2/ssl/cal_domain_com.ca-bundle
        
                <FilesMatch "\.(cgi|shtml|phtml|php)$">
                        SSLOptions +StdEnvVars
                </FilesMatch>
                <Directory /usr/lib/cgi-bin>
                        SSLOptions +StdEnvVars
                </Directory>
        
                BrowserMatch "MSIE [2-6]" \
                        nokeepalive ssl-unclean-shutdown \
                        downgrade-1.0 force-response-1.0
                BrowserMatch "MSIE [17-9]" ssl-unclean-shutdown
        
            </VirtualHost>
        </IfModule>
        
4. Nice. Next, enable the two sites, restart apache, and tell Baikal you're ready to configure it.

        sudo a2ensite cal.domain.com.conf
        sudo a2ensite cal.domain.com-ssl.conf
        sudo service apache2 restart
        sudo touch /var/www/cal.domain.com/Specific/ENABLE_INSTALL
    
5. All done. Navigate to https://cal.domain.com and complete the remaining few setup questions. The defaults are fine for small setups. 
