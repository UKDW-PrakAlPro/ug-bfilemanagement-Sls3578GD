import KoalaMenari

Test = {
    "Nada1":['"Goyang Eucalyptus","Lompat Pohon","Pelukan Bambu"'],
    "Nada2":['"Petik Senar","Gesek Pelan","Tiup Lembut"'],
    "Nada3":['"Berdiri Anggun","Guling Depan","Jungkir Balik","Ayun Pita"'],
    "Nada4":['"Sapuan Kuas","Cipratan Warna","Gores Dalam"']
}
def test():
    nilai = 0
    for i in range(1,5):
        filename = f"Nada{i}.txt"
        hasil = KoalaMenari.gerakan(filename)
        
        isCorrect = '✅' if hasil == Test[filename[0:-4]][0] else '❌'
        if isCorrect == '✅':
            nilai += 25
        print(f"Test {i}:  {isCorrect} ")
    print(f"Nilai Kamu: {nilai}")
        
if __name__ == "__main__":
    test()