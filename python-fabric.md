# Python Fabric

### Use Context Manager to Allow Run To Warn Only

    from fabric.context_managers import settings
    
    with settings(warn_only=True):
        run('some command')
        
### Run a collection of commands under sudo

    with settings(sudo_user="otheruser"):
        sudo("command 1")
        sudo("command 2")
