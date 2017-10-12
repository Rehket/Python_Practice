# Database is made up of two portions. The Actual Images compresses in bz2 and text files
# which contain the image metadata. The directories containing the images and the metadata are adjacent to one another.
# Each directory containing images has information about the images encoded into the image name.

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


def main():
    print(dir_list(a.input_dir))
    image_dir = "C:/Workspace/colorferet/colorferet/dvd1/data/images/00001"
    images = os.listdir(image_dir)
    print(images)

    img = []

    # generate a list of images in a directory.
    for i in filter_by_contents(images, ["_fa_", "_fb_"]):
        img.append(i)

    # From https://stackoverflow.com/questions/16963352/decompress-bz2-files
    # make sure that there are images in the list.
    assert (len(img) > 0), "No Image in folder..."
    for im in img:
        # Set up input image and stuff
        bz_image_path = os.path.join(image_dir, im)
        # Setup output image format and stuff
        ppm_image_path = a.out_dir + im[:-4]
        print(bz_image_path)
        with open(ppm_image_path, 'wb') as new_file, bz2.BZ2File(bz_image_path, 'rb') as file:
            # What does the 100*1024 do?
            for data in iter(lambda: file.read(100 * 1024), b''):
                new_file.write(data)


# Main Entry point
main()


