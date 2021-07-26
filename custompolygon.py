import random
from collections import namedtuple 
#from PyClassicRound import classic_round
from decimal import *
import cmath
import math
from session11 import Polygon

class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self.length = self._m - 2
        #self._polygons = [Polygon(i, R) for i in range(3, m+1)]
        
    def __len__(self):
        return self.length
    
    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'

    def __iter__(self):
        return self.PolyIterator(self)
    
    # def __getitem__(self, s):
    #     return self._polygons[s]
    
    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons, 
                                 key=lambda p: p.area/p.perimeter,
                                reverse=True)
        return sorted_polygons[0]

    class PolyIterator:
        def __init__(self, poly_obj):
            self._poly_obj = poly_obj
            self._index = 3
            
        def __iter__(self):
            return self

        def __next__(self):
            if self._index > self._poly_obj._m:
                raise StopIteration
            else:
                item = Polygon(self._index, self._poly_obj._R)
                self._index += 1
                return item

if __name__ == '__main__':
    
    for num in Polygons(25,6):
        print(num)

    p2 = Polygons(10,8)
    p = iter(p2)
    for p in p:
        print(f'number of vertices = {p.count_edges} number of edges = {p.count_edges} Edge Length = {p.side_length} interior angle = {p.interior_angle} apothem = {p.apothem} area = {p.area} perimeter = {p.perimeter}')
        print(f'number of vertices = {p.count_edges} number of edges = {p.count_edges} Edge Length = {p.side_length} interior angle = {p.interior_angle} apothem = {p.apothem} area = {p.area} perimeter = {p.perimeter}')
    


    # print(p.__repr__())
    # print(p.area)
    # print(p.area)