# recursion
def find(a_list, finding_element):
    if not a_list:
        return False

    if a_list[0] == finding_element:
        return True

    return find(a_list[1:], finding_element)

l = [2, 4, 6, 8, 10]

print(find(l, 6))
print(find(l, 11))
