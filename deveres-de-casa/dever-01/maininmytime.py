# ====================================
# Title: A barreira do n²
# Author: Caio Silveira
# Created: 05/03/2026
# Post-history: 05/03/2026
# ====================================

import time
import random

# 1.Implementation random unsorted list makes
def sort_numberlist(lenzada):
    unsorted_list = [random.randint(0,lenzada) for i in range (0,lenzada)]

# 2.Implementation insertsort function
def insertsort(unsorted_list):
    list_2 = list(unsorted_list)
    n=len(unsorted_list)
    for i in range(1,n):
        insert_index = i
        current_value = list_2.pop(i)
        for j in range(i-1, -1, -1):
            if list_2[j] > current_value:
                insert_index = j
        list_2.insert(insert_index, current_value)


# 3.Call timsort function(I used native function in this case) and insertsort function

list_choices = [1000, 5000, 10000, 20000, 50000]
choices_len = len(list_choices)

for i in range (0, choices_len):

    sort_numberlist(list_choices[i])

    start_time_t=time.time()
    sorted(list_choices)
    end_time_t=time.time()

    start_time_i=time.time()
    insertsort(list_choices)
    end_time_i=time.time()

    i_time = end_time_i - start_time_i
    t_time = end_time_t - start_time_t

    # 4.Compare algorithm execution time
    if i_time > t_time:
        print(f"Timsort if size {list_choices[i]} was faster by {i_time - t_time:.6f} seconds")
    elif t_time > i_time:
        print(f"Insertion sort if siza {list_choices[i]} was faster by {t_time - i_time:.6f} seconds")
    else:
        print("Both algorithms had the same execution time")

    i+=1