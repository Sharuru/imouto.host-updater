imouto.host-updater
===================

##Intro
imouto.host updater is an easy hosts updater for imouto.host published on [zxdrive/imouto.host](https://github.com/zxdrive/imouto.host) with limited library support based on Python 3.4.1.

##Advantage
Easy to use and easy to customize.

##Usage
+ Clone this repository to everywhere you like. (for example: under 'etc' folder.)
+ Backup your own hosts record if needed.
+ Run ```python updater.py```
+ Your hosts is **UP-TO-DATE**!

##Am I needed to backup my own hosts record?
imouto.host updater will save all the custom hosts record after mark '#+END' before updating and will write it back after using 'a' method.

**If you are first running this updater, I highly recommend you to backup your hosts at different places though the updater will auto backup and added it after the '#+END' mark.**

##Where is projecth.org/sources?
It is sad that projecth.org/sources is too unstable. So for some other reason and this updater is write for me, I remove that support.

##Others
For Windows users, updater will flush dns record automatically and I recommend you write a launcher such as:
```
@echo off
python updater.py
```
Then saved as .bat and run it when system starts.

For other platforms, I will add auto-flush function later.

For more information, please check it out in [Issue.](https://github.com/Sharuru/imouto.host-updater/issues)

##Latest Version
v0.3.1 Fix encoding problem
