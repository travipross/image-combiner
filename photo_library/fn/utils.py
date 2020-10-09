from photo_library import ALBUM_ID_ARCHIVE
from gphotospy.media import Media
from gphotospy.album import Album


def list_archived_menus(service):
    # Create managers
    media_mgr = Media(service)

    # Search album for all media items
    media_items = media_mgr.search_album(ALBUM_ID_ARCHIVE)

    # Display results
    for m in media_items:
        print(f"filename: {m.get('filename', ''):35}| id: {m.get('id')}")


def list_albums(service, api_only=False):
    # Create managers
    album_mgr = Album(service)

    # Search album for all media items
    albums = album_mgr.list(api_only)

    # Display results
    for a in albums:
        print(f"title: {a.get('title', ''):35}| id: {a.get('id')}")