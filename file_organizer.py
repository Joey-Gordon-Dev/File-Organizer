import os
import shutil

current_dir = os.getcwd()
videos_folder = current_dir + "/Videos"
pictures_folder = current_dir + "/Pictures"
files_in_dir = os.listdir()

length_of_files_in_dir = len(files_in_dir)

os.makedirs(pictures_folder)
os.makedirs(videos_folder)


def main():
    for i in range(length_of_files_in_dir):
        # adding picture files to picture folder
        if files_in_dir[i].endswith(".png") or files_in_dir[i].endswith(".jpeg") or files_in_dir[i].endswith(".jpg"):
            shutil.move(current_dir + "/" + files_in_dir[i], pictures_folder)
        # adding video files to video folder
        if files_in_dir[i].endswith(".mp3") or files_in_dir[i].endswith(".wav") or files_in_dir[i].endswith(".mp4") or files_in_dir[i].endswith(".mov") or files_in_dir[i].endswith(".mkv"):
            shutil.move(current_dir + "/" + files_in_dir[i], videos_folder)


main()