# Minecraft

### Very crude Minecraft Overviewer installation

Assuming Debian/Ubuntu, and a home directory of `jeremy`, update sources:

    [/etc/apt/sources.list]
    ...
    deb http://overviewer.org/debian ./

Add key for repo

    wget -O - http://overviewer.org/debian/overviewer.gpg.asc | sudo apt-key add -

Update apt and install Minecraft Overviewer

    sudo apt-get update
    sudo apt-get install minecraft-overviewer

Obtain client for textpack

    VERSION=1.9
    wget https://s3.amazonaws.com/Minecraft.Download/versions/${VERSION}/${VERSION}.jar -P ~/.minecraft/versions/${VERSION}/

Create a configuration file for rendering parameters

    [config.txt]
    worlds["Pickle"] = "/home/jeremy/minecraft/mnt/minecraft/world"
    outputdir = "/home/jeremy/minecraft/mcmap"
    texturepath = "/home/jeremy/.minecraft/versions/1.9/1.9.jar"
    renders["normalrender"] = {
        "world": "Pickle",
        "title": "Normal Render",
    }
    renders["smooth-lighting"] = {
        "world": "Pickle",
        "title": "Smooth Lighting, aww yeah",
    }
    renders["cave"] = {
        "world": "Pickle",
        "title": "Caves",
    }
    renders["lighting"] = {
        "world": "Pickle",
        "title": "Lighting",
    }

Start the rendering

    overviewer.py --config=./config.txt
    
If not already installed, install Nginx

    sudo apt-get install nginx
    
Create site confirmation for Minecraft map

    [/etc/nginx/sites-available/mcmap.cnf]
    server {
        root /home/jeremy/minecraft/mcmap;
    
        location / {
        }
    }

Link site configuration to enabled sites and remove default site

    sudo rm /etc/nginx/sites-enabled/default
    sudo ln -s /etc/nginx/sites-available/mcmap.cnf /etc/nginx/sites-enabled/mcmap.cnf
    
Restart Nginx
    
    sudo service nginx reload