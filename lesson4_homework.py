# 1. Add apples to basket and calculate total, average per person
# 1.alex => 4.500 kg  2.Hanna => 5.500 kg
# 3.zina =>2.300 kg  4.haim => 1.500 kg



def alex():
    return 4.500

def hanna():
    return 5.500

def zina():
    return 2.300

def haim():
    return 1.500

basket = 0
count = 0
basket = alex()
count = count + 1
print(f"in basket {basket:.3f} kg")

basket = basket + hanna()
count = count + 1
print(f"in basket {basket:.3f} kg")

basket = basket + zina()
count = count + 1
print(f"in basket {basket:.3f} kg")

basket = basket + haim()
count = count + 1
print(f"in basket {basket:.3f} kg")

print(f"total in basket {basket:.3f} kg")

# print(f" average {basket / 4:.3f} kg per person")
print(f"average {basket / count:.3f} kg per person")


# 2. define function which get number and returt
# value minus 100
# subtract100(value)

def substraction100(value):
    return value - 100
result = substraction100(250)
print("result = ", result)


# 3.advanced
def calculate_percent(value, percent):
    return value * percent / 100
value = 80
percent = 20
result = calculate_percent(value, percent)
print(f"result = {result:.2f}")



