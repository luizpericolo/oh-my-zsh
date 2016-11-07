#! /usr/bin/env python

from shell_cmds import run_command


def get_cron_tasks():
    return run_command("crontab -l").split("\n")


def list_cron_tasks():
    tasks = get_cron_tasks()
    print_cron_tasks(tasks)


def print_cron_tasks(tasks):
    if tasks:
        print("These are the cron tasks:")
        for i, task in enumerate(tasks):
            print("{} -> {}".format(i, task))
    else:
        print("There are not cron tasks")

if __name__ == "__main__":
    list_cron_tasks()
