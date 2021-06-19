# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 18:53:53 2018

@author: Eric
"""

import tkinter as tk
import random

class Grid:
    def __init__(self, n):
        self.size = n
        self.cells = self.generate_empty_grid()
        """設定標誌，用來判斷
        是否壓縮、合併、移動"""
        self.compressed = False
        self.merged = False
        self.moved = False
    
    """生成空的棋盤"""
    def generate_empty_grid(self):
        emptyGrid = []
        for i in range(self.size):
            rowGrid = []
            for j in range(self.size):
                rowGrid.append(0)
                
            emptyGrid.append(rowGrid)
                
        return emptyGrid
    
    def retrieve_empty_cells(self):
        empty_cells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.cells[i][j] == 0:
                    empty_cells.append((i, j))
                    
        return empty_cells
    
    """隨機選一個空的棋格生成數字2"""
    def random_cell(self):
        cell = random.choice(self.retrieve_empty_cells())
        i = cell[0]
        j = cell[1]
        self.cells[i][j] = 2
        
    """直接設定格子"""
    def set_cells(self, col , row , num):
        self.cells[col][row] = num
        
        """清除標誌"""
    def clear_flags(self):
        self.compressed = False
        self.merged = False
        self.moved = False
        
        """向左壓縮"""
    def left_compress(self):
        self.compressed = False
        new_grid = self.generate_empty_grid()
        
        for i in range(self.size):
            count = 0
            for j in range(self.size):
                if self.cells[i][j] != 0:
                    new_grid[i][count] = self.cells[i][j]
                    if count != j:
                        self.compressed = True
                    count += 1
        self.cells = new_grid
    
    """向上壓縮"""
    def up_compress(self):
        self.compressed = False
        new_grid = self.generate_empty_grid()
        
        for i in range(self.size):
            count = 0
            for j in range(self.size):
                if self.cells[j][i] != 0:
                    new_grid[count][i] = self.cells[j][i]
                    if count != j:
                        self.compressed = True
                    count += 1
                    
        self.cells = new_grid

    """向右壓縮"""
    def right_compress(self):
        self.compressed = False
        new_grid = self.generate_empty_grid()
        
        for i in range(self.size):
            count = self.size -1
            for j in range(self.size -1,-1,-1):
                if self.cells[i][j] != 0:
                    new_grid[i][count] = self.cells[i][j]
                    if count != j:
                        self.compressed = True
                    count -= 1
                    
        self.cells = new_grid
        
    """向下壓縮"""
    def down_compress(self):
        self.compressed = False
        new_grid = self.generate_empty_grid()
        
        for i in range(self.size):
            count = self.size -1
            for j in range(self.size -1,-1,-1):
                if self.cells[j][i] != 0:
                    new_grid[count][i] = self.cells[j][i]
                    if count != j:
                        self.compressed = True
                    count -= 1
                    
        self.cells = new_grid

    """向左合併"""
    def left_merge(self):
        self.merged = False
        for i in range(self.size):
            for j in range(self.size - 1):
                
                if self.cells[i][j] == self.cells[i][j + 1] \
                and  self.cells[i][j] != 0:
                    
                    self.cells[i][j] *= 2
                    self.cells[i][j + 1] = 0
                    self.merged = True
                    
    
    """向上合併"""             
    def up_merge(self):
        self.merged = False
        for i in range(self.size):
            for j in range(self.size - 1):
                
                if self.cells[j][i] == self.cells[j+1][i] \
                and self.cells[j][i] != 0:
                    
                    self.cells[j][i] *= 2
                    self.cells[j+1][i] = 0
                    self.merged = True
                    
    """向右合併"""               
    def right_merge(self):
        self.merged = False
        for i in range(self.size):
            for j in range(self.size -1, 0, -1):
                
                if self.cells[i][j] == self.cells[i][j - 1] \
                and self.cells[i][j] != 0:
                    
                    self.cells[i][j] *= 2
                    self.cells[i][j - 1] = 0
                    self.merged = True
                    
    """向下合併"""             
    def down_merge(self):
        self.merged = False
        for i in range(self.size):
            for j in range(self.size -1, 0, -1):
                
                if self.cells[j][i] == self.cells[j-1][i] \
                and self.cells[j][i] != 0:
                    
                    self.cells[j][i] *= 2
                    self.cells[j-1][i] = 0
                    self.merged = True
                    
        """找到2048這個數字"""
    def found_2048(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.cells[i][j] >= 2048:
                    return True
        return False

    """有沒有空的格子"""
    def has_empty_cells(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.cells[i][j] == 0:
                    return True
        return False

    """是否可以合併"""
    def can_merge(self):
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.cells[i][j] == self.cells[i][j + 1]:
                    return True
        for j in range(self.size):
            for i in range(self.size - 1):
                if self.cells[i][j] == self.cells[i + 1][j]:
                    return True
        return False
    

class GamePanel():
    
    """整體背景顏色"""
    BACKGROUND_COLOR = '#92877d'
    
    """空格子顏色"""
    EMPTY_CELL_COLOR = '#9e948a'
    
    """數字背景顏色"""
    CELL_BACKGROUND_COLOR_DICT = {
        '2': '#eee4da',
        '4': '#ede0c8',
        '8': '#ede2c8',
        '16':  '#ede5c7',
        '32':  '#ede9c8',
        '64':  '#ede8c8',
        '128':  '#nde4c5',
        '256':  '#ede3c8',
        '512':  '#ede2c8',
        '1024':  '#ede1c8',
        '2048':  '#ede0c4',
        'default': '#f9f6f2'
    }
    
    """數字字體顏色 """
    CELL_COLOR_DICT = {
        '2': '#776e65',
        '4': '#776e45',
        '8': '#973921',
        '16':'#7d3051',
        '32':'#7d3157',
        '64':'#7d3152',
        '128':'#7d3141',
        '256':'#7d3751',
        '512':'#7d3121',
        '1024':'#7d3651',
        '2048':'#7d3158',
        'default': '#f9f6f2'
    }
    
    FONT = ('Verdana', 24, 'bold')
    UP_KEYS = ('w', 'W', 'Up')
    LEFT_KEYS = ('k', 'K', 'Left')
    DOWN_KEYS = ('c', 'C', 'Down')
    RIGHT_KEYS = ('a', 'A', 'Right')

    def __init__(self , grid):
        """將grid放入類別屬性內"""
        self.grid = grid
        self.size = grid.size
        """建立一個tkinter主視窗"""
        self.window = tk.Tk()
        """設定視窗標題"""
        self.window.title("2048")
        """設定遊戲背景"""
        self.background = tk.Frame(self.window, bg=self.BACKGROUND_COLOR)
        """建立空串列，用來儲存格子Label"""
        self.cell_labels = []
        
        """初始化文字"""
        """用二維巢狀迴圈建立二維串列"""
        for i in range(self.size):
            #建立一個儲存"列"的串列
            row_labels = []
            for j in range( self.size):
                """背景顏色為EMPTY_CELL_COLOR"""
                """font為剛剛設置的FONT"""
                label = tk.Label(self.background, text='',
                                 bg= self.EMPTY_CELL_COLOR,
                                 font= self.FONT,
                                 width=4, height=2)
                """設定label位置"""
                label.grid(row=  i  , column=  j , padx=10, pady=10)
                """將新增好的Label放入row_labels內"""
                row_labels.append( label )
                """將新增好的row_labels放入cell_labels內"""
            self.cell_labels.append(row_labels  )
            #將background放置到window畫面上
        self.background.grid()
        

    """把格子和字上色"""
    def paint(self):
        """用兩個迴圈掃過網格"""
        for i in range(self.size):
            for j in range(self.size):
                
                 #如果那個格子數字是0
                if self.grid.cells[i][j] == 0:
                    """設定該格子的文字為空，背景為MPTY_CELL_COLOR"""
                    self.cell_labels[i][j].configure(text = '',
                                    bg = GamePanel.EMPTY_CELL_COLOR)
                    
                #如果不是0，則依照字典顏色上色
                #bg->background(背景)
                #fg->foreground(前景)
                else:
                    """cell_text為該格子的數值，轉為字串型態"""
                    cell_text = str(self.grid.cells[i][j])
                    """如果數字超過2048"""
                    if self.grid.cells[i][j] > 2048:
                        """color等於預設值"""
                        bg_color = GamePanel.CELL_BACKGROUND_COLOR_DICT.get('beyond')
                        fg_color = GamePanel.CELL_COLOR_DICT.get('beyond')
                        """如果數字沒超過2048"""
                    else:
                        """color由字典取值"""
                        bg_color = GamePanel.CELL_BACKGROUND_COLOR_DICT.get(cell_text)
                        fg_color = GamePanel.CELL_COLOR_DICT.get(cell_text)
                        
                    self.cell_labels[i][j].configure(
                        text= cell_text      ,
                        bg= bg_color (1,0,0)   , fg=fg_color  (0,1,0 )
                    
"""控制整個遊戲流程"""
class Game:
    def __init__(self, grid, panel):
        self.grid = grid
        self.panel = panel
        self.start_cells_num = 2
        self.over = False
        self.won = False

    """遊戲停止(輸了或贏了)"""
    def is_game_terminated(self):
        return self.over or self.won

    """遊戲開始"""
    def start(self):
        self.add_start_cells()
        self.panel.paint()
        self.panel.window.bind('<Key>', self.key_handler)
        self.panel.window.mainloop()

    """開始遊戲後產生的格子"""
    def add_start_cells(self):
        for i in range(self.start_cells_num):
            self.grid.random_cell()

    """判斷有沒有辦法移動(合併)"""
    def can_move(self):
        return self.grid.has_empty_cells() or self.grid.can_merge()

    """當按下鍵盤時所要做的事情"""
    def key_handler(self, event):
        if self.is_game_terminated():
            return

        self.grid.clear_flags()
        key_value = event.keysym
        
        #print('{} key pressed'.format(key_value))
        
        #判斷按下的按鍵是哪個功能
        if key_value in GamePanel.UP_KEYS:
            self.up()
        elif key_value in GamePanel.LEFT_KEYS:
            self.left()
        elif key_value in GamePanel.DOWN_KEYS:
            self.down()
        elif key_value in GamePanel.RIGHT_KEYS:
            self.right()
        else:
            pass

        self.panel.paint()
        
        """如果找到2048"""
        if self.grid.found_2048():
            self.you_win()
        
        """如果已經移動完了，則產生一個隨機數字"""
        if self.grid.moved:
            self.grid.random_cell()


        self.panel.paint()
        
        """如果無法再移動"""
        if not self.can_move():
            self.over = True
            self.game_over()

    """遊戲勝利"""
    def you_win(self):
        if not self.won:
            self.won = True
            print('You Win!')

    """遊戲失敗"""
    def game_over(self):
        print('Game over!')

    def up(self):
        self.grid.up_compress()
        self.grid.up_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.up_compress()

    def left(self):
        self.grid.left_compress()
        self.grid.left_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.left_compress()

    def down(self):
        self.grid.down_compress()
        self.grid.down_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.down_compress()

    def right(self):
        self.grid.right_compress()
        self.grid.right_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.right_compress()

size = 4
grid = Grid(size)
panel = GamePanel(grid)
game2048 = Game(grid, panel)
game2048.start()


