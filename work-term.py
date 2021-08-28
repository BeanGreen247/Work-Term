# python3 -m pip install codetiming timer notify-py
# if notification error
# debian
# sudo apt-get install libnotify-bin notification-daemon dbus at-spi2-core python3-tk python3-dev python3
# arch
# sudo pacman -S libnotify notification-daemon dbus at-spi2-core tk python
import tkinter as tk
#from tkinter import *
from tkinter import simpledialog

import time
from threading import Timer
from notifypy import Notify

root = tk.Tk()
root.title("Work-Term")
root.geometry('250x100')

about = tk.Tk()
about.title("About")
about.geometry('500x250')

options = tk.Tk()
options.title("Options")
options.geometry('250x100')

#Creating a universal alarm sound variable that can be accessed by all of the frames
alarmSound = "alarm-sound.wav"

class AboutApp(tk.Frame):
    def __init__(self, master=about):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self, master=about):
        self.label = tk.Label(self)
        self.label.config(font=("Courier", 12))
        self.label["text"] = "Work-Term is a pomodoro timer" + "\ncreated in Python with tkinter." + "\n\nCreated by BeanGreen247." + "\n\nContact info:" + \
            "\nGithub > https://github.com/BeanGreen247" + "\nEmail-1 > mozdrent@gmail.com" + "\nEmail-2 > mozdrent.business@outlook.com" + "\n\nAdditional contributions from Will-Bo: \n Email > awill4me@gmail.com" +"\n\n2021"
        self.label.pack(side="top")


class Options(tk.Frame):
    timernum = 1500
    OGTime = timernum

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_options()
        timernum = 1500
        OGTime = timernum

    def create_options(self, master=options):
        self.label = tk.Label(self)
        self.label.config(font=("Courier,12"))
        self.label["text"] = "Time: " + str(self.getTime()/60)
        self.label.pack(side="top")

        self.plusButton = tk.Button(self)
        self.plusButton["text"] = "+ 1min"
        self.plusButton["command"] = (lambda: self.updateTime(60, master))
        self.plusButton.pack(side="right")

        self.minusButton = tk.Button(self)
        self.minusButton["text"] = "- 1min"
        self.minusButton["command"] = (lambda: self.updateTime(-60, master))
        self.minusButton.pack(side="left")
        
        self.soundButton = tk.Button(self)
        self.soundButton["text"] = "Timer Sound"
        self.soundButton["command"] = (lambda: self.changeSound())
        self.soundButton.pack(side="bottom")

        self.label.pack(side="top")
    
    def updateTime(self, addition, master):
        self.setTime(self.getTime()+addition)
        #print(self.getTime())
        self.label["text"]="Time: " + str(self.getTime()/60)
    
    def setTime(self, time):
        self.timernum = time

    def getTime(self):
        return self.timernum

    def getOGTime(self):
        return self.OGTime

    def changeSound(self):
        global alarmSound 
        alarmSound = simpledialog.askstring("Input", "What is the name of the alarm sound file? Make sure it is in the same directory as work-term.py!",parent=options)

class Application(tk.Frame):
    def __init__(self, optionsPanel, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        # self.options(optionsPanel)
        self.create_widgets(optionsPanel)
    
    def create_widgets(self, optionsPanel, master=None):
        self.label = tk.Label(self)
        self.label.config(font=("Courier", 44))
        self.label["text"] = optionsPanel.getTime()/60
        self.label.pack(side="top")
        
        #print("label created")
        
        self.startbutton = tk.Button(self)
        self.startbutton["text"] = "Start"
        self.startbutton["command"] = (lambda: self.starttimer(optionsPanel))
        self.startbutton.pack(side="left")
        
        #print("button1 created")
        
        self.quit = tk.Button(self, text="Exit", command=self.master.destroy)
        self.quit.pack(side="right")
        #print("button2 created")

    def starttimer(self, optionsPanel, master=None):
        #print("timer started")
        
        actime = 0
        while actime == 0:
            timernum = optionsPanel.getTime()
            # timernum=5
            while timernum != 0:
                timeins = timernum
                timeinmin = int(timernum / 60)
                finaltime = str(str(timeinmin) + ":" + str(timeins % 60))
                root.update()
                self.label["text"] = finaltime
                root.update()
                time.sleep(1)
                timernum = timernum - 1
                self.label["text"] = finaltime
                # print(finaltime)
                root.update()
                if timernum == 0:
                    actime = 1
                    root.update()
                    self.label["text"] = finaltime
                    root.update()
                    self.label["text"] = "00:00"
                    root.update()
                    #print("timer stopped")
                    notification = Notify()
                    notification.title = "Timer is up"
                    notification.message = str(optionsPanel.getOGTime()/60) + " minutes elapsed! Go take a rest. ;)"
                    notification.audio = alarmSound
                    notification.send(block=False)
#	def update(self, master=None):
#		label.config(text=str(finaltime))
#		root.after(1000, update)


#root.after(1000, update)
AboutWindow = AboutApp(master=about)
optionsWindow = Options(master=options)
app = Application(optionsWindow,master=root)
optionsWindow.mainloop()
app.mainloop()
AboutWindow.mainloop()
