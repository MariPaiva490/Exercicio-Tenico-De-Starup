import random  # Módulo para sorteios aleatórios (como o "Shark Fight")

# Classe que representa uma startup
class Startup:
    def __init__(self, nome, slogan, ano):
        # Atributos principais da startup
        self.nome = nome
        self.slogan = slogan
        self.ano = ano
        self.pontos = 70  # Toda startup começa com 70 pontos

        # Estatísticas dos eventos recebidos durante o torneio
        self.estatisticas = {
            'pitch': 0,
            'bugs': 0,
            'tracao': 0,
            'investidor': 0,
            'fake_news': 0,
            'seguranca_dados': 0
        }

    # Método para aplicar os efeitos de um evento na pontuação
    def aplicar_evento(self, evento):
        eventos = {
            'pitch': 6,        # Pitch convincente
            'bugs': -4,        # Produto com bugs
            'tracao': 3,       # Boa tração de usuários
            'investidor': -6,  # Investidor irritado
            'fake_news': -8,
            'seguranca_dados': 8    # Fake news no pitch
        }
        if evento in eventos:
            self.pontos += eventos[evento]          # Aplica o efeito na pontuação
            self.estatisticas[evento] += 1          # Atualiza a estatística

# A função que ira servir para cadastrar as startups
def cadastrar_startups():
    startups = []
    print(" Cadastro de Startups (mínimo 4, máximo 8 — só pares)")

    while True:
        nome = input("Nome da startup: ")
        
        slogan = input("Slogan (frase relacionada à startup): ")

        while True:
            ano = input("Ano de fundação: ")
            if ano.isdigit() and len(ano) == 4:  # Se atingir mais que 4 digitos ele ira avisar e perguntar novamente
                break
            print(" Ano deve conter exatamente 4 dígitos númericos.") 
        startups.append(Startup(nome, slogan, ano))

        total = len(startups)

        # Se atingir o máximo, encerra
        if total == 8:
            print("Máximo de 8 atingido. Prosseguindo.")
            break

        # Se chegar a 4 ou 6, pergunta se quer adicionar mais
        if total in (4, 6):
            cont = input(f"Você cadastrou {total}. Quer adicionar mais? (s/n): ").strip().lower()
            if cont == 'n':
                break
            # se for 's', continua o loop para chegar a 6 ou 8

            # Serve para que o print apareça somente até o 4, chegando ao 4 ele encerra
        elif total < 4:
            faltam = 4 - total
            print(f"Ainda faltam {faltam} para o mínimo de 4.")

    return startups

# Função que administra uma batalha entre duas startups
def administrar_batalha(s1, s2):
    print(f"\nBatalha: {s1.nome} VS {s2.nome}")
    print(f"{s1.nome}: {s1.pontos} pontos")
    print(f"{s2.nome}: {s2.pontos} pontos")

    # Lista de eventos possíveis
    eventos = ['pitch', 'bugs', 'tracao', 'investidor', 'fake_news', 'seguranca_dados']

    # Para cada startup na batalha, ira perguntar quais eventos ocorreram
    for s in [s1, s2]:
        print(f"\nEventos para {s.nome}:")
        for evento in eventos:
            aplicar = input(f"{evento.replace('_', ' ').title()}? (s/n): ").lower()
            if aplicar == 's':
                s.aplicar_evento(evento)

    # Verifica se houve empate
    if s1.pontos == s2.pontos:
        print("Empate! Shark Fight ativada!")
        escolhida = random.choice([s1, s2])  # Escolhe uma startup aleatória para ganhar 2 pontos
        escolhida.pontos += 2
        print(f"{escolhida.nome} recebeu +2 pontos!")

    # Determina o vencedor com maior pontuação
    vencedor = s1 if s1.pontos > s2.pontos else s2
    vencedor.pontos += 30  # Bônus por vitória
    print(f"\n {vencedor.nome} venceu a batalha e ganhou +30 pontos!\n")
    return vencedor

# Função que gerencia todas as rodadas do torneio
def torneio(startups):
    rodada = 1  # Contador de rodadas
    while len(startups) > 1:
        print(f"\n Rodada {rodada}")
        random.shuffle(startups)  # Embaralha as startups para sorteio dos pares
        vencedores = []
        for i in range(0, len(startups), 2):
            vencedor = administrar_batalha(startups[i], startups[i+1])  # Duplas batalham
            vencedores.append(vencedor)
        startups = vencedores  # Avançam para próxima rodada
        rodada += 1
    return startups[0]  # Retorna a campeã

# Gera um relatório com as estatísticas de todas as startups
def relatorio(finalistas):
    print("\n Resultado Final do Torneio \n")
    # Ordena por pontuação final
    finalistas.sort(key=lambda x: x.pontos, reverse=True)
    for s in finalistas:
        print(f"{s.nome}: {s.pontos} pontos")
        print(f"   Pitch: {s.estatisticas['pitch']} | Bugs: {s.estatisticas['bugs']} | Boa tração de usuários: {s.estatisticas['tracao']}")
        print(f"   Investidor irritado: {s.estatisticas['investidor']} | Fake News: {s.estatisticas['fake_news']} | Segurança nos dados: {s.estatisticas['seguranca_dados']}")
    # Exibe o slogan da campeã
    print(f"\n Campeã: {finalistas[0].nome} - \"{finalistas[0].slogan}\"")

# Função principal que organiza todo o processo
def main():
    participantes = cadastrar_startups()            # Cadastro de startups
    original_participantes = participantes.copy()   # Guarda todos para relatório final
    campea = torneio(participantes)                # Inicia o torneio
    relatorio(original_participantes)              # Mostra os resultados

# Inicia o programa
if __name__ == "__main__":
    main()
