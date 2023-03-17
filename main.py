class field():
    def __init__(self):
        #import the libraries and then create self variables so that all necessary imports are initialized only once
        import matplotlib.pyplot as plt
        from matplotlib.patches import Rectangle as rect
        self.plt = plt
        self.rect = rect
        
    
    def union_pitch(self, pitch_color = 'white', line_color = 'Black', poles = False, linestyle = '-', line_alpha=1):
        
        #draw the rectangle that makes up the pitch and lies behind the field lines
        ax.add_patch(self.rect((0, 0), 100, 70, fc = pitch_color, zorder=0))

        #top & bottom lines
        plt.hlines(0, 0, 100, line_color), plt.hlines(70, 0, 100, line_color)

        #ends, half, 22s
        for x in range(5):
            c = [0, 22, 50, 78, 100]
            plt.vlines(c[x], 0, 70, line_color)

        #vertical and horizontal coordinates
        vertical_lines = [(2, 8), (12, 18), (68, 62), (58, 52), (22, 31), (39, 48)]
        horizontal_lines = [(47, 53), (37, 43), (57, 63), (19, 25), (75, 81), (5, 11), (95, 89)]
        vertical_y, horizontal_y = [5, 40, 60, 95], [5, 15, 55, 65]

        #lines
        for x in range(6):
            for y in range(4):
                plt.vlines(vertical_y[y], vertical_lines[x][0], vertical_lines[x][1], line_color, linestyle, line_alpha)
        for x in range(7):
            for y in range(4):
                plt.hlines(horizontal_y[y], horizontal_lines[x][0], horizontal_lines[x][1], line_color, linestyle, line_alpha)
        
        #if poles is true draw two thick rectangles at either end of the field
        if poles is True:
                plt.vlines(0, 30, 40, line_color, '-', alpha=1, linewidth=5)
                plt.vlines(100, 30, 40, line_color, '-', alpha=1, linewidth=5)
                
    def league_pitch(self, pitch_color = 'white', line_color = 'Black', poles = False, line_style = '-', line_alpha=1):
        
        #draw the rectangle that makes up the pitch and lies behind the field lines
        ax.add_patch(self.rect((0, 0), 100, 70, fc = pitch_color, zorder=0))

        #top & bottom lines
        plt.hlines(0, 0, 100, line_color), plt.hlines(70, 0, 100, line_color)
        
        #ends, half
        for x in range(3):
            c = [0, 50, 100]
            plt.vlines(c[x], 0, 70, line_color)

        #vertical and horizontal coordinates
        for x in range(9):
            plt.vlines(10*(x+1), 0, 70, color=line_color, linestyle=line_style, alpha=line_alpha)
            
        horizontal_y = [10, 20, 60, 50]
        
        for x in range(9):
            for i in range(4):
                plt.hlines(horizontal_y[i], 10*(x+1)-3, 10*(x+1)+3, color=line_color, linestyle=line_style, alpha=line_alpha)
        
        #if poles is true draw two thick rectangles at either end of the field
        if poles == True:
                plt.vlines(0, 30, 40, line_color, '-', alpha=1, linewidth=5)
                plt.vlines(100, 30, 40, line_color, '-', alpha=1, linewidth=5)
