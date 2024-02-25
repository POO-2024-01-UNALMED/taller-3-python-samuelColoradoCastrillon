class Control:
    # Constructor
    def __init__(self, tv):
        self.tv = tv
    
    #Métodos
    def turnOn(self, estado):
        self.tv.estado = True
    def turnOff(self, estado):
        self.tv.estado = False
    def canalUp(self):
        if self.tv.canal < 120 and self.tv.estado:
            self.tv.canal += 1
    def canalDown(self):
        if self.tv.canal > 1 and self.tv.estado:
            self.tv.canal -= 1
    def setCanal(self, canal):
        if canal >= 1 and canal <= 120 and self.tv.estado:
            self.tv.canal = canal
    def volumenUp(self):
        if self.tv.volumen < 7 and self.tv.estado:
            self.tv.volumen += 1
    def volumenDown(self):
        if self.tv.volumen > 0 and self.tv.estado:
            self.tv.volumen -= 1
    def setVolumen(self, volumen):
        if volumen >= 0 and volumen <= 7 and self.tv.estado:
            self.tv.volumen = volumen
    def enlazar(self, tv):
        self.tv = tv
        self.tv.setControl(self)
    def getTv(self):
        return self.tv
    def setTv(self, tv):
        self.tv = tv