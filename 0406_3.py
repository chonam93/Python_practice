class grandpa:
    def __init__(self):
        print('grandpa')

class parent(grandpa):
    def __init__(self):
        super().__init__()
        print('parent 1')

class parent2(grandpa):
    def __init__(self):
        super().__init__()
        print('parent 2')
        
class child(parent, parent2):
    def __init__(self):
        parent.__init__(self)
        parent2.__init__(self)
        print('child')

person = child()
