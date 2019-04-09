import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [7, 8, 9, 0, 1, 2]
    
def plotChart():
    sub, (sp1, sp2, sp3, sp4) = plt.subplots(4)
    sp1.plot(x, y)
    sp2.plot(x, y)
    sp3.plot(x, y)
    sp4.plot(x, y)
    sub.subplots_adjust(hspace=0)
    plt.show()
