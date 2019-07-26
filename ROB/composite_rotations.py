import numpy as np
from itertools import repeat
from math import cos, sin, radians


def init_transform(n=4):
    return np.identity(4)


def get_rotation_matrix(axis, t, in_degrees=True):
    # axis value can be 1, 2 or 3.
    axis = int(axis)
    # t is in degrees.
    if in_degrees:
        t = radians(t)
    
    rotation_matrices = {
        1: lambda t1: np.array([
                [1, 0,       0,        0],
                [0, cos(t1), -sin(t1), 0],
                [0, sin(t1), cos(t1),  0],
                [0, 0,       0,        1]
           ]),
        2: lambda t2: np.array([
                [cos(t2),  0, sin(t2), 0],
                [0,        1, 0,       0],
                [-sin(t2), 0, cos(t2), 0],
                [0,        0, 0,       1]
           ]),
        3: lambda t3: np.array([
                [cos(t3), -sin(t3), 0, 0],
                [sin(t3), cos(t3),  0, 0],
                [0,       0,        1, 0],
                [0,       0,        0, 1]
           ])
    }
    return rotation_matrices[axis](t)


def get_translation_matrix(x, y, z):
    return np.array([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ])


def get_coords():
    # returns coordinates in homogeneous reference.
    return [float(i) for i in input("Enter the coordinates:").split()] + [1]


def algo():
    # taking the input in the format:
    # Q val: performing Q with val degrees. Q \in {R, T}
    
    TRANSFORMATIONS = {
        "R": get_rotation_matrix, 
        "T": get_translation_matrix
    }
    
    n_q = int(input("Enter the number of transformations: "))
    queries = [input().split() for _ in repeat(None, n_q)]
    T = init_transform()
    for query in queries:
        action = TRANSFORMATIONS.get(query[0])
        assert action is not None, "Invalid action given."
        T = np.matmul(T, action(*map(float, query[1:])))
    
    return np.matmul(T, get_coords())[:3]

    
print(algo())
