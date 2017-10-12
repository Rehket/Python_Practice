# Database is made up of two portions. The Actual Images compresses in bz2 and text files
# which contain the image metadata. The directories containing the images and the metadata are adjacent to one another.
# Each directory containing images has information about the images encoded into the image name.


import bz2
import xml
import argparse
import os


# The user will specify the directory containing the image data and associated metadata.
parser = argparse.ArgumentParser()
parser.add_argument("--input_dir", required=True, help="path to folder containing image and ground_truths directories")


a = parser.parse_args()


# Method to count sub-directories taken from :
# https://stackoverflow.com/questions/19747408/how-get-number-of-subfolders-and-folders-using-python-os-walks
def dir_list(path):
    dirs = os.listdir(path)
    assert (dirs.__contains__("ground_truths") and dirs.__contains__("images")), \
        "Make sure that the directory has the images and ground_truths directories."
    return dirs


def main():
    print(dir_list(a.input_dir))



main()


