class Televisao:
    # Passando parâmetros
    def __init__(self, canal_max, canal):
        self.ligada = False
        self.canal = canal
        self.canal_max = canal_max
        self.historico = []

    # Métodos para mudar o canal
    def mudar_canal_baixo(self):
        # uma condição para diminuir o canal
        # sem que ele chegue em número menores que o inicado
        if self.canal - 1 >= self.canal_min:
            self.historico.append(self.canal)
            self.canal -= 1

    def mudar_canal_cima(self):
        # condicional para aumentar o valor do canal
        # em que ele ultrapasse o número máximo de canais
        if self.canal + 1 <= self.canal_max:
            self.historico.append(self.canal)
            self.canal += 1

    def voltar_canal(self):
        if self.historico:
            self.canal = self.historico.pop()
        else:
            print("Sem histórico para voltar")

    def __str__(self):
        return f"Canal atual: {self.canal} | Histórico: {self.historico}"
