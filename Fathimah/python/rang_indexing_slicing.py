n = range(10) #generate angka dari 0-9
print(list(n))

m = range(3,12)
print(list(m))

o = range(2,16,3) #generate angka dari 2-16 dengan langkah 3
print(list(o))

number = range(1,21)
print(list(number))

print(number[7])
print(number[15])
print(number[-1])

print(list(number[:10]))   
print(list(number[10:]))
print(list(number[2:10]))
print(list(number[2:18:3]))

# create a variable called 'numbers'
# creat a list of numbers 1 - 250 using list(range())
numbers = list(range(1,251))
# print a number from index 15
print(numbers[15])

# print an eight number from the back
# clue : negative indexing
print(numbers[-8])

# print a group of numbers, start from 55 until 67
print(numbers[54:67])

# print a group of even numbers, starts from 70 until 240
# clue : use step parameter
print(numbers[69:240:2])