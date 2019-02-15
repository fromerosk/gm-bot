class PieceColor:
    White: "W"
    Black: "B"



class _Piece:
    color = None

    def name(self):
        return type(self).__name__



class Pawn(_Piece):
    def __init__(self, color = PieceColor.White):
        self.color = color

class Rook(_Piece):
    pass

class Knight(_Piece):
    pass

class Bishop(_Piece):
    pass

class Queen(_Piece):
    pass

class King(_Piece):
    pass