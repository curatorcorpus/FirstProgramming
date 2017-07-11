#find the distance of two 2 dimensional points
def distance_points(x1,y1, x2,y2):
    dy = y2-y1 #rise
    dx = x2-x1 #run

    sqr = dx**2 + dy**2 #square both values
    sqrt = sqr**0.5 # square root the variable sqr
    return sqrt #answer
