score = 60
min_criteria = 75

if score == min_criteria:    #berikn indentasi/satu kli tab
    print("Anda Berhasil Naik Level")
else:
    print("Nilai Kamu Kurang dari Kkm")

nilai = 70

#<= 70 : c
# 70 - 80 : B
#>= 80 : A

if nilai >= 80:
    print("Grade A")
elif nilai >= 70 and nilai < 80:
    print("Grade B")
else:
    print("Grade C")

for i in range(10):
    print("Hello World")
    print(i)