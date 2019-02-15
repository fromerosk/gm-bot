from .pieces import Pawn, Rook, Knight, Bishop, King, Queen

class Board(list):

    @staticmethod
    def _emptyRow():
        return [None] * 8

    @staticmethod
    def _pawnRow(color):
        return [Pawn()] * 8

    def __init__(self, boar = None):
        if boar is not None:
            self = boar[:]
        else:
            self = []