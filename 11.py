#classwork
# a =input("Son kiriting: ")
# b =input("Son kiriting: ")
# c =input("Son kiriting: ")

# max_n = 0
# if a>b:
#     max_n = a
# else:
#     max_n = b

# if max_n >c:
#     max_n = c

# print(max_n)

# list = []
# for i in range(20):
#     a = input("Son kiriting: ")
#     list.append(a)
#     max_n = list[0]
#     min_n = list[0]
#     if a > max_n:
#         max_n = a
#     if a < min_n:
#         min_n = a

# print(f"Berilgan ro'yhat {list}")
# print(f"Berilgan ro'yhat {list} dagi eng katta son {max_n}")
# print(f"Berilgan ro'yhat {list} dagi eng kichik son {min_x}")

#homework
coffee = ['Americano', 'Latte', 'Espresso', 'Black Coffee', 'Mocha']
price = [16, 15, 20, 25, 22]
a = int(input("Nechi kishilik coffee olasz? :"))
schot = 0
for i in range(a):
    b = input("Kofe turini kiriting: ")
    list_coffee = []
    list_coffee.append(b)
    for i in range(10):
        if list_coffee[i] == coffee[i]:
            schot += price[i]

print("___________Xush kelibsiz!_____________")
print(f"Sizning buyurtmangiz {list_coffee}")
print(f"Siz {a}ta coffee oldingiz")
print(f"Va siz {schot} to'lashingiz kerak bo'lgan summa")
print('______Xaridingiz uchun raxmat!___________')