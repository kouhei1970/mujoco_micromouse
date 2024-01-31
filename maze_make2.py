import numpy as np

#2017 Clasic mouse expart final maze
smap=(
    "+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+",#    0
    "|   |                                                           |",#15  1
    "+   +   +   +---+---+---+---+---+---+---+---+---+---+   +   +---+",#    2
    "|       |   |               |               |       |   |       |",#14  3
    "+   +---+   +   +---+---+   +   +---+---+   +   +   +---+---+   +",#    4
    "|           |   |       |       |       |       |           |   |",#13  5
    "+   +---+   +   +   +   +---+---+   +   +---+---+---+---+   +   +",#    6
    "|           |       |               |               |       |   |",#12  7
    "+   +---+---+---+---+---+---+---+---+---+---+---+   +   +---+   +",#    8
    "|   |       |       |           |       |   |       |       |   |",#11  9
    "+   +   +   +   +   +   +   +   +   +   +   +   +---+---+   +   +",#   10
    "|   |   |       |       |   |       |           |           |   |",#10 11
    "+   +   +---+---+---+---+---+---+---+---+---+---+---+   +---+   +",#   12
    "|   |       |           |               |       |           |   |",# 9 13
    "+   +---+   +   +   +---+   +   +---+   +   +   +---+   +---+   +",#   14
    "|   |       |   |       |   |       |       |               |   |",# 8 15
    "+   +   +---+   +---+   +   +   +   +---+---+---+---+   +---+   +",#   16
    "|   |   |       |       |   |       |   |                   |   |",# 7 17
    "+   +   +   +---+   +---+   +---+---+   +   +   +---+---+---+   +",#   18
    "|   |       |           |                   |               |   |",# 6 19
    "+   +---+---+   +---+---+---+---+---+---+---+---+---+---+   +   +",#   20
    "|   |           |       |   |       |   |           |       |   |",# 5 21
    "+   +   +---+---+   +   +   +   +   +   +   +   +---+   +---+   +",#   22
    "|   |       |       |           |           |   |   |       |   |",# 4 23
    "+   +---+   +   +---+---+   +---+---+   +---+   +   +---+   +   +",#   24
    "|   |       |       |   |   |       |   |       |           |   |",# 3 25
    "+   +   +---+---+   +   +---+   +   +---+   +---+   +---+---+   +",#   26
    "|   |   |           |           |           |   |   |           |",# 2 27
    "+   +   +   +---+---+   +---+---+---+---+---+   +   +   +   +   +",#   28
    "|       |   |   |   |                               |   |   |   |",# 1 29
    "+   +---+   +   +   +---+---+---+---+---+---+---+---+---+---+   +",#   30
    "|   |                                                           |",# 0 31
    "+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+"#    32
    #  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
)

def print_header(row, col):
    size_x = (col * 0.180+0.012)/2
    size_y = (row * 0.180+0.012)/2
    pos_x = size_x - 0.006
    pos_y = size_y - 0.006
    print('<mujoco model="maze">\n'
          '    <worldbody>\n'
          '        <!--ベース板-->')
    print('        <body name="base_plate" pos="{} {} 0.006">'.format(pos_x, pos_y))
    print('        <geom type="box" mass="0.1" size="{} {} 0.006" rgba="0.2 0.2 0.2 1" friction="0.0 0.0 0.0"/>'.format(size_x, size_y ) )
    print('        </body>')

def print_footer():
    print('    </worldbody>\n'
          '</mujoco>')

def print_colmun(index, cx, cy):
    print()
    print('        <!-- Column {}-->'.format(index))
    print('        <body pos="{} {} 0.037">'.format(cx*0.18,cy*0.18))
    print(
        '            <body pos="0 0 -0.0005">\n'
        '                <geom type="box" mass="0.01" size="0.006 0.006 0.0245" rgba="1 1 1 1"/>\n'
        '            </body>\n'
        '            <!--柱上赤蓋-->\n'
        '            <body pos="0 0 0.0245">\n'
        '                <geom type="box" mass="0.01" size="0.006 0.006 0.0005" rgba="1 0 0 1"/>\n'
        '            </body>\n'
        '        </body>')

def print_horizontal_wall(index, wx, wy):
    print()
    print('        <!-- Wall {}-->'.format(index))
    print('        <body pos="{} {} 0.037">'.format(wx,wy))
    print(
        '            <body pos="0 0 -0.0005">\n'
        '                <geom type="box" mass="0.01" size="0.084 0.006 0.0245" rgba="1 1 1 1"/>\n'
        '            </body>\n'
        '            <!--壁上赤蓋-->\n'
        '            <body pos="0 0 0.0245">\n'
        '                <geom type="box" mass="0.01" size="0.084 0.006 0.0005" rgba="1 0 0 1"/>\n'
        '            </body>\n'
        '        </body>')

def print_vertical_wall(index, wx, wy):
    print()
    print('        <!-- Wall {}-->'.format(index))
    print('        <body pos="{} {} 0.037">'.format(wx,wy))
    print(
        '            <body pos="0 0 -0.0005">\n'
        '                <geom type="box" mass="0.01" size="0.006 0.084 0.0245" rgba="1 1 1 1"/>\n'
        '            </body>\n'
        '            <!--壁上赤蓋-->\n'
        '            <body pos="0 0 0.0245">\n'
        '                <geom type="box" mass="0.01" size="0.006 0.084 0.0005" rgba="1 0 0 1"/>\n'
        '            </body>\n'
        '        </body>')


#迷路の大きさ    
M = 16 #行
N = 16 #列

print_header(M, N)
#Put Colmun
index = 1
for cy in range(M+1):
    for cx in range(N+1):
        print_colmun(index, cx, cy)
        index += 1
#Put Wall
index = 1
#Horizontal
for i in range(N+1):#南北方向
    for j in range(M):#//東西方向
        if smap[32-2*i][2+4*j]=='-':
            print_horizontal_wall(index, j * 0.18 + 0.09, i * 0.18)
            index += 1
#Vertical
for i in range(N):#南北方向
    for j in range(M+1):#//東西方向
        if smap[31-2*i][4*j]=='|':
            print_vertical_wall(index, j * 0.18, i * 0.18 + 0.09)
            index += 1

print_footer()