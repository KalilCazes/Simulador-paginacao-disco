#!/usr/bin/python3.5
from quadro import Quadro


def simulador(n_quadros, sequencia_paginas):

    falhas_pagina = 0

    quadros = []
    for i in range(n_quadros):
        quadros.append(Quadro())

    iterador_pagina = 0
    quadro_mais_antigo = 0

    while iterador_pagina < len(sequencia_paginas):

        pagina = sequencia_paginas[iterador_pagina]

        if not pagina_em_memoria(pagina, quadros):

            falhas_pagina += 1
            quadro_livre = checa_quadro_livre(quadros)
            if quadro_livre != -1:
                quadros[quadro_livre].ocupado = True
                quadros[quadro_livre].pagina = pagina
            else:
                quadros[quadro_mais_antigo % n_quadros].pagina = pagina
                quadro_mais_antigo += 1

        iterador_pagina += 1

    return falhas_pagina


def pagina_em_memoria(pagina, quadros):
    for i in range(len(quadros)):
        if quadros[i].pagina == pagina:
            return True

    return False


def checa_quadro_livre(quadros):
    for i in range(len(quadros)):
        if not quadros[i].ocupado:
            return i

    return -1