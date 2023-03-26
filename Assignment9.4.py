#This is problem to convert all the negative coordinates to a positive coordinates;The agenda is to get all the coordinates in 0 or positive values keeping the relative distance same;We can add or delete any number from the coordinates ; however graph should not be changed;
#Input: [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
#Output : [(9,6), (6, 12), (7,7),(0, 5), (8, 12), (18,5)]

def convert_to_positive(coordinates):
    min_x = min([c[0] for c in coordinates])
    min_y = min([c[1] for c in coordinates])
    new_coordinates = [(c[0] + abs(min_x), c[1] + abs(min_y)) for c in coordinates]
    return new_coordinates