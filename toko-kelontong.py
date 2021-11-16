datasembako = ["Beras","Gula","Minyak","Jagung"]
dataobat = ["Bodrex","Paramex","Diapet","Amoxilin"]
dataperlengkapanmemasak = ["Gas 3Gk","Pisau","Talenan","Panci"]
datamakananringan = ["Keripik Talas","Usu Krispi","Pisang Sale","Kuaci"]
dataminuman = ["Coca-coal","Sprit","Teh Gelas 220ml","Aqua 20ml"]
keranjang = []
totalharga = []
jumlahbarang = []
hitung = 0

print("Selamat datang di toko kami")
nama_pembeli= input("Masukkan nama Anda : ")
print ("\n===== Selamat datang Bpk/Ibu",nama_pembeli,"=====")
print("Silahkan Memilih Jenis Barang yang ingi dibeli")


def jenisbarang():
    print("\n==========================================")
    print("============== Menu Barang ===============")
    print("==========================================")
    print("1. |            Sembako               | --")
    print("2. |          Obat-obatan             | --")
    print("3. |       Perlengkapan Masak         | --")
    print("4. |         Makanan Ringan           | --")
    print("5. |            Minuman               | --")
    print("==========================================")
    pilih1 = int(input("Pilih Nomer Pesanan Anda : "))
    if pilih1 == 1:
        listsembako()
    elif pilih1 == 2:
        listobat()
    elif pilih1 == 3:
        perlengkapanmemasak()
    elif pilih1 == 4:
        makanringan()
    elif pilih1 == 5:
        listminuman()
    else:
       print("Menu Belum Terdaftar !!")


def listsembako():
    print("\n=========================================")
    print("============= Daftar Sembako ============")
    print("=========================================")
    print("1. |    Beras 1kg     = Rp.10.000    | --")
    print("2. |    Gula 1kg      = Rp.10.000    | --")
    print("3. |    Minyak 900ml  = Rp.13.000    | --")
    print("4. |    Jagung 1kg    = Rp.15.000    | --")
    print("=========================================")
    sembako = int(input("Pilih nomer pesanan : "))
    if sembako == 1:
        keranjang.append(datasembako[0])
        jumlah_sembako = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 10000 * jumlah_sembako
        jumlahbarang.append(jumlah_sembako)
        totalharga.append(total1)
        bertanya()
    elif sembako == 2 :
        keranjang.append(datasembako[1])
        jumlah_sembako = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 10000 * jumlah_sembako
        jumlahbarang.append(jumlah_sembako)
        totalharga.append(total1)
        bertanya()
    elif sembako == 3 :
        keranjang.append(datasembako[2])
        jumlah_sembako = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 13000 * jumlah_sembako
        jumlahbarang.append(jumlah_sembako)
        totalharga.append(total1)
        bertanya()
    elif sembako == 4 :
        keranjang.append(datasembako[3])
        jumlah_sembako = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 15000 * jumlah_sembako
        jumlahbarang.append(jumlah_sembako)
        totalharga.append(total1)
        bertanya()
    else:
        while True:
            jawab = input("Perbaiki jawaban anda y/t :")
            if jawab == "y":
                break
        listsembako()

def listobat():
    print("\n=========================================")
    print("=============== Daftar Obat =============")
    print("=========================================")
    print("1. |  Bodrek   1 strip  = Rp.5.000   | --")
    print("2. |  Paramex  1 strip  = Rp.6.000   | --")
    print("3. |  Diapet   1 strip  = Rp.7.000   | --")
    print("4. |  Amoxilin 1 strip  = Rp.10.000  | --")
    print("=========================================")
    obat = int(input("Pilih nomer pesanan : "))
    if obat == 1:
        keranjang.append(dataobat[0])
        jumlah_obat = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 5000 * jumlah_obat
        jumlahbarang.append(jumlah_obat)
        totalharga.append(total1)
        bertanya()
    elif obat == 2 :
        keranjang.append(dataobat[1])
        jumlah_obat = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 6000 * jumlah_obat
        jumlahbarang.append(jumlah_obat)
        totalharga.append(total1)
        bertanya()
    elif obat == 3 :
        keranjang.append(dataobat[2])
        jumlah_obat = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 7000 * jumlah_obat
        jumlahbarang.append(jumlah_obat)
        totalharga.append(total1)
        bertanya()
    elif obat == 4 :
        keranjang.append(dataobat[3])
        jumlah_obat = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 10000 * jumlah_obat
        jumlahbarang.append(jumlah_obat)
        totalharga.append(total1)
        bertanya()
    else:
        while True:
            jawab = input("Perbaiki jawaban anda y/t :")
            if jawab == "y":
                break
        listobat()


def perlengkapanmemasak():
    print("\n=========================================")
    print("============ Daftar p. masak ============")
    print("=========================================")
    print("1. | Gas 3gk  isi ulang = Rp.18.000  | --")
    print("2. | Paramex  1 strip   = Rp.21.000  | --")
    print("3. | Diapet   1 strip   = Rp.15.000  | --")
    print("4. | Amoxilin 1 strip   = Rp.35.000  | --")
    print("=========================================")
    masak = int(input("Pilih nomer pesanan : "))
    if masak == 1:
        keranjang.append(dataperlengkapanmemasak[0])
        jumlah_masak = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 18000 * jumlah_masak
        jumlahbarang.append(jumlah_masak)
        totalharga.append(total1)
        bertanya()
    elif masak == 2 :
        keranjang.append(dataperlengkapanmemasak[1])
        jumlah_masak = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 21000 * jumlah_masak
        jumlahbarang.append(jumlah_masak)
        totalharga.append(total1)
        bertanya()
    elif masak == 3 :
        keranjang.append(dataperlengkapanmemasak[2])
        jumlah_masak = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 15000 * jumlah_masak
        jumlahbarang.append(jumlah_masak)
        totalharga.append(total1)
        bertanya()
    elif masak == 4 :
        keranjang.append(dataperlengkapanmemasak[3])
        jumlah_masak = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 35000 * jumlah_masak
        jumlahbarang.append(jumlah_masak)
        totalharga.append(total1)
        bertanya()
    else:
        while True:
            jawab = input("Perbaiki jawaban anda y/t :")
            if jawab == "y":
                break
        perlengkapanmemasak()


def makanringan():
    print("\n============================================")
    print("============= Daftar Makanan R. ============")
    print("============================================")
    print("1. | Keripik Talas 9000gram = Rp.10.000 | --")
    print("2. | Usus Krispi   900gram  = Rp.10.000 | --")
    print("3. | Pisang Sale   1kg      = Rp.13.000 | --")
    print("4. | Kuaci         500gram  = Rp.15.000 | --")
    print("=========================================")
    makanan_ringan = int(input("Pilih nomer pesanan : "))
    if makanan_ringan == 1:
        keranjang.append(datamakananringan[0])
        jumlah_makananringan = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 7000 * jumlah_makananringan
        jumlahbarang.append(jumlah_makananringan)
        totalharga.append(total1)
        bertanya()
    elif makanan_ringan == 2 :
        keranjang.append(datamakananringan[1])
        jumlah_makananringan = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 9000 * jumlah_makananringan
        jumlahbarang.append(jumlah_makananringan)
        totalharga.append(total1)
        bertanya()
    elif makanan_ringan == 3 :
        keranjang.append(datamakananringan[2])
        jumlah_makananringan = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 15000 * jumlah_makananringan
        jumlahbarang.append(jumlah_makananringan)
        totalharga.append(total1)
        bertanya()
    elif makanan_ringan == 4 :
        keranjang.append(datamakananringan[3])
        jumlah_makananringan = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 10000 * jumlah_makananringan
        jumlahbarang.append(jumlah_makananringan)
        totalharga.append(total1)
        bertanya()
    else:
        while True:
            jawab = input("Perbaiki jawaban anda y/t :")
            if jawab == "y":
                break
        makanringan()

def listminuman():
    print("\n===============================================")
    print("================ Daftar Minuman ===============")
    print("===============================================")
    print("1. | Coca-cola       1 kiter  = Rp.10.000  | --")
    print("2. | Prit            1 liter  = Rp.10.000  | --")
    print("3. | Teh Gelas 220m  1 dus    = Rp.13.000  | --")
    print("4. | Aqua 220ml      1 dus    = Rp.15.000  | --")
    print("=========================================")
    minuman = int(input("Pilih nomer pesanan : "))
    if minuman == 1:
        keranjang.append(dataminuman[0])
        jumlah_makananringan = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 9000 * jumlah_makananringan
        jumlahbarang.append(jumlah_makananringan)
        totalharga.append(total1)
        bertanya()
    elif minuman == 2 :
        keranjang.append(dataminuman[1])
        jumlah_makananringan = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 9000 * jumlah_makananringan
        jumlahbarang.append(jumlah_makananringan)
        totalharga.append(total1)
        bertanya()
    elif minuman == 3 :
        keranjang.append(dataminuman[2])
        jumlah_makananringan = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 18000 * jumlah_makananringan
        jumlahbarang.append(jumlah_makananringan)
        totalharga.append(total1)
        bertanya()
    elif minuman == 4 :
        keranjang.append(dataminuman[3])
        jumlah_makananringan = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 25000 * jumlah_makananringan
        jumlahbarang.append(jumlah_makananringan)
        totalharga.append(total1)
        bertanya()
    else:
        while True:
            jawab = input("Perbaiki jawaban anda y/t :")
            if jawab == "y":
                break
        listminuman()
    

def bertanya ():
    for i in range(len(keranjang)):
        print("==== Anda Membeli barang :",keranjang[i],"berjumlah",jumlahbarang[i])
    pilihan = input("Tambah pesanan ? y/t :")
    if pilihan == "y":
        jenisbarang()
    elif pilihan == "t":
        hasil()
    else:
        while True:
            jawab = input("Perbaiki Jawab Anda y/t : ")
            if jawab == "y":
                break
        bertanya()
        

def hasil():
    print("\n================================================")
    print("======== S T R U K  P E M B A Y A R A N ========")
    print("================================================")
    print("==== Nama : ",nama_pembeli)
    for i in range(len(keranjang)):
        print("==== Anda Membeli barang :",keranjang[i],"berjumlah",jumlahbarang[i])
    jumlah = sum(totalharga)
    print("==== Jumlah pembyaran anda : Rp.",jumlah)
    uang = int(input("==== Jumlah Pembayaran Anda : Rp."))
    kembalian = int(uang-jumlah)
    print("==== Kembalian anda : Rp.",kembalian)


jenisbarang()
