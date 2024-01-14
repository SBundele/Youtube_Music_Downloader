from pytube import YouTube

def downloadVideo(url):
    yt = YouTube(url)
    video = yt.streams.filter(resolution='720p',file_extension='mp4').first()
    video.download()

def downloadAudio(url):
    yt = YouTube(url)
    audio = yt.streams.get_audio_only()
    audio.download()

def main():
    while True:
        print()
        print("***Welcome to Audio and Video downloader from Youtube***")
        print()
        print("1.Download Video 2.Download Audio 3.Exit")
        user_choice = input("Enter your choice (1/2/3): ")
        if user_choice == "1":
            url = input("Enter url of the video: ")
            downloadVideo(url)
        elif user_choice == "2":
            url = input("Enter url of the audio: ")
            downloadAudio(url)
        elif user_choice == "3":
            print()
            print("***Thank you for using the app***")
            return
        else:
            print("Enter a valid choice!!")

main()