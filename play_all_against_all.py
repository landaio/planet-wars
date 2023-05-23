import argparse
import os
import shlex
import subprocess
from itertools import combinations

import tools.play_utils
import tools.map_generator as map_generator
import tools.map_generator_v2

GAME_ENGINE_COMMAND = "java -jar tools/PlayGame-1.2.jar"

BOTS = [
    "AmitBot.py",
    "Adi2Bot.py",
    "AsianBot.py",
    "DenisBot.py",
    "HadarBot.py",
    "ShiranBot.py",
]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Play multiple Planet Wars games with a random maps.")
    parser.add_argument(
        "--old_maps", action="store_true", dest="old_maps",
        help="whether to generate maps using the old map generator.")
    parser.add_argument(
        "--max_turn_time", action="store", default=1000, type=int,
        help="maximum time (in ms) that a bot can have on its turn.", dest="max_turn_time")
    parser.add_argument(
        "--max_num_turns", action="store", default=200, type=int,
        help="maximum number of turns that a game can last.", dest="max_num_turns")
    parser.add_argument(
        "number_games", action="store", type=int, help="number of games to play.")
    arguments = parser.parse_args()

    if not arguments.old_maps:
        map_generator = tools.map_generator_v2

    games = list(combinations(BOTS, 2))

    scores = {}

    for game_number in range(arguments.number_games):
        map_path = f"maps/multiple{game_number + 1}.txt"
        map_generator.save_map(map_path)

    for game in games:
        one, two = game
        player_one = tools.play_utils.get_command(f"starterbots/python_starterbot/{one}")
        player_two = tools.play_utils.get_command(f"starterbots/python_starterbot/{two}")

        player_one_name = one.replace('.py', '')
        player_two_name = two.replace('.py', '')

        """ Play the games below! Very cool!"""

        # (draw, bot one, bot two)
        result_tracker_list = [0, 0, 0]

        for game_number in range(arguments.number_games):
            map_path = f"maps/multiple{game_number + 1}.txt"
            command = "{} {} {} {} \"\" \"{}\" \"{}\"".format(
                GAME_ENGINE_COMMAND, map_path, arguments.max_turn_time, arguments.max_num_turns,
                player_one, player_two
            )

            result = subprocess.run(
                shlex.split(command), stdout=open(os.devnull, "w+"), stderr=subprocess.PIPE
            )

            verdict = result.stderr.decode().strip().split("\n")[-1]
            if verdict.count(" ") == 2:
                result_tracker_list[int(verdict.split(" ")[1])] += 1
            else:
                result_tracker_list[0] += 1

            verdict = verdict.replace("Player 1", player_one_name).replace("Player 2", player_two_name)
            # print(f"Game {game_number + 1} verdict: {verdict}", end="  ")
            # print(f"(+{result_tracker_list[1]}={result_tracker_list[0]}-{result_tracker_list[2]})")

        print("---")
        print(f"  {player_one_name} wins: {result_tracker_list[1]}")
        print(f"  {player_two_name} wins: {result_tracker_list[2]}")
        print(f"  Draws: {result_tracker_list[0]}")
        if player_one_name not in scores:
            scores[player_one_name] = 0
        if player_two_name not in scores:
            scores[player_two_name] = 0
        scores[player_one_name] += result_tracker_list[1]
        scores[player_two_name] += result_tracker_list[2]

    print(f'Winners: {scores}')

