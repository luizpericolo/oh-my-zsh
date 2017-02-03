#! /usr/bin/env python

import re

from shell_cmds import run_command

def get_cron_tasks():
    tasks = run_command('crontab -l')
    if tasks:
        return tasks.split('\n')
    return []

def list_cron_tasks():
    tasks = get_cron_tasks()
    print_cron_tasks(tasks)


def print_cron_tasks(tasks):
    if tasks:
        print("These are the cron tasks:")
        for i, task in enumerate(tasks):
            print("{} -> {}".format(i, task))
    else:
        print("There are no cron tasks")

if __name__ == "__main__":
    list_cron_tasks()
