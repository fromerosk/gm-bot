from .pieces import PieceColor, Blacks, Whites #, Pawn, Rook, Knight, Bishop, King, Queen

class Board(list):

    def __init__(self, boar = None):
        if boar is None:
            self.append(self._piecesRow(PieceColor.White))
            self.append(self._pawnRow(PieceColor.White))
            self.append(self._emptyRow())
            self.append(self._emptyRow())
            self.append(self._emptyRow())
            self.append(self._emptyRow())
            self.append(self._pawnRow(PieceColor.Black))
            self.append(self._piecesRow(PieceColor.Black))
        else:
            self = self.extend(boar)

    @staticmethod
    def _emptyRow():
        return [0] * 8

    @staticmethod
    def _pawnRow(color):
        if color == PieceColor.White:
            return [Whites.Pawn] * 8
        else:
            return [Blacks.Pawn] * 8

    @staticmethod
    def _piecesRow(color):
        if color == PieceColor.White:
            return [Whites.Rook, Whites.Knight, Whites.Bishop, Whites.Queen, Whites.King, Whites.Bishop, Whites.Knight, Whites.Rook]
        else:
            return [Blacks.Rook, Blacks.Knight, Blacks.Bishop, Blacks.Queen, Blacks.King, Blacks.Bishop, Blacks.Knight, Blacks.Rook]


    # def move():
        