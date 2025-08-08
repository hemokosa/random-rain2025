import random

WIDTH = 80
HEIGHT = 25

# 1行目：固定
header = 'v                                    vvvvvvvv' + ' ' * (WIDTH - 45)
lines = [header]

# 2～22行目：ランダムに ? を配置
for _ in range(1, 22):
    row = [' '] * WIDTH
    q_positions = random.sample(range(WIDTH), 2)
    for pos in q_positions:
        row[pos] = '?'
    lines.append(''.join(row))

# 23〜25行目：固定文字列
footer_23 = '                                     >>>>>>>>v' + ' ' * (WIDTH - 46)
footer_24 = 'vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"Rain."<vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv'
footer_25 = '????????????????????????????????????<>,#$:_@ >??????????????????????????????????'
lines.append(footer_23)
lines.append(footer_24)
lines.append(footer_25)

# ファイル保存
with open('straight_rain.bf', 'w') as f:
    for line in lines:
        f.write(line + '\n')

print("straight_rain.bf generated.")
