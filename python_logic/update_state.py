# will handle game logic not related to printing

class UpdateState:
    def process_pick(self, pick_id, available_board, user_board, board):
        print(user_board)
        print(available_board)
        user_board[pick_id] = available_board[pick_id]
        
        return user_board