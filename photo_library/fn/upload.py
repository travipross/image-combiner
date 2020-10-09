from photo_library import (
    ALBUM_ID_ARCHIVE,
    ALBUM_ID_MAIN,
    ALBUM_ID_HOME,
    ALBUM_ID_ORIGINALS,
)
from collections.abc import Iterable
from gphotospy import authorize
from gphotospy.media import Media
from gphotospy.album import Album

import os
import logging

# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def add_photo_to_album(
    service, album_id, photo_id=None, filepath=None, remove_old=False
):
    # Create managers
    media_mgr = Media(service)
    album_mgr = Album(service)

    # If no photo_id provided, attempt to upload file from filepath
    if photo_id is None:
        logger.info("No photo_id provided, uploading by filepath.")
        if filepath is None:
            raise ValueError("Must provide one of either photo_id or filepath.")

        file_meta = upload_photos_to_album(
            service, [filepath], album_id=ALBUM_ID_ARCHIVE
        ).pop(0)
        logger.debug(f"File meta: {file_meta}")

        photo_id = file_meta["mediaItem"]["id"]
        logger.info(f"{file_meta['mediaItem']['filename']} uploaded. id: {photo_id}")

    # Get current photo(s) in album (should only be one)
    old_items = media_mgr.search_album(album_id)

    # Add photos to album
    album_mgr.batchAddMediaItems(album_id=album_id, items=[photo_id])

    # Remove old photos from album
    items_to_remove = [o["id"] for o in old_items if o["id"] != photo_id]
    logger.info(f"Found {len(items_to_remove)} other items in album.")
    if remove_old and len(items_to_remove):
        logger.info("Removing other items.")
        album_mgr.batchRemoveMediaItems(
            album_id=album_id,
            items=items_to_remove,
        )


def set_menu(service, photo_id=None, filepath=None):
    add_photo_to_album(
        service,
        album_id=ALBUM_ID_MAIN,
        photo_id=photo_id,
        filepath=filepath,
        remove_old=True,
    )


def set_home(service, photo_id=None, filepath=None):
    add_photo_to_album(
        service,
        album_id=ALBUM_ID_HOME,
        photo_id=photo_id,
        filepath=filepath,
        remove_old=True,
    )


def upload_photos_to_album(
    service, filepaths: list, album_id=None, album_name="Unnamed Album"
):
    # Create managers
    media_mgr = Media(service)

    # stage/upload anonymous data from filepath
    for f in filepaths:
        logger.info(f"Uploading {f}")
        media_mgr.stage_media(os.path.expanduser(f))

    # If no album specified, create new album
    if album_id is None:
        album_mgr = Album(media_mgr._service)
        album_id = album_mgr.create(album_name)["id"]

    # Associate data with album
    meta_list = media_mgr.batchCreate(album_id=album_id)

    return meta_list


def upload_originals(service, filepath):
    # if filepath is a folder, find all files
    filepath = os.path.expanduser(filepath)
    if os.path.isdir(filepath):
        filepaths = [os.path.join(filepath, f) for f in os.listdir(filepath)]
    elif os.path.isfile(filepath):
        filepaths = [filepath]
    else:
        raise FileNotFoundError(f"Invalid filepath: {filepath}")

    logger.info(f"Files to upload: {len(filepaths)}")
    upload_photos_to_album(service, filepaths=filepaths, album_id=ALBUM_ID_ORIGINALS)


if __name__ == "__main__":
    service = authorize.init()