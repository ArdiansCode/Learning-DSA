# buat array
# buat variabel n untuk menanmpung jumlah data
# lakukan perulangan untuk mencari nilai terkecil dari array, pindahkan nilai terendah ke bagian depan dari bagian array yang belum diurutkan
# lakukan perulangan sampai data terurutkan

array = [9, 2, 5, 12, 29, 32,3, 6]
n = len(array)

for i in range(n):
    min_idex = i
    for j in range(i+1, n):
        if array[j] < array[min_idex]:
            min_idex = j
    array[i], array[min_idex] = array[min_idex], array[i]

print('data yg sudah diurutkan :', array)