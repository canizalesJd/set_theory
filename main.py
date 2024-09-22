# Get X set Partition
def partitions(set_):
    if not set_:
        return [[]]
    
    first_element = set_[0]
    rest_partitions = partitions(set_[1:])
    
    result = []
    for partition in rest_partitions:
        result.append([[first_element]] + partition)
        for i, subset in enumerate(partition):
            new_partition = partition[:i] + [[first_element] + subset] + partition[i+1:]
            result.append(new_partition)
    
    return result

# Modify your set here
set_ = [1, 2, 3]
print("================")
print(f"Set {set_} partition")
print(partitions(set_))
print("================")

def power_set(set_):
    if not set_:
        return [[]]

    first_element = set_[0]
    subsets_without_first = power_set(set_[1:])
    subsets_with_first = [[first_element] + subset for subset in subsets_without_first]
    return subsets_without_first + subsets_with_first

# Modify your set here
set_ = [1, 2, 3]
print("================")
print(f"Set {set_} Power")
print(power_set(set_))
print("================")

def intersection(set1, set2):
    return [x for x in set1 if x in set2]

# Modify your sets here
A = [1, 2, 3, 4]
B = [3, 4, 5, 6]
print("================")
print(f"Intersection of A {A} and B{B}")
print(intersection (A, B))
print("================")

def difference(set1, set2):
    return [x for x in set1 if x not in set2]
# Modify your sets here
A = [1, 2, 3, 4]
B = [3, 4, 5, 6]

print("================")
print(f"Difference of A {A} and B{B}")
print(difference (A, B))
print("================")

def simetrical_difference(set1, set2):
    return [x for x in set1 if x not in set2] + [x for x in set2 if x not in set1]

# Ejemplo de uso
A = [1, 2, 3, 4]
B = [3, 4, 5, 6]
print("================")
print(f"Simetrical Difference of A {A} and B{B}")
print(simetrical_difference (A, B))
print("================")