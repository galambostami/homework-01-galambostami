import sys
from reviews import model

def main()->None:
    try:
        n = int(sys.argv[1])
        if n <= 0:
            raise ValueError("Az argumentumnak pozitív számnak kell lennie.")

        ertekelesek = []
        for c in range(n):
            line = input()
            tokens = line.split(";")

            if len(tokens)==4:
                ertekeles = Ertekelesek(tokens[0], tokens[1], tokens[2])
                ertekelesek.append(ertekeles)
            else:
                reszlet = Reszletes(tokens[0], tokens[1, tokens[2], bool(tokens[3]))
                ertekelesek.append(reszlet)

        ertekelesek.sort()
        for ertek in ertekelesek:
            print(ertek)

if __name__=='__main__':
    main()