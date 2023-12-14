import pygame
import sys

def play_wav(audiofile):
    pygame.mixer.init()
    pygame.mixer.music.load('/home/hs/heuschrank/'+audiofile+'.wav')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


if __name__ == '__main__':
    play_wav(sys.argv[1])
