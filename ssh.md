# SSH

## Key Management

### Add an identity to authentication agent

    ssd-add path/to/private_key
    
### Remove an identity from authentication agent

    ssh-add -d path/to/public_key
    
### Remove all identities from authentication agent

    ssh-add -D
    
### Obtain and save public key from an existing private key

    ssh-keygen -y -f path/to/private_key > path/to/private_key.pub
    
### Generating, deploying and using private key for SSH authentication

    # On local system, generate private key and save it into .ssh dir within home directory
    ssh-keygen -f path/to/ssh/dir/new_private_key  # Provide a pass phrase, when prompted, if preferred
    
    # Use ssh-copy-id script to push the **public** key to the remote system. If user does not have a password 
    # or password based logins are disabled, please see section on "Adding user's public key to authorized 
    # keys as another user" below.
    ssh-copy-id -i path/to/ssh/dir/new_private_key.pub someuser@some.remote.host
    
    # Connect using identity 
    ssh -i path/to/ssh/dir/new_private_key someuser@some.remote.host
    
### Adding user's public key to authorized keys as another user

There are a gazillion ways to do this, obviously. Below shows a scriptable example using an admin user with 
sudoer rights. 

    # Parameters
    ADMINUSER=ubuntu
    USERTOADDKEY=someuser
    USERPUBKEY=path/to/users_public_key
    REMOTEHOST=some.remote.host
    
    # If necessary, create .ssh dir for user
    ssh $ADMINUSER@$REMOTEHOST "sudo mkdir /home/$USERTOADDKEY/.ssh"
    
    # Read public key and append to user's authorized_keys file as admin user 
    cat $USERPUBKEY | (ssh $ADMINUSER@$REMOTEHOST "sudo su -c 'cat - >> /home/$USERTOADDKEY/.ssh/authorized_keys'")
    
    # If necessary, set permissions and ownership on .ssh dir and authorized_keys file
    ssh $ADMINUSER@$REMOTEHOST "sudo chown $USERTOADDKEY:$USERTOADDKEY /home/$USERTOADDKEY/.ssh /home/$USERTOADDKEY/.ssh/authorized_keys"
    ssh $ADMINUSER@$REMOTEHOST "sudo chmod 700 /home/$USERTOADDKEY/.ssh"
    ssh $ADMINUSER@$REMOTEHOST "sudo chmod 600 /home/$USERTOADDKEY/.ssh/authorized_keys"

### Bypass host key check

    ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no ubuntu@ip

### OR, add host key first

    ssh-keyscan github.com >> ~/.ssh/known_hosts

### Deal w/ "Too many authentication failures for <username>" (excessive key offerings)
    
    # Add entry ~/.ssh/config
    Host 192.168.54.54
    IdentityFile ~/.ssh/<specific identify file>
    IdentitiesOnly yes
    Port 22
    
### Port forwarding/redirection

    ssh -L <local port>:<remote computer>:<remote port> <user>@<remote ip>
