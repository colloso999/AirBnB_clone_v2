#!/usr/bin/python3
"""
Compress web static package
"""
from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['100.25.161.158', '52.72.9.18']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """
    Deploy web files to server
    """
    try:
        if not (path.exists(archive_path)):
            return False

        # upload archive
        put(archive_path, '/tmp/')
        print("Uploaded `archive_path` to `/tmp/`.")

        # create target dir
        archive_timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\
                releases/web_static_{}/'.format(archive_timestamp))

        # uncompress archive and delete .tgz
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
                /data/web_static/releases/web_static_{}'\
                .format(archive_timestamp, archive_timestamp))
        print("Extracted archive `/tmp/web_static_{}.tgz` to \
                `/data/web_static/releases/web_static_{}/`."\
                .format(archive_timestamp, archive_timestamp))

        # remove archive
        run('sudo rm /tmp/web_static_{}.tgz'.format(archive_timestamp))

        # move contents into host web_static
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
                /data/web_static/releases/web_static_{}'\
                .format(archive_timestamp))

        # remove extraneous web_static dir
        run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'\
                .format(archive_timestamp))

        # delete pre-existing sym link
        run('sudo rm -rf /data/web_static/current')

        # re-establish symbolic link
        run('sudo ln -s /data/web_static/releases/\
                web_static_{}/ /data/web_static/current'.\
                format(archive_timestamp))
    except Exception as e:
        print(e)
        return False

    # return True on success
    return True
