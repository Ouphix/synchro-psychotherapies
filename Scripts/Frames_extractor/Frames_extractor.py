import os
#dir path is the place of the videos
dirPath = "/Users/Ofix/Documents/Fac/internat/Recherche/projets/synchro/synchroData/images/convertingVideos/"
videos = os.listdir(dirPath)
print videos
#os.system("ffmpeg.exe -i \"%s\" -vcodec png -ss 50 -vframes 1 -an -f rawvideo .\\images\\%s.png" % ("F:\\Monrado vid\\00027.MTS", "test.png"))
for video in videos :
    if not video.endswith(".mov") :
        continue
#Create amnually a folder with images where to put frames
    os.system("./ffmpeg -i \"%s\" -vcodec png -ss 10 -vframes 1 -an -f rawvideo ./images/%s.png" % (dirPath + video, video))
