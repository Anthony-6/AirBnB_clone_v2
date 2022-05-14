#!/usr/bin/python3
''' Fabric script that generates a .tgz archive from the contents of
    the web_static folder '''
from datetime import datetime
from fabric.operations import local, run, put
from fabric.api import env
import os

env.hosts = ['35.237.143.24', '34.73.58.201']


def do_pack():
    '''compress the file '''
    local('mkdir -p versions')
    compress_file = local('tar -cvzf versions/web_static_{}.tgz web_static'
                          .format(datetime.
                                  strftime(datetime.now(), "%Y%m%d%H%M%S")))
    if compress_file.failed is True:
        return None
    return compress_file


def do_deploy(archive_path):
    ''' distribute archive to my webserver '''
    if not os.path.exists(archive_path):
        return False

    file_path = archive_path.split('/')
    filename_no_extention = file_path[1].split('.')
    filename = file_path[1]
    exc = put('versions/{}'.format(filename), '/tmp/{}'.format(filename))
    if exc.failed:
        return False
    exc = run('mkdir -p /data/web_static/releases/{}/'
              .format(filename_no_extention[0]))
    if exc.failed:
        return False
    exc = run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
              .format(filename, filename_no_extention[0]))
    if exc.failed:
        return False
    exc = run('rm /tmp/{}'.format(filename))
    if exc.failed:
        return False
    exc = run('mv /data/web_static/releases/{}'
              '/web_static/* /data/web_static/releases/{}/'
              .format(filename_no_extention[0], filename_no_extention[0]))
    if exc.failed:
        return False
    exc = run('rm -rf /data/web_static/releases/{}/web_static'
              .format(filename_no_extention[0]))
    if exc.failed:
        return False
    exc = run('rm -rf /data/web_static/current')
    if exc.failed:
        return False
    exc = run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
              .format(filename_no_extention[0]))
    if exc.failed:
        return False
    print('New version deployed!')
    return True


def deploy():
    '''script that reates and distributes an archive to a web server'''
    filepath = do_pack()
    if filepath is None:
        return False
    print('test')
    return (do_deploy(filepath))
