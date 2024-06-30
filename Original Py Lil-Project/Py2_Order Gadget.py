import time

available_units = {
    'Poco X6 5G' : {
        'OS Android Version' : 13,
        'RAM' : 12,
        'Internal Memories' : 256,
        'Rear Camera Resolution' : 64,
        'Front Camera Resolution' : 16,
        'Battery Capacity' : 5100,
        'Price (Rp.)' : 3799000
    },
    'Vivo Y100 5G' : {
        'OS Android Version' : 14,
        'RAM' : 8,
        'Internal Memories' : 128,
        'Rear Camera Resolution' : 50,
        'Front Camera Resolution' : 8,
        'Battery Capacity' : 5000,
        'Price (Rp.)' : 3400000
    },
    'Poco M6 Pro' : {
        'OS Android Version' : 13,
        'RAM' : 8,
        'Internal Memories' : 256,
        'Rear Camera Resolution' : 64,
        'Front Camera Resolution' : 16,
        'Battery Capacity' : 5000,
        'Price (Rp.)' : 3049000
    },
    'Realme C67' : {
        'OS Android Version' : 13,
        'RAM' : 8,
        'Internal Memories' : 256,
        'Rear Camera Resolution' : 108,
        'Front Camera Resolution' : 8,
        'Battery Capacity' : 5000,
        'Price (Rp.)' : 2369000
    },
    'Oppo A77s' : {
        'OS Android Version' : 12,
        'RAM' : 8,
        'Internal Memories' : 128,
        'Rear Camera Resolution' : 50,
        'Front Camera Resolution' : 8,
        'Battery Capacity' : 5000,
        'Price (Rp.)' : 2099000
    },
    'Redmi Note 10S' : {
        'OS Android Version' : 11,
        'RAM' : 6,
        'Internal Memories' : 64,
        'Rear Camera Resolution' : 64,
        'Front Camera Resolution' : 13,
        'Battery Capacity' : 5000,
        'Price (Rp.)' : 2249000
    },
    'Tecno Pova 4' : {
        'OS Android Version' : 12,
        'RAM' : 8,
        'Internal Memories' : 128,
        'Rear Camera Resolution' : 50,
        'Front Camera Resolution' : 8,
        'Battery Capacity' : 6000,
        'Price (Rp.)' : 2390000
    }
}

def system_filter(unit, nom):
    ask = input("Apakah kebutuhan gadget Anda menyesuaikan uang dompet? ")
    if ask == 'ya':
        unit_price = []
        for a in unit.items():
            unit_price.append(a[0])
            unit_price.append(a[1]['Price (Rp.)'])

        chunked = list()
        chunked_size = 2
        for i in range(0, len(unit_price), chunked_size):
            chunked.append(unit_price[i:i+chunked_size])

        for model in chunked:
            if model[1] < nom:
                print ("REKOMENDASI : {} dengan harga Rp.{}".format(model[0], model[1]))
    print("----————————————————----")

def specs():
    opsi_produk = ['Poco X6 5G','Vivo Y100 5G','Poco M6 Pro','Realme C67','Oppo A77s','Redmi Note 10S','Tecno Pova 4']
    produk_pesan = []

    while True:
        view_spec = input("Silahkan dipilih : ")
        produk_pesan.append(view_spec)
        if view_spec not in opsi_produk:
            print("Produk yang Anda cari tidak tersedia di toko kami.")
        else:
            print("Produk {} tersedia dengan spesifikasi: ".format(view_spec))

            for brand in available_units.items():
                if view_spec == brand[0]:
                    for spec in brand[1].items():
                        print("> {} : {}".format(spec[0], spec[1]))
                        if 'Price (Rp.)' == spec[0]:
                            produk_pesan.append(spec[1])
            
            return produk_pesan

def uang_dompet():
    while True:
        dana = input("Berapa banyak uang (Rp.) yang Anda bawa? ")
        if dana.isdigit():
            dana = int(dana)
            if dana >= 2099000:
                break
            elif dana > 0 and dana < 2099000:
                print("Nominal uang Anda kurang mencukupi untuk setidaknya dapat membeli unit gadget termurah kami.")
            else:
                print("Apabila Anda tidak punya uang, dimohon untuk kembali lagi ya!")
        else:
            print("Mohon masukkan dalam bentuk bilangan bulat!")
        
    return dana

def order():
    print("————————Selamat Datang di Papa's Gadgetria————————")
    nominal = uang_dompet()

    print("Silahkan dilihat gadget yang tersedia.")
    [print("- {}".format(produk)) for produk in available_units]
    print("----————————————————----")
    time.sleep(2)

    system_filter(available_units, nominal)
    time.sleep(2)

    print("Anda juga bisa melihat spesifikasi dari untuk gadget yang Anda mungkin tertarik.")
    while True:
        produk_beli = specs()
        print("----————————————————----")
        konfirmasi = input("Apakah Anda yakin dengan pilihan Anda? ")
        if konfirmasi == "ya":
            kembalian = nominal - produk_beli[1]
            print("Terima kasih telah membeli produk {} kami, dengan kembalian Rp.{}. Harap kembali.".format(produk_beli[0], kembalian)")
            break

order()
