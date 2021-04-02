nama_Pengunjung = input("Masukkan nama pengunjung : ")
jenis_kelamin = input('Masukkan jenis kelamin pengunjung [L/P]')

if jenis_kelamin == "L":
    print("Selamat datang, Tuan %s!" % nama_Pengunjung)
else:
    print("Selamat datang, Nyonya %s!" % nama_Pengunjung)