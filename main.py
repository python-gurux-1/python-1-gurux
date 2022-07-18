from data import *

print("""
Kim foydalanyapti
1.Do'kon egasi
2.Xaridor""")

foydalanuvchi = int(input("Raqamni kiriting: "))

if foydalanuvchi == DOKON_EGASI:
    print("Bu xizmat xozircha mavjud emas")
elif foydalanuvchi == 2:
    boshi = 0
    while True:
        for i in maxsulotlar_malumoti:
            print(i.center(29,' '),'|', end='')
        print('\n')
        print('_'*154,'\n')
        maxsulotlar_chiqish = list(maxsulotlar.keys())[boshi:boshi+3]
        for i in maxsulotlar_chiqish:
            print(str(i).center(29,' '),'|',end='')

            for i in maxsulotlar[i]:
                print(str(i).center(29,' '),'|',end='')
            print('\n')
        if boshi >= len(maxsulotlar):
            print("Maxsulotlar tugadi ortga qayting")

        print('*. <-'.center(29,' '),'|',end='')
        print('0. Sotib olish'.center(91,' '),'|',end='')
        print('#. ->'.center(29,' '),'|',end='')
        print('\n')
        buyruq = input("Buyruqni tanlang: ")
        if buyruq=='#' and boshi <= len(maxsulotlar):
            boshi+=3
        if buyruq=='*' and  boshi-3>0:
            boshi-=3
