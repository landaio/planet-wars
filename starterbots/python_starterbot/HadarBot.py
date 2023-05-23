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
    log_file = open("log.txt", "a")
    # (1) If we currently have a fleet in flight, just do nothing.

    # (2) Find my planet with the most amount of ships
    my_planets = pw.MyPlanets()
    my_planets.sort(key=lambda planet: planet.NumShips(), reverse=True)
    my_planets = list(filter(lambda planet: planet.NumShips() >= 50, my_planets))
    if not my_planets:
        return
    best_planet = my_planets[0]
    enemy_planets = []
    for p in pw.NotMyPlanets():
        distance = pw.Distance(best_planet.PlanetID(), p.PlanetID())
        ships = p.NumShips()
        owner = 0.9 if p.Owner() == 0 else 1
        enemy_planets.append((p, distance, ships, owner))

    enemy_planets.sort(key=lambda x: x[1]*x[2]*x[3])
    enemy_planets = [planet for planet, *_ in enemy_planets]
    if enemy_planets:
        enemy_planet = enemy_planets[0]
        for my_planet in my_planets:
            num_ships = my_planet.NumShips()//2
            pw.IssueOrder(my_planet.PlanetID(), enemy_planet.PlanetID(), num_ships)
    log_file.close()


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
