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

        if not pagina_em_memoria(pagina, quadros):
            falhas_pagina += 1
            quadro_livre = checa_quadro_livre(quadros)
            if quadro_livre != -1:
                quadros[quadro_livre].ocupado = True
                quadros[quadro_livre].pagina = pagina
            else:
                quadro_a_substituir = calcula_posicao_otima(quadros, sequencia_paginas, iterador_pagina)
                quadros[quadro_a_substituir].pagina = pagina

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


def calcula_posicao_otima(quadros, sequencia_paginas, iterador_pagina):
    quadros_temp = quadros.copy()
    for i in range(len(quadros_temp)):
        quadros_temp[i].data_proxima_ocorrencia = -1

    for j in range(len(quadros_temp)):
        for i in range(iterador_pagina, len(sequencia_paginas)):
            if sequencia_paginas[i] == quadros_temp[j].pagina:
                quadros_temp[j].data_proxima_ocorrencia = i
                break

    maior_data = -1
    pos_maior_data = -1
    for i in range(len(quadros_temp)):
        if quadros_temp[i].data_proxima_ocorrencia == -1:
            return i
        if quadros_temp[i].data_proxima_ocorrencia > maior_data:
            maior_data = quadros_temp[i].data_proxima_ocorrencia
            pos_maior_data = i

    return pos_maior_data
