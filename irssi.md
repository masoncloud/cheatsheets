# Irssi

### Page up/down mac (may need shift)

    fn + Up/Down

### Cycle windows

    ctrl+p, ctrl+n

### Initial setup w/ example server configuration

    vi ~/.irssi/config

Example conf:

    [config]
    servers = (
        {
            address = "irc.zimage.com";
            chatnet = "zimage";
            port = "6697";
            use_ssl = "yes";
            ssl_verify = "no";
            autoconnect = "yes";
        }
    );
    
    chatnets = {
        zimage = {
            type = "IRC";
        };
    };
    
    channels = (
        { name = "#linux"; chatnet = "zimage"; autojoin = "Yes"; }
        { name = "#tech"; chatnet = "zimage"; autojoin = "Yes"; }
    );
    
    settings = {
        core = { real_name = "real_name"; user_name = "user_name"; nick = "nick"; };
        "fe-text" = { actlist_sort = "refnum"; term_force_colors = "yes"; scrollback_time = "7day"; };
        "fe-common/core" = { theme = "default"; };
    };

### Bare install, connecting to host without configuration

    irssi -n <nick_name>
    /SET user_name <user_name>
    /SET real_name <real_name>
    /connect irc.hackint.org 9999
    /join #defconctf 

### Adding a server w/ specific cert path

    /server add -auto -ssl -ssl_verify -ssl_capath /etc/ssl/certs -network zimage irc.zimage.com 6697

### Disable SSL verify

    /server add -auto -ssl -ssl_capath /etc/ssl/certs -network zimage irc1.zimage.com 6697
