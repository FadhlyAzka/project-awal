import time

def pesanan_makanan(menu):
    if menu[2] == "":
        print(f"Anda memesan menu makanan {menu[0]} sebanyak {menu[1]}")
    else:
        print(f"Anda memesan menu makanan {menu[0]} sebanyak {menu[1]} pesanan dengan topping ekstra:")
        for ekstra in menu[2:]:
            print(f"- {ekstra}")
    
    biaya_makanan = 1
    if menu[0] == "Burger":
        biaya_makanan = biaya_makanan * menu[1] * 20
    elif menu[0] == "Kentang goreng":
        biaya_makanan = biaya_makanan * menu[1] * 7
    elif menu[0] == "Bawang goreng":
        biaya_makanan = biaya_makanan * menu[1] * 6
    
    if menu[2] != "":
        biaya_makanan = biaya_makanan + (len(menu) - 2) * 3
    
    return biaya_makanan

def pesanan_minuman(menu):
    print(f"Anda memesan menu minuman {menu[0]} sebanyak {menu[1]}")

    biaya_minuman = 1
    if menu[0] == "Teh":
        biaya_minuman = biaya_minuman * menu[1] * 5
    elif menu[0] == "Jus apel":
        biaya_minuman = biaya_minuman * menu[1] * 6
    elif menu[0] == "Espresso":
        biaya_minuman = biaya_minuman * menu[1] * 8
    
    return biaya_minuman
    

def pembelianMakan():
    list_makanan = []
    opsi_makanan = ["Burger", "Kentang goreng", "Bawang goreng"]
    
    while True:
        while True:
            menuMakanan_pelanggan = input("Pesan makanan    : ")
            if menuMakanan_pelanggan not in opsi_makanan:
                print("Menu yang Anda cari tidak tersedia. Silahkan pilih yang lain!")
            else:
                break
        while True:
            jumlahMakanan_pelanggan = int(input("Jumlah pesanan     : "))
            if jumlahMakanan_pelanggan == 0:
                print("Silahkan atur banyaknya pesanan menu Anda dengan benar!")
            else:
                break
        topping_pelanggan = input("Perlu ekstra topping? ")
        pesanan_makanan = (menuMakanan_pelanggan, jumlahMakanan_pelanggan, topping_pelanggan)
        list_makanan.append(pesanan_makanan)

        pelanggan = input("Konfirmasi pesanan anda atau k untuk Keluar: ")
        if pelanggan == "k":
            break
    
    return list_makanan

def pembelianMinum():
    list_minuman = []
    opsi_minuman = ["Teh", "Jus apel", "Espresso"]
    
    while True:
        while True:
            menuMinuman_pelanggan = input("Pesan minuman    : ")
            if menuMinuman_pelanggan not in opsi_minuman:
                print("Menu yang Anda cari tidak tersedia. Silahkan pilih yang lain!")
            else:
                break
        while True:
            jumlahMinuman_pelanggan = int(input("Jumlah pesanan     : "))
            if jumlahMinuman_pelanggan == 0:
                print("Silahkan atur banyaknya pesanan menu Anda dengan benar!")
            else:
                break
        pesanan_minuman = (menuMinuman_pelanggan, jumlahMinuman_pelanggan)
        list_minuman.append(pesanan_minuman)

        pelanggan = input("Konfirmasi pesanan anda atau k untuk Keluar: ")
        if pelanggan == "k":
            break
    
    return list_minuman

def uang_dompet():
    while True:
        dana = input("Berapa banyak koin yang Anda bawa? ")
        if dana.isdigit():
            dana = int(dana)
            if dana > 0:
                break
            else:
                print("Apabila Anda tidak punya uang, dimohon untuk kembali lagi ya!")
        else:
            print("Mohon masukkan dalam bentuk bilangan bulat!")
    
    return dana


def menu():
    print("————————Selamat Datang di Papa's Burgeria————————")
    nominal = uang_dompet()

    time.sleep(2)
    print("Silahkan dipesan hidangan!")
    print("___Makanan___ \n\ \
        Burger          | 20 Koin \n\ \
        Kentang goreng  | 7 koin \n\ \
        Bawang goreng   | 6 koin \n \
___Minuman___ \n\ \
        Teh             | 5 koin \n\ \
        Jus Apel        | 6 koin \n\ \
        Espresso        | 8 koin")
    print("Anda dapat menambahkan ekstra bahan (3 koin per bahan)\n \
    Tersedia: Beef, Keju, Tomat, Selada, Mentimun\n \
————————————————————")
    
    makanan = pembelianMakan()
    minuman = pembelianMinum()
    biaya = []
    print("----————————————————----")
    for tipeMakanan in makanan:
        biaya_makan = pesanan_makanan(tipeMakanan)
        biaya.append(biaya_makan)
    for tipeMinuman in minuman:
        biaya_minum = pesanan_minuman(tipeMinuman)
        biaya.append(biaya_minum)
    biaya = sum(biaya)
    print(f"Total biaya pesanan Anda sebesar {biaya} koin")
    print("----————————————————----")
    time.sleep(2)

    kembalian = nominal - biaya
    if kembalian >= 0:
        print(f"Anda telah membayar pesanan Anda dengan kembalian sebesar {kembalian} koin")
    else:
        print(f"Maaf, uang yang Anda bayarkan kurang sebesar {-kembalian} koin")

menu()
