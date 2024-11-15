import pygame
import numpy as np
import math
import time

pygame.init()

bits = 16 #cd quality
sample_rate = 44100
pygame.mixer.pre_init(sample_rate, bits)

def sin_x(amp, freq, time):
    return int(round(amp * math.sin(2 * math.pi * freq * time)))

class Tone:
    
    def sine(freq, duration=1, amp=1, speaker = None): #default duration is 1 sec 
                                                       #amp has to be between 0 and 1
                                                       
        num_samples = int(round(duration*sample_rate))
        sound_buffer = np.zeros((num_samples, 2), dtype = np.int16)
        amplitude = amp*(2 ** (bits - 1) - 1)
        
        for sample_num in range(num_samples):
            t = float(sample_num)/sample_rate
            
            sine = sin_x(amplitude, freq, t)
            
            if speaker == 'r':
                sound_buffer[sample_num][1] = sine
            elif speaker == 'l':
                sound_buffer[sample_num][0] = sine
            else:
                sound_buffer[sample_num][1] = sine
                sound_buffer[sample_num][0] = sine
                            
        sound = pygame.sndarray.make_sound(sound_buffer)
        sound.play(loops=1, maxtime=int(duration*1000))
        time.sleep(duration)