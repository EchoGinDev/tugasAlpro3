inputan = input("masukkan usian anda :")

try:
    usia = int(inputan)
    if usia <= 5:
        print("Balita")
    elif usia >= 6 and usia <= 11:
        print("Kanak-kanak")
    elif usia >=12 and usia <= 25:
        print("Remaja")
    elif usia >= 26 and usia <= 45:
        print("Dewasa")
    elif usia >=45 and usia <= 69:
        print("Lansia")
    elif usia > 70:
        print("Leluhur")
except ValueError:
    print("Format yang anda masukkan salah")