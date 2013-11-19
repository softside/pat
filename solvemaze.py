from maze import Maze
def main():
    maze =buildMaze("mazefile.txt")
    if maze.findpath():
        print "path found..."
        maze.draw()
    else:
        print "Path not found..."

def buildMaze(filename):
    infile = open(filename,'r')

    nrows,ncols = readValuePair(infile)
    maze = Maze(nrows,ncols)

    row.col = readValuePair(infile)
    maze.setStart(row,col)

    row.col = readValuePair(infile)
    maze.setExit(row,col)

    for row in range(nrows):
        line = infile.readline()
        for col in range(len(line)):
            maze.setWall(row,col)

    infile.close()
    return maze

def readValuePair(infile):
    line = infile.readline()
    valA, valB = line.split()
    return int(valA),int(valB)
#main()
buildMaze("maze_map.txt")
