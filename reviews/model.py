from functools import total_ordering

@total_ordering
class Ertekelesek:
    name: str
    _kov_telj: int
    __segito_k: int

    def __init__(self, name: str, kov_telj: int, segito_k: int = 3):
        self.name = name
        self._kov_telj = kov_telj
        self.__segito_k = segito_k

    @property
    def kov_telj(self):
        return self._kov_telj

    @kov_telj.setter
    def kov_telj(self, ertek):
        if ertek>=0:
            self._kov_telj = ertek
        else:
            print("Nemnegatív értéket adjon meg")

    @property
    def segito_k(self):
        return self.__segito_k

    @segito_k.setter
    def segito_k(self,ertek):
        if ertek >=0:
            self.__segito_k = ertek
        else:
            print("Nemnegatív értéket adjon meg")

    def __repr__(self)->str:
        return f"{self.name}, {self._kov_telj}, {self.__segito_k}"

    def __str__(self)->str:
        return f"{self.name} ({self._kov_telj} / {self.__segito_k})"

    def __eq__(self, other: object)->bool:
        if isinstance(other,Ertekelesek):
            return (self.name==other.name and self.__segito_k == other.__segito_k
                    and self._kov_telj==other._kov_telj)
        return False

    def __lt__(self, other)->bool:
        if not isinstance(other, Ertekelesek):
            return NotImplemented
        if self.name != other.name:
            return self.name < other.name  #növekvő
        elif self._kov_telj != other._kov_telj:
            return self._kov_telj > other._kov_telj  #csökk
        else:
            return self.__segito_k > other.__segito_k  #csökk

    @staticmethod
    def tanarok(ertekeles: list[Ertekelesek]):
        ls =[]
        for t in ertekeles:
            if ertekeles._kov_telj and ertekeles.__segito_k >3:
                ls.append(ertekeles.name)

        return ls



class Reszletes(Ertekelesek):
    __szexi: bool


    def __init__(self,name: str, kov_telj: int, segito_k: int, szexi: bool):
        super().__init__(name,kov_telj,segito_k)
        self.__szexi = szexi


    @property
    def szexi(self)->bool:
        return self.__szexi

    @szexi.setter
    def szexi(self, value):
        self.__szexi = value


    def __repr__(self)->str:
        return f"{super().__repr__()}, {self.__szexi}"


    def __str__(self)->str:
        return f"{super().__repr__()}: {self.__szexi}"

    




