import subprocess
import os
import argparse
from datetime import date, timedelta
from itertools import zip_longest

WEEK_LENGTH = 7
TODAY = date.today()
PARSED_INPUT = []
COMMIT_FILE_NAME = "art"


def get_program_arguments():
    parser = argparse.ArgumentParser(description='sampleText')

    parser.add_argument('-input', metavar='i', type=str, help='Name of input file', required=True)

    parser.add_argument('--start', metavar='s', type=str, help='', default='min')
    # YYYY.MM.DD, MM/DD/YYYY or DD.MM.YYYY
    # Specify top-left position of art, by weeks (0 - 52) default tight fit to left side
    # TODO allow more precision in placement
    return parser.parse_args()


def parse_input(file):
    with open(file) as f:
        counter = 0
        for row in f:
            if counter < WEEK_LENGTH:
                counter += 1
                PARSED_INPUT.append(list(row[:-1]))  # exclude \n line ending
                # TODO max of 53 char
    return [list(filter(None, i)) for i in zip_longest(*PARSED_INPUT)]


def get_sunday(n_weeks):
    if n_weeks == 'min':
        n_weeks = len(PARSED_INPUT) - 1  # untested
    if n_weeks == 'max':
        n_weeks = 52
    try:
        n_weeks = int(n_weeks)
        return TODAY - timedelta(TODAY.weekday() + (1 + 7 * n_weeks))  # n = 0 is current week sunday
    except:
        raise Exception(f"Date ({args.start}) input formatted incorrectly.")


def send_commits(send_date):
    # traverse through parsed input
    # each list represents a week
    # at end of list, go to next week
    # for each non-whitespace character, git push
    for column in PARSED_INPUT:
        for char in column:
            if char != ' ':
                # print(send_date.strftime('%Y.%m.%d'))
                git_commit(send_date.strftime('%Y.%m.%d'))
            send_date += timedelta(1)
        send_date += timedelta(6 - send_date.weekday() % 7)
        # no need to check if its already sunday, only progresses if not sunday


def initalize():
    if os.name == 'posix':
        os.system(f'touch {COMMIT_FILE_NAME}')
    elif os.name == 'nt':
        inp = input("Windows platform detected. Are you using cmd or powershell? Press 1 for cmd or 2 for powershell:")
        if inp == "1":
            os.system(f'NUL>{COMMIT_FILE_NAME}')
        elif inp == "2":
            os.system(f'New-Item -path \"./\" -type file -name \"{COMMIT_FILE_NAME}\"')
        else:
            raise Exception('Invalid number entered.')
    else:
        raise Exception('Could not detect platform information.')


def git_commit(commit_date):
    # os.system(f'git add {COMMIT_FILE_NAME}')
    os.system(f'git commit -m {COMMIT_FILE_NAME} --date {commit_date} --allow-empty')


if __name__ == '__main__':
    args = get_program_arguments()
    # initalize() -- creating a file not necessary if git allows empty commits
    PARSED_INPUT = parse_input(args.input)
    send_commits(get_sunday(args.start))
    os.system('git pull')
    os.system('git push origin master --force')
