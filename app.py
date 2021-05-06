#!/usr/bin/env python3

from os import system

class FruitBox:
    def __init__( self, apples, oranges, err = "error" ):
        
        if ((apples + oranges) > 50 ):
            self.apples = err
            self.oranges = err
        else:
            if ( type(apples) == int ):
                self.apples = apples
            else:
                self.apples = err
        
            if ( type(oranges) == int ):
                self.oranges = oranges
            else:
                self.oranges = err
    
    def __str__(self):
        return f"In box: Apples: {self.apples} & Oranges: {self.oranges}"
    
    def __add__( self, other_box ):
        return FruitBox(self.apples + other_box.apples, self.oranges + other_box.oranges)

a_box = FruitBox( 3, 1, "ERROR" )
b_box = FruitBox( 5, 2, "ERROR" )

result_box = a_box + b_box
str(result_box)
system( "clear" )
print(result_box)


