def toFile(list, x):
    print("Apakah anda ingin menyimpan hasil permainan? (Y/N)")
    choice = input()
    if choice == "Y" or choice == "y":
        filename = input("Masukkan nama file: ")
        path = "test/" + filename + ".txt"
        with open(path, 'w') as f:
            f.write(str(list[1]) + "\n")
            for i in range(x):
                f.write(list[0][i][0] + " ")
            f.write("\n")
            for i in range(x):
                f.write(str(list[0][i][1][0] + 1) + ", " + str(list[0][i][1][1] + 1) + "\n")
        print("Hasil permainan berhasil disimpan di " + path)
    print("Terima kasih telah menggunakan program ini!")