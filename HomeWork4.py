mutable_list = [1, 2, "sun", 3.5, False]
print(mutable_list)
mutable_list[2] = "moon"
mutable_list[0] = -1
mutable_list[1] = str(2)
print(mutable_list)

immutable_var = (1, 2, "car", 3.5, True)
print(immutable_var)
immutable_var[2] = "plane"
# кортежи не поддерживают обращение к элементам. Это значит, что нельзя заменить один элемент в кортеже на другой.
# Однако, если элементом кортежа будет список, то этот список можно будет изменить внутри кортежа.
