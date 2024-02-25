class TV:
    # Atributos
    _numTV = 0

    # Constructor
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.precio = 500
        self.volumen = 1
        self.control = None

    # Métodos
    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self.marca = marca
    def getCanal(self):
        return self.canal
    def setCanal(self, canal):
        self.canal = canal
    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.precio = precio
    def getVolumen(self):
        return self.volumen
    def setVolumen(self, volumen):
        self.volumen = volumen
    def getControl(self):
        return self.control
    def setControl(self, control):
        self.control = control
    def getTV(self):
        return self.marca
    def setTV(self, _numTV):
        self._numTV = _numTV
    def getEstado(self):
        return self.estado
    def turnOn(self, estado):
        self.estado = True
    def turnOff(self, estado):
        self.estado = False
    def canalUp(self):
        if self.canal < 120 and self.estado:
            self.canal += 1
    def canalDown(self):
        if self.canal > 1 and self.estado:
            self.canal -= 1
    def volumenUp(self):
        if self.volumen < 7 and self.estado:
            self.volumen += 1
    def volumenDown(self):
        if self.volumen > 0 and self.estado:
            self.volumen -= 1