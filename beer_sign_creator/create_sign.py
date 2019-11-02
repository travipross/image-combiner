import argparse
import os
import imageio
import cv2

def combine_images(image_paths, output_folder=None, width=960, height=540):
    img_left = imageio.imread(os.path.expanduser(image_paths[0]))
    img_right = imageio.imread(os.path.expanduser(image_paths[1]))

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
