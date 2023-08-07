
class Node:
    def __eq__(self, other) -> bool:
        if not isinstance(other, Node):
            return NotImplemented
        return (type(self) is type(other) and 
                self.__dict__ == other.__dict__)
    def __ne__(self, other) -> bool:
        return not (self == other)

class Block(Node):
    def __init__(self, statements) -> None:
        self.statements = statements
    
class Statement(Node):
    def __init__(self, expr) -> None:
        self.expr = expr

class Number(Node):
    def __init__(self, value) -> None:
        self.value = value