#!/usr/bin/python3
''' comment line '''
from fabric.operations import local
from datetime import datetime


def do_pack():
    local('mkdir -p versions')
    compress_file = local('tar -cvzf versions/web_static_{}.tgz web_static'
                          .format(datetime.
                                  strftime(datetime.now(), "%Y%m%d%H%M%S")))
    if compress_file.failed is True:
        return None
    else:
        return compress_file
