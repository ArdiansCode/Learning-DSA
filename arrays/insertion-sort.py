array = [9, 2, 5, 12, 29, 32,3, 6]
n = len(array)

for i in range(1,n):
    insert_index = i
    current_value = array[i]
    for j in range(i-1, -1, -1):
        if array[j] > current_value:
            array[j+1] = array[j]
            insert_index = j
        else:
            break
    array[insert_index] = current_value

print("Sorted array:", array)