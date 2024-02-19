# non-recursion
def find(a_list, finding_element):
   for element in a_list:
       if element == finding_element:
           return True
   else:
       return False

l = [2, 4, 6, 8, 10]

print(find(l, 20))
print(find(l, 8))