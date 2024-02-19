# recursion
def find(a_list, finding_element):
    if not a_list:
        return False

    if a_list == finding_element:
        return True

    # Call the function recursively until it run through the rest of the elements.
    return find(a_list[1:], finding_element)

l = [2, 4, 6, 8, 10]

print(find(l, 6))
print(find(l, 11))
