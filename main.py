#!/usr/bin/env python3.5
import sys
import lru


def main():

    n_quadros = int(sys.argv[1])

    sequencia_paginas = []
    for pagina in sys.stdin:
        sequencia_paginas.append(int(pagina))

    print(lru.simulador(n_quadros, sequencia_paginas))


if __name__ == "__main__":
    main()
