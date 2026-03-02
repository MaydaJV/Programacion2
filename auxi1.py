class Anime:
    def __init__(self, nombre: str, genero: str, nroEpisodios: int):
        self.nombre = nombre
        self.genero = genero
        self.nroEpisodios = nroEpisodios
        self.episodios = []

    def agregar_episodio(self, episodio: str):
        if len(self.episodios) < self.nroEpisodios:
            self.episodios.append(episodio)
        else:
            print("No se pueden agregar más episodios.")

    def __str__(self):
        return f"Anime: {self.nombre}, Género: {self.genero}, Episodios: {self.nroEpisodios}"


class Televisor:
    def __init__(self, marca: str = "", resolucion: int = 0, tipo: str = ""):
        self.marca = marca
        self.resolucion = resolucion
        self.tipo = tipo

    def __str__(self):
        return f"Televisor Marca: {self.marca}, Resolución: {self.resolucion}p, Tipo: {self.tipo}"


class Instrumento:
    def __init__(self, nombre: str, material: str, tipo: str):
        self.nombre = nombre
        self.material = material
        self.tipo = tipo

    def getnombre(self):
        return self.nombre

    def getmaterial(self):
        return self.material

    def gettipo(self):
        return self.tipo

    def setnombre(self, nombre):
        self.nombre = nombre

    def setmaterial(self, material):
        self.material = material

    def settipo(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"Instrumento: {self.nombre}, Material: {self.material}, Tipo: {self.tipo}"



class Principal:
    anime1 = Anime("Naruto", "Acción", 220)
    anime2 = Anime("Death Note", "Suspenso", 37)
    print(anime1)
    print(anime2)
    tv1 = Televisor("Samsung", 1080, "LED")
    tv2 = Televisor("LG", 4_000, "OLED")
    print(tv1)
    print(tv2)
    instrumento1 = Instrumento("Guitarra", "Madera", "Cuerda")
    instrumento2 = Instrumento("Flauta", "Metal", "Aire")
    print(instrumento1)
    print(instrumento2)