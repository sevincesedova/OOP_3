class Hesabla:
    def my_list(self):
        return [2, 4, 6, 8, 10, 12]

    def sum(self, eded):
        mylist = self.my_list()
        return [(i, j) for i in range(len(mylist)) for j in range(i + 1, len(mylist)) if mylist[i] + mylist[j] == eded]

hesab = Hesabla()
listt = hesab.my_list()
print(f"List: {listt}")
eded = int(input("Ededi daxil edin: ")) 
cut = hesab.sum(eded)
if cut:
    for pair in cut:
       print(f"{eded} ededi listdeki {pair[0]}, {pair[1]} index'li ededlerin cemidir")
else:
    print(-1)
