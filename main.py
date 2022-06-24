DOKON_EGASI = 1
XARIDOR = 2

maxsulotlar_malumoti = ['nomi','narx','malumot','sana','soni']

maxsulotlar = {
    'non':[2500, 'Uy noni 250gr', '2022/06/15', 50],
    'fanta':[ 8500, 'gazli ichimlik', '2021/11/10', 20],
    'cola':[8000, 'gazli ichimlik 1L', '2021/10/11', 50],
    'non1':[2500, 'Uy noni 250gr', '2022/06/15', 50],
    'fanta1':[ 8500, 'gazli ichimlik', '2021/11/10', 20],
    'cola1':[8000, 'gazli ichimlik 1L', '2021/10/11', 50],
    'non2':[2500, 'Uy noni 250gr', '2022/06/15', 50],
    'fanta2':[ 8500, 'gazli ichimlik', '2021/11/10', 20],
    'cola2':[8000, 'gazli ichimlik 1L', '2021/10/11', 50],
    'non3':[2500, 'Uy noni 250gr', '2022/06/15', 50],
    'fanta3':[ 8500, 'gazli ichimlik', '2021/11/10', 20],
    'cola3':[8000, 'gazli ichimlik 1L', '2021/10/11', 50],
    'non4':[2500, 'Uy noni 250gr', '2022/06/15', 50],
    'fanta4':[ 8500, 'gazli ichimlik', '2021/11/10', 20],
    'cola4':[8000, 'gazli ichimlik 1L', '2021/10/11', 50],
    'non5':[2500, 'Uy noni 250gr', '2022/06/15', 50],
    'fanta5':[ 8500, 'gazli ichimlik', '2021/11/10', 20],
    'cola5':[8000, 'gazli ichimlik 1L', '2021/10/11', 50],
    'non6':[2500, 'Uy noni 250gr', '2022/06/15', 50],
    'fanta6':[ 8500, 'gazli ichimlik', '2021/11/10', 20],
    'cola6':[8000, 'gazli ichimlik 1L', '2021/10/11', 50],
}


xaridorlar = [
    ['id','ism','maxsulotlar','summa']
]

print("""
Kim foydalanyapti
1.Do'kon egasi
2.Xaridor
""")

foydalanuvchi = int(input("Raqamni kiriting: "))

if foydalanuvchi == DOKON_EGASI:
    print("Bu xizmat xozircha mavjud emas")
elif foydalanuvchi == XARIDOR:
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
        if len(maxsulotlar_chiqish)<3:
            print("Maxsulotlar tugadi ortga qayting")

        print('*. <-'.center(29,' '),'|',end='')
        print('0. Sotib olish'.center(91,' '),'|',end='')
        print('#. ->'.center(29,' '),'|',end='')
        print('\n')
        buyruq = input("Buyruqni tanlang: ")
        if buyruq=='#' and not len(maxsulotlar_chiqish)<3:
            boshi+=3
