# AIT-Framework

![python-versioin](https://img.shields.io/badge/python-2.7%2C%203.6-blue.svg)
[![ev3rt-version](https://img.shields.io/badge/EV3RT-%CE%B26--1%2C%20%CE%B26--2%2C%20%CE%B26--3%2C%20%CE%B27-brightgreen.svg)](http://dev.toppers.jp/trac_user/ev3pf/wiki/WhatsEV3RT)
[![gcc-arm-version](https://img.shields.io/badge/gcc--arm--none--eabi-5.4--2016q2-yellow.svg)](https://launchpad.net/gcc-arm-embedded)

**AIT-Framework** is a framework for [EV3RT](http://dev.toppers.jp/trac_user/ev3pf/wiki/WhatsEV3RT) projects.<br>
This framework makes easier to add objects, directories, or libraries in your projects.

## Install
Before installing, change directory to workspace in sdk directory of hrp2.

Installation is done cloning from [Github](https://github.com/Yuki-Mori/AIT-Framework):

	$ git clone https://github.com/Yuki-Mori/AIT-Framework.git

If you can `install` option, you can make alias `aitfw`.

	$ sudo ./aitfw.py install

## Usage
In this framework, you usually use `aitfw`(or `./aitfw.py`) command when what you do something.

You can use some options:

* `compile [-d debug]`: compile project for EV3 and be made `app` file at workspace directory. if you use `-d` option, you can leave `app.cfg` and `Makefile.ini` used when compiling.
* `mkdir <directory name>`: be made directory for package and also made `include` and `src` directory in that.
* `uninstall`: uninstall `aitfw` alias.