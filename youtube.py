import pytube
def youtube(url):
	youtube = pytube.YouTube(url)
	video = youtube.streams.first()
	return video.url