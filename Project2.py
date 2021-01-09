#Project2
fileTeks = open("DataKaryawan.dat", "r")
isiTeks = fileTeks.readlines()

kodeKrywn = input("Masukkan Kode Karyawan : ")
try :    
    for i in range(len(isiTeks)):
        if (kodeKrywn in isiTeks[i]):
            ganti = isiTeks[i].replace("\n", "")
            hapus = ganti.split("|")
    dataKrywn = {kodeKrywn : [hapus[1], hapus[2], hapus[3], hapus[4], hapus[5]]}
    if(dataKrywn[kodeKrywn][2] == "A"):
        gajipokok = 4000000
    elif(dataKrywn[kodeKrywn][2] == "B"):
        gajipokok = 4500000
    else:
        gajipokok = 5000000
    print("\nKode Karyawan          :", kodeKrywn)
    print("Nama Karyawan          :", dataKrywn[kodeKrywn][0])
    print("Alamat Karyawan        :", dataKrywn[kodeKrywn][1])        
    print("Golongan Karyawan      :", dataKrywn[kodeKrywn][2])
    print("Gaji Pokok Karyawan    : Rp.", gajipokok)
    print("Tanggal Lahir Karyawan : {0} (Usia: {1} Tahun) ".format(dataKrywn[kodeKrywn][3], dataKrywn[kodeKrywn][4]))

except Error:
    print("Data Karyawan Tidak Ditemukan / Data Tidak Valid")

