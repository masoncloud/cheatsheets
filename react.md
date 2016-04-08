# React

### Comment out line or block

    {/*  content */}

### Why isn't my map propagating a function?

If you do something like this:

    var nodes = this.props.data.map(function(item) {
        return (
            <Item key={item.key} onAction={this.handleAction} />
        );
    });

`this.props.onAction` on the child `Item` node will be undefined. This is because `this` isn't defined in the map function scope. Map accepts a second argument for passing `this` in:

    var nodes = this.props.data.map(function(item) {
        return (
            <Item key={item.key} onAction={this.handleAction} />
        );
    }, this);

