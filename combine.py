def combine_audio(vidname, audname, outname): 
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname)

combine_audio("outvideo.mp4", "finalout.mp3", "translatedvideo.mp4")
