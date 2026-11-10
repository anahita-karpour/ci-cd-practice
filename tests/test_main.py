import os

import pytest

from practice_pkg.main import add, get_api_key, subtract


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(5, 3) == 2


@pytest.mark.skipif("API_KEY" not in os.environ, reason="API_KEY is not set")
def test_get_api_key():
    assert get_api_key() != ""
