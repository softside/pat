from array import Array2D
#from lliststack import Stack

class Maze:
    MAZE_WALL = "*"
    PATH_TIKEN = "x"
    TRIED_TOKEN = "o"

    def __init__(self,numRows,numCols):
        self._mazeCells = Array2D(numRows,numCols)
        self._startCell = None
        self._exitCell = None

    def numRows(self):
        return self._mazeCells.numRows()

    def numCols(self):
        return self._mazeCells.numCols()

    def setWall(self,row,col):
        assert row>=0 and row<self.numRows() and\
            col >= 0 and col< self.numCols(),"Cell index out of range"
        self._mazeCells.set(row,col,self.MAZE_WALL)

    def setStart(self,row,col):
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), "Cell index out of range."
        self._startCell = _CellPosition( row, col )

        def setExit( self, row, col ):
            assert row >= 0 and row < self.numRows() and \
                col >= 0 and col < self.numCols(), "Cell index out of range."
            self._exitCell = _CellPosition( row, col )

    def finpath(self):
        pass

    def reset(self):
        pass
    def draw(self):
        pass
