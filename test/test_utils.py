# coding: utf-8

import os


def get_base_path():
    return os.environ.get('BASE_PATH', 'http://localhost:3000')
