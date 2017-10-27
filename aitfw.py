#! /usr/bin/python

from config.settings import *
from config import generator as gn
import os
import sys

COMPILE_OPTIONS = [
    '',
    'debug',
]

def compile(option):
    if option not in COMPILE_OPTIONS:
        os.system('echo \"error: not compile option \\\"{op}\\\"\"'.format(op=option))
        return

    with open('./app.cfg', mode='w') as f:
        f.write(gn.generateConfig())
    with open('./Makefile.inc', mode='w') as f:
        f.write(gn.generateMakefile())
    os.chdir('../')
    os.system('make app={app_name}'.format(app_name=APP_NAME))
    os.chdir('{dir_name}'.format(dir_name=APP_NAME))
    if option != 'debug':
        os.remove('./app.cfg')
        os.remove('./Makefile.inc')

def mkdir(dir_name):
    os.system('mkdir {dir_name}'.format(dir_name = dir_name))
    os.system('mkdir {dir_name}/src'.format(dir_name = dir_name))
    os.system('mkdir {dir_name}/include'.format(dir_name = dir_name))

def usage():
    output_str='Usage: aitfw [compile [option]] [mkdir <dir_name>]'
    os.system('echo \"{str}\"'.format(str=output_str))


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 2:
        usage()
    elif sys.argv[1] == 'compile':
        if argc >= 3:
            option = sys.argv[2]
        else:
            option = ''
        compile(option)
    elif sys.argv[1] == 'mkdir' and argc >= 3:
        mkdir(sys.argv[2])
    else :
        usage()
