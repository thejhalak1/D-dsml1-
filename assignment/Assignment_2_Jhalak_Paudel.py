#from prompt_toolkit.key_binding.bindings.named_commands import transpose_chars

# Problem 1: Reverse a List | Comprehension....................

numbers =[1,2,3,4,5,6,7]
reverse_list = [i for i in numbers[::-1]]
print(reverse_list)

# Problem 2: Concatenate two List | Comprehension.............................
list_a = [1,2,3,4,5,6,7]
list_b = list_a [::-1]
print(list_b)
        # Simple Concatenation
concatenate = [[list_a[i],list_b[i]] for i in range(len(list_a))]
print(concatenate)


list_c = list_a + list_b
print(list_c)
        #By index
list_d = (list_a[1],list_b[1]), (list_a[2],list_b[2]), (list_a[3],list_b[3])
print(list_d)

        # equal length of list a and b
list_d = [(list_a [i], list_b [i]) for i in range(len(list_b))]
print(list_d)

# Problem 3: Turn Every Item of a list into a Square | Comprehension..................

numbers = [1,2,3,4,5,6,7]
every_num_sq = [ i**2 for i in numbers]
print(every_num_sq)

# Problem 4: Iterate two list simultaneously | Comprehension..........................
list1 = [1,2,3,4,5,6,7]
list2 = [2,4,6,8,10,12,14]
# zip
iterate_sim = [(a, b) for a, b in zip(list1, list2)]
print(iterate_sim)
print([(a+b) for a, b in zip(list1, list2)])

# Problem 5: Removal of Empty Strings from a List of Elements | Comprehension..........................

sample_str = ['removal', 'of', '', 'empty', 'string', '', 'from', 'a', '', 'list', 'of', 'elements']
print([i for i in sample_str if i])

# Problem 6: Add new Item to a List After a Specified Item................................

list = [1,2,3,4,5,6,7]
item_to_add = 2
position = 4
add_place = list.index(position) + 1
list.insert(add_place, item_to_add)
print(list)

# Problem 7: Extend a nested list by adding a Sublist.................................
list_nested = iterate_sim.copy()
print(list_nested)
nest_to_add = [(8,16), (10,20)]
nested_list = (list_nested + nest_to_add)
print(nested_list)

# Problem 8: Replace the list Item with new Value if Found | Comprehension....................................
list1 = [1,2,3,4,5,6,7]
list2 = [2,4,6,8,10,12,14]
#replacing/ adding new item in list 1 if there are any new items in list2
#print([list1[i] if list1[i] != list2[i] else list2[i] for i in range(list2)])

# Problem 9: Remove all occurances of a Specific Item if Found | Comprehension..............................

raw_item = [1,2,'i', 'jhalak', '', 3,4,5,6,7]

# if for filtering the data
print([i for i in raw_item if isinstance(i, int)])

# King Problem
# Problem 10: Find Transpose of a Nested List.............................
# king_item = nested_list
# print(king_item)
#
# print(transpose_chars(king_item))




