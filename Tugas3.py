# Nama : Viona Aziz Syahputri
# NIM ; 2311104008 

bilangan_acak = [21, 61, 28, 72, 44, 68, 37, 52, 75, 71]

bilangan_acak_terurut = sorted(bilangan_acak)

def binary_search(daftar, target):
    rendah = 0
    tinggi = len(daftar) - 1

    while rendah <= tinggi:
        mid = (rendah + tinggi) // 2
        tebakan = daftar[mid] 
        if tebakan == target:
            return mid
        elif tebakan < target:
            rendah = mid + 1
        else:
            tinggi = mid - 1
    return -1

angka_yang_dicari = int(input("Masukkan angka acak: "))

hasil = binary_search(bilangan_acak_terurut, angka_yang_dicari)

if hasil != -1:
    print(f"Angka {angka_yang_dicari} ditemukan di indeks ke-{hasil}.")
else:
    print(f"Angka {angka_yang_dicari} tidak ditemukan dalam daftar bilangan acak.")