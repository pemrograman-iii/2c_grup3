pkg = __import__('1174067_pandas')

loop=True 
while loop: 
    choice = input("Jawaban Soal No.[3-7, 9]: ")
  
    if choice=='3':
        print("\n")
        no3 = pkg.ListModePandas()
        print("\n")
    elif choice=='4':
        print("\n")
        pkg.DictModePandas()
        print("\n")
    elif choice=='5':
        print("\n")
        pkg.DateFormatStandardDataFrame()
        print("\n")
    elif choice=='6':
        print("\n")
        pkg.IndexColumn()
        print("\n")
    elif choice=='7':
        print("\n")
        pkg.ChangeAttribute()
        print("\n")
    elif choice=='9':
        print("\n")
        pkg.WritePandas()
        print("\n")
    else:
        break
        