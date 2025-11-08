class Glass:
    capacity: float = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml: int) -> str:
        if self.content + ml > self.capacity:
            return f"Cannot add {ml} ml"

        self.content += ml
        return f"Glass filled with {ml} ml"

    def empty(self) -> str:
        self.content = 0
        return "Glass is now empty"

    def info(self) -> str:
        return f"{self.capacity - self.content} ml left"