from project.song import Song
from project.album import Album

class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: list[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        album = next(a for a in self.albums if album_name == a.name)

        if not album:
            return f"Album {album_name} is not found."

        if album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(album)
        return f"Album {album_name} has been removed."

    def details(self):
        return (f"Band {self.name}\n" +
                "\n".join(a.details() for a in self.albums))