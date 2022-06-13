from math import sin, cos, tan, sqrt
from typing import Optional, TypeVar


T = TypeVar('T', int, float)
S = TypeVar('S', bound=str)
A = TypeVar('A', bound=int)


class NoValue(Exception):
    def __init__(self, var : S) -> S:
        super().__init__(f'No value given for: {var}')

class NoSideToBeFound(Exception):
    def __init__(self):
        super().__init__('No side was inputted to be found')

        
def SideName(side : S):
    if side == 'opposite' or 'o':
        return 'o'
    elif side == 'adjacent' or 'a':
        return 'a'
    elif side == 'hypotenuse' or 'h':
        return 'h'

def check_none(item):
    if item == '':
        return None
    else:
        return item


        
class Solve:
    def __init__(self, opposite : Optional[T], adjacent : Optional[T], hypotenuse : Optional[T], find : S, angle : A):
        self.opposite = opposite
        self.adjacent = adjacent
        self.hypotenuse = hypotenuse
        self.find_side = SideName(find.lower())
        self.angle = angle

    def resolve_expr(self):
        if self.find_side == 'o':
            if self.adjacent is not None:  
                tan_value = tan(self.angle)
                return float(tan_value) * float(self.adjacent)
            elif self.hypotenuse is not None:
                sin_value = sin(self.angle)
                return float(sin_value) * float(self.hypotenuse)
            else:
                raise NoValue('Opposite')
        elif self.find_side == 'a':
            if self.hypotenuse is not None:
                cos_value = cos(self.angle)
                return float(cos_value) * float(self.hypotenuse)
            elif self.opposite is not None:
                tan_value = tan(self.angle)
                return float(tan_value) * float(self.opposite)
            else:
                raise NoValue('Opposite')
        elif self.find_side == 'h':
            if self.opposite and self.adjacent is not None:
                # Pythagorean Theorem
                return sqrt(sum(float(self.opposite) ** 2, float(self.adjacent) ** 2))
            elif self.opposite is not None:
                sin_value = sin(self.angle)
                return float(sin_value) * float(self.opposite)
            elif self.adjacent is not None:
                cos_value = cos(self.angle)
                return float(cos_value) * float(self.adjacent)
            else:
                 raise NoValue('Opposite')
        else:
            raise NoSideToBeFound
            

class Main:
    def __init__(self):
        print("""Please type the value, if you don't have the value just press enter - 
              All lowercase""")
        print("-----------------")
        opposite = check_none(input('Type the opposite side length: '))
        adjacent = check_none(input('Type the adjacent side length: '))
        hypotenuse = check_none(input('Type the hypotenuse side length: '))
        angle = input('Type the angle measure: ')
        find = input('What are you finding? [o/a/h]: ')

        solution = Solve(opposite, adjacent, hypotenuse, find, angle).resolve_expr()
        print("-----------------")
        print(f'{find.capitalize} = {solution}')

Main()

#sin = 'opposite/hypotenuse'
#cose = 'adjacent/hypotenuse'
#tane = 'opposite/adjacent' 