#python3 -m pip install codetiming timer notify-py
# if notification error
# debian
# sudo apt-get install libnotify-bin notification-daemon dbus at-spi2-core python3-tk python3-dev python3
# arch
# sudo pacman -S libnotify notification-daemon dbus at-spi2-core tk python
import tkinter as tk
#from tkinter import *
import time
from threading import Timer
from notifypy import Notify

root = tk.Tk()
root.title("Work-Term")
root.geometry('250x100')
about = tk.Tk()
about.title("About")
about.geometry('500x250')

class AboutApp(tk.Frame):
	def __init__(self, master=about):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()
	
	def create_widgets(self, master=about):
		self.label = tk.Label(self)
		self.label.config(font=("Courier", 12))
		self.label["text"] = "Work-Term is a pomodoro timer" + "\ncreated in Python with tkinter." + "\n\nCreated by BeanGreen247." + "\n\nContact info:" + "\nGithub > https://github.com/BeanGreen247" + "\nEmail-1 > mozdrent@gmail.com" + "\nEmail-2 > mozdrent.business@outlook.com" + "\n\n2021"
		self.label.pack(side="top")	

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

	def create_widgets(self, master=None):
		self.label = tk.Label(self)
		self.label.config(font=("Courier", 44))
		self.label["text"] = "25:00"
		self.label.pack(side="top")

		self.startbutton = tk.Button(self)
		self.startbutton["text"] = "Start"
		self.startbutton["command"] = self.starttimer
		self.startbutton.pack(side="left")

		self.quit = tk.Button(self, text="Exit", command=self.master.destroy)
		self.quit.pack(side="right")

	def starttimer(self, master=None):
		#print("timer started")
		actime=0
		while actime == 0 :
			timernum=1500
			#timernum=5
			while timernum !=0:
				timeins=timernum
				timeinmin=int(timernum/60)
				finaltime=str(str(timeinmin)+":"+str(timeins%60))
				root.update()
				self.label["text"]=finaltime
				root.update()
				time.sleep(1)
				timernum=timernum-1
				self.label["text"]=finaltime
				#print(finaltime)
				root.update()
				if timernum == 0:
					actime=1
					root.update()
					self.label["text"]=finaltime
					root.update()
					self.label["text"]="00:00"
					root.update()
					#print("timer stopped")
					notification = Notify()
					notification.title = "Timer is up"
					notification.message = "25 minutes elapsed! Go take a rest. ;)"
					notification.audio = "alarm-sound.wav"					
					notification.send(block=False)
#	def update(self, master=None):
#		label.config(text=str(finaltime))
#		root.after(1000, update)

#root.after(1000, update)
AboutWindow = AboutApp(master=about)
app = Application(master=root)
app.mainloop()
AboutWindow.mainloop()