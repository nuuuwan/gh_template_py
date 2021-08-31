"""Uploaded data to nuuuwan/gh_template_py:data branch."""

import os


def upload_data():
    """Upload data."""
    os.system('echo "test data" > /tmp/gh_template_py.test.txt')
    os.system('echo "# gh_template_py" > /tmp/README.md')


if __name__ == '__main__':
    upload_data()
