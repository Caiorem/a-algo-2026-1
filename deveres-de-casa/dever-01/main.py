# ====================================
# Title: A barreira do n²
# Author: Caio Silveira
# Created: 04/03/2026
# ====================================

import time
import random

# 1.Define unsorted arrays
list_choices = [1000, 5000, 10000, 20000, 50000]

def make_random_list(n):
    """Gera e retorna uma lista aleatória de tamanho n."""
    return [random.randint(0, n) for _ in range(n)]

# 2.Implementation insertsort function (insertion sort clássico)
def insertsort(unsorted_list):
    a = unsorted_list[:]  # copia
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# 3. Mede Timsort (sorted) e Insertion Sort sobre as MESMAS listas
random.seed(42)  # opcional, para reprodutibilidade

for size in list_choices:
    data = make_random_list(size)

    start_time_t = time.perf_counter()
    result_t = sorted(data)
    end_time_t = time.perf_counter()

    start_time_i = time.perf_counter()
    result_i = insertsort(data)
    end_time_i = time.perf_counter()

    # Verificação de correção
    assert result_i == result_t, "Insertion sort produziu resultado incorreto!"

    i_time = end_time_i - start_time_i
    t_time = end_time_t - start_time_t

    # 4.Compare algorithm execution time
    if i_time > t_time:
        print(f"[n={size}] Timsort foi mais rápido por {i_time - t_time:.6f} s "
              f"(Timsort={t_time:.6f}s, Insertion={i_time:.6f}s)")
    elif t_time > i_time:
        print(f"[n={size}] Insertion sort foi mais rápido por {t_time - i_time:.6f} s "
              f"(Timsort={t_time:.6f}s, Insertion={i_time:.6f}s)")
    else:
        print(f"[n={size}] Ambos tiveram o mesmo tempo ({t_time:.6f}s)")