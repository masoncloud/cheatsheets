# GNU Screen

### Share a session

    screen -d -m -S shared   # create a named screen session
    screen -x shared  # attachterm

### Create new terminal

    ctrl-a c

### Split Screen #

    ctrl-a, S    # Split horizontally
    ctrl-a, |    # Split vertically
    ctrl-a, tab  # Jump to next region
    ctrl-a, X    # Close current region
    ctrl-a, Q    # Remove all regions except current region
    ctrl-a, "    # Select session to bind to current region
    ctrl-a, n    # Change current region to next session
    ctrl-a, p    # Change current region to previous session
    ctrl-a, 0..9 # Change current region to window by number

### Save entire buffer to file

    ctrl+a : 
    hardcopy -h <filename>
	
### Why is split screen so slow on debian/ubuntu?

No idea, but install from http://savannah.gnu.org/git/?group=screen to resolve

    sudo apt-get install build-essential libtool ncurses-dev
    ./autogen.sh

### Remove screen region when ctrl-a,X doesn't work

    ctrl-a,:remove[enter]

### Upgrade screen on MacOS

    brew install autoconf automake libtool gettext
    git clone https://github.com/FreedomBen/screen-for-OSX.git && cd screen-for-OSX && ./install.sh
    echo 'alias screen="/usr/local/bin/screen"' >> ~/.bash_profile

### Preserve split layout

    echo "layout save default" >> ~/.screenrc