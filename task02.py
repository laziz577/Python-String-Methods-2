price = " {fruit} mahsuloti narxi {prices}$"

fruit = input()
prices = float(input())

print(price.format(fruit=fruit,prices=prices))
