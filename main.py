import subprocess
import os
import argparse
from datetime import date, timedelta

WEEKLENGTH = 7
TODAY = date.today()
PARSED_INPUT = []


def get_program_arguments():
    parser = argparse.ArgumentParser(description='sampleText')

    parser.add_argument('-input', metavar='i', type=str, help='Name of input file', required=True)

    parser.add_argument('--start', metavar='s', type=str, help='', default='min')
    # YYYY.MM.DD, MM/DD/YYYY or DD.MM.YYYY
    # Specify top-left position of art, by weeks (0 - 52) default tight fit to right side

    return parser.parse_args()


def parse_input(file):
    with open(file) as f:
        counter = 0
        for row in f:
            if counter < WEEKLENGTH:  # only parse first 7 rows of text file
                counter += 1
                current_row = []
                for letter in row:
                    if letter != '\n':
                        current_row.append(letter)
                PARSED_INPUT.append(current_row)
    return list(map(list, zip(
        *PARSED_INPUT)))  # https://www.geeksforgeeks.org/python-transpose-elements-of-two-dimensional-list/


def get_sunday(n_weeks):
    # TODO
    if n_weeks == 'min':
        n_weeks = len(PARSED_INPUT)
    if n_weeks == 'max':
        n_weeks = 51
    try:
        print(n_weeks)
        return TODAY - timedelta(TODAY.weekday() + (1 + 7 * n_weeks))  # .strftime('%Y.%m.%d')
        # n = 0 is current week sunday
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
                git_push(send_date.strftime('%Y.%m.%d'))
            send_date += timedelta(1)
        send_date += timedelta(6 - send_date.weekday() % 7)  # no need to check if its already sunday, only progresses if not sunday


def git_push(commit_date):
    if os.name == 'posix':
        os.system('touch test')
    elif os.name == 'nt':
        os.system('New-Item test')
    else:
        raise Exception('Could not detect platform information.')

    os.system('git add test')
    os.system(f'git commit -m test --date {commit_date}')
    os.system('git push origin master --force')


if __name__ == '__main__':
    args = get_program_arguments()
    print(args)
    PARSED_INPUT = parse_input(args.input)
    print(PARSED_INPUT)
    send_commits(get_sunday(args.start))
