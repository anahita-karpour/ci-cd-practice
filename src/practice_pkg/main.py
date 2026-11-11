import os


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def get_api_key():
    return os.environ["API_KEY"]
