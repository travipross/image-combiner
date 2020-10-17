from photo_library import ALBUM_ID_ARCHIVE, ALBUM_ID_ORIGINALS
from gphotospy.media import Media
from gphotospy.album import Album


def list_media_items_in_album(service, album_id):
    # Create managers
    media_mgr = Media(service)

    # Search album for all media items
    media_items = media_mgr.search_album(album_id)

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


def list_archived_menus(service):
    list_media_items_in_album(service, ALBUM_ID_ARCHIVE)


def list_originals(service):
    list_media_items_in_album(service, ALBUM_ID_ORIGINALS)
