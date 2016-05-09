import os
#dir path is the place of the videos
dirPath = "/Users/Ofix/Documents/Fac/internat/Recherche/projets/synchro/synchroData/videoEnCoursAnalyse/convertingVideos/"

videos = os.listdir(dirPath + "videosToConvert/")
print videos
#os.system("ffmpeg.exe -i \"%s\" -vcodec png -ss 50 -vframes 1 -an -f rawvideo .\\images\\%s.png" % ("F:\\Monrado vid\\00027.MTS", "test.png"))
for video in videos :
    if not video.endswith(".mov") :
        continue
#Create amnually a folder with images where to put frames
#remplacer
    #os.system("pwd")
    print dirPath + video
    os.system(dirPath + "/ffmpeg -i \"%s\" -vcodec copy -acodec copy %s.avi" % (dirPath + "videosToConvert/" + video, dirPath + "avimovies/" + video))
