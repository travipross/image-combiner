from photo_library import ALBUM_ID_ARCHIVE
from gphotospy.media import Media


def list_archived_menus(service):
    # Create managers
    media_mgr = Media(service)

    # Search album for all media items
    media_items = media_mgr.search_album(ALBUM_ID_ARCHIVE)

    # Display results
    for m in media_items:
        print(f"filename: {m.get('filename', ''):35}| id: {m.get('id')}")