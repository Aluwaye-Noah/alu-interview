#!/usr/bin/python3

"""
This function calculates the amount of water retained after it rains between the walls.
"""

def rain(walls):
    """
    This function calculates the rainwater retained
    """
    if len(walls) == 0:
        return 0

    left_wall, right_wall = 0, len(walls) - 1
    left_wall_max, right_wall_max = walls[left_wall], walls[right_wall]
    amount_water = 0

    while left_wall < right_wall:
        if left_wall_max < right_wall_max:
            left_wall += 1
            left_wall_max = max(left_wall_max, walls[left_wall])
            amount_water += left_wall_max - walls[left_wall]
        else:
            right_wall -= 1
            right_wall_max = max(right_wall_max, walls[right_wall])
            amount_water += right_wall_max - walls[right_wall]

    return amount_water
