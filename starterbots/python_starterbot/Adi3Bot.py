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
import random



def ships_parameter(pw, isSource=True):
    lst = pw.MyPlanets() if isSource else pw.NotMyPlanets()
    return sorted(lst, key=lambda x: x.NumShips())

def growth_parameter(pw, isSource=True, all_ships=False):
    my_ships = pw.MyPlanets()
    not_my_ships = pw.NotMyPlanets()
    if all_ships:
        return sorted(my_ships + not_my_ships, key=lambda x: x.GrowthRate())
    else:
        lst = pw.MyPlanets() if isSource else pw.NotMyPlanets()
        return sorted(lst, key=lambda x: x.GrowthRate())


def distance_parameter(pw, source_planet):
    lst = pw.MyPlanets()
    return sorted(lst, key=lambda x: pw.Distance(source_planet, x.PlanetID()))


def DoTurn(pw):
    """
    Your code goes in this function
    :param pw: The planet wars object
    """

    # (1) If we currently have a fleet in flight, just do nothing.
    if len(pw.MyFleets()) >= 1:
        return

    # get source planet
    sorted_num_ships = ships_parameter(pw)
    rand = random.randint(0, len(sorted_num_ships) - 1)
    source_planet = sorted_num_ships[rand]
    source_planet_id = source_planet.PlanetID()

    # get destination planet
    sorted_growth = growth_parameter(pw, False, True)
    destination_planet = sorted_growth[len(sorted_growth) - 1]
    destination_planet_id = destination_planet.PlanetID()

    num_ships = source_planet.NumShips()
    pw.IssueOrder(source_planet_id, destination_planet_id, num_ships)


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
