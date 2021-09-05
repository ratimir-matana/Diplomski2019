class Slagalica:
def __init__(self, slova, slova2):
self.slova = slova
self.slova2 = slova2

def __add__(self, drugi):           # ekvivalentno int._add__()
slova = self.slova + drugi.slova
slova2 = self.slova2 + drugi.slova2
s3 = Slagalica(slova, slova2)

return s3

def display(self):
print(self.slova)
print(self.slova2)


def main():
s1 = Slagalica('ban', 'ana')
s2 = Slagalica('ana', 'nas')

s3 = s1 + s2     # ekvivalentno Slagalica.__add__(s1, s2)

s3.display()


if __name__ == '__main__':
main()
