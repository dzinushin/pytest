import pytest

from app.sample import func


def method_that_throws_Exception():
    raise Exception()


def test_answer():
    assert func(3) == 4


def test_other():
    assert 1 == 1

def test_that_should_throw_exception():
  with pytest.raises(Exception):
    method_that_throws_Exception()