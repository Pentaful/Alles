from pytube import YouTube
from pytube.cli import on_progress



url = input("url? ")
yt = YouTube(url, on_progress_callback=on_progress)
ys = yt.streams.get_highest_resolution()
print(yt.streams.get_highest_resolution())

info = input("Mehr Informationen? y/n ")
if info == "y":
    print("")
    print("Titel: ",yt.title)
    print("")
    print("Views: ",yt.views)
    print("")
    print("Länge: ",float(yt.length/60.0), "Minuten")
    print("")
    print("Description:\n\n ",yt.description)
    print("\n\n")
    confirm = input("Download? y/n ")
    if confirm == "y":
        print("Downloading...")
        ys.download()
    else:
        exit()
else:
    confirm = input("Download? y/n")
    if confirm == "y":
        print("Downloading...")
        ys.download()