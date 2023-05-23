#!/usr/bin/env python
#

"""
// The DoTurn function is where your code goes. The PlanetWars object contains
// the state of the game, including information about all planets and fleets
// that currently exist. Inside this function, you issue orders using the
// pw.IssueOrder() function. For example, to send 10 ships from planet 3 to
// planet 8, you would say pw.IssueOrder(3, 8, 10).
//
// There is already a basic strategy in place here. You can use it as a
// starting point, or you can throw it out entirely and replace it with your
// own.
"""

from PlanetWars import PlanetWars


def calculate_planet_value(pw, my_planet, planet):
    return planet.GrowthRate() * 2 - pw.Distance(my_planet.PlanetID(), planet.PlanetID())


def DoTurn(pw):
    """
    Your code goes in this function
    :param pw: The planet wars object
    """
    for p in pw.MyPlanets():
        num = float(p.NumShips())
        sorted_planets = sorted(pw.NotMyPlanets(), key=lambda other_p: calculate_planet_value(pw, p, other_p), reverse=True)

        for other_planet in sorted_planets:
            if other_planet:
                if other_planet.Owner() == 0:
                    s = other_planet.NumShips() + 1
                else:
                    s = other_planet.NumShips() + pw.Distance(p.PlanetID(), other_planet.PlanetID())
                if s <= num:
                    pw.IssueOrder(p.PlanetID(), other_planet.PlanetID(), s)
                    num -= s



"""
//
//
//
// YOU MAY NOT EDIT THE CODE BELOW, ONLY THE DoTurn function
//
//
//
"""


def main():
    map_data = ''
    while True:
        current_line = input()
        if len(current_line) >= 2 and current_line.startswith("go"):
            pw = PlanetWars(map_data)
            DoTurn(pw)
            pw.FinishTurn()
            map_data = ''
        else:
            map_data += current_line + '\n'


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('ctrl-c, leaving ...')
