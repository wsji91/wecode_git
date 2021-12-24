def get_even_num():
    even_num_list = []
    for i in range(1,51):
        if i % 2 == 0:
            even_num_list.append(i)
    return even_num_list

print(get_even_num())