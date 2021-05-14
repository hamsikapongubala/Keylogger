# Keylogger

Keylogging, also referred to as keystroke logger or keyboard capturing, is the act of capturing and recording a user’s keystrokes. This
kind of attack gives attackers the ability to monitor a victim’s keystrokes and therefore, gain access to confidential
information.

We created a lab which will allow you to install a software keylogger onto a victim's machine. These scripts once installed will be able
to track a victim's keystrokes, capture their screen, and record audio input. This information is then deleted off of the victim's
machine and sent to an attacker email account.

## How to run

Please note that the attacker and sender's email is not included in the final.py script. The email should be configured as a low security account in order for the
smtplib to access it. Also the logger is a continuous process which will not end until an interrupt is received.

Installing dependencies
```
$ pip install -r requirements.txt
```
Run logger
```
$ python logger.py
```
Run screen capture
```
$ python screenshots.py
```
Run audio tracker
```
$ python mic.py
```
Remove traces and send information
```
$ python final.py
```
