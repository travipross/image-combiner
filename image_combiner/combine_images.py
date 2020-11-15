import argparse
import os
import imageio
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tempfile
from photo_library.fn.download import download_photo_by_id
from photo_library.fn.upload import set_menu
from gphotospy import authorize

# TODO: Implement gphotospy to combine images from cloud
# TODO: Implement image preview for stitching
def combine_images(
    image_paths,
    output_folder=None,
    width=1024,
    height=600,
    fetch_cloud=False,
    upload_menu=False,
    service=None,
):
    """
    Combines two images side-by-side at a given final resolution.
    :param image_paths: Iterable containing at least two image paths
    :param output_folder: (Optional) Which directory in which to save the resulting image. If omitted, the image will
            simply be displayed
    :param width: Width in pixels of final image
    :param height: Height in pixels of final image
    :param fetch_cloud: Whether to fetch images from cloud
    :return:
    """

    # Load the images as numpy arrays
    imgs = []
    for image_path in image_paths:
        if fetch_cloud:
            image_id = image_path
            print(f"Downloading images from Google Photos by id: {image_id}")
            with tempfile.TemporaryDirectory() as tmpdir:
                downloaded_img = download_photo_by_id(
                    service, image_id, download_dir=tmpdir
                )
                imgs.append(imageio.imread(downloaded_img))
        else:
            try:
                imgs.append(imageio.imread(os.path.expanduser(image_path)))
            except FileNotFoundError:
                print("Error loading %s... Skipping." % image_path)

    # Exit if no images successfully loaded
    if not len(imgs):
        print("Could not load any of the specified images.. exiting")
        exit(1)

    # Resize the images to the proper portion of the final resolution
    imgs = [cv2.resize(img, (int(width / len(imgs)), int(height))) for img in imgs]

    # Combine the images side-by-side
    output_img = np.hstack(imgs) if len(imgs) > 1 else imgs.pop()

    # If output directory was specified, generate the necessary parent directories and a filename
    if output_folder:
        output_folder = os.path.expanduser(output_folder)

        # if specified path has an extension, assume it's a full file path
        if os.path.splitext(output_folder)[1] != "":
            output_path = output_folder
            output_folder, basename = os.path.split(output_path)
            filename, ext = os.path.splitext(basename)

        # Otherwise, assume a folder was specified
        else:
            # if the output folder does not exist, create it (and any parent directories)
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Build a full path including file name
            filename = "beer_sign"
            ext = ".jpg"
            output_path = os.path.join(output_folder, filename + ext)

        # If file already exists in the specified location, increment an integer suffix until a unique name is found
        n = "1"
        while os.path.isfile(output_path):
            output_path = os.path.join(output_folder, filename + n + ext)
            n = str(int(n) + 1)

        # Save the image
        imageio.imwrite(output_path, output_img)
        print("Output written to %s" % output_path)

    # If no directory was specified, simply display the image
    else:
        plt.imshow(output_img)
        plt.show()

    if upload_menu or input("Would you like to set this menu? (y/n): ") == "y":
        filename = input("Provide a filename for this menu: ") or "default-filename"
        if not filename.endswith(".jpg"):
            filename += ".jpg"

        with tempfile.TemporaryDirectory() as tmpdir:
            menu_fullpath = os.path.join(tmpdir, filename)
            imageio.imwrite(menu_fullpath, output_img)
            print(f"Uploading menu: {menu_fullpath}")
            set_menu(service, filepath=menu_fullpath)


def main():
    parser = argparse.ArgumentParser("Combine two images")
    parser.add_argument(
        "image_paths", nargs="+", type=str, help="Two paths of images to combine"
    )
    parser.add_argument(
        "-o", "--output_folder", help="Output folder", default=None, required=False
    )
    parser.add_argument(
        "-W",
        "--width",
        default=1024,
        required=False,
        type=int,
        help="Width of output image",
    )
    parser.add_argument(
        "-H",
        "--height",
        default=600,
        required=False,
        type=int,
        help="Height of output image",
    )
    parser.add_argument(
        "--credentials-file",
        type=str,
        required=False,
        help="Path to JSON credentials file",
        default=os.environ.get("GOOGLE_PHOTOS_CREDS"),
    )
    parser.add_argument(
        "--fetch-cloud",
        action="store_true",
        help="Assume image paths are cloud photo IDs to download",
    )
    parser.add_argument(
        "--upload-menu",
        action="store_true",
        help="Upload menu to cloud after creating",
    )

    args = vars(parser.parse_args())
    service = (
        authorize.init(args["credentials_file"]) if "credentials_file" in args else None
    )
    args.update({"service": service})
    del args["credentials_file"]

    combine_images(**args)


if __name__ == "__main__":
    main()
