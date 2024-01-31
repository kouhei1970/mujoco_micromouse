import numpy as np

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
        '            <body pos="0.0035 0.0035 -0.0005">\n'
        '                <geom type="box" mass="0.01" size="0.0025 0.0025 0.0245" rgba="1 1 1 1"/>\n'
        '            </body>\n'
        '            <body pos="0.0035 -0.0035 -0.0005">\n'
        '                <geom type="box" mass="0.01" size="0.0025 0.0025 0.0245" rgba="1 1 1 1"/>\n'
        '            </body>\n'
        '            <body pos="-0.0035 0.0035 -0.0005">\n'
        '                <geom type="box" mass="0.01" size="0.0025 0.0025 0.0245" rgba="1 1 1 1"/>\n'
        '            </body>\n'
        '            <body pos="-0.0035 -0.0035 -0.0005">\n'
        '                <geom type="box" mass="0.01" size="0.0025 0.0025 0.0245" rgba="1 1 1 1"/>\n'
        '            </body>\n'
        '            <body pos="0 0 -0.0005">\n'
        '                <geom type="box" mass="0.01" size="0.002 0.002 0.0245" rgba="1 1 1 1"/>\n'
        '            </body>\n'
        '            <!--柱上赤蓋-->\n'
        '            <body pos="0.0035 0.0035 0.0245">\n'
        '                <geom type="box" mass="0.01" size="0.002375 0.002375 0.0005" rgba="1 0 0 1"/>\n'
        '            </body>\n'
        '            <body pos="0.0035 -0.0035 0.0245">\n'
        '                <geom type="box" mass="0.01" size="0.002375 0.002375 0.0005" rgba="1 0 0 1"/>\n'
        '            </body>\n'
        '            <body pos="-0.0035 0.0035 0.0245">\n'
        '                <geom type="box" mass="0.01" size="0.002375 0.002375 0.0005" rgba="1 0 0 1"/>\n'
        '            </body>\n'
        '            <body pos="-0.0035 -0.0035 0.0245">\n'
        '                <geom type="box" mass="0.01" size="0.002375 0.002375 0.0005" rgba="1 0 0 1"/>\n'
        '            </body>\n'
        '            <body pos="0 0 0.0245">\n'
        '                <geom type="box" mass="0.01" size="0.002 0.002 0.0005" rgba="1 0 0 1"/>\n'
        '            </body>\n'
        '        </body>')

#迷路の大きさ    
M = 16 #行
N = 16 #列

print_header(M, N)
for cy in range(M+1):
    for cx in range(N+1):
        index = cy * (N+1) + cx + 1
        print_colmun(index, cx, cy)
print_footer()

