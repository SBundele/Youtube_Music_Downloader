from pytube import YouTube

def downloadVideo(url):
    pass

def downloadAudio(url):
    pass

def main():
    while True:
        print("***Welcome to Audio and Video downloader from Youtube***")
        print("1.Download Video 2.Download Audio 3.Exit")
        user_choice = input("Enter your choice (1/2/3): ")
        if user_choice == "1":
            url = input("Enter url of the video: ")
            downloadVideo(url)
        elif user_choice == "2":
            url = input("Enter url of the audio: ")
            downloadAudio(url)
        elif user_choice == "3":
            print("***Thank you for using the app***")
            return
        else:
            print("Enter a valid choice!!")

main()