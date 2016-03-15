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
    from observer import JSObserver
    worlds["Pickle"] = "/home/jeremy/minecraft/mnt/minecraft/world"
    outputdir = "/home/jeremy/minecraft/mcmap"
    texturepath = "/home/jeremy/.minecraft/versions/1.9/1.9.jar"
    observer = JSObserver(outputdir)
    
    renders["pickle_day"] = {
        "world": "Pickle",
        "title": "Normal Day",
        "rendermode": lighting,
        "dimension": "overworld",
    }
    renders["pickle_night"] = {
        "world": "Pickle",
        "title": "Normal Night",
        "rendermode": night,
        "dimension": "overworld",
    }
    
    # Day
    renders["pickle_day_smooth_south"] = {
        "world": "Pickle",
        "title": "Smooth Day South",
        "rendermode": smooth_lighting,
        "northdirection" : "lower-right",
        "dimension": "overworld",
    }
    renders["pickle_day_smooth_north"] = {
        "world": "Pickle",
        "title": "Smooth Day North",
        "rendermode": smooth_lighting,
        "northdirection" : "upper-left",
        "dimension": "overworld",
    }
    renders["pickle_day_smooth_east"] = {
        "world": "Pickle",
        "title": "Smooth Day East",
        "rendermode": smooth_lighting,
        "northdirection" : "lower-left",
        "dimension": "overworld",
    }
    renders["pickle_day_smooth_west"] = {
        "world": "Pickle",
        "title": "Smooth Day West",
        "rendermode": smooth_lighting,
        "northdirection" : "upper-right",
        "dimension": "overworld",
    }
    
    # Night
    renders["pickle_night_smooth_south"] = {
        "world": "Pickle",
        "title": "Smooth Night South",
        "rendermode": smooth_night,
        "northdirection" : "lower-right",
        "dimension": "overworld",
    }
    renders["pickle_night_smooth_north"] = {
        "world": "Pickle",
        "title": "Smooth Night North",
        "rendermode": smooth_night,
        "northdirection" : "upper-left",
        "dimension": "overworld",
    }
    renders["pickle_night_smooth_east"] = {
        "world": "Pickle",
        "title": "Smooth Night East",
        "rendermode": smooth_night,
        "northdirection" : "lower-left",
        "dimension": "overworld",
    }
    renders["pickle_night_smooth_west"] = {
        "world": "Pickle",
        "title": "Smooth Night West",
        "rendermode": smooth_night,
        "northdirection" : "upper-right",
        "dimension": "overworld",
    }
        
    # Caves
    renders["pickle_cave_south"] = {
        "world": "Pickle",
        "title": "Cave South",
        "rendermode": cave,
        "northdirection" : "lower-right",
        "dimension": "overworld",
    }
    renders["pickle_cave_north"] = {
        "world": "Pickle",
        "title": "Cave North",
        "rendermode": cave,
        "northdirection" : "upper-left",
        "dimension": "overworld",
    }
    renders["pickle_cave_east"] = {
        "world": "Pickle",
        "title": "Cave East",
        "rendermode": cave,
        "northdirection" : "lower-left",
        "dimension": "overworld",
    }
    renders["pickle_cave_west"] = {
        "world": "Pickle",
        "title": "Cave West",
        "rendermode": cave,
        "northdirection" : "upper-right",
        "dimension": "overworld",
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