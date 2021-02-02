def onscreen(a):
    for i in range(4):
        print(a[i])

def wincheck(a):
    d1 = 0
    d2 = 0
    for i in range(1, 4):
        x = 0
        y = 0
        if a[i][i] == a[i-1][i-1] and a[i][j] != "-":
            d1 += 1
        if a[i][-i] == a[i-1][-i-1] and a[i][-j] != "-":
            d2 += 1
        for j in range(1, 4):
            if a[i][j] == a[i][j-1] and a[i][j] != "-":
                x += 1
            if a[j][i] == a[j-1][i] and a[i][j] != "-":
                y += 1
            if x == 2 or y == 2 or d1 == 2 or d2 == 2:
                print("Игра завершена. выиграл игрок:", a[i][j])


gamemap = [["_", "1", "2", "3"], ["1", "-", "-", "-"], ["2", "-", "-", "-"], ["3", "-", "-", "-"]]
onscreen(gamemap)
prevstep = "-"
while "-" in [element for a_list in gamemap for element in a_list]:
    step = list(input("Введите свой ход, в формате СТРОКА СТОЛБЕЦ СИМВОЛ(х/о):").split())
    if 1 <= int(step[0]) <= 3 and 1 <= int(step[1]) <= 3:
        if step[2] == "x" or step[2] == "o":
            if gamemap[int(step[0])][int(step[1])] == "-":
                if step[2] != prevstep:
                    gamemap[int(step[0])][int(step[1])] = step[2]
                    onscreen(gamemap)
                    wincheck(gamemap)
                    prevstep = step[2]
                else:
                    print("Игроки должны чередоваться")
            else:
                print("Данная ячейка уже занята")
        else:
            print("Необходимо использовать только символы x или o")
    else:
        print("Выход за границу поля, сходите заного:")