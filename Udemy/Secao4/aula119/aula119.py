# como utilizar Enum em python

from enum import Enum, auto


class Directions(Enum):
    right = auto()  # ao inves de chumbar um valor, utiliza-se o auto()
    left = auto()
    up = auto()
    down = auto()


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction.')

    return f'Moving {direction.name}'
    #return f'Moving {direction.value}'



if __name__ == '__main__':
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))
    print(move(Directions.down))

    print('-=-' * 20)

    for direction in Directions:
        print(direction, direction.value, direction.name)