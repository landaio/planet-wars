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
import itertools
from PlanetWars import PlanetWars



def DoTurn(pw):
    """
    Your code goes in this function
    :param pw: The planet wars object
    """

    # (1) If we currently have a fleet in flight, just do nothing.
    if len(pw.MyFleets()) >= 1:
        return

    source_planet = -1
    source_num_ships = 0
    my_planets = pw.MyPlanets()

    for p in my_planets:
        score = float(p.NumShips())
        if score > source_num_ships:
            source_planet = p.PlanetID()
            source_num_ships = p.NumShips()

    not_my_planets = pw.NotMyPlanets()
    closest_planets = 5
    distances = {}
    for p in not_my_planets:
        if p.NumShips() < source_num_ships:
            distances[p.PlanetID()] = pw.Distance(source_planet, p.PlanetID())

    sorted_dict = dict(sorted(distances.items(), key=lambda x: x[1], reverse=False))
    closest_planets = dict(itertools.islice(sorted_dict.items(), closest_planets))
    for id_, distance in closest_planets.items():
        num_ships = source_num_ships / 3
        pw.IssueOrder(source_planet, id_, num_ships)
        source_num_ships -= num_ships
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
