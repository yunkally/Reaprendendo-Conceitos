agente = {
    'nome': 'Jett',
    'funcao': 'Duelista',
    'pais': 'Coreia do Sul'
}
agente['habilidade'] = 'Tormenta de aço'
print(agente['habilidade'])
for chave, valor in agente.items():
    print(f'{chave}: {valor}')
