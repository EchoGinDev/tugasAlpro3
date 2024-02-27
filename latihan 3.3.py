try:
    bulan = int(input("Masukkan bulan (1-12): "))
    a = 31
    b = 30
    c = 28

    if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 9 or bulan == 11:
        print("Jumlah_Hari :",a )
    elif bulan == 2:
        print("Jumlah_Hari :",c )
    elif bulan == 4 or bulan == 6 or bulan == 8 or bulan == 10 or bulan == 12:
        print("Jumlah_Hari :",b )
except ValueError:  
    print("masukkan angka 1-12")