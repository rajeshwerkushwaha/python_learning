from moviepy.editor import *

# clip = (VideoFileClip("input.mp4"))
clip = (VideoFileClip("input.mov").subclip((0.0),(15.0))
        .resize(0.5))
clip.write_gif("output.gif")