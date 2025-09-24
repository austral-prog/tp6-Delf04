# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    lista = list_to_remove_elements.copy()

    if len(lista) > 5:
        del lista[5]
    if len(lista) > 4:
        del lista[4]
    if len(lista) > 0:
        del lista[0]
    return lista


def add_elements(list_to_add_elements):
    list_to_add_elements.append("Yellow")
    list_to_add_elements.insert(0, "Pink")
    return list_to_add_elements

def is_empty(list_to_check):
    return len(list_to_check) == 0

def check_lists(list_to_compare1, list_to_compare2):
    return len(list_to_compare1) == len(list_to_compare2)

def list_of_lists(list_of_lists_to_modify):
    list_of_lists_to_modify[0] = list_of_lists_to_modify[0][0:2]
    list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:4]
    list_of_lists_to_modify[2] = list_of_lists_to_modify[2][-2:]
    return list_of_lists_to_modify
