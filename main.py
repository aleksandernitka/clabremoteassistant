import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
from urllib import request, parse
import json

# thanks to 
# https://www.pythontutorial.net/tkinter/
# https://www.accadius.com/send-message-slack-python-program/

# SECRET - DO NOT SHARE
whook = "URL_FROM_SLACK_API"
locations = [" ", "Lab1", "Lab2", "Lab3"]
#

### Functions

def quitask():
    answer = askyesno(title='Confirmation',
                    message='Are you sure that you want to quit?')
    if answer:
        root.destroy()


def sendtoslack_help():
    message = 'Help ss'
    post = {"text": "{0}".format(message)}
    try:
        json_data = json.dumps(post)
        req = request.Request(whook,
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = request.urlopen(req)
        
        # Fedback
        showinfo(title='Info', message = 'The Team has been notified. Informacja zostala przeslana do zespolu.')

    except Exception as em:
        print("EXCEPTION: " + str(em))
        showerror(title='Error', message = 'An error has occurred, please seek experimenter. Wysapil blad, prosze poszukac badajacego.')


# root window
root = tk.Tk()
root.geometry("300x300")
root.title('C-Lab Remote Assistant')
root.resizable(0, 0)
#icon = tk.PhotoImage(file = 'icon2.png')
#root.iconphoto(False, icon)


# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=5)

### Elements

# pp id
pp_label = ttk.Label(root, text="Participant ID:")
pp_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
pp_entry = ttk.Entry(root)
pp_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# exp id
exp_label = ttk.Label(root, text="Experimenter:")
exp_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
exp_entry = ttk.Entry(root)
exp_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# room id
var_lab = tk.StringVar()
var_lab.set(locations[0])
lab_label = ttk.Label(root, text="Lab:")
lab_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
lab_entry = ttk.OptionMenu(root, var_lab, *locations)
lab_entry.config(width = 16)
lab_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

### HELP

# Help fn


def send2slack(msg):

    post = {"text": msg}
    try:
        json_data = json.dumps(post)
        req = request.Request(whook,
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = request.urlopen(req)
        
        # Fedback
        showinfo(title='Info', message = 'The Team has been notified. Informacja zostala przeslana do zespolu.')

    except Exception as em:
        print("EXCEPTION: " + str(em))
        showerror(title='Error', message = 'An error has occurred, please seek experimenter. Wysapil blad, prosze poszukac badajacego.')

# Help button
help_button = ttk.Button(root, text="Help", command = lambda: send2slack('For {0}: pp {1} in lab {2} requires HELP.'.format(exp_entry.get(), pp_entry.get(), var_lab.get())))
help_button.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=5)


### PROBLEM

# Problem button
prob_button = ttk.Button(root, text="Problem", command = lambda: send2slack('For {0}: pp {1} in lab {2} has a PROBLEM.'.format(exp_entry.get(), pp_entry.get(), var_lab.get())))
prob_button.grid(column=1, row=4, sticky=tk.EW, padx=5, pady=5)


### FINISHED

# Finished button
fini_button = ttk.Button(root, text="Finished", command = lambda: send2slack('For {0}: pp {1} in lab {2} has FINISHED.'.format(exp_entry.get(), pp_entry.get(), var_lab.get())))
fini_button.grid(column=1, row=5, sticky=tk.EW, padx=5, pady=5)


### QUIT

# Quit button
quit_button = ttk.Button(root, text="Quit", command = quitask)
quit_button.grid(column=1, row=6, sticky=tk.EW, padx=5, pady=5)


root.mainloop()