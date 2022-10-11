unmodified_string = 'абв абвгде аваыджолп фываждлыв абвг ввв ааа'.split()
modified_lst = list(filter(lambda e: 'абв' not in e, unmodified_string))
modified_string = ""
for i in range(len(modified_lst)):
    modified_string += modified_lst[i] + " "
print(modified_string)

