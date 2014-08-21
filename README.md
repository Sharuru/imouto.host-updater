imouto.hosts-updater
===================

##Intro
imouto.hosts updater is an easy hosts updater for imouto.hosts published on [projecth.org/sources](https://www.projecth.us/sources) with limited library support based on Python 2.7.8.

##Advantage
Easy to use and easy to customize.

##Usage
+ Clone this repositority to everywhere you like. (for example: under 'etc' folder.)
+ Modify your own hosts record if needed.
+ Run ```python updater.py```
+ Your hosts is **UP-TO-DATE**!

##Am I needed to modify my own hosts record?
imouto.hosts updater will save all the custom hosts record after mark '#+END' before updating and will write it back after using 'a' method. So, if your own hosts record is before '#+END', you should modify it after that mark.

##I don't like imouto.hosts, I want to use other sources published on projecth.org/sources!
Though this updater is simple and almost write for **me** :), you can still choose your own sources on projecth.org/sources. Just change source_id and make a little work in regexp, you can make your own updater!

##Others
For Windows users, updater will flush dns record automatically. And recommend you write a booter such as:
```@echo off```+```python updater.py```saved as .bat and run it at system starts.

For other platforms, I will add auto-flush function later.

For more information, please check it out in [Issue.](https://github.com/Sharuru/imouto.hosts-updater/issuesIssue)

##Latest Version
v0.1.4 Delete hosts
