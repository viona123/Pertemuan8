# I = [1, 4, 6, 46, 99, 100, 209, 230, 789, 45,34, 22, 56, 89, 90, 88, 67, 23 ]
# x = int(input('Masukan angka yang ingin dicari: '))
# idx = -1

# for i in range(len(I)):
#     if I[i] == x:
#         idx = i
#         break

# if idx == -1:
#     print('Nilai', x, 'tidak ditemukan dalam list.')
# else:
#     print('Nilai', x, 'ditemukan pada index ke-', idx)


# Nama : Viona AZIZ Syahputri
# NIM : 2311104008

#kalo data binery harus diurutkan angkanya dengan bener dari terkecil
I = [104,100,67,102,55,70,85,80,103,99,100,76,98,75,77,55,81,12,111]
dicari = int(input('Masukan angka yang ingin dicari: '))
print('Mencari nilai', dicari, 'dengan binary search pada list', I)
ditemukan = False
batas_awal = 0
batas_akhir = len(I) -1

while not ditemukan and batas_awal <= batas_akhir:
    pos_cari = batas_awal + (batas_akhir - batas_awal) // 2
    print('posisi pencarian: index', pos_cari, 'dengan nilai', I[pos_cari])
    if I[pos_cari] == dicari:
        ditemukan = True
    elif I[pos_cari] > dicari:
        batas_akhir = pos_cari -1
    else:
        batas_awal = pos_cari + 1

if ditemukan:
    print('Nilai', dicari, 'ditemukan pada index', pos_cari)
else:
    print('Nilai', dicari, 'tidak ditemuikan')
