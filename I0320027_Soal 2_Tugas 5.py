nama_mhs = input("Masukkan nama mahasiswa : ")
nilai = float(input('Masukkan nilai mahasiswa : '))

if nilai >= 85:
    print("Halo, %s! Nilai anda setelah dikonversi adalah A" % nama_mhs)
elif nilai >= 80:
    print("Halo, %s! Nilai anda setelah dikonversi adalah A-" % nama_mhs)
elif nilai >= 75:
    print("Halo, %s! Nilai anda setelah dikonversi adalah B+" % nama_mhs)
elif nilai >= 70:
    print("Halo, %s! Nilai anda setelah dikonversi adalah B" % nama_mhs)
elif nilai >= 65:
    print("Halo, %s! Nilai anda setelah dikonversi adalah C+" % nama_mhs)
elif nilai >= 60:
    print("Halo, %s! Nilai anda setelah dikonversi adalah C" % nama_mhs)
elif nilai < 60:
    print("Halo, %s! Nilai anda setelah dikonversi adalah E" % nama_mhs)
else:
    pass