#----------------------------------------------
# play an audio file with pygame
#----------------------------------------------

import pygame
pygame.init()
pygame.mixer.init()

while True:
    ans = input("which song would you like to listen? --> ").lower()
    if ans.startswith("nai"):
        pygame.mixer.music.load("../../../../6.     AUDIO/Ringtones/NAINA NIHARE Ringtone flex start.mp3")
        pygame.mixer.music.play()

        # while pygame.mixer.music.get_busy():
        #     pygame.time.Clock().tick(10)
    elif ans.startswith("in"):
        pygame.mixer.music.load("../../../../6.     AUDIO/Ringtones/in aankhon me tum  X1.mp3")
        pygame.mixer.music.play()

        # while pygame.mixer.music.get_busy():
        #     pygame.time.Clock().tick(10)
    elif ans.startswith("you"):
        pygame.mixer.music.load("../../../../6.     AUDIO/Ringtones/youth and truth last music.mp3")
        pygame.mixer.music.play()
    elif ans.startswith("bi"):
        pygame.mixer.music.load("../../../../6.     AUDIO/Ringtones/ringtone birano yo mandir ma.mp3")
        pygame.mixer.music.play()
    elif ans.startswith("man"):
        pygame.mixer.music.load("../../../../6.     AUDIO/Ringtones/man lagena ab bin tohar short tone 4.mp3")
        pygame.mixer.music.play()
    else: break
pygame.quit()