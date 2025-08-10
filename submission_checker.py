#!/usr/bin/env python3
import grade_util as gu
import shutil
import os
import stat
import glob
import yaml
import json
import subprocess
import unittest
import logging
from typing import List

from gradescope_utils.autograder_utils.decorators import weight, visibility
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

logging.basicConfig()
LOGGER = logging.getLogger('autograder')
LOGGER.setLevel(logging.INFO)

ZERO_LEADERBOARD = [
    {
        'name': 'Score',
        'value': 0
    }
]

def ZERO_RESULT(msg):
    return {
        'score': 0.0,
        'stdout_visibility': 'hidden',
        'output': msg,
        'leaderboard': ZERO_LEADERBOARD
    }


def BAD_FORMAT(file):
    return ZERO_RESULT('Required file not submitted. Check assignment for correct naming.')
    # return ZERO_RESULT('Required file not submitted: \'{0}\'.'.format(file))


def SUBMISSIONS_EXCEEDED(limit):
    return ZERO_RESULT('Exceeded maximum number of submissions: {}'.format(limit))


def NUM_SUBMISSIONS_INFO(num, limit):
    return ZERO_RESULT('Submission {} out of {}'.format(num, limit))


#  class used in generating unittest TestCase's
class Test(type):

    def __new__(mcs, test, bases, attrs):
        attrs[test.__doc__] = test
        return super(Test, mcs).__new__(mcs, test.__doc__, bases, attrs)


def get_test_dirs() -> List[str]:
    '''
    Returns a list of directory paths, as strings, for each test contained in 'tests' directory
    '''
    return [dr[:-1] for dr in glob.glob(gu.Config.TEST_DIR + '/*/')]


def load_yaml(file: str):
    try:
        with open(file, 'r') as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        return {}


def generate_test(dir_name):
    settings = load_yaml(os.path.join(gu.Config.TEST_DIR, dir_name, 'test.yml'))
    LOGGER.info('Generating test \'{}\''.format(settings.get('name', '')))

    def run_test():
        run_path = os.path.join(gu.Config.TEST_DIR, dir_name, 'run_test')
        os.chmod(run_path, os.stat(run_path).st_mode | stat.S_IEXEC)
        subprocess.check_call(['dos2unix', 'run_test'], cwd=os.path.join(gu.Config.TEST_DIR, dir_name),
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.check_output(['./run_test'], cwd=os.path.join(gu.Config.TEST_DIR, dir_name),
                                stderr=subprocess.STDOUT, timeout=settings.get('timeout', None))

    @weight(settings.get('weight', 1))
    @visibility(settings.get('visibility', 'visible'))
    def wrapper(self):
        show_output = settings.get('show_output', True)
        try:
            run_test()
        except subprocess.CalledProcessError as e:  # test script returned non-zero
            msg = '{}\n\n{}'.format(settings.get('message', ''),
                                    e.output.decode() if show_output else '')
            raise Exception(msg)
        except subprocess.TimeoutExpired as e:
            msg = '{}\n\n{}'.format('Test timed out', e.output.decode() if show_output else '')
            raise Exception(msg)

    wrapper.__doc__ = '{}'.format(settings.get('name', os.path.basename(dir_name)))
    return wrapper


#  Execution begins here
if __name__ == '__main__':

    pending_messages = []
    LOGGER.info('Loading config.yml file')
    config = load_yaml('config.yml')

    limit = config.get('limit_submissions', -1)
    LOGGER.info('Using submission limit: {}'.format(limit))
    if limit is not -1:
        num_submissions = gu.number_submissions() + 1
        if num_submissions > limit:
            LOGGER.info('Submission limit reached. Observed submissions: {}'.format(num_submissions))
            gu.write_result(**SUBMISSIONS_EXCEEDED(limit))
            exit(0)
        else:
            pending_messages.append((NUM_SUBMISSIONS_INFO(num_submissions, limit)))

    for file in config.get('required_files', []):
        LOGGER.info('Attempting to load file: {}'.format(file))
        #  check if required file is submitted
        if not gu.is_submitted(file):
            LOGGER.info('File not submitted: {}'.format(file))
            gu.write_result(**BAD_FORMAT(file))
            exit(0)

    exit(1)
