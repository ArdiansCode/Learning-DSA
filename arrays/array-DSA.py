# buat array
# buat variabel "minVal" nilai indeks 0
# telusuri array dengan perulangan
# jika nilai array lebih kecil dari nilai variabel "minVal", maka update "minVal" dengan nilai tersebut
# setelah selesai perulangan, minVal akan terisi nilai terendah dari array


array = [9, 2, 5, 12, 29, 32,3, 6]
minVal = array[0]

for i in array:
    if i < minVal:
        minVal = i

print("nilai terendahnya adalaha :", minVal)
