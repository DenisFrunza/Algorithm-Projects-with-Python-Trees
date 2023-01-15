class NaryNode:
    def __init__(self, value):
        self.value = value
        self.children: list[NaryNode] = []

    def add_child(self, child):
        self.children.append(child)
    
    def __str__(self):
        result = f'{self.value}:'

        for child in self.children:
            result += f' {child.value}'

        return result

if __name__ == '__main__':
    # Create two nodes named "root" and "a".
    root = NaryNode('Root')
    a = NaryNode('A')

    # Make "a" be the left child of "root."
    root.add_child(a)
    print(root)