#! /usr/local/bin/python3

from config.settings import *
from config import generator as gn
import os
import sys

def compile():
    #print('-------------------------')
   # print(APP_CONFIG_HEADER)
    #print(gn.generateConfig())
    #print('-------------------------')
    #print(gn.generateMakefile())
    with open('./app.cfg', mode='w') as f:
        f.write(gn.generateConfig())
    with open('./Makefile.inc', mode='w') as f:
        f.write(gn.generateMakefile())
    os.chdir('../')
    os.system('make app={app_name}'.format(app_name=APP_NAME))
    os.chdir('{dir_name}'.format(dir_name=APP_NAME))
    os.remove('./app.cfg')
    os.remove('./Makefile.inc')

def mkdir(dir_name):
    os.system('mkdir {dir_name}'.format(dir_name = dir_name))
    os.system('mkdir {dir_name}/src'.format(dir_name = dir_name))
    os.system('mkdir {dir_name}/include'.format(dir_name = dir_name))

def usage():
    output_str='Usage: aitfw [compile] [mkdir <dir_name>]'
    os.system('echo \"{str}\"'.format(str=output_str))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    elif sys.argv[1] == 'compile':
        compile()
    elif sys.argv[1] == 'mkdir' and len(sys.argv) >= 3:
        mkdir(sys.argv[2])
    else :
        usage()
