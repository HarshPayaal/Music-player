import pygame
import tkinter as tkr
from tkinter import ttk
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk 
import os

def set_volume(volume):
    pygame.mixer.music.set_volume(float(volume))

def play_next():
    current_index = play_list.curselection()
    if current_index:
        current_index = int(current_index[0])
        next_index = (current_index + 1) % play_list.size()
        play_list.selection_clear(current_index)
        play_list.activate(next_index)
        play_list.selection_set(next_index)
        play()

def play_previous():
    current_index = play_list.curselection()
    if current_index:
        current_index = int(current_index[0])
        previous_index = (current_index - 1) % play_list.size()
        play_list.selection_clear(current_index)
        play_list.activate(previous_index)
        play_list.selection_set(previous_index)
        play()

def update_progress_bar():
    if pygame.mixer.music.get_busy():
        current_time = pygame.mixer.music.get_pos() / 1000 
        total_time = pygame.mixer.Sound(play_list.get(tkr.ACTIVE)).get_length() 

        progress = (current_time / total_time) * 100
        progress_bar["value"] = progress

    music_player.after(100, update_progress_bar) 
music_player = tkr.Tk()
music_player.title("My Music Player")
music_player.geometry("450x450")


background_image = Image.open("tree.png")
background_photo = ImageTk.PhotoImage(background_image)


background_label = tkr.Label(music_player, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='yellow', selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    update_progress_bar()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

Button1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="blue", fg="white")
Button2 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")
Button3 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="purple", fg="white")
Button4 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="orange", fg="white")
Button5 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="NEXT", command=play_next, bg="green", fg="white")
Button6 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PREVIOUS", command=play_previous, bg="yellow", fg="black")

var = tkr.StringVar()
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

volume_scale = tkr.Scale(music_player, from_=0, to=1, orient=tkr.HORIZONTAL, resolution=0.1, label="Volume", command=set_volume)
volume_scale.set(0.5)

progress_bar = ttk.Progressbar(music_player, orient="horizontal", length=300, mode="determinate")

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
Button5.pack(fill="x")
Button6.pack(fill="x")
volume_scale.pack(fill="x")
progress_bar.pack(fill="x")
play_list.pack(fill="both", expand="yes")

music_player.mainloop()