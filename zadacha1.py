import math
try:
    n = int(input())
except ValueError:
    print("Неверный ввод")
print(math.sin(math.radians(n)))
print(math.cos(math.radians(n)))
print(math.tan(math.radians(n)))
