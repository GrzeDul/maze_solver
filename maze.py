from cell import Cell
import time, random
class Maze:
    def __init__(
        self, 
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrence_and_exit()
        random.seed(seed)
        self._break_all_r(0,0)      
                
    def _create_cells(self):
        for col_num in range(self._num_cols):
            row = []
            for row_num in range(self._num_rows):
                row.append(Cell(self._win))
            self._cells.append(row)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)
                
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.00)
    
    def _break_entrence_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[self._num_cols-1][self._num_rows-1].has_right_wall = False
        self._draw_cell(0,0)
        self._draw_cell(self._num_cols-1, self._num_rows-1)
    
    def _break_all_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        adjecent_cells = {
        'left': None,
        'top' : None,
        'right': None,
        'bottom': None}
        while True:
            not_visited = []
            if i != 0:
                adjecent_cells['left'] = (i-1,j,'left','right')
            if j != 0:
                adjecent_cells['top'] = (i,j-1,'top','bottom')
            if i != self._num_cols-1:
                adjecent_cells['right'] = (i+1,j,'right','left')
            if j != self._num_rows-1:
                adjecent_cells['bottom'] = (i,j+1,'bottom','top')
            for tuple in adjecent_cells.values():
                if tuple and not self._cells[tuple[0]][tuple[1]].visited:
                    not_visited.append(tuple)
            if not not_visited:
                return
            next_cell_ij = random.choice(not_visited)
            next_cell = self._cells[next_cell_ij[0]][next_cell_ij[1]]
            setattr(current,f'has_{next_cell_ij[2]}_wall', False)
            setattr(next_cell,f'has_{next_cell_ij[3]}_wall', False)
            self._draw_cell(i, j)
            self._draw_cell(next_cell_ij[0], next_cell_ij[1])
            self._break_all_r(next_cell_ij[0], next_cell_ij[1])
        

            
