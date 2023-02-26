class Control:
#+++++++++ Constructor +++++++++++++
    def __init__(self):
        self._tv = None
    
    def getTV(self):
        return self._tv
    def setTV(self, tv):
        self._tv = tv
#++++++++ metodos de acceso para el TV +++++++++
    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown()

    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()

    def volumenUp(self):
        self._tv.volumenUp()
    def volumen(self):
        self._tv.volumenDown()
    
    def setCanal(self, num5):
        self._tv.setCanal(num5)
#+++++++++ Enlazar +++++++++++++++++
    def enlazar(self, tv):
        self._tv = tv
        self._tv.setControl(self)