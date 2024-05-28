# jenis hewan
jenis_hewan = """
|==============================================|
|              Pet Shop Lovely Heart!          |
|==============================================|
|              Pilih Jenis Hewan               |
|==============================================|
| 1. Hewan Anjing                              |
| 2. Hewan Kucing                              |
|==============================================|
"""

# set nilai awal
total_treatment_ajg = 0
total_treatment_cat = 0
anjing = []
kucing = []

def grooming_anjing():
    print("|=======================================================|")
    print("|        Pilihan grooming untuk anjing                  |")
    print("|=======================================================|")
    print("|1. Grooming kering                      Rp.40.000      |")
    print("|2. Grooming basic                       Rp.50.000      |")
    print("|3. Grooming shampoo Anti kutu           Rp.60.000      |")
    print("|4. Grooming shampoo Anti jamur          Rp.70.000      |")
    print("|5. Grooming shampoo anti kutu & jamur   Rp.80.000      |")
    print("|6. Grooming shampoo whitening           Rp.100.000     |")
    print("|=======================================================|")

def grooming_cat():
    print("|=======================================================|")
    print("|             Pilihan grooming untuk kucing             |")
    print("|=======================================================|")
    print("|1. Grooming kering                      Rp.20.000      |")
    print("|2. Grooming basic                       Rp.25.000      |")
    print("|3. Grooming shampoo Anti kutu           Rp.30.000      |")
    print("|4. Grooming shampoo Anti jamur          Rp.30.000      |")
    print("|5. Grooming shampoo anti kutu & jamur   Rp.60.000      |")
    print("|6. Grooming shampoo whitening           Rp.80.000      |")
    print("|=======================================================|")

def print_nota():
    print("\n---------------------------------------------")
    print("|               Nota Reservasi              |")
    print("---------------------------------------------")
    print(f"Nama Pemilik : {nama_pemilik}")
    print(f"No Pemilik   : {no_pemilik}")
    print(f"Alamat       : {alamat_pemilik}")
    print(f"Kondisi Hewan: {kondisi_hewan}")
    print("---------------------------------------------")

    if anjing:
        print("Detail Reservasi Anjing:")
        for nama, treatment, harga in anjing:
            print(f"* {nama} : {treatment} - Rp {harga}")
        print("---------------------------------------------")

    if kucing:
        print("Detail Reservasi Kucing:")
        for nama, treatment, harga in kucing:
            print(f"* {nama} : {treatment} - Rp {harga}")
        print("---------------------------------------------")
    
    total_harga = total_treatment_ajg + total_treatment_cat
    print(f"Total Biaya  : Rp {total_harga}")
    print("---------------------------------------------")

while True:
    print(jenis_hewan)
    jenis = int(input("Masukkan jenis hewan 1 atau 2 (atau 0 untuk selesai): "))
    
    if jenis == 0:
        print("===== Masukkan Data Reservasi =====")
        nama_pemilik = input("Masukkan nama pemilik hewan: ")
        no_pemilik = input("Masukkan no pemilik hewan: ")
        alamat_pemilik = input("Masukkan alamat pemilik: ")
        kondisi_hewan = input("Masukkan kondisi hewan: ")
        print_nota()
        break

    elif jenis == 1:
        grooming_anjing()
        pilihan_treatment = int(input("Masukkan pilihan treatment (1-6): "))
        nama_hewan = input("Masukkan nama anjing: ")

        if 1 <= pilihan_treatment <= 6:
            harga = [40000, 50000, 60000, 70000, 80000, 100000][pilihan_treatment - 1]
            menu_treatment = ["Grooming kering", "Grooming basic", "Grooming shampoo Anti kutu", 
                                "Grooming shampoo Anti jamur", "Grooming shampoo anti kutu & jamur", 
                                "Grooming shampoo whitening"][pilihan_treatment - 1]
            total_treatment_ajg += harga
            anjing.append((nama_hewan, menu_treatment, harga)) 
        else:
            print("Pilihan tidak valid.")

    elif jenis == 2:
        grooming_cat()
        pilihan_treatment = int(input("Masukkan pilihan treatment (1-6): "))
        nama_hewan = input("Masukkan nama kucing: ")

        if 1 <= pilihan_treatment <= 6:
            harga = [20000, 25000, 30000, 30000, 60000, 80000][pilihan_treatment - 1]
            menu_treatment = ["Grooming kering", "Grooming basic", "Grooming shampoo Anti kutu", 
                                "Grooming shampoo Anti jamur", "Grooming shampoo anti kutu & jamur", 
                                "Grooming shampoo whitening"][pilihan_treatment - 1]
            total_treatment_cat += harga
            kucing.append((nama_hewan, menu_treatment, harga)) 
        else:
            print("Pilihan tidak valid.")
    
    else:
        print("Pilihan tidak valid. Masukkan 1 atau 2.")