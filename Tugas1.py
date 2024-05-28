# Nama : Viona Aziz Syahputri
# NIM : 2311104008

database = ['R 300 SR', 'R 1234 DJ', 'R 701 LP', 'R 3218 RR', 'R 007 TU', 'R 3 ST', 'R 999 RT', 'R 210 RO', 'R 1111 II', 'R 4987 LH']

def sequential_search(database, target):
    for i in range(len(database)):
        if database[i] == target:
            return True
    return False

# Input nomor plat mobil
input_plat = input("Masukkan nomor plat mobil: ")

# Periksa apakah input terdapat dalam database
if sequential_search(database, input_plat):
    print("Nomor plat mobil tersebut terdapat dalam database.")
else:
    print("Nomor plat mobil tersebut tidak terdapat dalam database.")