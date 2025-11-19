class ImageArea:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def __eq__(self, other: "ImageArea"):
        return self.get_area() == other.get_area()

    def __ne__(self, other: "ImageArea"):
        return self.get_area() != other.get_area()

    def __gt__(self, other: "ImageArea"):
        return self.get_area() > other.get_area()

    def __ge__(self, other: "ImageArea"):
        return self.get_area() >= other.get_area()

    def __lt__(self, other: "ImageArea"):
        return self.get_area() < other.get_area()

    def __le__(self, other: "ImageArea"):
        return self.get_area() <= other.get_area()