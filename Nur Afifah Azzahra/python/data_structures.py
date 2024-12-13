names = ["Ahmad", "Deni", "Chika", "Fatih"]
print(names)

data_siswa = ["Salsa", 12, True]
print(data_siswa)

animals = list(("fish", "cat", "Panda"))
print(animals)

animals[0] = "Dolphin" #updte list
print(animals)

animals.append("Frog") #add list
print(animals)

animals.remove("cat") #remove list
print(animals)

#tuple

fruits = ("apple", "banana", "cherry")
print(fruits)

buah = tuple(("appla", "banani", "cherro"))
print(buah)

print(fruits[1])

#fruits[2] = "watermelon" #error : item tupple tidak bisa diubah/manipulasi
#kalo mau diubh item tupple, kita ubah dulu ke list(konversi) kalo udah mu di lock ubah lagi ke tupple

fruits_list = list(fruits)
print(fruits_list)
fruits_list[2] = "watermelon"
print(fruits_list)

#klau mau di lock diubah ke tupple
fruits_tupple = tuple(fruits_list)
print(fruits_tupple)

#SET
numbers = {1,2,3,4,15,6,7} #set berfungsi untuk mengurutkan integral
print(numbers)

negara = set(("indonesia", "malaysia", "singapura")) #set tidak berurut
print(negara)

#print(negara[1]) #error : set tidk dpt diakses

name = "Alhazen"
letters = set(name)
print(letters)

negara.add("Laos")
print(negara)

negara.discard("Filipina")
print(negara)

negara.remove("singapura")
print(negara)

negara.pop()
print(negara)

#dictionary
employees = {
    "name" : "Joko",
    "Age" : 21,
    "Address" : "Jakarta",
    "status" : False
}
print(employees)

print(employees["Age"])
employees["Age"] = 22
print(employees)
employees["hobbies"] = "swimming"
print(employees)
employees.pop("status")
print(employees)