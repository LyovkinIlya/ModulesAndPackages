from fake_math import divide as f_d
from true_math import divide as t_d

result1 = f_d(5, 2)
result2 = f_d(1, 0)
result3 = t_d(10, 2)
result4 = t_d(2, 0)
print(result1) # 2.5
print(result2) # Ошибка
print(result3) # 5.0
print(result4) # inf