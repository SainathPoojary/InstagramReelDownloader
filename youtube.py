import pytube
def youtube(url):
	youtube = pytube.YouTube(url)
	video = youtube.streams.get_highest_resolution()
	return video.url