# Python Fabric

### Use Context Manager to Allow Run To Warn Only

    from fabric.context_managers import settings
    
    with settings(warn_only=True):
        run('some command')