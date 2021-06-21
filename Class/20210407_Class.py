from matplotlib import pyplot as plt


plt.plot(["first : Alex", "second : Fiona", "third : Lex"], [123, 321, 213])
y = [18, 21, 24]
x = range(len(y))
plt.bar(x, y, width = 0.1, color = "darkgray")
plt.xlabel('Player Number')
plt.ylabel('Player Point')
plt.title("The Game Point Notice Board")
plt.legend(['Point', 'age'])
plt.show()
