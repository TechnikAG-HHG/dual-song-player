from time import *
from tkinter import *
from tkinter import filedialog
import vlc
import threading


#Init
global Path1
global Path2
global pause1
global pause2

Path1 = ""
Path2 = ""
pause1 = 0
pause2 = 0


#window################################################################################
root = Tk()
root.config(bg="gray")
root.title("Song-Player")  # gui window title
root.geometry("1920x1080")   # Size of gui


#Label
title = Label(root, text="Song-Player", bg="Black", fg="white", font=("Arial", 40), width=50, height=1)

title.grid(row=0, column=0, columnspan=2)


#Player 1################################################################################
#Buttons
btnPlay1 = Button(root, text="Play", command=lambda : Player1(), state=NORMAL, bg="black", fg="white", font=("Arial", 40), width=25)
btnPause1 = Button(root, text="Pause", command=lambda : Player1pause(), state=DISABLED, bg="black", fg="white", font=("Arial", 40), width=25)
btnStop1 = Button(root, text="Stop", command=lambda : Player1stop(), state=DISABLED, bg="black", fg="white", font=("Arial", 40), width=25)
btnSelect1 = Button(root, text="Select File", command=lambda : btnSelectFileClicked1(), state=NORMAL, bg="black", fg="white", font=("Arial", 40), width=25)

btnPlay1.grid(row=2, column=0)
btnPause1.grid(row=3, column=0)
btnStop1.grid(row=4, column=0)
btnSelect1.grid(row=8, column=0)


#Labels
loadedfile1 = Label(root, text="Loaded File: " + Path1, bg="Black", fg="white", font=("Arial", 20), width=48, height=1)
title1 = Label(root, text="Player 1", bg="Black", fg="white", font=("Arial", 40), width=25, height=1)

loadedfile1.grid(row=7, column=0)
title1.grid(row=1, column=0)


#VLC configuration
vlc_obj1 = vlc.Instance()
music1 = vlc_obj1.media_player_new()
vlcmedia1 = vlc_obj1.media_new(Path1)
music1.set_media(vlcmedia1)


#Functions
def Player1off():
    btnPlay1["state"] = NORMAL
    btnStop1["state"] = DISABLED
    btnPause1["state"] = DISABLED


def Player1on():
    btnPlay1["state"] = DISABLED
    btnStop1["state"] = NORMAL
    btnPause1["state"] = NORMAL


def Player1():
    music1.play()
    Player1on()
    global pause1
    pause1 = 0
    

def Player1pause():
    music1.set_pause(1)
    Player1off()
    global pause1
    pause1 = 1


def Player1stop():
    vlcmedia1 = vlc_obj1.media_new(Path1)
    music1.set_media(vlcmedia1)
    Player1off()


def btnSelectFileClicked1():
    global pause1
    global loadedfile1
    global Path1
    global music1

    Path1 = filedialog.askopenfilename(initialdir = "",
                                          title = "Select a File",
                                          filetypes = (("Audio Files", "*.mp3*"),
                                                       ("all files", "*.*")))
    

    loadedfile1.config(text="Loaded File: " + Path1)

    vlcmedia1 = vlc_obj1.media_new(Path1)
    music1.set_media(vlcmedia1)
    
    pause1 = 1


def set_volume1(value1):
    volume1 = int(value1)
    music1.audio_set_volume(volume1)


def setposition1(position1):
    if refresh1 == 0:
        music1.set_position(int(position1)/100)
        bar1.set(position1)
        sleep(0.025)


def status1(bar1, music1):
    while True:
        if pause1 == 0:
            global refresh1
            refresh1 = 1
            position1 = music1.get_position()
            position1b = position1*100
            bar1.set(position1b)
            if music1.is_playing() == False:
                Player1stop()
            sleep(0.05)
            refresh1 = 0


#Sliders
volume1b = Scale(root, from_ = 0, to = 100, orient=HORIZONTAL, command = set_volume1, bg="black", fg="white", font=("Arial", 40), width=25, activebackground="gray", length=775, label="Volume Control")
bar1 = Scale(root, from_ = 0, to = 100, orient=HORIZONTAL, command=setposition1, bg="black", fg="white", font=("Arial", 40), width=25, activebackground="gray", length=775, label="Progress Bar")

volume1b.grid(row=5, column=0)
bar1.grid(row=6, column=0)


#Threads
t1 = threading.Thread(target=status1, args=(bar1, music1)).start()


#Init 2
volume1b.set(70)
music1.audio_set_volume(70)



#Player 2######################################################################################
#Buttons
btnPlay2 = Button(root, text="Play", command=lambda : Player2(), state=NORMAL, bg="black", fg="white", font=("Arial", 40), width=25)
btnPause2 = Button(root, text="Pause", command=lambda : Player2pause(), state=DISABLED, bg="black", fg="white", font=("Arial", 40), width=25)
btnStop2 = Button(root, text="Stop", command=lambda : Player2stop(), state=DISABLED, bg="black", fg="white", font=("Arial", 40), width=25)
btnSelect2 = Button(root, text="Select File", command=lambda : btnSelectFileClicked2(), state=NORMAL, bg="black", fg="white", font=("Arial", 40), width=25)

btnPlay2.grid(row=2, column=1)
btnPause2.grid(row=3, column=1)
btnStop2.grid(row=4, column=1)
btnSelect2.grid(row=8, column=1)


#Labels
loadedfile2 = Label(root, text="Loaded File: " + Path2, bg="Black", fg="white", font=("Arial", 20), width=48, height=1)
title2 = Label(root, text="Player 2", bg="Black", fg="white", font=("Arial", 40), width=25, height=1)

loadedfile2.grid(row=7, column=1)
title2.grid(row=1, column=1)


#VLC configuration
vlc_obj2 = vlc.Instance()
music2 = vlc_obj2.media_player_new()
vlcmedia2 = vlc_obj2.media_new(Path2)
music2.set_media(vlcmedia2)


#Functions
def Player2off():
    btnPlay2["state"] = NORMAL
    btnStop2["state"] = DISABLED
    btnPause2["state"] = DISABLED


def Player2on():
    btnPlay2["state"] = DISABLED
    btnStop2["state"] = NORMAL
    btnPause2["state"] = NORMAL


def Player2():
    try:
        music2.play()
    except:
        music2.play()
    Player2on()
    global pause2
    pause2 = 0
    

def Player2pause():
    music2.set_pause(1)
    Player2off()
    global pause2
    pause2 = 1


def Player2stop():
    vlcmedia2 = vlc_obj2.media_new(Path2)
    music2.set_media(vlcmedia2)
    Player2off()


def btnSelectFileClicked2():
    global pause2
    global loadedfile2
    global Path2
    global music2

    Path2 = filedialog.askopenfilename(initialdir = "",
                                          title = "Select a File",
                                          filetypes = (("Audio Files", "*.mp3*"),
                                                       ("all files", "*.*")))
    

    loadedfile2.config(text="Loaded File: " + Path2)

    vlcmedia2 = vlc_obj2.media_new(Path2)
    music2.set_media(vlcmedia2)
    
    pause2 = 1


def set_volume2(value2):
    volume2 = int(value2)
    music2.audio_set_volume(volume2)


def setposition2(position2):
    if refresh2 == 0:
        music2.set_position(int(position2)/100)
        bar2.set(position2)
        sleep(0.025)


def status2(bar2, music2):
    while True:
        if pause2 == 0:
            global refresh2
            refresh2 = 1
            position2 = music2.get_position()
            position2b = position2*100
            bar2.set(position2b)
            if music2.is_playing() == False:
                Player2stop()
            sleep(0.05)
            refresh2 = 0


#Sliders
volume2b = Scale(root, from_ = 0, to = 100, orient=HORIZONTAL, command = set_volume2, bg="black", fg="white", font=("Arial", 40), width=25, activebackground="gray", length=775, label="Volume Control")
bar2 = Scale(root, from_ = 0, to = 100, orient=HORIZONTAL, command=setposition2, bg="black", fg="white", font=("Arial", 40), width=25, activebackground="gray", length=775, label="Progress Bar")

volume2b.grid(row=5, column=1)
bar2.grid(row=6, column=1)


#Threads
t2 = threading.Thread(target=status2, args=(bar2, music2)).start()


#Init 2
volume2b.set(70)
music2.audio_set_volume(70)



#mainloop
root.mainloop()