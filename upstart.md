# Upstart

### Use Upstart to Have an App Start at System Boot

Create an Upstart configuration file for your app:

    vi /etc/init/a-very-fancy-app.conf

Within this file, consider the following template to have the following take place:

 * App launches upon network interface initialization
 * App stops on system shutdown
 * App will respawn if it dies
 * App will run as the 'some_user' user
 * Upstart will change directories into /my/project/directory before executing the app
 * Upstart will start the app with the following command `./bin/python a_very_fancy_app.py`
  
  
    description "My very fancy app"
    
    start on net-device-up
    stop on shutdown
    
    respawn
    
    setuid some_user
    chdir /my/project/directory
    exec ./bin/python a_very_fancy_app.py

The app may now be launched via

    sudo start a-very-fancy-app
