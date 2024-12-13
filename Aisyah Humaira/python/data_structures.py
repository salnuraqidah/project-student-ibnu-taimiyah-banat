#list
names = ["Andi", "Beni", "Cahyo"]
print(names)
#List bisa pake kurung kotak

data_siswa = ["Salsa", 12, True]
print(data_siswa)

animals = list(("Fish", "Cat", "Panda", "Lion"))
#Urutan    :      0       1       2        3
print(animals)
#Bisa juga dipanggil dulu. Kurungnya dua
#Bisa dimanipulasi
animals[0] = "Dolphin"
print(animals)

animals.append("Frog") #add list
print(animals)

animals.remove("Cat") #Remove list
print(animals)

#tuple (Gak bisa dimanipulasi) (Pake kurung)
fruits = ("Apple", "Banana", "Mango")
print(fruits)

buah = tuple(("Apple", "Banana", "Mango"))
print(fruits[0])

#fruits[2] = "watermelon" #gak bisa di manipulasi, error

fruits_list = list(fruits)
print(fruits_list)

fruits_list[2] = "Watermelon"
print(fruits_list)

fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

#set (Tidak bisa diakses, tidak berurutan, tidak bisa dimanipulasi)
numbers = {1,2,3,4,5,6}
print(numbers)

negara = set(("Indonesia", "Malaysia", "Singapura", "Vietnam"))
print(negara)

#print = (negara[1]) : error, tidak dapat diakses, bisa dimanipulasi

negara.add("Singapura")
print(negara)
negara.remove("Vietnam")
print(negara)
negara.discard("Filipina") #lebih aman
print(negara)
negara.pop() #menghapus data paling ujung
print(negara)

#dictionary
employees = {
    "name" : "Joko",
    "age" : 21,
    "address" : "Jakarta",
    "status" : False,
    "siblings" : ["John", "Jake"]
}
print(employees)

mahasiswa = dict(name = "Siti", address = "Bogor")
print(mahasiswa)

print(employees["age"])
print(employees["name"])

employees["age"] = 22 #mengubah
print(employees)

employees["hobbies"] = "Swimming" #menambah
print(employees)

employees.pop("status")
print(employees)