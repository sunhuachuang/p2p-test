#!/usr/bin/python

import re
from subprocess import call

num_reg = re.compile(r'\d+')

with open('.running_pids', 'r+') as f:
    pids = f.readlines()
    for pid_string in pids:
        pid_list = num_reg.findall(pid_string)
        if pid_list:
            call('kill ' + pid_list[0], shell=True)
