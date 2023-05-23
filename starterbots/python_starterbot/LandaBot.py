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

    # (1) If we currently have a fleet in flight, just do nothing.
    if len(pw.MyFleets()) >= 1:
        return

    # (2) Find my planet with the most amount of ships
    source_planet = -1
    source_num_ships = 0
    my_planets = pw.MyPlanets()
    for p in my_planets:
        score = float(p.NumShips())
        if score > source_num_ships:
            source_planet = p.PlanetID()
            source_num_ships = p.NumShips()

    # (3) Find the weakest enemy or neutral planet.
    best_planet = -1
    best_planet_distance = 999999.0
    best_planet_score = 999999.0
    not_my_planets = pw.NotMyPlanets()
    for p in not_my_planets:
        if p.NumShips() < best_planet_score and \
                (best_planet == -1 or pw.Distance(best_planet, p.PlanetID()) < best_planet_distance):
            best_planet_score = p.NumShips()
            best_planet_distance = pw.Distance(best_planet, p.PlanetID())
            best_planet = p.PlanetID()

    # (4) Send half the ships
    if source_planet >= 0 and best_planet >= 0:
        num_ships = source_num_ships / 2
        pw.IssueOrder(source_planet, best_planet, num_ships)


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
