pkg = __import__('1174067_pandas')

loop=True 
while loop: 
    choice = input("Jawaban soal no [3-7]: ")
  
    if choice=='3':
        print("\n")
        no3 = pkg.ListModePandas()
    elif choice=='4':
        print("\n")
        pkg.DictModePandas()
    elif choice=='5':
        print("\n")
        pkg.DateFormatStandardDataFrame()
    elif choice=='6':
        print("\n")
        pkg.IndexColumn()
    elif choice=='7':
        print("\n")
        pkg.ChangeAttribute()
    else:
        break
        