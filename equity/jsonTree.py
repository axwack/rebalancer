from collections import defaultdict

class Classification:
    def __init__(self, text, index,):
        self.text = text
        self.index = index

c1 = Classification('Kingdom1', 'Phylum1', 'Class1', 'Species1')
c2 = Classification('Kingdom1', 'Phylum1', 'Class1', 'Species2')
c3 = Classification('Kingdom1', 'Phylum2', 'Class3', 'Species3')
c4 = Classification('Kingdom1', 'Phylum2', 'Class4', 'Species4')
c5 = Classification('Kingdom2', 'Phylum3', 'Class5', 'Species5')

all_classifications = [c1, c2, c3, c4, c5]

def nested_to_tree(key, source):
    result = {'name': key, 'children':[]}
    for key, value in source.items():
        if isinstance(value, list):
            result['children'] = value
        else:
            child = nested_to_tree(key, value)
            result['children'].append(child)

    return result

nested_dict = defaultdict(
    lambda: defaultdict(
        lambda: defaultdict(list)
    )
)

for c in all_classifications:
    nested_dict[c.kingdom][c.phylum][c.klass].append(c.species)

result = nested_to_tree('root', nested_dict)
print(result)