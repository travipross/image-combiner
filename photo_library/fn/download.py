from gphotospy.media import Media, MediaItem
import os


def download_photo_by_id(service, photo_id, download_dir="", filename=None):
    media_manager = Media(service)

    media_item = MediaItem(media_manager.get(photo_id))

    new_filename = filename or media_item.filename()
    output_filepath = os.path.expanduser(os.path.join(download_dir, new_filename))

    with open(output_filepath, "wb") as f:
        f.write(media_item.raw_download())

    return output_filepath
