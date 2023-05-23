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


def DoTurn(pw):
    """
    Your code goes in this function
    :param pw: The planet wars object
    """
    not_my_planets = pw.NotMyPlanets()
    my_planets = pw.MyPlanets()

    if len(not_my_planets) == 0:
        return

    for my_planet in my_planets:
        closess_planet = not_my_planets[0]
        close_planet_distance = pw.Distance(my_planet.PlanetID(), closess_planet.PlanetID())
        for not_my_planet in not_my_planets:
            if close_planet_distance > pw.Distance(my_planet.PlanetID(), not_my_planet.PlanetID()):
                closess_planet = not_my_planet

        my_planet_fleet = my_planet.NumShips() / 2

        if  my_planet.NumShips() < 20:
            return

        pw.IssueOrder(my_planet.PlanetID(), closess_planet.PlanetID(), my_planet_fleet)

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
