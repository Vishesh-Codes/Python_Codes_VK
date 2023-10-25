#----------------------------------------------
# play an audio file with pygame
#----------------------------------------------

import pygame
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("../../../../6.     AUDIO/Ringtones/youth and truth last music.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.quit()