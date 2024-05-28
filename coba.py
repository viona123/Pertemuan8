
nama_toko = "Pet Shop Lovely Hart"
print("|==============================================|")
print("|              Pet Shop Lovely hart            |")
print("|==============================================|")

# jenis hewan
jenis_hewan = """
|==============================================|
|              Pilih Jenis Hewan               |
|==============================================|
| 1. Hewan Anjing                              |
| 2. Hewan Kucing                              |
|==============================================|
"""
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
    

def print_nota(reservasi):
  groomings = ["nanti masukin list grooming"]
  total_harga = 0
  print("\n--- Nota Reservasi Grooming ---")
  for idx, data in enumerate(reservasi):
    print("Reservasi", idx + 1)
    print("Nama Pemilik:", data["nama_pemilik"])
    print("Nomor Pemilik:", data["nomor_pemilik"])
    print("Alamat Pemilik:", data["alamat_pemilik"])
    print("Nama Hewan:", data["nama_hewan"])
    print("Kondisi Hewan:", data["kondisi_hewan"])
    print("Pilihan Grooming:", groomings[int(data["pilihan_grooming"])-1])
    harga = calculate_price(data["pilihan_grooming"], data["jenis_hewan"])
    print("Harga:", harga)
    total_harga += harga
  print("Total Harga: Rp", total_harga)
  print("---------------------------------")

while True:
    print(jenis_hewan)
    jenis = int(input("Masukkan jenis hewan 1 atau 2 (atau 0 untuk selesai): "))

    if jenis == 1:
        grooming_anjing()
        pilihan_treatment = int(input("Masukkan pilihan treatment (1-6): "))
        nama_hewan = input("Masukkan nama anjing: ")

        if 1 <= pilihan_treatment <= 6:
            harga = [40000, 50000, 60000, 70000, 80000, 100000]
            treatment = ["Grooming kering", "Grooming basic", "Grooming shampoo Anti kutu", "Grooming shampoo Anti jamur", "Grooming Shampoo Anti kutu & jamur", "Grooming shampoo Whitening"]
            total_treatment_ajg += harga
            anjing.append((nama_hewan, treatment, harga)) 
        else:
            print("Pilihan tidak valid")

  
    
