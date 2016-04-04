# Nginx

## Installation

### Installing Nginx on Ubuntu/Debian via APT Package

    sudo apt-get install nginx

### Installating on MacOS

    brew install nginx
    # Configuration in /usr/local/etc/nginx/nginx.conf
    
## Configuration

### Create Site Configuration Which Proxies to Local Webserver

Create a configuration file for your site. For example:

    sudo vi /etc/nginx/sites-available/app.domain.com
    
Within this file, consider the following template which listens on port 80 for requests matching server name "app.domain.com" and proxies them on to a local webserver listening on port 8000.

    server {
        listen 80;
        server_name app.domain.com;
        
        location / {
            proxy_pass http://localhost:8000;
        }
    }

Finally, make this an enabled configuration by linking from the available configuration and reload Nginx

    sudo ln -s /etc/nginx/sites-available/app.domain.com /etc/nginx/sites-enabled/app.domain.com
    sudo service nginx reload
    
### Creating a Location Within a Site Which Serves Static Content

Within an existing `server` stanza, you may add a location which aliases to a local directory for Nginx to serve static files from. Consider the following example:

    server {
        ...
        
        location /static {
            alias /path/to/static/content;
        }
        
        ...
    }

### Configure Nginx to Connect Via Unix Domain Sockets

Instead of having Nginx pass things along via TCP, you may use a Unix domain socket to (possibly) achieve better performance via inter-process communications. Another potential advantage is if you have multiple backend services running, using Unix domain sockets will remove the need to juggle backend ports.  Within a given server location stanza, declare these additional parameters. You will also need to have your backend service bind to the same file descriptor (example: unix:/tmp/app.domain.com.socket).

    server {
        ...
        
        location / {
            proxy_set_header Host $host;
            proxy_pass http://unix:/tmp/app.domain.com.socket;
        }
        
        ...
    }

### Default Log Location on Ubuntu/Debian

Unless declared explicitly within a site configuration, Nginx will log to the following files:

 * access_log `/var/log/nginx/access.log`
 * error_log `/var/log/nginx/error.log`
 
These settings may be changed in `/etc/nginx/nginx.conf` or overridden within your specific server configuration files as the example below shows:

     server {
        ...
        
        access_log /var/log/nginx/mysite.domain.com.access.log
        error_log /var/log/nginx/mysite.domain.com.error.log
        
        ...
     }

### Verify Current Nginx Configuration is Valid

    sudo nginx -t

## Usage

### Starting Nginx Web Server

    sudo service nginx start
    
### Reload Nginx Configuration

    sudo service nginx reload
    


    
