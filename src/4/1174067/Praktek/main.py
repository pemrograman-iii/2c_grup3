pkg = __import__('1174067_csv')

loop=True 
while loop: 
    choice = input("Jawaban Soal No.[1/2, 8] : ")
  
    if choice=='1':
        print("\n")
        no3 = pkg.ListMode()
        print("\n")
    elif choice=='2':
        print("\n")
        no2 = pkg.DictMode()
        print("\n")
    elif choice=='8':
        print("\n")
        no2 = pkg.Write()
        print("\n")
    else:
        break
        