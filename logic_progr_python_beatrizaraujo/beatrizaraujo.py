'''
COMO FRITAR UM OVO para uma pessoa 🍳:

Ingredientes:

- 1 ovo.
- 1 frigideira.
- 1 colher de óleo, manteiga ou azeite.

Modo de preparo:

Em uma frigideira, adicione uma colher de óleo, manteiga ou azeite e aqueça em fogo médio.
Após o óleo aquecer, quebre o ovo na frigideira e deixe fritar até o ponto desejado e em seguida,
vire o ovo para fritar do outro lado.

Após fritar, passe para um recipiente e adicione sal e/ou outro tempero de sua preferêcia.
Em seguida, sirva!

'''


def fritar_ovo(tipo_gema):
    print('Como fritar um ovo simples 🍳: ')
    print('Porção para 1 pessoa.')
    print('1. Pegue uma frigideira e adicione uma colher de óleo, manteiga ou azeite. ')
    print('2. Aqueça o óleo em fogo médio. ')
    print('3. Após aquecer o óleo, quebre o ovo e adicione na frigideira. ')
    print('4. Vire o ovo para fritar do outro lado. ')
    print('5. Ponto da gema: A gosto. Caso queira a gema mole, deixar fritar por menos tempo.')
    print('6. Após fritar, passe para um recipiente. ')
    print('7. Adicione sal e/ou outro tempero de sua preferência.')
    print('8. Em seguida, sirva! ')


    if tipo_gema.lower() == 'mole':
        resultado = 'Ovo frito com gema mole'
    else:
        resultado = 'Ovo frito com gema dura'
        
        return resultado
    meu_ovo = fritar_ovo('mole')
    print(f'minha receita: {meu_ovo}')