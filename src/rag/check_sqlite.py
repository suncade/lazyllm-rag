from lazyllm.common.queue import sqlite3_check_threadsafety

"""
如果结果为False,则你需要先重装sqlite,使之⽀持多线程。
以macbook为例
$ brew update
$ brew install sqlite
$ which sqlite3
/opt/homebrew/opt/sqlite/bin/sqlite3
如果结果不是homebrew下的sqlite,则你需要设置如下环境变量,并重装python
$ brew uninstall python@3.10
$ export PATH="/opt/homebrew/opt/sqlite/bin:$PATH"
$ export LDFLAGS="-L/opt/homebrew/opt/sqlite/lib"
$ export CPPFLAGS="-I/opt/homebrew/opt/sqlite/include”
$ brew install python@3.10
"""
print(sqlite3_check_threadsafety())
