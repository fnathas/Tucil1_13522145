def result(list: tuple[list[tuple[str, tuple[int, int]]], int], x: int) -> None:
    print("result: ")
    print(list[1])
    for i in range(x):
        print(list[0][i][0], end=" ")
    print()
    for i in range(x):
        print(str(list[0][i][1][0] + 1) + ", " + str(list[0][i][1][1] + 1))
    print()
    
    