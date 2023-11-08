#==========================================
# Exercise - 7 : Healthy Programmer
#==========================================
"""
What is this program about?
→ This program simply reminds a programmer to take a break for drinking water, resting eyes and for doing some physical activities. This program helps a programmer to stay healthy while being in coding profession.
"""
from time import time
from datetime import datetime
from pygame import mixer

def play_music_now(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        programmer_ans = input().lower()
        if programmer_ans == stopper:
            mixer.music.stop()
            break

def log_event(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg}\t\t\t\t{datetime.now()}\n")

if __name__ == '__main__':
    notice_time = time()
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    water_interval = 8
    eyes_interval = 15
    exercise_interval = 20

    while True:
        if time() - init_water > water_interval:
            print("Drink water now. Enter 'drank' to stop the alarm.")
            play_music_now("water.mp3", "drank")
            init_water = time()
            log_event("Drunk water at")
            
        if time() - init_eyes > eyes_interval:
            print("Take break for eyes. Enter 'eydone' to stop the alarm.")
            play_music_now("eyes.mp3", "eydone")
            init_eyes = time()
            log_event("Eyes relaxed at")

        if time() - init_exercise > exercise_interval:
            print("Do some exercise now. Enter 'exdone' to stop the alarm.")
            play_music_now("physical.mp3", "exdone")
            init_exercise = time()
            log_event("Exercise done at")

        if notice_time + 3 * 60 * 60 < time():
            print("The Healthy Programmer App has stopped automatically after 3 hrs.")
            break