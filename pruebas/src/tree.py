'''
-María Álvarez Hernández
-Luis ALonso Calderón Achío
-Enrique Díaz Delgado
-Derian Sibaja Chavarría
'''
class Tree():
    def __init__(self, value):
        self.children = []
        self.value = value
    def addChild(self, otherTree):
        self.children.append(otherTree)

    def isLeaf(self):
        return len(self.children) == 0

    def printear(self, ident=""):
        print(f'{ident}{self.value}')
        for c in self.children:
            c.printear(ident + "    ")

    def __str__(self):
        return str(self.value) if self.isLeaf else f"{self.value}{str(self.children)}"