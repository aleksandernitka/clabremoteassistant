# C-lab Remote Assistant
Small GUI application I have put together based on Tkinter tutorial by [pythontutorial.net](https://www.pythontutorial.net/tkinter/) and Slack integration article by [Preston Rohner](https://www.accadius.com/send-message-slack-python-program/). It's been written to help us ([C-Lab](https://www.clab.pl)) with participants communicating with researcher who is not in the room se we can miniminse direct contact time. The app is capable of sending messages to the slack channel, after proper configuration. 

# How to make it work
1. Set up a [new Slack app](https://api.slack.com/apps?new_app=1) for your workspace, you may need to delete some apps as free version of Slack only allows 10 apps to be installed. 
2. Enable Socket mode; you will be given an url which allows for messages to be posted using a link. 
3. Paste this webhook link into the code. 

# How to make an exe file
Application can be started using `python main.py` from the command line. You may want to have a destop app which can be run with double click and without cmd window open. For that you will need to install two tools; `pip install pyinstaller` and `pip install auto-py-to-exe`. The former tool coverts py to exe and the latter is an user-friendly GUI based wrapper which allows for all functions to be used. Note, that if you want to make a Windows exe file you must run `auto-py-to-exe` on a Windows machine. It is possible to compile to a macOS app, but I have not had the need for such version. 