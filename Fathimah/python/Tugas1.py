buah = list(("apel", "jeruk", "pisang"))
buah.append("mangga")
buah.remove("jeruk")
print(buah)

mahasiswa = {
    "nama" : "budi",
    "umur" : 20,
    "jurusan" : "Informatika",
    "hobi" : ["berenang", "membaca"]
}

print(mahasiswa["nama"])
mahasiswa["umur"] = 21
mahasiswa["alamat"] = "Jakarta"
mahasiswa["hobi"].append("Coding")
print(mahasiswa)