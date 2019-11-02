import argparse
import os
import imageio
import cv2
import numpy as np
import matplotlib.pyplot as plt


def combine_images(image_paths, output_folder=None, width=960, height=540):
    img_left = imageio.imread(os.path.expanduser(image_paths[0]))
    img_right = imageio.imread(os.path.expanduser(image_paths[1]))
    img_left = cv2.resize(img_left, (int(width/2), int(height)))
    img_right = cv2.resize(img_right, (int(width/2), int(height)))

    output_img = np.hstack((img_left, img_right))

    if output_folder:
        imageio.imwrite(os.path.expanduser(os.path.join(output_folder, "sign.jpg")), output_img)
    else:
        plt.imshow(output_img)
        input()

    print("Hello world")


def main():
    parser = argparse.ArgumentParser("Combine two images")
    parser.add_argument("image_paths",
                        nargs=2,
                        type=str,
                        help="Two paths of images to combine")
    parser.add_argument("-o", "--output_folder",
                        help="Output folder",
                        default=None,
                        required=False)
    parser.add_argument("-W", "--width",
                        default=960,
                        required=False,
                        help="Width of output image")
    parser.add_argument("-H", "--height",
                        default=540,
                        required=False,
                        help="Height of output image")

    args = vars(parser.parse_args())
    combine_images(**args)


if __name__ == "__main__":
    main()
