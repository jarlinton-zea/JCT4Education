import requests


def find_pairs(nba_players: list, height_in: int = 0):
    """
    @params: nba_players NBA DATASET
    """

    matches = dict()
    """
        val: index -> 'h_in' 
        val: first_name + last_name
        index: index on nba_players
        {'id_player': 'h_in'}
    """

    for id_player, player in enumerate(nba_players):
        diff = str(height_in - int(player["h_in"]))

        if diff in matches.values():
            # getting the idx for the pair_player on nba_players
            sec_id_player = int(
                list(matches.keys())[list(matches.values()).index(diff)]
            )
            sec_player = nba_players[sec_id_player]

            print(
                f"- {sec_player['first_name']} {sec_player['last_name']} \t {player['first_name']} {player['last_name']}"
            )

        matches[str(id_player)] = player["h_in"]

    # print(matches.values())
    # print(nba_players)


if __name__ == "__main__":

    try:
        HEIGHT = 139
        END_POINT_URL = "https://mach-eight.uc.r.appspot.com/"

        response = requests.get(END_POINT_URL)
        response.raise_for_status()
        NBA_PLAYERS = response.json()["values"]

        find_pairs(nba_players=NBA_PLAYERS, height_in=HEIGHT)

    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
