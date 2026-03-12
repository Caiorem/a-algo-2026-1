# ====================================
# Title: A barreira do n²
# Author: Caio Silveira
# Created: 05/03/2026
# ====================================

import time
import sys


def fatorial(n):
    """Calcula o fatorial de n de forma recursiva."""
    # Caso base: a condição de parada da recursão
    if n == 0 or n == 1:
        return 1
    # Passo recursivo: a função chama a si mesma reduzindo o problema
    return n * fatorial(n - 1)


# Aumenta o limite da pilha para suportar n=1000
sys.setrecursionlimit(2000)

# Lista de valores para teste
lista_de_n = [10, 100, 500, 1000]

print("Iniciando medições de tempo:")
print("-" * 30)

for n in lista_de_n:
    # Início do cronômetro com alta precisão
    tempo_inicio = time.perf_counter()
    
    fatorial(n)
    
    # Fim do cronômetro
    tempo_fim = time.perf_counter()
    
    tempo_total = tempo_fim - tempo_inicio
    print(f"n = {n:4} | Tempo Total = {tempo_total:.6f} segundos")

# ====================================
# Análise de Complexidade Assintótica
# ====================================
# O algoritmo possui complexidade O(n).
#
# Raciocínio:
# 1. Para calcular o fatorial de 'n', a função realiza exatamente 'n' 
#    chamadas recursivas até atingir o caso base (1).
# 2. Em cada chamada, é realizada apenas uma operação de multiplicação 
#    e uma subtração (n-1), que são operações de tempo constante O(1).
# 3. Como o número de operações cresce de forma linear e proporcional 
#    ao tamanho da entrada 'n', o tempo de execução segue a função T(n) = n.
# 4. Portanto, a complexidade é Linear: O(n).