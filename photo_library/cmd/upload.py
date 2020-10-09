from photo_library.fn.upload import (
    set_home as set_home_fn,
    set_menu as set_menu_fn,
    upload_originals as upload_originals_fn,
)
from gphotospy import authorize
import argparse
import os


def set_home():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--photo-id",
        type=str,
        required=False,
        help="Media Item ID from Google Photos API",
    )
    parser.add_argument(
        "--filepath", type=str, required=False, help="Path to image file to upload"
    )
    parser.add_argument(
        "--credentials-file",
        type=str,
        required=False,
        help="Path to JSON credentials file",
        default=os.environ.get("GOOGLE_PHOTOS_CREDS"),
    )
    args = parser.parse_args()

    if args.credentials_file is None:
        raise ValueError("Missing credentials")

    service = authorize.init(args.credentials_file)
    set_home_fn(service, photo_id=args.photo_id, filepath=args.filepath)


def set_menu():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--photo-id",
        type=str,
        required=False,
        help="Media Item ID from Google Photos API",
    )
    parser.add_argument(
        "--filepath", type=str, required=False, help="Path to image file to upload"
    )
    parser.add_argument(
        "--credentials-file",
        type=str,
        required=False,
        help="Path to JSON credentials file",
        default=os.environ.get("GOOGLE_PHOTOS_CREDS"),
    )
    args = parser.parse_args()

    if args.credentials_file is None:
        raise ValueError("Missing credentials")

    service = authorize.init(args.credentials_file)
    set_menu_fn(service, photo_id=args.photo_id, filepath=args.filepath)


def upload_originals():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filepath",
        type=str,
        required=False,
        help="Path to image file (or directory of image files) to upload",
    )
    parser.add_argument(
        "--credentials-file",
        type=str,
        required=False,
        help="Path to JSON credentials file",
        default=os.environ.get("GOOGLE_PHOTOS_CREDS"),
    )
    args = parser.parse_args()

    if args.credentials_file is None:
        raise ValueError("Missing credentials")

    service = authorize.init(args.credentials_file)

    upload_originals_fn(service, args.filepath)
