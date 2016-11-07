#! /usr/bin/env python

from subprocess import Popen, PIPE

def run_command(cmd, shell=True, stdout=PIPE):
    return Popen(cmd, shell=shell, stdout=stdout).stdout.read().decode("utf-8").strip()
