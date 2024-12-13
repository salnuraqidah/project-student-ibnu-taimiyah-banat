print("SOAL 1")

buah = ["apel", "jeruk", "pisang"]
print(buah)

buah.append("mangga")
print(buah)

buah.remove("jeruk")
print(buah)

print("SOAL 2")

data_mahasiswa = {
    "nama" : "Budi",
    "umur" : 20,
    "jurusan" : "Informatika",
    "hobi" : ["berenang", "membaca"]
}
print(data_mahasiswa)

print(data_mahasiswa["nama"])
data_mahasiswa["umur"] = 21
print(data_mahasiswa)
data_mahasiswa["alamat"] = "Jakarta"
data_mahasiswa["hobi"].append("Coding")
print(data_mahasiswa)