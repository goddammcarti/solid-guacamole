import random
a = [random.randint(0, 10)for i in range(10)]
print(a)
b = [random.randint(0, 10)for i in range(10)]
print(b)
diff_list1_list2 = list(set(a) - set(b))
diff_list2_list1 = list(set(b) - set(a))
c = diff_list1_list2 + diff_list2_list1
print(c)