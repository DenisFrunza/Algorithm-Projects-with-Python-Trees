from __future__ import annotations

class BinaryNode:
    def __init__(
        self,
        value,
        left_child: BinaryNode=None,
        right_child: BinaryNode=None
    ) -> None:
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def add_left(self, child):
        self.left_child = child

    def add_right(self, child):
        self.right_child = child

    def __str__(self):
        result = f'{self.value}:'

        if self.left_child:
            result += f' {self.left_child.value}'
        else:
            result += f' None'
        
        if self.right_child:
            result += f'{self.right_child.value}'
        else:
            result += f' None'
        
        return result

if __name__ == '__main__':
    root = BinaryNode('Root')
    a = BinaryNode('A')

    # Make "a" be the left child of "root."
    root.add_left(a)
    print(root)