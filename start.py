#!/usr/bin/python

import sys
import os
import shutil
import subprocess
from subprocess import call


def create_test_dir():
    if os.path.isdir('.test'):
        shutil.rmtree('.test')

    os.makedirs('.test')


def create_template_dir():
    shutil.copytree('.', '.test/template',
                    ignore=lambda directory,
                    contents: ['.test'] if directory == '.' else [])


def create_port_dir(port):
    shutil.copytree('.test/template', '.test/' + str(port))


def custom_port_dir(port):
    with open('.test/' + str(port) + '/.port', 'wt') as f:
        f.write(str(port))


def start_process(port, cmd):
    create_port_dir(port)
    custom_port_dir(port)
    main_cwd = os.getcwd()
    os.chdir(main_cwd + '/.test/' + str(port))
    subprocess.Popen(cmd)
    os.chdir(main_cwd)


def parse_ports():
    pass


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('invlid start, end, cmd!')
        exit(0)
    start, end, cmd = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3:]
    create_test_dir()
    create_template_dir()
    for port in range(start, end):
        start_process(port, cmd)

    cmd_string = ' '.join(cmd)

    pid_cmd = 'ps -eo pid,args | grep "' + cmd_string + '" | grep -v service \
           | grep -v init.d | grep -v grep | cut -c1-6'

    with open('.running_pids', 'w+') as f:
        call(pid_cmd, shell=True, stdout=f)
