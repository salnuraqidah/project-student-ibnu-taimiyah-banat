nilai = int(input("Masukkan nilai Anda : "))

if nilai >= 85:
    print("Grade is A")
elif nilai >= 70 and nilai < 85:
    print("Grade is B")
elif nilai >= 50 and nilai < 70:
    print("Grade is C")
else:
    print("Grade is D")