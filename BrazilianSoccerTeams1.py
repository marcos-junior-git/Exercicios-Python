def brazilian_soccer_teams():
    a = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos',
    'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atletico-GO', 'Avaí', 'Juventude')
    print(f'Lista de times Brasileirão {a}')
    print(f'Os 5 primeiros são {a[0:5]}')
    print(f'Os 4 ultimos são {a[-4:]}')
    print(f'Ordem alfabetica {sorted(a)}')
    print(f'São Paulo está na {a.index("São Paulo")} posição')
