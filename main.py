#!/usr/bin/env python3.5
import sys
import fifo
import lru
import opt


def main():
    n_quadros = int(sys.argv[1])

    sequencia_paginas = []
    for pagina in sys.stdin:
        sequencia_paginas.append(int(pagina))

    print(str(n_quadros) + " quadros, " + str(len(sequencia_paginas)) + " refs: FIFO: " + str(
        fifo.simulador(n_quadros, sequencia_paginas)) + "PFs, " +
          "LRU: " + str(lru.simulador(n_quadros, sequencia_paginas)) + "PFs, OPT: " + str(
        opt.simulador(n_quadros, sequencia_paginas)) + "PFs")


if __name__ == "__main__":
    main()
