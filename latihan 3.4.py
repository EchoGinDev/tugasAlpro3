try:
    
    sisi1 = int(input("masukkan sisi 1: "))
    sisi2 = int(input("masukkan sisi 2: "))
    sisi3 = int(input("masukkan sisi 3: "))

    if sisi1 == sisi2 and sisi2 == sisi3:
        print("3 sisi sama")
    elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
        print("2 sisi sama")
    else:
        print("tidak ada yang sama!!!")

except ValueError:
    print("format salah")