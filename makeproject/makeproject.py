#!/usr/bin/python

from __future__ import division, print_function

import argparse
import os
import errno
import shutil

class CommandError(Exception):
    pass

def run():
    parser = argparse.ArgumentParser(description='Create project template for kaggle competition.')
    parser.add_argument('name', type=str,
                        help='name of the project, use . to create in current directory')
    parser.add_argument('--template', type=str,
                        help='type of the template',
                        choices=['kaggle'],
                        default='kaggle')

    args = parser.parse_args()
    name = args.name
    template = args.template

    if name == '.':
        top_dir = os.getcwd()
    else:
        top_dir = os.path.join(os.getcwd(), name)
        try:
            os.makedirs(top_dir)
        except OSError as e:
            if e.errno == errno.EEXIST:
                message = "'%s' already exists" % top_dir
            else:
                message = e
            raise CommandError(message)

    template_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates', template)
    # print(list(os.listdir(template_dir)))
    prefix_length = len(template_dir) + 1
    # print(template_dir, prefix_length)

    for root, dirs, files in os.walk(template_dir):
        # print(root, dirs, files)
        path_inside = root[prefix_length:]

        current_dir = os.path.join(top_dir, path_inside)

        for dirname in dirs:
            new_dir = os.path.join(top_dir, dirname)
            os.mkdir(new_dir)
            # print('os.mkdir({})'.format(new_dir))

        for filename in files:
            if os.path.splitext(filename)[1] in {'.pyc', '.pyo'}:
                continue
            old_file = os.path.join(root, filename)
            new_file = os.path.join(current_dir, filename)
            shutil.copy2(old_file, new_file)
            # print('shutil.copy2({}, {})'.format(old_file, new_file))

if __name__ == '__main__':
    run()



