class porta():

    def __init__(self):
        self.estadoAtual = False

    def estadoGet(self):
        return self.estadoAtual

    def estadoSet(self, estado):
        self.estadoAtual = estado
