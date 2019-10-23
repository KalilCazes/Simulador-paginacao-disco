#!/usr/bin/python3.5
from quadro import Quadro


def simulador(n_quadros, sequencia_paginas):

    falhas_pagina = 0

    quadros = []
    for i in range(n_quadros):
        quadros.append(Quadro())

    iterador_pagina = 0

    while iterador_pagina < len(sequencia_paginas):

        pagina = sequencia_paginas[iterador_pagina]
        posicao_pagina_memoria = buscar_pagina_em_memoria(pagina, quadros)

        if posicao_pagina_memoria == -1:
            falhas_pagina += 1
            quadro_livre = checa_quadro_livre(quadros)
            if quadro_livre != -1:
                quadros[quadro_livre].ocupado = True
                quadros[quadro_livre].pagina = pagina
                quadros[quadro_livre].data_ultimo_acesso = iterador_pagina
            else:
                quadro_lru = calcula_posicao_lru(quadros)
                quadros[quadro_lru].pagina = pagina
                quadros[quadro_lru].data_ultimo_acesso = iterador_pagina

        else:
            quadros[posicao_pagina_memoria].data_ultimo_acesso = iterador_pagina
            
        iterador_pagina += 1

    return falhas_pagina


def buscar_pagina_em_memoria(pagina, quadros):
    for i in range(len(quadros)):
        if quadros[i].pagina == pagina:
            return i

    return -1


def checa_quadro_livre(quadros):
    for i in range(len(quadros)):
        if not quadros[i].ocupado:
            return i

    return -1


def calcula_posicao_lru(quadros):
    lru = 0
    for i in range(len(quadros)):
        if quadros[i].data_ultimo_acesso < quadros[lru].data_ultimo_acesso:
            lru = i

    return lru
