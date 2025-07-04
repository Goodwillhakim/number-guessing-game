import random

#INPUT

print("=" *41)
print("            Game Tebak Angka")
print("=" *41)
print("Saya Mempunyai Angka 1-100 ")
Angka_Rahasia = random.randint (1,100)
tebakan = None
jumlah_tebakan = 0

#PROSES

while tebakan != Angka_Rahasia:
    try:
        tebakan = int(input("Tebak Angka Rahasia: "))
        jumlah_tebakan += 1
        if tebakan > Angka_Rahasia :
            print("Tebakan Terlalu Besar")
        elif tebakan < Angka_Rahasia :
            print(" Tebakan Terlalu Kecil") 
        else :
            print(f"Tebakan Anda Benar, Anda Menebak {jumlah_tebakan} kali")
    except ValueError :
        print("Masukan Angka Yang Valid")        

