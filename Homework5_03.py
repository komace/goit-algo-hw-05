import timeit
import random


# Алгоритми Boyer-Moore для пошуку підрядка в тексті
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return []

    last = {}
    for k in range(m):
        last[pattern[k]] = k
    indices = []
    s=0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            indices.append(s)
            s += m if s + m < n else m - last.get(text[s + m], -1)         
        else:
            s += max(1, j - last.get(text[s + j], -1))
    return indices

# Алгоритми KMP для пошуку підрядка в тексті
def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)
    lps = [0] * m
    j = 0   
    
    def compute_lps_array(pattern, m, lps):
        length = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

    compute_lps_array(pattern, m, lps)
    i = 0
    indices = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            indices.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return indices

# Алгоритми Rabin-Karp для пошуку підрядка в тексті
def rabin_karp(text, pattern):
    m = len(pattern)
    n = len(text)
    hpattern = hash(pattern)
    htext = hash(text[:m])
    indices = []

    for i in range(n - m + 1):
        if hpattern == htext and text[i:i + m] == pattern:
            indices.append(i)
        if i < n - m:
            htext = hash(text[i + 1:i + m + 1])

    return indices


# Читання файлу
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# Шляхи до файлів
file1 = 'stattya_1.txt'
file2 = "stattya_2.txt"

#Вибираємо підрядки для пошуку
substring_exists = "структури даних"
substring_not_exists = "новий рік"

# Читаємо файли
text1 = read_file(file1)
text2 = read_file(file2)    

# Вимірюємо час виконання алгоритмів
def measure_time(text, pattern, algorithm):
    timer = timeit.Timer(lambda: algorithm(text, pattern))
    return timer.timeit(number=1)


# Результати першого файлу 

print("Результати для першого файлу:")
print(f"Boyer-Moore: з існуючим підрядком, {measure_time(text1, substring_exists, boyer_moore)} секунд")
print(f"Boyer-Moore: з неіснуючим підрядком, {measure_time(text1, substring_not_exists, boyer_moore)} секунд")

print(f"KMP: з існуючим підрядком, {measure_time(text1, substring_exists, kmp_search)} секунд")
print(f"KMP: з неіснуючим підрядком, {measure_time(text1, substring_not_exists, kmp_search)} секунд")

print(f"Rabin-Karp: з існуючим підрядком, {measure_time(text1, substring_exists, rabin_karp)} секунд")
print(f"Rabin-Karp: з неіснуючим підрядком, {measure_time(text1, substring_not_exists, rabin_karp)} секунд")

# Результати другого файлу 
print("Результати для другого файлу:")
print(f"Boyer-Moore: з існуючим підрядком, {measure_time(text2, substring_exists, boyer_moore)} секунд")
print(f"Boyer-Moore: з неіснуючим підрядком, {measure_time(text2, substring_not_exists, boyer_moore)} секунд")

print(f"KMP: з існуючим підрядком, {measure_time(text2, substring_exists, kmp_search)} секунд")
print(f"KMP: з неіснуючим підрядком, {measure_time(text2, substring_not_exists, kmp_search)} секунд")

print(f"Rabin-Karp: з існуючим підрядком, {measure_time(text2, substring_exists, rabin_karp)} секунд")
print(f"Rabin-Karp: з неіснуючим підрядком, {measure_time(text2, substring_not_exists, rabin_karp)} секунд")