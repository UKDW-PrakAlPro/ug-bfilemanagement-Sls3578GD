import re
"""
Soal :
Cari Teks di Dalam Nada.txt yang Diampit oleh "
Contoh:

Pak Wombat, mengajarkan gerakan pertama: "Goyang Eucalyptus".
Aku sudah bisa melakukan "Lompat Pohon"

output = '"Goyang Eucalyptus","Lompat Pohon"'
Dalam bentuk String

Hint :
BisaFungsi String startswith('"') atau j.endswith('"') untuk menemukan awalan dan akhiran
"""
def gerakan(filename):
    
    filename = print(input("Masukkan nama file: "))
    handle = open(filename, 'r')

    for line in handle:
        if handle == "Nada1.txt":    
            line = line.strip()
            if line.startswith('"') or line.endswith('"'):
                print(f"Nada1" ,{line})
        
        if handle == "Nada2.txt":    
            line = line.strip()
            if line.startswith('"') or line.endswith('"'):
                print(f"Nada2" ,{line})

        if handle == "Nada3.txt":    
            line = line.strip()    
            if line.startswith('"') or line.endswith('"'):
                print(f"Nada3" ,{line})

        if handle == "Nada4.txt":    
            line = line.strip()    
            if line.startswith('"') or line.endswith('"'):
                print(f"Nada4" ,{line})
        
    return