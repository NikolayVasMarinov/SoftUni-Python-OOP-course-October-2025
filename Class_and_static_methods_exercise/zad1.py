from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages

        self.photos: list[list[str]] = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> "PhotoAlbum":
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str) -> str:
        if len(self.photos[-1]) == 4:
            return "No more free slots"

        page_number = 0

        for page in self.photos:
            page_number += 1
            if len(page) == 4:
                continue

            page.append(label)
            return f"{label} photo added successfully on page {page_number} slot {len(page)}"

    def display(self) -> str:
        result = "-" * 11
        for page in self.photos:
            result += "\n" + ("[] " * len(page)).strip() + "\n" + "-" * 11

        return result