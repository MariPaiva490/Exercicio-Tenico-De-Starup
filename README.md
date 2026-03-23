# Torneio de Startups

Simulação interativa de batalhas entre startups, com eventos que influenciam a pontuação e uma competição em formato de torneio até que uma única campeã seja coroada.

## Descrição

Este projeto em Python simula um torneio de startups, onde cada uma começa com uma pontuação inicial e enfrenta outras em batalhas diretas. A cada rodada, eventos como **pitch de sucesso**, **problemas com bugs**, **atração de usuários**, **investidores irritados** e até **fake news** podem impactar a pontuação das startups.

Caso uma rodada termine empatada, ativa-se o modo "Shark Fight", que concede 2 pontos extras a uma das startups de forma aleatória.

## Como Funciona

1. O usuário cadastra de 4 a 8 startups (apenas número par).
2. O sistema sorteia duplas e inicia o torneio.
3. Para cada batalha:
   - O usuário responde se determinados eventos aconteceram para cada startup.
   - A pontuação é atualizada com base nos eventos.
   - A vencedora da rodada avança.
4. Ao final, é exibido um relatório com estatísticas e a campeã do torneio.

## Funcionalidades

- Cadastro de startups com nome, slogan e ano de fundação.
- Sistema de pontuação baseado em eventos.
- Torneio em eliminatórias (1x1).
- "Shark Fight" para resolver empates.
- Relatório final com estatísticas de desempenho.

##  Requisitos

- Python 3.x

## Como Executar

1. Clone este repositório ou baixe o arquivo `main.py`.
2. Execute no terminal:

```bash
python main.py
```

3. Siga as instruções no console para cadastrar startups e jogar o torneio.

## Eventos e Pontuação

| Evento             | Efeito na Pontuação |
|--------------------|---------------------|
| Pitch convincente  | +6 pontos           |
| Produto com bugs   | -4 pontos           |
| Boa tração         | +3 pontos           |
| Investidor irritado| -6 pontos           |
| Fake News no pitch | -8 pontos           |
| Segurança nos dados| +8 pontos           |

## Exemplo de Resultado

```
 Campeã: Fogo - "Queimando obstáculos com inovação"
Fogo: 150 pontos
   Pitch: 3 | Bugs: 1 | Boa tração de usuários: 2
   Investidor irritado: 1 | Fake News: 0 | Segurança nos dados:1
```
