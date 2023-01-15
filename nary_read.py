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
    root = NaryNode('Root')
    a = NaryNode('A')

    root.add_child(a)
    print(root)