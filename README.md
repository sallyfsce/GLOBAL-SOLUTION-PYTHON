# Mission Control AI

Sistema de monitoramento de missão espacial desenvolvido em Python.

**Global Solution 2026 | FIAP — Pensamento Computacional e Automação com Python**

---

## Descrição

O projeto simula o monitoramento de uma missão espacial experimental dividida em ciclos. A cada ciclo, o sistema analisa cinco áreas operacionais, calcula o risco, gera alertas automáticos e no final exibe um relatório completo da missão.

---

## Como executar

Pré-requisito: Python 3.10 ou superior. Sem dependências externas.

```bash
python mission_control.py
```

---

## Estrutura do projeto

```
mission-control-ai/
├── README.md
└── mission_control.py
```

---

## Estrutura dos dados

A variável `dados_missao` é uma lista de listas. Cada linha representa um ciclo da missão e cada coluna representa uma área monitorada, nesta ordem:

| Posição | Área | Unidade |
|---------|------|---------|
| 0 | Temperatura interna | °C |
| 1 | Comunicação com a base | % |
| 2 | Sistema de energia (bateria) | % |
| 3 | Suporte de oxigênio | % |
| 4 | Estabilidade operacional | % |

---

## Regras de alerta

### Temperatura (°C)
| Condição | Classificação |
|----------|--------------|
| menor que 18 | ATENÇÃO |
| de 18 até 30 | NORMAL |
| de 31 até 35 | ATENÇÃO |
| maior que 35 | CRÍTICO |

### Comunicação (%)
| Condição | Classificação |
|----------|--------------|
| menor que 30 | CRÍTICO |
| de 30 até 59 | ATENÇÃO |
| 60 ou mais | NORMAL |

### Bateria (%)
| Condição | Classificação |
|----------|--------------|
| menor que 20 | CRÍTICO |
| de 20 até 49 | ATENÇÃO |
| 50 ou mais | NORMAL |

### Oxigênio (%)
| Condição | Classificação |
|----------|--------------|
| menor que 80 | CRÍTICO |
| de 80 até 89 | ATENÇÃO |
| 90 ou mais | NORMAL |

### Estabilidade (%)
| Condição | Classificação |
|----------|--------------|
| menor que 40 | CRÍTICO |
| de 40 até 69 | ATENÇÃO |
| 70 ou mais | NORMAL |

---

## Pontuação de risco

| Classificação | Pontos |
|--------------|--------|
| NORMAL | 0 |
| ATENÇÃO | 1 |
| CRÍTICO | 2 |

Pontuação máxima por ciclo: **10 pontos** (5 áreas × 2 pontos).

---

## Classificação do ciclo

| Pontuação | Classificação |
|-----------|--------------|
| 0 a 2 | MISSÃO ESTÁVEL |
| 3 a 5 | MISSÃO EM ATENÇÃO |
| 6 a 10 | MISSÃO CRÍTICA |

---

## Funções implementadas

| Função | Descrição |
|--------|-----------|
| `analisar_temperatura()` | Classifica a temperatura do ciclo |
| `analisar_comunicacao()` | Classifica a qualidade do sinal |
| `analisar_bateria()` | Classifica o nível de bateria |
| `analisar_oxigenio()` | Classifica o nível de oxigênio |
| `analisar_estabilidade()` | Classifica a estabilidade operacional |
| `classificar_ciclo()` | Determina o status geral do ciclo |
| `gerar_recomendacao()` | Gera recomendação automática por ciclo |
| `analisar_tendencia()` | Compara risco do primeiro e último ciclo |
| `identificar_area_mais_afetada()` | Retorna a área com maior risco acumulado |
| `gerar_relatorio_final()` | Exibe o relatório consolidado da missão |

---

## Integrantes

| Nome | RM |
|------|----|
| Aneliza Rondina Bonafé - RM: 572977 |
| Rafaella Ferreira de Moraes - RM: 571030 |

---

## Vídeo

[Assistir no YouTube](https://youtube.com/SEU_LINK_AQUI)
