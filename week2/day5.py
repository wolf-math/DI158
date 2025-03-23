spaces = [
    ["","",""],
    ["","",""],
    ["","",""]
    ]

board = f"""
 1     2    3
1   |     |    
   --------------
2   |  {spaces[1][1]}   |
   --------------
3   |     | 

"""

def play():
    display_board()
    x = player_input