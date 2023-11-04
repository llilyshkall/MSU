class Shared:
    objects = 0
    live = 0
    total = 0
    local = 0

    def __init__(self) -> None:
        Shared.objects = Shared.objects + 1
        Shared.live = Shared.live + 1

    def __invert__(self) -> int:
        Shared.total = Shared.total + 1
        self.local = self.local + 1
        return self.local

    def __del__(self) -> None:
        Shared.live = Shared.live - 1

    def __str__(self) -> str:
        return f'|{self.objects}/{self.live}/{self.total}/{self.local}|'
