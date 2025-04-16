import pytest
from lazyllm.common.queue import sqlite3_check_threadsafety


def test_sqlite3_check_threadsafety():
    """
    测试sqlite3_check_threadsafety函数
    """
    assert sqlite3_check_threadsafety() is True
