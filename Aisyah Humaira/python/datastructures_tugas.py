#Soal 1
buah = ["Apel", "Jeruk", "Pisang"]
buah.append("Mangga")
buah.remove("Jeruk")
print(buah)

#Soal 2
mahasiswa = {
    "nama" : "Budi",
    "umur" : 20,
    "jurusan" : "Informatika",
    "hobi" : ["Berenang", "Membaca"]
}
print(mahasiswa["nama"])
mahasiswa["umur"] = 21
mahasiswa["alamat"] = "Jakarta"
mahasiswa["hobi"].append("Coding")
print(mahasiswa)