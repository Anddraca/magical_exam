# will handle game logic not related to printing
from random import shuffle
class UpdateState:
    # def process_pick(self, pick_id, available_board, user_board, board):
    #     print(user_board)
    #     print(available_board)
    #     user_board[pick_id] = available_board[pick_id]
        
    #     return user_board

    def process_pick(self, pick_id, available_board, board):
        # print(available_board)
        try:
            shuffle(board[pick_id])
            available_board[pick_id] = board[pick_id]
            print("AVAILABELE BOAR")
            print(available_board)
        except KeyError:
            print('ID not recognized, please try again')

        return available_board

    def remove_top_card(self, pick_id, available_board):
        available_board[pick_id].pop(0)