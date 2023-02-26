class Marca:
#++++++++++++ atributos y constructor +++++++++++++
    def __init__(self,nombre):
        self._nombre = nombre
#++++++++++++ metodos de acceso +++++++++++++
    def getNombre(self):
        return self._nombre
    def setNombre(self, name):
        self._nombre = name