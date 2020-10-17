from photo_library.fn.download import download_photo_by_id as download_photo_by_id_fn
from gphotospy import authorize
import argparse
import os


def download_photo_by_id():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--photo-id",
        type=str,
        required=True,
        help="Id of image file to download",
    )
    parser.add_argument(
        "--download-dir",
        type=str,
        required=False,
        default="",
        help="Directory in which to download file",
    )
    parser.add_argument(
        "--filename",
        type=str,
        required=False,
        default=None,
        help="Filename to assign downloaded file",
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

    download_photo_by_id_fn(service, args.photo_id, args.download_dir, args.filename)
