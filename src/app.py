"""
    Program description...
"""
import sys
import requests


def find_pairs(nba_players: list, height_in: int):
    """
    @params: nba_players NBA dataset
    @params: height_in  Height in inches to be adds up
    """
    matches = dict()

    counter_matching_pairs: int = 0

    for id_player, player in enumerate(nba_players):
        diff = str(height_in - int(player["h_in"]))

        if diff in matches.values():
            counter_matching_pairs += 1
            # getting the idx for the pair_player on nba_players
            sec_id_player = int(
                list(matches.keys())[list(matches.values()).index(diff)]
            )
            sec_player = nba_players[sec_id_player]

            print(
                f"- {sec_player['first_name']} {sec_player['last_name']} \t {player['first_name']} {player['last_name']}"
            )

        matches[str(id_player)] = player["h_in"]

    if counter_matching_pairs == 0:
        print("No matches found")

    # included only for testing purpose
    return counter_matching_pairs


if __name__ == "__main__":

    try:
        HEIGHT = int(sys.argv[1])
        END_POINT_URL = "https://mach-eight.uc.r.appspot.com/"

        response = requests.get(END_POINT_URL)
        response.raise_for_status()
        NBA_PLAYERS = response.json()["values"]

        find_pairs(nba_players=NBA_PLAYERS, height_in=HEIGHT)

    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    except IndexError:
        print("You did not specify the height in inches to be adds up")
