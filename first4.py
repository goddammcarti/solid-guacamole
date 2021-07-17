import random
t = [random.randint(0, 10) for i in range(20)]
print(t, "Первоначальная версия")
s = []
for i in t:
       if i not in s:
          s.append(i)
print(sorted(s), "Отсортированная версия")