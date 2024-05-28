# Nama : Viona Aziz Syahputri
# NIM : 2311104008

data = [12102001, 12102002, 12102003, 12102004, 12102005, 12102006, 12102007, 12102008, 12102009, 12102010, 12102011, 12102012, 12102013]

# Fungsi untuk melakukan binary search pada data
def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Input NIM yang ingin dicari
input_nim = int(input("Masukkan NIM mahasiswa: "))

# Periksa apakah NIM tersebut terdapat dalam data
if binary_search(data, input_nim):
    print(f"NIM {input_nim} terdapat dalam data.")
else:
    print(f"NIM {input_nim} tidak terdapat dalam data.")