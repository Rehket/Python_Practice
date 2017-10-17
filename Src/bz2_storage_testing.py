# Database is made up of two portions. The Actual Images compresses in bz2 and text files
# which contain the image metadata. The directories containing the images and the metadata are adjacent to one another.
# Each directory containing images has information about the images encoded into the image name.

# Extracts All the front facing images of the people.



# TODO: Remove Color Feret stuff and focus on bz2 here.

import bz2
import argparse
import os
import json


# The user will specify the directory containing the image data and associated metadata.
parser = argparse.ArgumentParser()
parser.add_argument("--input_dir", required=True, help="Path to folder containing image and ground_truths directories.")
parser.add_argument("--out_dir", required=True, help="Path to folder where the unzipped images will be placed.")

a = parser.parse_args()


# Method to count sub-directories taken from :
# https://stackoverflow.com/questions/19747408/how-get-number-of-subfolders-and-folders-using-python-os-walks
# TODO: Is this really necessary?
def dir_list(path):
    dirs = os.listdir(path)
    assert (dirs.__contains__("ground_truths") and dirs.__contains__("images")), \
        "Make sure that the directory has the images and ground_truths directories."
    return dirs


# For every string in the sequence that contains the value, return it.
def filter_by_contents(seq, value = []):
    for el in seq:
        for v in value:
            if v in el:
                yield el

# TODO: Explain what is happening here better
def get_data_from_text(path):
    my_data = []
    with open(path) as f:
        temp_data = f.readlines()
    temp_data = [x.strip() for x in temp_data]
    for text_data in temp_data:
        text=text_data.split("=")
        my_data.append((text[0], text[1]))
    return my_data


# Get the Image paths, then get the data once we know what paths were are accessing.
# Got some of the file processing info from:
# https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
def get_image_paths(tags):
    path_list = []
    # The path to all the images
    images_path = os.path.join(a.input_dir, dir_list(a.input_dir)[1])

    # print(os.listdir(images_path))
    for item in os.listdir(images_path):
        my_images_path = os.path.join(images_path, item)

        my_images_list = os.listdir(my_images_path)
        # Get the Front Images
        for i in filter_by_contents(my_images_list, tags):
            path_list.append(i)

    return path_list


def get_data_paths(tags):
    path_list = []
    data_path = os.path.join(a.input_dir, dir_list(a.input_dir)[0])

    # The path to all the data
    data_path = os.path.join(data_path, os.listdir(data_path)[0])

    # Get the data for the front images
    for item in os.listdir(data_path):

        # The path to the data in the subfolder
        my_data_path = os.path.join(data_path, item)

        my_data_list = os.listdir(my_data_path)

        # TODO: Maybe add an example of what this actually does.
        for i in filter_by_contents(my_data_list, tags):
            path_list.append(os.path.join(my_data_path, i))

    return path_list

def main():
    # print(dir_list(a.input_dir))
    tags = ["_fa", "_fb"]
    images_path = get_image_paths(tags)
    data_paths = get_data_paths(tags)

    print(images_path)
    print(data_paths)

    print(len(images_path))
    print(len(data_paths))

    # From https://stackoverflow.com/questions/16963352/decompress-bz2-files
    # make sure that there are images in the list.
    assert (len(images_path) > 0), "No Image in folder..."
    counter = 1
    for im in images_path:
        counter += 1
        # Set up input image and stuff
        # bz_image_path = im[0]

        # Setup output image format and stuff
        # ppm_image_path = os.path.join(a.out_dir, str(counter) +".ppm")
        # print(bz_image_path + " to " + ppm_image_path)



        # with open(ppm_image_path, 'wb') as new_file, bz2.BZ2File(bz_image_path, 'rb') as file:
            # What does the 100*1024 do?
        #     for data in iter(lambda: file.read(100 * 1024), b''):
         #       new_file.write(data)



# Main Entry point
main()


