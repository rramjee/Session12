import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        self.polydict={}
        
        
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def count_vertices(self):
        if self.polydict.get("count_vertices"): 
            print("picking from calculated value")
            return self.polydict["count_vertices"]
        else:  
            print("Calculating for the first time")
            self.polydict["count_vertices"]  =   self._n     
            return self._n  
    
    @property
    def count_edges(self):
        if self.polydict.get("count_edges"): 
            print("picking from calculated value")
            return self.polydict["count_edges"]
        else:  
            print("Calculating for the first time")
            self.polydict["count_edges"]  =   self._n     
            return self._n          
    
    @property
    def circumradius(self):
        if self.polydict.get("circumradius"): 
            print("picking from calculated value")
            return self.polydict["circumradius"]
        else:  
            print("Calculating for the first time")
            self.polydict["circumradius"]  =   self._R     
            return self._R 
    
    @property
    def interior_angle(self):
        if self.polydict.get("interior_angle"): 
            print("picking from calculated value")
            return self.polydict["interior_angle"]
        else:  
            print("Calculating for the first time")
            self.polydict["interior_angle"]  =   (self._n - 2) * 180 / self._n     
            return self.polydict["interior_angle"]

    @property
    def side_length(self):
        if self.polydict.get("side_length"): 
            print("picking from calculated value")
            return self.polydict["side_length"]
        else:  
            print("Calculating for the first time")
            self.polydict["side_length"]  =  2 * self._R * math.sin(math.pi / self._n)    
            return self.polydict["side_length"]

    
    @property
    def apothem(self):
        if self.polydict.get("apothem"): 
            print("picking from calculated value")
            return self.polydict["apothem"]
        else:  
            print("Calculating for the first time")
            self.polydict["apothem"]  =  self._R * math.cos(math.pi / self._n)    
            return self.polydict["apothem"]
    
    @property
    def area(self):
        if self.polydict.get("area"): 
            print("picking from calculated value")
            return self.polydict["area"]
        else:  
            print("Calculating for the first time")
            self.polydict["area"]  =  self._n / 2 * self.side_length * self.apothem    
            return self.polydict["area"]
    
    @property
    def perimeter(self):
        if self.polydict.get("perimeter"): 
            print("picking from calculated value")
            return self.polydict["perimeter"]
        else:  
            print("Calculating for the first time")
            self.polydict["perimeter"]  =  self._n * self.side_length    
            return self.polydict["perimeter"]
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented

    
if __name__ == '__main__':
    p = Polygon(25,6)
    print(p.__repr__())
    print(p.area)
    print(p.area)
    #print(p.__len__())
