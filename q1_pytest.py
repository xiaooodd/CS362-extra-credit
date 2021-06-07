import pytest
import q1

def test1():
    result = q1.sen_rev("sen is tom")
    assert result == "tom is sen"

def test2():
    result = q1.sen_rev("2000 is nosn 2")
    assert result == "2 nosn is 2000"
