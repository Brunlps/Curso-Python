# Classe principal
class Televisao:
    # construtor: onde cosntrimos os atributos da classe
    def __init__(self):
        self.ligada = False
        self.canal = 2

    # Métodos da classe
    def mudar_canal_para_baixo(self):
        self.canal -= 1

    def mudar_canal_para_cima(self):
        self.canal += 1

   
# Objeto que recebe a classe principal.
tv = Televisao()
tv.mudar_canal_para_baixo()
tv.mudar_canal_para_cima()
tv.canal