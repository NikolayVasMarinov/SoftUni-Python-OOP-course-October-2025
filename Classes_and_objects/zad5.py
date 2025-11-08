class Smartphone:
    def __init__(self, memory: float):
        self.memory = memory
        self.apps: list[str] = []
        self.is_on = False

    def power(self) -> None:
        self.is_on = not self.is_on

    def install(self, app: str, app_memory: float) -> str:
        if self.memory - app_memory < 0:
            return f"Not enough memory to install {app}"

        if not self.is_on:
            return f"Turn on your phone to install {app}"

        self.memory -= app_memory
        self.apps.append(app)

        return f"Installing {app}"

    def status(self) -> str:
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"