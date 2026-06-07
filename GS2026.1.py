"""
Mission Control AI
Sistema de Monitoramento de Missão Espacial
Global Solution 2026 | FIAP - Pensamento Computacional e Automação com Python
"""

import random


#  Identificação da missão

NOME_MISSAO = "USG Ishimura"
NOME_EQUIPE = "Equipe Anesidora"


#  Áreas monitoradas (mesma ordem das colunas)

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]


#  Geração aleatória da matriz da missão
#  Cada linha = 1 ciclo
#  Colunas: [temperatura, comunicacao, bateria, oxigenio, estabilidade]

def gerar_ciclo_estavel():
    return [
        random.randint(18, 30),    # temperatura normal
        random.randint(60, 100),   # comunicação normal
        random.randint(50, 100),   # bateria normal
        random.randint(90, 100),   # oxigênio normal
        random.randint(70, 100),   # estabilidade normal
    ]

def gerar_ciclo_atencao():
    return [
        random.randint(31, 35),    # temperatura em atenção
        random.randint(30, 59),    # comunicação em atenção
        random.randint(20, 49),    # bateria em atenção
        random.randint(80, 89),    # oxigênio em atenção
        random.randint(40, 69),    # estabilidade em atenção
    ]

def gerar_ciclo_critico():
    return [
        random.randint(36, 45),    # temperatura crítica
        random.randint(10, 29),    # comunicação crítica
        random.randint(10, 19),    # bateria crítica
        random.randint(70, 79),    # oxigênio crítico
        random.randint(10, 39),    # estabilidade crítica
    ]

def gerar_dados_missao():

    narrativas = [
        # Piora progressiva: começa bem, termina mal
        [
            gerar_ciclo_estavel(),
            gerar_ciclo_estavel(),
            gerar_ciclo_atencao(),
            gerar_ciclo_atencao(),
            gerar_ciclo_critico(),
            gerar_ciclo_critico(),
        ],
        # Crise no meio: começa bem, piora, tenta recuperar
        [
            gerar_ciclo_estavel(),
            gerar_ciclo_atencao(),
            gerar_ciclo_critico(),
            gerar_ciclo_critico(),
            gerar_ciclo_atencao(),
            gerar_ciclo_estavel(),
        ],
        # Caos desde o início: começa crítico, recuperação parcial
        [
            gerar_ciclo_critico(),
            gerar_ciclo_critico(),
            gerar_ciclo_atencao(),
            gerar_ciclo_estavel(),
            gerar_ciclo_atencao(),
            gerar_ciclo_critico(),
        ],
    ]
    return random.choice(narrativas)

dados_missao = gerar_dados_missao()



#  Funções de análise por área

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura abaixo do ideal"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif valor < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif valor < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif valor < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif valor < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(pontuacao, resultados):
    if pontuacao == 0:
        return "Manter operação normal e continuar monitoramento."

    criticos = []
    if resultados[0][0] == "CRÍTICO":
        criticos.append("Verificar controle térmico da missão")
    if resultados[1][0] == "CRÍTICO":
        criticos.append("Tentar restabelecer contato com a base")
    if resultados[2][0] == "CRÍTICO":
        criticos.append("Ativar modo de economia de energia")
    if resultados[3][0] == "CRÍTICO":
        criticos.append("Acionar protocolo de suporte à vida")
    if resultados[4][0] == "CRÍTICO":
        criticos.append("Reduzir operações não essenciais")

    if len(criticos) >= 3:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."
    elif criticos:
        return criticos[0] + "."
    else:
        return "Monitorar sistemas em atenção e preparar plano de contingência."


def analisar_tendencia(riscos):
    if riscos[-1] > riscos[0]:
        return "A missão apresentou tendência de piora."
    elif riscos[-1] < riscos[0]:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontos_por_area):
    maior = max(pontos_por_area)
    indice = pontos_por_area.index(maior)
    return areas_monitoradas[indice]


def gerar_relatorio_final(riscos, pontos_por_area, medias):
    ciclo_critico = riscos.index(max(riscos)) + 1
    risco_medio   = sum(riscos) / len(riscos)
    qtd_criticos  = sum(1 for r in riscos if r >= 6)
    tendencia     = analisar_tendencia(riscos)
    area_afetada  = identificar_area_mais_afetada(pontos_por_area)

    classificacao_final = classificar_ciclo(round(risco_medio))

    print("=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão : {NOME_MISSAO}")
    print(f"Equipe : {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(riscos)}")
    print()
    print(f"Média de temperatura  : {medias[0]:.2f} °C")
    print(f"Média de comunicação  : {medias[1]:.2f}%")
    print(f"Média de bateria      : {medias[2]:.2f}%")
    print(f"Média de oxigênio     : {medias[3]:.2f}%")
    print(f"Média de estabilidade : {medias[4]:.2f}%")
    print()
    print(f"Ciclo mais crítico       : Ciclo {ciclo_critico}")
    print(f"Maior pontuação de risco : {max(riscos)}")
    print(f"Risco médio da missão    : {risco_medio:.2f}")
    print(f"Ciclos críticos          : {qtd_criticos}")
    print()
    print(f"Tendência da missão: {tendencia}")
    print()
    print("Pontuação acumulada por área:")
    for i in range(len(areas_monitoradas)):
        print(f"  {areas_monitoradas[i]}: {pontos_por_area[i]} pontos")
    print()
    print(f"Área mais afetada: {area_afetada}")
    print()
    print(f"Classificação final da missão: {classificacao_final}")
    print()

    if classificacao_final == "MISSÃO CRÍTICA":
        conclusao = ("A missão enfrentou situações de alto risco. "
                     "É necessário acionar protocolos de emergência.")
    elif classificacao_final == "MISSÃO EM ATENÇÃO":
        conclusao = ("A missão apresentou instabilidade relevante durante a operação. "
                     "A equipe deve manter o plano de contingência ativo.")
    else:
        conclusao = ("A missão foi concluída dentro dos parâmetros de segurança. "
                     "Continuar monitoramento preventivo.")

    print(f"Conclusão: {conclusao}")
    print("=" * 60)



#  Execução principal

def main():
    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missão  : {NOME_MISSAO}")
    print(f"Equipe  : {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)

    riscos          = []
    pontos_por_area = [0, 0, 0, 0, 0]
    somas           = [0, 0, 0, 0, 0]

    for i in range(len(dados_missao)):
        ciclo        = dados_missao[i]
        numero_ciclo = i + 1

        temperatura  = ciclo[0]
        comunicacao  = ciclo[1]
        bateria      = ciclo[2]
        oxigenio     = ciclo[3]
        estabilidade = ciclo[4]

        res_temp = analisar_temperatura(temperatura)
        res_com  = analisar_comunicacao(comunicacao)
        res_bat  = analisar_bateria(bateria)
        res_oxi  = analisar_oxigenio(oxigenio)
        res_est  = analisar_estabilidade(estabilidade)

        resultados = [res_temp, res_com, res_bat, res_oxi, res_est]

        pontuacao = sum(r[1] for r in resultados)
        riscos.append(pontuacao)

        for j in range(5):
            pontos_por_area[j] += resultados[j][1]

        somas[0] += temperatura
        somas[1] += comunicacao
        somas[2] += bateria
        somas[3] += oxigenio
        somas[4] += estabilidade

        classificacao = classificar_ciclo(pontuacao)
        recomendacao  = gerar_recomendacao(pontuacao, resultados)

        print(f"\nCICLO {numero_ciclo}")
        print("-" * 60)
        print(f"Temperatura  : {temperatura} °C  | {res_temp[0]} | {res_temp[2]}")
        print(f"Comunicação  : {comunicacao}%    | {res_com[0]} | {res_com[2]}")
        print(f"Bateria      : {bateria}%         | {res_bat[0]} | {res_bat[2]}")
        print(f"Oxigênio     : {oxigenio}%        | {res_oxi[0]} | {res_oxi[2]}")
        print(f"Estabilidade : {estabilidade}%    | {res_est[0]} | {res_est[2]}")
        print(f"Pontuação de risco do ciclo: {pontuacao}")
        print(f"Classificação do ciclo: {classificacao}")
        print(f"Recomendação: {recomendacao}")

    qtd = len(dados_missao)
    medias = [somas[j] / qtd for j in range(5)]

    print()
    gerar_relatorio_final(riscos, pontos_por_area, medias)


if __name__ == "__main__":
    main()