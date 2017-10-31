#! /usr/bin/python

from config.settings import *
from config import generator as gn
import os
import sys

COMPILE_OPTIONS = [
    '',
    '-d',
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
    install_str='usage: ./aitfw.py install'
    uninstall_str='usage: aitfw uninstall'
    compile_str='usage: aitfw compile [-d debug]'
    mkdir_str='usage: aitfw mkdir <directory name>'
    os.system('echo \"{str}\"'.format(str=install_str))
    os.system('echo \"{str}\"'.format(str=uninstall_str))
    os.system('echo \"{str}\"'.format(str=compile_str))
    os.system('echo \"{str}\"'.format(str=mkdir_str))

def install():
    os.system('echo \"alias aitfw=\'./aitfw.py\'\" >> ~/.bash_profile')
    os.system('source ~/.bash_profile')

def uninstall():
    os.system('sed -i -e  \"/aitfw.py/d\" ~/.bash_profile')
    os.system('source ~/.bash_profile')

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
    elif sys.argv[1] == 'install':
        install()
    elif sys.argv[1] == 'uninstall':
        uninstall()
    else :
        usage()
