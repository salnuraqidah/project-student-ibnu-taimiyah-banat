score = 60
kkm = 75

if score >= kkm:
    print("Selamat! Anda Lulus")
else:
    print("Yah gembel!")

    nilai = 100

    # <=70 : C
    # 70 - 80 : B
    # >= 80 : A

    if nilai >= 80:
        print("Grade A")
    elif nilai >= 70 and nilai < 80:
        print("Grade B")
    else:
        print("Grade C")

for f in range(17):
    print("Capybara is here!")
    print(f)

y = 1

while y <= 5:
    print("Capyyy")
    y+=1

score = int(input("Masukaan score anda"))

if score >= 85:
     print("Grade A")
elif score >= 70 and score < 85:
     print("Grade B")
elif score >=50 and score < 70:
     print("Grade C")
else:
     print("Grade D")