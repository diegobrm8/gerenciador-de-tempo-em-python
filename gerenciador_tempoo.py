import datetime


class GerenciadorDeTempo:
    def __init__(self):
        self.atividades = {}

    def iniciar_atividade(self, nome_atividade):
        if nome_atividade not in self.atividades:
            self.atividades[nome_atividade] = {'hora_inicio': datetime.datetime.now(), 'hora_fim': None}

    def parar_atividade(self, nome_atividade):
        if nome_atividade in self.atividades and self.atividades[nome_atividade]['hora_fim'] is None:
            self.atividades[nome_atividade]['hora_fim'] = datetime.datetime.now()

    def tempo_total_atividade(self, nome_atividade):
        if nome_atividade in self.atividades:
            hora_inicio = self.atividades[nome_atividade]['hora_inicio']
            hora_fim = self.atividades[nome_atividade]['hora_fim'] if self.atividades[nome_atividade][
                'hora_fim'] else datetime.datetime.now()
            return hora_fim - hora_inicio
        else:
            return datetime.timedelta(0)

    def gerar_relatorio(self):
        tempo_total_por_atividade = {}
        for atividade, tempos in self.atividades.items():
            tempo_total_por_atividade[atividade] = self.tempo_total_atividade(atividade)
        return tempo_total_por_atividade

    def imprimir_relatorio(self):
        relatorio = self.gerar_relatorio()
        for atividade, tempo in relatorio.items():
            print(f"Atividade: {atividade} - Tempo total: {tempo}")


gerenciador = GerenciadorDeTempo()

gerenciador.iniciar_atividade("Estudar Python")
gerenciador.parar_atividade("Estudar Python")
print("\nRelatório de Atividades:")
gerenciador.imprimir_relatorio()
