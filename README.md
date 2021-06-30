# C-lab Remote Assistant
Small GUI application I have put together based on tutorials by X and Y. It's been written to help us with participants calling for help or to nitify the team that they have finished while we miniminse the time the experimneter and participants spend together. The app is capable of sending messages to the slack channel, after proper configuration. 

# How to make it work
1. Set up a [new Slack app](https://api.slack.com/apps?new_app=1) for your workspace, you may need to delete some apps as free version of Slack only allows 10 apps to be installed. 
2. Enable Socket mode; you will be given an url which allows for messages to be posted using a link. 
3. Paste this webhook link into the code. 

# How to make an exe file
Application can be started using `python main.py` from the command line. You may want to have a destop app which can be run with double click and without cmd window open. For that you will need to install two tools; `pip install pyinstaller` and `pip install auto-py-to-exe`. The former tool coverts py to exe and the latter is an user-friendly GUI based wrapper which allows for all functions to be used. 