from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=tWiBewIP6bM")
yt.streams.first().download()

# to download the audio version:
yt.streams.filter(only_audio=True).first().download()
