#calculating limits
#differentiator

def q_formula(a, b, c):
    q = b**2 - 4*a*c
    if q < 0:
        return "invalid characters"
    q_positive = -b + q**0.5
    q_negative = -b - q**0.5
    final_q_postive = q_positive/(2*a)
    final_q_negative = q_negative/(2*a)
    return "positive sqrt: ", final_q_postive, "negative sqrt: ", final_q_negative

def parametric_line(xp,yp,zp, t, dx,dy,dz):
    x = xp + t*dx
    y = yp + t*dy
    z = zp + t*dz
    print "The Parametric Vector is: "
    return x, y, z

def unit_vector(x, y, z):
    ux = x
    uy = y
    uz = z
    u = (ux)**2 + (uy)**2 + (uz)**2 #make sure negative values work
    absu = u**0.5
    unit_vector1 = ux/absu
    unit_vector2 = uy/absu
    unit_vector3 = uz/absu
    return unit_vector1, unit_vector2, unit_vector3

def vectors_perpen(x1,y1,z1, x2,y2,z2): #Vector perpendicular equation a.b = 0 
    x = x1*x2
    y = y1*y2
    z = z1*z2
    total = x+y+z
    if total == 0:
        return "The two vectors are perpendicular"
    else:
        return "The two vectors are not perpendicular"

def projections(xa,ya,za, dx,dy,dz):
    unit_vector_d = dx**2 + dy**2 + dz**2
    unit_vector_d2 = unit_vector_d*0.5
    x2 = dx/unit_vector_d2
    y2 = dy/unit_vector_d2
    z2 = dz/unit_vector_d2

    
    abs_d_vector1 = abs(x2)
    abs_d_vector2 = abs(y2)
    abs_d_vector3 = abs(z2)

    projection = xa*abs_d_vector1 + ya*abs_d_vector2 + za*abs_d_vector3
    projection2 = abs(projection)

    return "The absolute vector of direction is: ", abs_d_vector1, abs_d_vector2, abs_d_vector3, projection2, """The last
    value is the projection value"""
    #Check that this function 100 gives right answer
    #FIX THIS SEMANTIC ERROR 'The [last\n]    value is the projection value')

def projection_vector(projections_scalar, unit_d1,unit_d2,unit_d3):
    projection1 = projections_scalar*unit_d1    
    projection2 = projections_scalar*unit_d2
    projection3 = projections_scalar*unit_d3

    return "The projection vector is", projection1, projection2, projection3, """ Make sure
    to use the projections(xa,ya,za, dx,dy,dz) function to find the values and enter abs_d_vectors 1, 2, 3"""
    #Check that this function 100 gives right answer
    #FIX THIS SEMANTIC ERROR 'The [last\n]    value is the projection value')



#def q_formula(a, b,c):
#    """

#   >>> q_formula(1, 5, 1)
#    False
#    >>> q_formula(1, 2, 3)
#   False
#   >>> q_formula(1, 6, 1)
#   True
#    >>> q_formula(6, 10, 6)
#    True
#    >>> q_formula(-1, 5, -1)
#    False
#    >>> q_formula(1, -5, 1)
#    True
#   """
#    return True

#if __name__ == "__main__":
#    import doctest
#    doctest.testmod(verbose=True)
    
