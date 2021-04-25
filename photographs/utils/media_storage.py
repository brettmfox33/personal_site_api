import pathlib

def store_album_image(instance, file):
    return f"album/{instance.uuid}/cover_image{pathlib.Path(file).suffix}"


def store_photograph_image(instance, file):
    return f"album/{instance.album.uuid}/photographs/{file}"