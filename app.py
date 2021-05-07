#!/usr/bin/env python3

from os import system

class FruitBox:
    def __init__( self, apples, oranges ):
        
        
        if ((apples + oranges) > 50 ):
            print("Too much fruits in box")
            input( "hit Enter to continue ..." )
        else:
            if ( type(apples) == int ):
                self.apples = apples
            else:
                print("Enter an integer quantity!")
        
            if ( type(oranges) == int ):
                self.oranges = oranges
            else:
                print("Enter an integer quantity!")
    
    def __str__(self):
        return f"In box: Apples: {self.apples} & Oranges: {self.oranges}"
    
    def __add__( self, other_box ):
        return FruitBox(self.apples + other_box.apples, self.oranges + other_box.oranges)

a_box = FruitBox( 50, 1 )
b_box = FruitBox( 5, 2.2 )

#result_box = a_box + b_box
system( "clear" )
print( a_box )
#print ( b_box )


