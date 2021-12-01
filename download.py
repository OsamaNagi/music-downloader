from pytube import YouTube
import os

while True:
    link = input("enter url: ") # link to the video you want to download
    if(link == 'a'):
        break
    video = YouTube(link)
    for stream in video.streams.filter(only_audio = True, mime_type = "audio/mp4"):
        stream = video.streams.get_by_itag(140)
        stream.download(output_path="") #path
    print("done")

path_folder = r'' #file path to change the extension of inner folders 
print()
print('Path: {}'.format(path_folder))
print()
old_extension = '.' + input('Enter the old extension (e.g. txt, mp3) --> ')
new_extension = '.' + input('Enter the new extension (e.g. txt, mp3) --> ')
print()
files_counter = 0
with os.scandir(path_folder) as files_and_folders:
    for element in files_and_folders:
        if element.is_file():
            root, ext = os.path.splitext(element.path)
            if ext == old_extension:
                new_path = root + new_extension
                os.rename(element.path, new_path)
                files_counter += 1

print('** RECAP **')
print()
print('Number of files processed: {}'.format(files_counter))
print('Extension: from {} to {}'.format(old_extension, new_extension))
# ---------------------------------------------------------------------------------
