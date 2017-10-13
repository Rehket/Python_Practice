# Database is made up of two portions. The Actual Images compresses in bz2 and text files
# which contain the image metadata. The directories containing the images and the metadata are adjacent to one another.
# Each directory containing images has information about the images encoded into the image name.

# Extracts All the front facing images of the people.



# TODO: Set up xml parser and cv2image tools

import bz2
import argparse
import os


# The user will specify the directory containing the image data and associated metadata.
parser = argparse.ArgumentParser()
parser.add_argument("--input_dir", required=True, help="Path to folder containing image and ground_truths directories.")
parser.add_argument("--out_dir", required=True, help="Path to folder where the unzipped images will be placed.")


a = parser.parse_args()


# Method to count sub-directories taken from :
# https://stackoverflow.com/questions/19747408/how-get-number-of-subfolders-and-folders-using-python-os-walks
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
def get_image_paths():
    path_list = []
    data_path = os.path.join(a.input_dir, dir_list(a.input_dir)[0])
    # The path to all the data
    data_path = os.path.join(data_path, os.listdir(data_path)[0])
    # The path to all the images
    images_path = os.path.join(a.input_dir, dir_list(a.input_dir)[1])

    print(os.listdir(images_path))
    for item in os.listdir(images_path):
        my_images_path = os.path.join(images_path, item)
        my_data_path = os.path.join(data_path, item)
        myImages_list = os.listdir(my_images_path)
        myData_list = os.listdir(my_data_path)
        print(my_data_path)
        image_data_pairs = []
        temp_image_list = []
        temp_data_list = []
        # Get the Front Images
        for i in filter_by_contents(myImages_list, ["_fa", "_fb"]):
            temp_image_list.append(i)
        # Get the data for the front images
        for i in filter_by_contents(myData_list, ["_fa", "_fb"]):
            temp_data_list.append(i)
        # if we have the same amount  of data entries as we have for images, we are good to go.
        if len(temp_data_list) == len(temp_image_list):
            count = 0
            for img_p in temp_image_list:
                parsed_data = get_data_from_text(os.path.join(my_data_path, temp_data_list[count]))
                # print(parsed_data)
                path_list.append((os.path.join(my_images_path, img_p), parsed_data[8], parsed_data[13], parsed_data[14], parsed_data[15]))
                count += 1
    return path_list

def decompress_image(img_path, dest_path):
    print("Hallo")


def main():
    print(dir_list(a.input_dir))
    images_data_paths = get_image_paths()
    image_dir = "C:/Workspace/colorferet/colorferet/dvd1/data/images/00001"
    images = os.listdir(image_dir)
    print(images)

    # From https://stackoverflow.com/questions/16963352/decompress-bz2-files
    # make sure that there are images in the list.
    assert (len(images_data_paths) > 0), "No Image in folder..."
    counter = 1
    for im in images_data_paths:
        counter += 1
        # Set up input image and stuff
        bz_image_path = im[0]

        # Setup output image format and stuff
        ppm_image_path = os.path.join(a.out_dir, str(counter) +".ppm")
        print(bz_image_path + " to " + ppm_image_path)



        with open(ppm_image_path, 'wb') as new_file, bz2.BZ2File(bz_image_path, 'rb') as file:
            # What does the 100*1024 do?
            for data in iter(lambda: file.read(100 * 1024), b''):
                new_file.write(data)



# Main Entry point
main()


