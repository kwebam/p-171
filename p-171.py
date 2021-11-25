from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root = Tk()
root.geometry("1000x1000")
#-----------------India-----------------
india_label = Label(root, text = "India")
india_label.place(relx = 0.2, rely = 0.02, anchor = CENTER)
india_image = ImageTk.PhotoImage(Image.open("india (1).jpg"))

india_clock = Label(root)
india_clock["image"] = india_image
india_clock.place(relx = 0.2, rely = 0.20, anchor = CENTER)

india_time = Label(root)
india_time.place(relx = 0.2, rely = 0.65, anchor = CENTER)
#-----------------USA-----------------
usa_label = Label(root, text = "USA")
usa_label.place(relx = 0.7, rely = 0.02, anchor = CENTER)
usa_image = ImageTk.PhotoImage(Image.open("usa (1).jpg"))

usa_clock = Label(root)
usa_clock["image"] = usa_image
usa_clock.place(relx = 0.7, rely = 0.20, anchor = CENTER)

usa_time = Label(root)
usa_time.place(relx = 0.7, rely = 0.65, anchor = CENTER)

class India():
    def times(self):
        home = pytz.timezone('Asia/Kolkata')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        india_time["text"] = "Time of India:" + current_time
        india_time.after(200, self.times)
class USA():
    def times(self):
        home = pytz.timezone('US/Central')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        usa_time["text"] = "Time of USA:" + current_time
        usa_time.after(200, self.times)
        
obj_india = India()
obj_USA = USA()
india_btn = Button(root, text = "Show Time of India", command = obj_india.times)
india_btn.place(relx = 0.2, rely = 0.36, anchor = CENTER)
USA_btn = Button(root, text = "Show Time of USA", command = obj_USA.times)
USA_btn.place(relx = 0.7, rely = 0.40, anchor = CENTER)
#--adding Australia and Japan--
#-----------------Australia-----------------
Australia_label = Label(root, text = "Australia")
Australia_label.place(relx = 0.2, rely = 0.46, anchor = CENTER)
australia_image = ImageTk.PhotoImage(Image.open("australia.jpg"))

Australia_clock = Label(root)
Australia_clock["image"] = australia_image
Australia_clock.place(relx = 0.23, rely = 0.65, anchor = CENTER)

Australia_time = Label(root)
Australia_time.place(relx = 0.25, rely = 0.90, anchor = CENTER)
#-----------------Japan-----------------
Japan_label = Label(root, text = "Japan")
Japan_label.place(relx = 0.7, rely = 0.46, anchor = CENTER)
japan_image = ImageTk.PhotoImage(Image.open("japan (1).jpg"))

Japan_clock = Label(root)
Japan_clock["image"] = japan_image
Japan_clock.place(relx = 0.7, rely = 0.65, anchor = CENTER)

Japan_time = Label(root)
Japan_time.place(relx = 0.7, rely = 0.4, anchor = CENTER)

class Australia():
    def times(self):
        home = pytz.timezone('Australia/ACT')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        india_time["text"] = "Time of Austrailia:" + current_time
        india_time.after(200, self.times)
class Japan():
    def times(self):
        home = pytz.timezone('Japan')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        Japan_time["text"] = "Time of Japan :" + current_time
        Japan_time.after(200, self.times)
        
obj_Australia = Australia()
obj_Japan = Japan()
Australia_btn = Button(root, text = "Show Time of Austrailia", command = obj_Australia.times)
Australia_btn.place(relx = 0.2, rely = 0.85, anchor = CENTER)
Japan_btn = Button(root, text = "Show Time of Japan", command = obj_Japan.times)
Japan_btn.place(relx = 0.7, rely = 0.85, anchor = CENTER)

root.mainloop()