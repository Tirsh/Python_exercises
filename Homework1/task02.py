# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def is_predicate(x, y, z): return not (x or y or z) == (
    not x and not y and not z)  # функция определеня истинности выражения


xyz_bool_array = [[bool(int(i)) for i in str(bin(x))[2:].zfill(3)]
                  for x in range(8)]  # заполняем массив всеми комбинациями x, y, z

print("Проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z")
for xyz in xyz_bool_array:
    print(f"¬({xyz[0]} ⋁ {xyz[1]} ⋁ {xyz[1]} = ¬{xyz[0]} ⋀ ¬{xyz[1]} ⋀ ¬{xyz[2]}  {is_predicate(*xyz)}")
