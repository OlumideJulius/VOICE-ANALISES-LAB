import threading
import sys
import time
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import wave
import speech_recognization as sr
from speech_recognization import AudioData
stop_event = threading.Event()
audio_frames = []
def wait_for_enter():
    input("\n  press Enter to stop recording...\n")
    stop_event.set()
def spinner():
    chars = '|/-\\'
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f'\r Redcording... {chars[i % 4]}')
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
    print("\r Recording complete!         ")
def callback(indata, frames, time_info, status):
    if status:
        print(status)
    audio_frames.append(indata.copy())
def record_audio():
    global audio_frames
    audio_frames = []
    samplerate = 16000
    threading.Thread
    
    

    















    except sr.UnknownValueError:
        print()