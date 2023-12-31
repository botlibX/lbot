#!/usr/bin/env python3
# This file is placed in the Public Domain.
#
# pylint: disable=C0412,C0115,C0116,W0212,R0903,C0207,C0413,W0611
# pylint: disable=C0411,E0402,E0611


"runtime"


import os
import readline
import sys
import termios
import time
import traceback


sys.path.insert(0, os.getcwd())


from lbot.methods import parse
from lbot.runtime import Cfg, Client, Errors, Event, command, output, scan
from lbot.storage import Storage
from lbot.utility import mods


import lbot.modules as modules
import lbot.runtime


Storage.workdir = os.path.expanduser(f"~/.lbot")


lbot.runtime.output = print


class CLI(Client):

    def announce(self, txt):
        pass

    def raw(self, txt):
        print(txt)
        sys.stdout.flush()


class Console(CLI):

    def dispatch(self, evt):
        parse(evt)
        command(evt)
        evt.wait()

    def poll(self) -> Event:
        return self.event(input("> "))


def daemon():
    pid = os.fork()
    if pid != 0:
        os._exit(0)
    os.setsid()
    os.umask(0)
    with open('/dev/null', 'r', encoding="utf-8") as sis:
        os.dup2(sis.fileno(), sys.stdin.fileno())
    with open('/dev/null', 'a+', encoding="utf-8") as sos:
        os.dup2(sos.fileno(), sys.stdout.fileno())
    with open('/dev/null', 'a+', encoding="utf-8") as ses:
        os.dup2(ses.fileno(), sys.stderr.fileno())


def wrap(func) -> None:
    old = None
    try:
        old = termios.tcgetattr(sys.stdin.fileno())
    except termios.error:
        pass
    try:
        func()
    except (EOFError, KeyboardInterrupt):
        print("")
        sys.stdout.flush()
    finally:
        if old:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old)
    Errors.show()


def main():
    parse(Cfg, " ".join(sys.argv[1:]))
    if "a" not in Cfg.opts:
        Cfg.mod = ",".join(modules.__dir__())
    if "d" in Cfg.opts:
        daemon()
    if "d" in Cfg.opts:
        cli = CLI()
        scan(modules, Cfg.mod, True)
        cli.forever()
    elif "c" in Cfg.opts:
        if 'v' in Cfg.opts:
            dtime = time.ctime(time.time()).replace("  ", " ")
            print(f"LBOT started at {dtime} {Cfg.opts.upper()} {Cfg.mod.upper()}")
        scan(modules, Cfg.mod, "i" in Cfg.opts, True)
        csl = Console()
        csl.start()
        csl.forever()
    else:
        cli = CLI()
        scan(modules, Cfg.mod)
        evt = cli.event(Cfg.otxt)
        parse(evt)
        command(evt)
        evt.wait()


if __name__ == "__main__":
    wrap(main)
