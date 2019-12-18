#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@author zhangbohan.dell@gmail.com
@function:
@create 12/12/2019 5:28 PM
"""

import json
import os
import typing


class Swagger:

    def __init__(self, file) -> None:
        super().__init__()
        self._file = file

    @property
    def file(self) -> typing.AnyStr:
        return self._file

    @file.setter
    def file(self, file) -> None:
        self._file = file

    def dispose(self)-> typing.AnyStr:
        file = os.curdir + self._file
        with open(file, encoding='utf8', mode='r') as f:
            load = json.load(f)
            return load


if __name__ == '__main__':
    swagger = Swagger("/resource/api-docs.json")
    print(swagger.dispose())