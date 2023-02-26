class TV:
#+++++++++ metodo contador +++++++++++++++++++
    _numTV = 0
    @classmethod
    def getNumTV(cls):
        return cls._numTV
    @classmethod
    def setNumTV(cls,num0):
        cls._numTV = num0
#++++++++++ init y constructor ++++++++++++
    def __init__(self, marca, estado):
        self._marca = marca; self._estado = estado
        self._canal = 1; self._precio = 500
        self._volumen = 1; self._control = None
        TV._numTV += 1
#++++++++ metodos de acceso +++++++++++++++++
    def getMarca(self):
        return self._marca
    def setMarca(self, marca):
        self._marca = marca
#--------------------------------------------
    def getEstado(self):
        return self._estado
    def setEstado(self, estado):
        self._estado = estado
#--------------------------------------------
    def getCanal(self):
        return self._canal
    def setCanal(self, num1):
        if (self._estado == True):
            if (num1 >= 1 and num1 <= 120):
                self._canal = num1
#--------------------------------------------
    def getPrecio(self):
        return self._precio
    def setPrecio(self, num2):
        self._precio = num2
#--------------------------------------------
    def getVolumen(self):
        return self._volumen
    def setVolumen(self, num3):
        if (self._estado == True):
            if (num3 >= 0 and num3 <= 7):
                self._volumen = num3
#--------------------------------------------
    def getControl(self):
        return self._control
    def setControl(self, control):
        self._control = control
#+++++++++++ encedido y apagado +++++++++++++++++
    def turnOn(self):
        self._estado = True
    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado
#++++++++++ Cambio de Canal ++++++++++++++++++++
    def canalUp(self):
        if (self._estado == True):
            if (self._canal < 120):
                self._canal += 1
    
    def canalDown(self):
        if (self._estado == True):
            if (self._canal > 1):
                self._canal -= 1
#++++++++++ Cambio de volumen ++++++++++++++++++
    def volumenUp(self):
        if (self._estado == True):
            if (self._volumen < 7):
                self._volumen += 1
    def volumenDown(self):
        if (self._estado == True):
            if (self._volumen > 0):
                self._volumen -= 1
