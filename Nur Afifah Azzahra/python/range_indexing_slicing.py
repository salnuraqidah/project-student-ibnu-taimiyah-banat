n = range(10)
print(list(n)) #generate angka dari 0 - 9

m = range(3,12)
print(list(m)) #generate angka dari 3 - 11

o = range(2,16,3)
print(list(o)) #generate angka dari 2 - 16 dengan langkah 3 -- start, stop, step

number = range(1,21)
print(list(number))

print(number[4])#positiveindexing

print(number[-3])#negativeindexing

print(list(number[:10]))
print(list(number[10:]))
print(list(number[2:10]))
print(list(number[2:18:3]))

print("=============================================")

numbers = list(range(1,251))
print(numbers)
print(numbers[15])
print(numbers[-8])
print(numbers[54:67])
print(numbers[69:240:2])