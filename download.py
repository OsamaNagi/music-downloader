from pytube import YouTube
while True:
    link = input("enter url: ") # link to the video you want to download
    video = YouTube(link)
    for stream in video.streams.filter(only_audio = True, mime_type = "audio/mp4"):
        stream = video.streams.get_by_itag(140)
        stream.download(output_path="/Users/alsha/Desktop/down/music")
    print("done")
# ---------------------------------------------------------------------------------
