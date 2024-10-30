from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3

root = Tk()
root.title("Text to Speech Converter")
root.geometry("1000x500+200+80")
root.resizable(False, False)
root.configure(bg="orange")

tts = pyttsx3.init()

def speaknow():
    text = t1.get(1.0, END).strip()
    gender = c1.get()
    speed = c2.get()

    if not text:
        print("Please enter some text.")
        return

    voices = tts.getProperty("voices")

    # Set voice based on gender
    if gender == "Male":
        tts.setProperty('voice', voices[0].id)
    else:
        tts.setProperty('voice', voices[1].id)

    # Set speed based on user selection
    if speed == "Fast":
        tts.setProperty('rate', 250)
    elif speed == 'Medium':
        tts.setProperty('rate', 150)
    else:
        tts.setProperty('rate', 60)

    tts.say(text)
    tts.runAndWait()

# GUI Elements
upper_frame = Frame(root, bg="blue", width=1200, height=130)
upper_frame.place(x=0, y=0)

Label(upper_frame, text="Text to Speech Converter", font="TimesNewRoman 40 bold", bg="white").place(x=150, y=20)

t1 = Text(root, font="calibri 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
t1.place(x=30, y=150, width=940, height=180)

c1 = Combobox(root, value=['Male', 'Female'], font="Roboto 12", state='r', width=12)
c1.place(x=340, y=400)
c1.set("Male")

c2 = Combobox(root, value=['Fast', 'Medium', 'Slow'], font="Roboto 12", state='r', width=12)
c2.place(x=540, y=400)
c2.set("Medium")

Label(root, text="Select Voice", font="TimesNewRoman 15 bold", bg="blue", fg="white").place(x=340, y=370)
Label(root, text="Select Speed", font="TimesNewRoman 15 bold", bg="blue", fg="white").place(x=540, y=370)

b1 = Button(root, text="Play", compound=LEFT, bg="white", width=5, height=1, font="10", borderwidth="0.1c", command=speaknow)
b1.place(x=435, y=450)

root.mainloop()
