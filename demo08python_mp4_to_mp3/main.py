from moviepy.editor import *
import os

mp4Path = r'./mp4/'
mp3Path = './mp3/'
for mp4Name in os.listdir(mp4Path): 
    #print(mp4Name)
    try:
        video = VideoFileClip('./mp4/'+mp4Name)
        audio = video.audio
        audio.write_audiofile('./mp3/'+mp4Name[:-4]+'.mp3')
    except:
        print("errors:")
        try:
            print(mp4Name)
        except:
            print("name can't print")