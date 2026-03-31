# buat array
# buat variabel n untuk menampung banyaknya data
# lakukan perulangan dan membandingkan angka saat ini dengan angka berikutnya, jika lebih besah angknya, maka ditaruh paling belakang
# lakukan sebanyak data tersebut, jika perulangan selesai, data akan terurut dari yg terkecil sampai yg terbesar

array = [9, 2, 5, 12, 29, 32,3, 6]
n = len(array)

for i in range (n-1):
    for j in range (n-1-i):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print("data yg sudah diurutkan:", array)
        