#! /usr/bin/env python
from subprocess import Popen, PIPE, DEVNULL


def run_command(cmd, shell=True, stdout=PIPE):
    return Popen(cmd, shell=shell, stdout=stdout, stderr=DEVNULL).stdout.read().decode("utf-8").strip()
