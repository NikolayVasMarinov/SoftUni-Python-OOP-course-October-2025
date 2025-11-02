def draw_rombus(n: int) -> None:
    for i in range(n - 1, 0, -1):
        print(" " * i, "* " * (n - i))
    for i in range(n):
        print(" " * i, "* " * (n - i))

num: int = int(input())
draw_rombus(num)