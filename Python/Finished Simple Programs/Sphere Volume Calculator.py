def sphere_volume(radius):
    if radius<0:
        print "Error, cannot use a negative value for volume of sphere."
        return

    volume = (4*3.14159265359*radius**3)/3
    return volume
