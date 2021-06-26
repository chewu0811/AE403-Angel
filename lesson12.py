# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:21:26 2021

@author: Admin
"""

import tkinter as tk
import random
from tkinter import messagebox


class Grid:
    def __init__(self, n):
        self.size = n
        self.cells = self.generate_empty_grid()
        """設定標誌，用來判斷是否壓縮、合併、移動"""
        self.compressed = False
        self.merged = False
        self.moved = False
        self.score = 0
    
    """生成空的棋盤"""
    def generate_empty_grid(self):
        #建立一個儲存整個二維串列
        emptyGrid = []
        """用二維巢狀迴圈建立二維串列"""
        for i in range(self.size):
            #建立一個儲存"列"的串列
            rowGrid = []
            for j in range(self.size):
                rowGrid.append(0)
                
            emptyGrid.append(rowGrid)
                
        return emptyGrid
    
    """取得所有空的格子"""
    def retrieve_empty_cells(self):
        #建立一個儲存所有空格子的串列
        empty_cells = []
        """用二維朝狀迴圈掃過網格"""
        for i in range(self.size):
            for j in range(self.size):
                """如果該格子等於0,則在empty_cells新增"""
                if self.cells[i][j] == 0:
                    empty_cells.append((i, j))
                    
        return empty_cells
    
    """隨機選一個空的棋格生成數字2"""
    def random_cell(self):
        cell = random.choice(self.retrieve_empty_cells())
        """把取到的元祖資料分別存入i和j"""
        i = cell[0]
        j = cell[1]
        self.cells[i][j] = 2
        
    """直接設定格子"""
    def set_cells(self, col , row , num):
        """直接設定格子的數值"""
        self.cells[col][row] = num
        
    """清除標誌"""
    def clear_flags(self):
        self.compressed = False
        self.merged = False
        self.moved = False
        
    """向左壓縮"""
    def left_compress(self):
        self.compressed = False
        """重新生成一個空的二為串列網格，儲存至new_grid"""
        new_grid = self.generate_empty_grid()
        
        """用二維網格掃過網格"""
        for i in range(self.size):
            count = 0
            for j in range(self.size):
                """如果該格子的值不等於0，則進行壓縮"""
                if self.cells[i][j] != 0:
                    new_grid[i][count] = self.cells[i][j]
                    """如果count不等於j，則表示有進行過壓縮"""
                    if count != j:
                        self.compressed = True
                    """若成功進行壓縮，count值加一"""
                    count += 1
        """全部壓縮完後，將舊的網格取代成新的網格"""
        self.cells = new_grid
    
    """向上壓縮"""
    def up_compress(self):
        self.compressed = False
        """重新生成一個空的二為串列網格，儲存至new_grid"""
        new_grid = self.generate_empty_grid()
        
        """用二維網格掃過網格"""
        for i in range(self.size):
            count = 0
            for j in range(self.size):
                """如果該格子的值不等於0，則進行壓縮"""
                if self.cells[j][i] != 0:
                    new_grid[count][i] = self.cells[j][i]
                    """如果count不等於j，則表示有進行過壓縮"""
                    if count != j:
                        self.compressed = True
                    """若成功進行壓縮，count值加一"""
                    count += 1
        """全部壓縮完後，將舊的網格取代成新的網格"""
        self.cells = new_grid

    """向右壓縮"""
    def right_compress(self):
        self.compressed = False
        """重新生成一個空的二為串列網格，儲存至new_grid"""
        new_grid = self.generate_empty_grid()
        
        """用二維網格掃過網格"""
        for i in range(self.size):
            count = self.size -1
            for j in range(self.size -1,-1,-1):
                """如果該格子的值不等於0，則進行壓縮"""
                if self.cells[i][j] != 0:
                    new_grid[i][count] = self.cells[i][j]
                    """如果count不等於j，則表示有進行過壓縮"""
                    if count != j:
                        self.compressed = True
                    """若成功進行壓縮，count值減一"""
                    count -= 1
        """全部壓縮完後，將舊的網格取代成新的網格"""
        self.cells = new_grid
        
    """向下壓縮"""
    def down_compress(self):
        self.compressed = False
        """重新生成一個空的二為串列網格，儲存至new_grid"""
        new_grid = self.generate_empty_grid()
        
        """用二維網格掃過網格"""
        for i in range(self.size):
            count = self.size -1
            for j in range(self.size -1,-1,-1):
                """如果該格子的值不等於0，則進行壓縮"""
                if self.cells[j][i] != 0:
                    new_grid[count][i] = self.cells[j][i]
                    """如果count不等於j，則表示有進行過壓縮"""
                    if count != j:
                        self.compressed = True
                    """若成功進行壓縮，count值減一"""
                    count -= 1
        """全部壓縮完後，將舊的網格取代成新的網格"""        
        self.cells = new_grid
    """向左合併"""
    def left_merge(self):
        self.merged = False
        """用二維網格掃過網格(須注意range範圍及串列索引值)"""
        for i in range(self.size):
            """由於cells[i][j+1]會超出索引值，因而此處range放size-1"""
            for j in range(self.size - 1):
                
                """如果數字相同，且不為0則合併"""
                if self.cells[i][j] == self.cells[i][j + 1] \
                and  self.cells[i][j] != 0:
                    self.score = self.score + self.cells[i][j]
                    """左方數字*2，右方數值等於0"""
                    self.cells[i][j] *= 2
                    self.cells[i][j + 1] = 0
                    self.merged = True
                    
    
    """向上合併"""             
    def up_merge(self):
        self.merged = False
        """用二維網格掃過網格(須注意range範圍及串列索引值)"""
        for i in range(self.size):
            for j in range(self.size - 1):
                
                """如果數字相同，且不為0則合併"""
                if self.cells[j][i] == self.cells[j+1][i] \
                and self.cells[j][i] != 0:
                    self.score = self.score + self.cells[i][j]
                    """上方數字*2，下方數值等於0"""
                    self.cells[j][i] *= 2
                    self.cells[j+1][i] = 0
                    self.merged = True
                    
    """向右合併"""               
    def right_merge(self):
        self.merged = False
        """用二維網格掃過網格(須注意range範圍及串列索引值)"""
        for i in range(self.size):
            for j in range(self.size -1, 0, -1):
                
                """如果數字相同，且不為0則合併"""
                if self.cells[i][j] == self.cells[i][j - 1] \
                and self.cells[i][j] != 0:
                    self.score = self.score + self.cells[i][j]
                    """右方數字*2，左方數值等於0"""
                    self.cells[i][j] *= 2
                    self.cells[i][j - 1] = 0
                    self.merged = True
                    
    """向下合併"""             
    def down_merge(self):
        self.merged = False
        """用二維網格掃過網格(須注意range範圍及串列索引值)"""
        for i in range(self.size):
            for j in range(self.size -1, 0, -1):
                
                """如果數字相同，且不為0則合併"""
                if self.cells[j][i] == self.cells[j-1][i] \
                and self.cells[j][i] != 0:
                    self.score = self.score + self.cells[i][j]
                    """下方數字*2，上方數值等於0"""
                    self.cells[j][i] *= 2
                    self.cells[j-1][i] = 0
                    self.merged = True
                    
        """找到2048這個數字"""
    def found_2048(self):
        """用二維網格掃過網格"""
        for i in range(self.size):
            for j in range(self.size):
                if self.cells[i][j] >= 8:
                    return True
        return False
    """有沒有空的格子"""
    def has_empty_cells(self):
        """用二維網格掃過網格，如果有任一格數值為0回傳True，否則為False"""
        for i in range(self.size):
            for j in range(self.size):
                if self.cells[i][j] == 0:
                    return True
        return False

    """是否可以合併"""
    def can_merge(self):
        """用二維網格掃過網格"""
        for i in range(self.size):
            for j in range(self.size - 1):
                """判斷水平方向是否有相鄰且相同的兩個數字，若有回傳True"""
                if self.cells[i][j] == self.cells[i][j + 1]:
                    return True
        """用二維網格掃過網格"""
        for j in range(self.size):
            for i in range(self.size - 1):
                """判斷垂直方向是否有相鄰且相同的兩個數字，若有回傳True"""
                if self.cells[i][j] == self.cells[i + 1][j]:
                    return True
        """如果都找不到則回傳False"""
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
        '8': '#f2b179',
        '16': '#f59563',
        '32': '#f67c5f',
        '64': '#f65e3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#edc850',
        '1024': '#edc53f',
        '2048': '#edc22e',
        'default': '3c3a32'
    }
    
    """數字字體顏色 """
    CELL_COLOR_DICT = {
        '2': '#776e65',
        '4': '#776e65',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#f9f6f2',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
        'default': '#f9f6f2'
    }
    
    FONT = ('Verdana', 24, 'bold')
    UP_KEYS = ('w', 'W', 'Up')
    LEFT_KEYS = ('a', 'A', 'Left')
    DOWN_KEYS = ('s', 'S', 'Down')
    RIGHT_KEYS = ('d', 'D', 'Right')

    def __init__(self , grid):
        """將grid放入類別屬性內"""
        self.grid = grid
        self.size = grid.size
        """建立一個tkinter主視窗"""
        self.window = tk.Tk()
        """設定視窗標題"""
        self.window.title('2048')
        """設定遊戲背景"""
        self.background = tk.Frame(self.window, bg=self.BACKGROUND_COLOR)
        """建立空串列，用來儲存格子Label"""
        self.cell_labels = []
        
        """初始化文字"""
        """用二維巢狀迴圈建立二維串列"""
        for i in range(self.size):
            #建立一個儲存"列"的串列
            row_labels = []
            for j in range(self.size):
                """背景顏色為EMPTY_CELL_COLOR"""
                """font為剛剛設置的FONT"""
                label = tk.Label(self.background, text='',
                                 bg=self.EMPTY_CELL_COLOR,
                                 font=self.FONT,
                                 width=4, height=2)
                """設定label位置"""
                label.grid(row=i, column=j, padx=10, pady=10)
                """將新增好的Label放入row_labels內"""
                row_labels.append(label)
                """將新增好的row_labels放入cell_labels內"""
            self.cell_labels.append(row_labels)
        self.background.grid()

    """把格子和字上色"""
    def paint(self):
        """用兩個迴圈掃過網格"""
        for i in range(self.size):
            for j in range(self.size):
                
                 #如果那個格子數字是0
                if self.grid.cells[i][j] == 0:
                    """設定該格子的文字為空，背景為MPTY_CELL_COLOR"""
                    self.cell_labels[i][j].configure(
                         text='',
                         bg=GamePanel.EMPTY_CELL_COLOR)
                    
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
                        text=cell_text,
                        bg=bg_color, fg=fg_color)
                    
            
"""控制整個遊戲流程"""
class Game:
    def __init__(self, panel):
        """將panel轉為Game的屬性"""
        self.panel = panel
        """將panel內的grid轉為Game的屬性"""
        self.grid = panel.grid
        self.start_cells_num = 2 #用來設定一開始隨機產生幾個數字2
        self.over = False
        self.won = False

    """遊戲停止(輸了或贏了)"""
    def is_game_terminated(self):
        
        """如果遊戲結束或勝利，那就回傳True，否則False"""
        return self.over or self.won
        
    """遊戲開始，控制整個遊戲流程
    1.隨機在網格中產生數字2
    2.將panel畫出來
    3.如果監聽到事件則進入到key_handler方法
    4.主視窗開始運行"""
    def start(self):
        self.add_start_cells()
        self.panel.paint()
        self.panel.window.bind('<Key>', self.key_handler)
        self.panel.window.mainloop()
        
    """開始遊戲後產生的格子"""
    def add_start_cells(self):
        for i in range(self.start_cells_num):
            """以for迴圈控制隨機產生幾次數字二
            進而呼叫grid裡面產隨機產生數字2的方法"""
            self.grid.random_cell()

    """判斷有沒有辦法移動(合併)"""
    def can_move(self):
        """如果網格中有空格子，或網格可以被合併則回傳True"""
        return self.grid.has_empty_cells() or self.grid.can_merge()

    """當按下鍵盤時所要做的事情"""
    def key_handler(self, event):
        """先判斷遊戲是否終止"""
        if self.is_game_terminated():
            return
        """每次點擊案件先清除網格的旗標(flags)"""
        self.grid.clear_flags()
        """設定變數儲存事件抓到的按鍵"""
        key_value = event.keysym
        
        
        #判斷按下的按鍵是哪個功能
        if key_value in GamePanel.UP_KEYS:
            self.up()
        elif key_value in GamePanel.LEFT_KEYS:
            self.left()
        elif key_value in GamePanel.DOWN_KEYS:
            self.down()
        elif key_value in GamePanel.RIGHT_KEYS:
            self.right()
            
        print(grid.score)
        
        """如果找到2048，呼叫you_win方法"""
        if self.grid.found_2048():
            self.you_win() messagebox.showinfo(title="you win",message="你贏了")
        
       
        
        """如果已經移動完了w，則產生一個隨機數字"""
        if self.grid.moved:
            self.grid.random_cell()

        """進行完按鍵動作後將panel現況畫出來"""
        self.panel.paint()
        
        """如果無法再移動"""
        if not self.can_move():
            self.over = True
            self.game_over()


    """遊戲勝利"""   
    def you_win(self):
        self.won = True
        print('You Win!')


    """遊戲失敗"""
    def game_over(self):
        print('Game over!')
        



    """往上移動的方法
    1.往上壓縮
    2.往上合併
    3.若有成功進行壓縮或合併，則grid.moved旗標設為True
    4.在次往上壓縮"""
    def up(self):
        self.grid.up_compress()
        self.grid.up_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.up_compress()
        
    """往左移動的方法
    1.往左壓縮
    2.往左合併
    3.若有成功進行壓縮或合併，則grid.moved旗標設為True
    4.在次往左壓縮"""
    def left(self):
        self.grid.left_compress()
        self.grid.left_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.left_compress()

    """往下移動的方法
    1.往下壓縮
    2.往下合併
    3.若有成功進行壓縮或合併，則grid.moved旗標設為True
    4.在次往下壓縮"""
    def down(self):
        self.grid.down_compress()
        self.grid.down_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.down_compress()

    """往右移動的方法
    1.往右壓縮
    2.往右合併
    3.若有成功進行壓縮或合併，則grid.moved旗標設為True
    4.在次往右壓縮"""
    def right(self):
        self.grid.right_compress()
        self.grid.right_merge()
        self.grid.moved = self.grid.compressed or self.grid.merged
        self.grid.right_compress()


size = 4
grid = Grid(size)
panel = GamePanel(grid)
game2048 = Game(panel)
game2048.start()


