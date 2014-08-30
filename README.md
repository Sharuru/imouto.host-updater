imouto.host-updater
===================

##Intro
imouto.host updater is an easy hosts updater for imouto.host published on [projecth.org/sources](https://www.projecth.us/sources) with limited library support based on Python 2.7.8.

##Advantage
Easy to use and easy to customize.

##Usage
+ Clone this repositority to everywhere you like. (for example: under 'etc' folder.)
+ Backup your own hosts record if needed.
+ Run ```python updater.py```
+ Your hosts is **UP-TO-DATE**!

##Am I needed to backup my own hosts record?
imouto.hosts updater will save all the custom hosts record after mark '#+END' before updating and will write it back after using 'a' method.

**If you are first running this updater, I highly recommend you to backup your hosts at different places though the updater will auto backup and added it after the '#+END' mark.**

##I am a new user and I can not connect to the projecth.us/sources!
Maybe your ISP block that site, you can try adding the following hosts record in your local hosts and try again:
```
#ProjectH START
106.186.31.197	projecth.us
106.186.31.197	www.projecth.us
106.186.31.197	forum.projecth.us
106.186.31.197	repo.projecth.us
#ProjectH END
```

##I don't like imouto.host, I want to use other sources published on projecth.org/sources!
Though this updater is simple and almost write for **me** :), you can still choose your own sources on projecth.org/sources. Just change source_id and make a little work in regexp, you can make your own updater!

##Others
For Windows users, updater will flush dns record automatically. And recommend you write a booter such as:
```@echo off```+```python updater.py```saved as .bat and run it at system starts.

For other platforms, I will add auto-flush function later.

For more information, please check it out in [Issue.](https://github.com/Sharuru/imouto.host-updater/issues)

##Latest Version
v0.1.8 Clean file object
