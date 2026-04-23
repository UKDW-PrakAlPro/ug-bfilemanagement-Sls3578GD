def cari_buku(daftar_judul, hanya_tersedia=False):
    
    handle = open("buku.txt", "r")
    for line in handle:
        line = line.strip()
        judul, status, author, tahun = line.split(",")
        tahun = tahun.strip()
        author = author.strip()
        judul = judul.strip()
        status = status.strip()
        
        if line(judul, daftar_judul):
            if hanya_tersedia:
                if status == "tersedia":
                    print(f"Judul : ",{judul})
                    print(f"Penulis : ",{author})
                    print(f"Tahun : ",{tahun})
                    print(f"Status : ",{status})
                    
                else:
                    print(f"Judul : ",{judul})
                    print(f"Penulis : ",{author})
                    print(f"Tahun : ",{tahun})
                    print(f"Status : ",{status})
                    
            else:
                print(f"Judul : ",{judul})
                print(f"Penulis : ",{author})
                print(f"Tahun : ",{tahun})
                print(f"Status : ",{status})

        return 

# TEST CASE DI BAWAH JANGAN DIUBAH YA!!!
cari_buku(["python", "data", "cihuy"])
print("\n"+"-"*30+"\n")
cari_buku(["cyber", "learning"], hanya_tersedia=True)
print("\n"+"-"*30+"\n")
cari_buku(["system", "code"])
print("\n"+"-"*30+"\n")
cari_buku(["data"], hanya_tersedia=True)
print("\n"+"-"*30+"\n")
cari_buku(["Blockchain", "Quantum"])
print("\n"+"-"*30+"\n")
cari_buku(["bAsIcS","cOncEPTs"])





















#ifthiswrongthensobeit
#  |
#  |
#  o
# /|\
# / \
#illhanfmyselftommorrow