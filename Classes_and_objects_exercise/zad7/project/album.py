from project.song import Song

class Album:
    def __init__(self, name: str, *args: Song):
        self.name = name
        self.songs = list(args)
        self.published: bool = False

    def add_song(self, song: Song) -> str:
        if self.published:
            return "Cannot add songs. Album is published."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."

        song = next((s for s in self.songs if song_name == s.name), None)

        if not song:
            return "Song is not in the album."

        self.songs.remove(song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self) -> str:
        if self.songs:
            return (f"Album {self.name}\n== " +
                    "\n== ".join(s.get_info() for s in self.songs))

        return f"Album {self.name}"