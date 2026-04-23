def skorpertandingan(filename):
    
    filename = print(input("Masukkan nama file: "))
    handle = open(filename, 'r')

    for line in handle:
        line = line.strip()
        opponent1, score1, score2, opponent2 = line.split(",")
        if int(score1) > int(score2):
            print(opponent1)
        elif int(score1) < int (score2):
            print(opponent2)
        else:
            print("Draw")

    return