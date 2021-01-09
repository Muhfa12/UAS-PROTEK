#Project1

from datetime import *
import os

if(os.path.exists):
    modeFileTeks = "a"
else:
    modeFileTeks = "w"
fileTeks = open("DataKaryawan.dat", modeFileTeks)
def addKaryawan (Nip, Nama, Alamat, Gol, TglLahir, usiaKrywn):
    listDataKrywn = [Nip, Nama, Alamat, Gol, TglLahir, str(usiaKrywn) + "\n"]
    fileTeks.write("|".join(listDataKrywn))   
def getUsia(TglLahir):
    splited = TglLahir.split("-")
    thnLhrKrywn = int(splited[0])
    thnSkrg = datetime.now()
    usiaKrywn = thnSkrg.year - thnLhrKrywn
    return usiaKrywn
while True:
    Nip = input("Masukkan NIP                             : ")
    Nama = input("Masukkan Nama                            : ")
    Alamat = input("Masukkan Alamat                          : ")
    Gol = input("Masukkan Golongan ( A / B / C )          : ")
    if(Gol.lower() == "a" or Gol.lower() == "b" or Gol.lower() == "c"):
        TglLahir = input("Masukkan Tgl Lahir (Format : yyyy-mm-dd) : ")
        umurKrywn = getUsia(TglLahir)
        try:
            if(datetime.strptime(TglLahir, "%Y-%m-%d")):
                inginTambah = input("\nTambah data ( y / n)                     : ")
                if(inginTambah == "y" or inginTambah == "Y" ):
                    addKaryawan(Nip, Nama, Alamat, Gol, TglLahir, umurKrywn)
                    continue
                elif(inginTambah == "n" or inginTambah == "N" ):
                    addKaryawan(Nip, Nama, Alamat, Gol, TglLahir, umurKrywn)
                    break
                else:
                    print("Input tidak valid")
                    addKaryawan(Nip, Nama, Alamat, Gol, TglLahir, umurKrywn)
                    break
        except ValueError:
            print("Input tidak valid")
            continue
    else:
        print("Input tidak valid")
        continue

fileTeks.close()


