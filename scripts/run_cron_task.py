#! /usr/bin/env python

import sys

from list_cron_tasks import get_cron_tasks
from shell_cmds import run_command


def run_cron_task(task):
    tasks = get_cron_tasks()

    if task > len(tasks):
        return ValueError("Choose between tasks {}".format(", ".join(range(len(tasks)))))
    else:
        try:
            cron_task = tasks[task]
            cmd_parts = cron_task.split(" ")[5:]
            cmd = " ".join(cmd_parts)
            print("Running command: {}".format(cmd))
            return run_command(cmd)
        except (Exception, e):
            return e

    return None


def inform_command_execution(cmd_status):
    if cmd_status:
        print("An error occurred: {}".format(cmd_status))
    else:
        print("Command was run successfully!")

if __name__ == "__main__":
    _, task = sys.argv
    cmd_status = run_cron_task(int(task))
    inform_command_execution(cmd_status)
