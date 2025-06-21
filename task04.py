day = "Bugun {week} kuni, dars soat {clock} da."
week = input()
clock = int(input())

print(day.format(week=week,clock=clock))
