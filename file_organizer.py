import os
import shutil

try:
    current_dir = os.getcwd()
    videos_folder = current_dir + "/Videos"
    pictures_folder = current_dir + "/Pictures"
    docs_folder = current_dir + "/Documents"
    files_in_dir = os.listdir()

    length_of_files_in_dir = len(files_in_dir)


    def main():
        for i in range(length_of_files_in_dir):
            if files_in_dir[i].endswith(".png") or files_in_dir[i].endswith(".jpeg") or files_in_dir[i].endswith(".jpg"):
                os.makedirs(pictures_folder)
                shutil.move(current_dir + "/" + files_in_dir[i], pictures_folder)
            if files_in_dir[i].endswith(".mp3") or files_in_dir[i].endswith(".wav") or files_in_dir[i].endswith(".mp4") or files_in_dir[i].endswith(".mov") or files_in_dir[i].endswith(".mkv"):
                os.makedirs(videos_folder)
                shutil.move(current_dir + "/" + files_in_dir[i], videos_folder)
            if files_in_dir[i].endswith(".pdf") or files_in_dir[i].endswith(".ppt") or files_in_dir[i].endswith(".xls") or files_in_dir[i].endswith(".doc"):
                os.makedirs(docs_folder)
                shutil.move(current_dir + "/" + files_in_dir[i], docs_folder)


    main()
except:
    print("Error: folder already exists.")
    ValueError
