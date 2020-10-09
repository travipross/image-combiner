from photo_library.fn.utils import list_archived_menus as list_archived_menus_fn
from gphotospy import authorize
import argparse
import os


def list_archived_menus():
    parser = argparse.ArgumentParser()
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

    list_archived_menus_fn(service)
