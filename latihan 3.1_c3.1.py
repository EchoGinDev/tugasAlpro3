try:
    pembelian = int(input("Pembelian = "))
    if pembelian > 100000:
        print("True")
    elif pembelian < 100000:
        print("False")
    elif pembelian == 100000:
        print("True")
except ValueError:
     print("Format yang anda masukkan salah")