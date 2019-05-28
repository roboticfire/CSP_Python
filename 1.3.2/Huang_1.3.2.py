def add_tip(total, tip_percent): 
    '''Return the total amount including tip'''
    tip = tip_percent*total
    return total + tip

def hyp(leg1, leg2):
    '''Gives the c value in an a,b,c right triangle'''
    a_squared = leg1*leg1
    b_squared = leg2*leg2
    c = (a_squared+b_squared)**0.5
    return c
    
def mean(a, b, c):
    '''Gives the mean value for a,b, and c'''
    mean = (a+b+c)/3.0
    return mean
    
def perimeter(base,height):
    '''Gives the Perimeter given the base and height'''
    perimeter = 2*(base + height)
    return perimeter
    
#1.3.2 Function Test
print add_tip(20,0.15)
print add_tip(30,0.15)
print hyp(3,4)
print mean(3,4,7)
print perimeter(3,4)