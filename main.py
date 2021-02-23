import os
import argparse
from datetime import date, timedelta
from itertools import zip_longest
import math


WEEK_LENGTH = 7
TODAY = date.today()
PARSED_INPUT = []
INPUT_LENGTH = 0
COMMIT_NAME = "cat"


def get_program_arguments():
    parser = argparse.ArgumentParser(description='sampleText')

    parser.add_argument('-input', metavar='i', type=str, help='Name of input file', required=True)

    parser.add_argument('--start', metavar='s', type=str, help='\"min\", \"max\", or the number weeks, starting from present, that []. \n'
                                                               'min - places art as close to the right side (present) as possible\n'
                                                               'max - places art as close to the left side as (1 year ago) as possible\n'
                                                               'custom - int n weeks (counting backwards) representing the leftmost position of the art', default='min')
    # YYYY.MM.DD, MM/DD/YYYY or DD.MM.YYYY
    # Specify top-left position of art, by weeks (0 - 52) default tight fit to left side

    # TODO allow more precision in placement
    parser.add_argument('--height_offset', metavar='h', type=str, help='', default='0')

    return parser.parse_args()

def parse_input(file):
    with open(file) as f:
        for i in range(WEEK_LENGTH):
            row = f.readline()
            if row == '':
                break  # works with empty line because \n is still there
            if len(row) > 54:
                print(list(row[:53]))
                PARSED_INPUT.append(list(row[:53]))
            else:
                print(list(row[:-1]))
                PARSED_INPUT.append(list(row[:-1]))  # exclude \n line ending
    return [list(filter(None, i)) for i in zip_longest(*PARSED_INPUT)]  # transpose 2d array
    # TODO transpose may still be truncating values, testing needed


def get_sunday(n_weeks):
    if n_weeks == 'min':
        n_weeks = len(PARSED_INPUT) - 1  # untested
    if n_weeks == 'max':
        n_weeks = 52
    try:
        n_weeks = int(n_weeks)
        return TODAY - timedelta(TODAY.weekday() + (1 + 7 * n_weeks))  # n = 0 is current week sunday
    except:
        try:
            # TODO convert a date string to date obj
            True
        except:
            raise Exception(f'Date ({args.start}) input formatted incorrectly.')


def send_commits(send_date):
    # traverse through parsed input
    # each list represents a week
    # at end of list, go to next week
    # for each non-whitespace character, git push
    for column in PARSED_INPUT:
        for char in column:
            # allow 2 formats: digit(0-4) and non-digit(whitespace-nonwhitespace)
            if char != ' ' and char != '0':
                try:
                    # TODO current problem: heatmap based on overall contribution
                    # on my heatmap, 1 and 2 commits both show up as smallest contribution
                    for i in range(int(math.pow(2, int(char) - 1))):  # convert 1,2,3,4 to 1,2,4,8
                        git_commit(send_date.strftime('%Y.%m.%d'))
                except:
                    git_commit(send_date.strftime('%Y.%m.%d'))
            send_date += timedelta(1)
        send_date += timedelta(6 - send_date.weekday() % 7)
        # no need to check if its already sunday, only progresses if not sunday


def git_commit(commit_date):
    os.system(f'git commit -m {COMMIT_NAME} --date {commit_date} --allow-empty')
    print(f'{commit_date}')


if __name__ == '__main__':
    args = get_program_arguments()
    PARSED_INPUT = parse_input(args.input)
    # send_commits(get_sunday(args.start))
    # os.system('git pull')
    # os.system('git push origin master --force')
    # print("Finished. Refresh your profile page to see your new creation!")
