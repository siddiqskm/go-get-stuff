"""
BattleShip Game
Input -
A series of 6 lines with various data detailed below

Output -
Which Player wins ?
"""
#
# System Imports
#
import sys
import enum
from typing import Any, List, Union
from pydantic import BaseModel


"""
Enum Classes
"""
class ShipWeight(enum.Enum):
    """
    Weights of Ships
    """
    P = 1
    Q = 2


"""
Data Classes
"""
class XY(BaseModel):
    """
    Co-Ordinates
    """
    x: int
    y: int


class Ship(BaseModel):
    """
    Data Class to store the following attributes -
        type: str
        health: integer
        coordinates: List[Associated Coordinates]
    """
    type: str = ''
    health: int = 0
    width: int = 0
    height: int = 0
    coordinates: List[XY] = []


class Layout(BaseModel):
    """
    Data class to store the following attributes -
        m: int (Rows)
        n: int (Columns)
    """
    m: int
    n: int


class Player(BaseModel):
    """
    Data class to store the following attributes -
        number: int
        ships: List[Ship]
    """
    id: int
    layout: Any
    ships: List[Ship]
    strikes: List[XY]
    next_strike_index: int


class Players(BaseModel):
    """
    Data class to store the player information -
        List[Player]
    """
    players: List[Player]


"""
Utility Functions
"""
def get_associated_index(input_char):
    """
    Returns the associated index for upper case characters
    """
    return ord(input_char) - 64


def get_ship_health(input_char):
    """
    Returns the ship health based on input character
    """
    if input_char == 'P':
        return ShipWeight.P.value
    else:
        return ShipWeight.Q.value


def get_ship_coordinates_with_start(width, height, input_coordinates):
    """
    Returns a list of indices based on width / height and start indices
    """
    alp, y = list(input_coordinates)
    x = get_associated_index(alp)
    coordinates = []
    for i in range(x, x + height):
        for j in range(int(y), int(y) + width):
            coordinates.append(XY(x = i, y = j))

    return coordinates


def get_associated_coordinates(input_pair):
    """
    Returns the associated co ordinates for the input string
    """
    alp, y = list(input_pair)
    return XY(x = get_associated_index(alp), y = int(y))


def print_layout(input_layout):
    """
    Prints the layout in readable format
    """
    # print("Input Layout is: %s" % input_layout)
    height = len(input_layout)
    width = len(input_layout[0])
    print('    ' + ' '.join([str(i) for i in range(1, width)]))
    print('-' * (width * 3))
    char_index = 65
    for i in range(1, height):
        temp_arr = []
        for j in range(1, width):
            if j == height - 1:
                temp_arr.append(input_layout[i][j])
                print("%s | " % chr(char_index) + ' '.join([str(ele) for ele in temp_arr]))
                temp_arr = []
                char_index += 1
            else:
                temp_arr.append(input_layout[i][j])


def prune_input(input_args):
    """
    Layout attribute 'layout' constitutes -
        First Line - width * height (in characters) ->
            Transform into m * n format (all numeric)
            Identified by the input arg - layout in BattleShip class
        Second Line - Number of BattleShips ->
            Identified by the input arg - num_of_ships in Battleship class
        Third + Fourth + Fifth + Sixth lines -> Player Information ->
            Identified by the attribute 'players' in Battleship class
                Space Separated strings are broken down into the
                following attributes ->
                    Identified by the attribute, ship_type - valid (P/Q)
                    Followed by Size -> Ship size (Assuming same for
                        both players)
                    Co-ordinates of ships for both players
            Ideally 'players' dict is of format -
            {
                player1: {
                    id: 1,
                    ships: [Class ship objects]
                    strikes: [Class strike objects]
                    }
                },
                player2: {
                    id: 1,
                    ships: [Class ship objects]
                    strikes: [Class strike objects]
                }
            }
    """
    # print("The input args are: ", input_args)
    m, n = input_args[0].split(' ')
    layout = Layout(
        m = int(m) + 1,
        n = get_associated_index(n) + 1
    )
    #
    # Consolidating Ship Info
    #
    num_of_ships = int(input_args[1])
    playera_ships = []
    playerb_ships = []
    for index in range(2, num_of_ships + 2):
        ship_info = input_args[index].split(' ')
        ship_info_type = ship_info[0]
        #
        # Player 1 Ships
        #
        a_ship = Ship()
        a_ship.type = ship_info_type
        a_ship.health = get_ship_health(ship_info[0])
        a_ship.width = int(ship_info[1])
        a_ship.height = int(ship_info[2])
        a_ship.coordinates = get_ship_coordinates_with_start(
            int(ship_info[1]), int(ship_info[2]), ship_info[3])
        playera_ships.append(a_ship)
        #
        # Player 2 Ships
        #
        b_ship = Ship()
        b_ship.type = ship_info_type
        b_ship.health = get_ship_health(ship_info[0])
        b_ship.width = int(ship_info[1])
        b_ship.height = int(ship_info[2])
        b_ship.coordinates = get_ship_coordinates_with_start(
            int(ship_info[1]), int(ship_info[2]), ship_info[4])
        playerb_ships.append(b_ship)
    #
    # Fetching Strike information
    #
    playera_strikes = [get_associated_coordinates(each_ele)
                       for each_ele in input_args[-2].split(' ')]
    playerb_strikes = [get_associated_coordinates(each_ele)
                       for each_ele in input_args[-1].split(' ')]
    #
    # Conoslidating players information
    #
    playera = Player(
        id = 1,
        layout = [[0 for _ in range(layout.m)] for _ in range(layout.n)],
        ships = playera_ships,
        strikes = playera_strikes,
        next_strike_index = 0
    )
    playerb = Player(
        id = 2,
        layout = [[0 for _ in range(layout.m)] for _ in range(layout.n)],
        ships = playerb_ships,
        strikes = playerb_strikes,
        next_strike_index = 0
    )
    return Players(players = [playera, playerb])


class BattleShip():
    """
    2 player game for battleship ->

    Input Args -
        Players

    Class variables -
        last_strike - boolean
            0 for miss
            1 for hit
    """
    def __init__(self, players):
        """
        Constructor
        """
        self.players = players.players
        print("Player Information -", self.players)
        self.initialize_game()
        self.begin_game()

    def initialize_game(self):
        """
        Initializes the layouts for the associated players
        """
        for index, player in enumerate(self.players):
            for each_ship in player.ships:
                print("Ship - %s" % each_ship)
                for pairs in each_ship.coordinates:
                    print("Marking the co-ordinates: %s in layout" % pairs)
                    self.players[index].layout[pairs.x][pairs.y] = 1

        print("Layouts after initialization is: %s" % self.players)
        print("\nPlayer A Battle Yard: \n")
        print_layout(self.players[0].layout)
        print("\nPlayer B Battle Yard: \n")
        print_layout(self.players[1].layout)

    def get_player_ship_consolidated_health(self, player_index):
        """
        Returns the consolidated health of the input player
        """
        final_health = 0
        for each_ship in self.players[player_index].ships:
            final_health += each_ship.health

        # print("Consolidated health for %s is %s" % (player_index, final_health))

        return final_health

    def are_attempts_left(self, player_index):
        """
        Checks the ships health of input user to decide if the user is in
        game still
            Returns - Boolean
        """
        health = self.get_player_ship_consolidated_health(player_index)
        return False if (health <= 0) else True

    def mark_strike_for_player(
            self,
            curr_player_index,
            strike_player_index,
            strike_location):
        """
        Marks an index for the current player and updates a class variable
        based on strike call
        """
        print("Curr %s, Striker %s, Strike Location %s"
              % (curr_player_index, strike_player_index, strike_location))
        strike_flag = False
        for each_ship in self.players[strike_player_index].ships:
            for each_loc in each_ship.coordinates:
                if each_loc.x == strike_location.x and each_loc.y == strike_location.y:
                    #print("Its a strike reducing ship health by 1")
                    each_ship.health -= 1
                    #print("After reducing - %s" % each_ship.health)
                    strike_flag = True
                    break
            if strike_flag:
                break
        #
        # Mark Strike Location
        #
        self.players[strike_player_index].layout[strike_location.x][strike_location.y] = 'X'
        self.players[curr_player_index].next_strike_index += 1

        print("\nMissile Fired on Player %s - Location - %s "
              "Fetching battle ground status ... \n"
              % (self.players[strike_player_index].id, strike_location))
        print("Here is the latest status of battleground ...\n")
        print_layout(self.players[strike_player_index].layout)
        print("*" * 30)

        if strike_flag:
            print("\nOhoo seems ship is hit !!!")
            return True
        else:
            print("\nNope Miss, Missile Wasted !!!")
            return False

    def begin_game(self):
        """
        Game begins with missile strikes and finally decides winner
        """
        curr_user_index = 0
        user_index_to_strike = 1
        #
        # A rude method to continue attempt - can be made smarter
        # Works only for 2 players
        #
        game_tie = False
        winner = None
        while self.are_attempts_left(curr_user_index):
            #
            # Current Player Stats
            #
            curr_player = self.players[curr_user_index]
            curr_player_strikes = curr_player.strikes
            #print("Current Player Strike index is: %s and total strikes is: %s"
            #      % (curr_player.next_strike_index, len(curr_player_strikes)))
            #
            # Striker Players Stats
            #
            player_on_strike = self.players[user_index_to_strike]
            player_on_strikes_list = player_on_strike.strikes

            strike_status = self.mark_strike_for_player(
                curr_user_index,
                user_index_to_strike,
                curr_player_strikes[curr_player.next_strike_index])

            # print("Player Health Status: %s" % self.players[curr_user_index])
            
            if strike_status:
                print("Missile HIT, Same Player continues !!!")
                if self.get_player_ship_consolidated_health(user_index_to_strike) == 0:
                    winner = curr_player.id
                    break
            else:
                print("Missile MISS, Time to change the player !!!")
                if curr_player.next_strike_index >= len(curr_player_strikes) and \
                    player_on_strike.next_strike_index >= len(player_on_strikes_list):
                    game_tie = True
                    break
                elif player_on_strike.next_strike_index < len(player_on_strikes_list):
                    curr_user_index, user_index_to_strike = \
                        user_index_to_strike, curr_user_index
                else:
                    print("No point in changing players, the current user will continue ...")

        if game_tie:
            print("No missiles left for any players - Its a draw !!!")
        else:
            print("Player %s wins !!!" % winner)


"""
Sample Input -
5 E
2
Q 1 1 A1 B2
P 2 1 D4 C3
A1 B2 B2 B3
A1 B2 B3 A1 D1 E1 D4 D4 D5 D5
"""
buffer = []
while True:
    line = sys.stdin.readline().rstrip('\n')
    if line == 'quit':
        break
    else:
        buffer.append(line)
#
# Prune Input
#
players = prune_input(buffer)
obj = BattleShip(players)