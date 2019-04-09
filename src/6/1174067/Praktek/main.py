lib = __import__('1174067_bar')
lib1 = __import__('1174067_pie')
lib2 = __import__('1174067_scatter')
lib3 = __import__('1174067_plot')


npm = input("NPM : ")
mod = int(npm)%3+2
print(mod)

if mod == 4:
    lib.barChart()    
    lib1.pieChart()
    lib2.scatterChart()
    lib3.plotChart()
else:
    exit()
