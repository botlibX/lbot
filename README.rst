NAME

::

   LBOT - the complete


DESCRIPTION


::

    LBOT is a python3 IRC bot intended to be programmable in a
    static, only code, no popen, no user imports and no reading
    modules from a directory, way. 

    LBOT provides a demo bot, it can connect to IRC, fetch and
    display RSS feeds, take todo notes, keep a shopping list
    and log text.


SYNOPSIS


::

    lbot <cmd> [key=val] 
    lbot <cmd> [key==val]
    lbot [-c] [-d] [-v] [-i]


INSTALL


::

    $ pipx install lbot

USAGE


::

    for easy typing use an alias

    $ alias lbot="python3 -m lbot"

    list of commands

    $ lbot cmd
    cmd,err,flt,sts,thr,upt

    start a console

    $ lbot -c
    >

    start additional modules

    $ lbot -c mod=<mod1,mod2>
    >

    list of modules

    $ lbot mod
    bsc,err,flt,irc,log,mod,rss,shp,
    sts,tdo,thr,udp

    to start irc, add mod=irc when
    starting

    $ lbot -ci mod=irc

    to start rss, also add mod=rss
    when starting

    $ lbot -ci mod=irc,rss

    start as daemon

    $ lbot -d mod=irc,rss
    $ 


CONFIGURATION


::

    irc

    $ lbot cfg server=<server>
    $ lbot cfg channel=<channel>
    $ lbot cfg nick=<nick>

    sasl

    $ lbot pwd <nsvnick> <nspass>
    $ lbot cfg password=<frompwd>

    rss

    $ lbot rss <url>
    $ lbot dpl <url> <item1,item2>
    $ lbot rem <url>
    $ lbot nme <url< <name>


COMMANDS

::

    cmd - commands
    cfg - irc configuration
    dlt - remove a user
    dpl - sets display items
    ftc - runs a fetching batch
    fnd - find objects 
    flt - instances registered
    log - log some text
    met - add a user
    mre - displays cached output
    nck - changes nick on irc
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    rss - add a feed
    slg - slogan
    thr - show the running threads


SYSTEMD

::

    replace <user> with the username giving the pipx command.

    [Unit]
    Description=library to program bots
    Requires=network.target
    After=network.target

    [Service]
    DynamicUser=True
    Type=forking
    User=<user>
    Group=<uer>
    PIDFile=lbot.pid
    WorkingDirectory=/home/<user>/.lbot
    ExecStart=/home/<user>/.local/pipx/venvs/lbot/bin/lbot -d mod=irc,rs
    RemainAfterExit=yes

    [Install]
    WantedBy=multi-user.target


FILES

::

    ~/.local/bin/lbot
    ~/.local/pipx/venvs/lbot/


AUTHOR

::

    botlib <botlib@proton.me>


COPYRIGHT

::

    LBOT is placed in the Public Domain.
