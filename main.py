def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result


students = [[1, 'Jane Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brain Howell', 'V'], [4, ' Lynnoe Foster', 'VII']]

print("\nOriginal list of lists:")
print(students)
print("\nConverted list to a  dictionary:")  
print(test(students))