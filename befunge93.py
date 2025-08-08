import sys
import random
import time

WIDTH = 80
HEIGHT = 25

program = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

lines = sys.stdin.read().splitlines()
for y, line in enumerate(lines[:HEIGHT]):
    for x, ch in enumerate(line[:WIDTH]):
        program[y][x] = ch

x, y = 0, 0
dx, dy = 1, 0
stack = []
string_mode = False
output_buffer = ""

def pop():
    return stack.pop() if stack else 0

step = 0

while True:
    print(f"\n--- Step {step} ---")
    for yy in range(HEIGHT):
        row = ""
        for xx in range(WIDTH):
            if xx == x and yy == y:
                row += f"\033[7m{program[yy][xx]}\033[0m"
            else:
                row += program[yy][xx]
        print(row)
    print(f"IP:({x:2},{y:2}) Dir:({dx:+2},{dy:+2}) Cmd:{repr(program[y][x]):^2}")
    #print(f"Stack: {stack}")
    #if string_mode:
    #    print("(string mode)")
    time.sleep(0.05)

    cmd = program[y][x]
    if string_mode:
        if cmd == '"':
            string_mode = False
        else:
            stack.append(ord(cmd))
    else:
        if cmd == '>':
            dx, dy = 1, 0
        elif cmd == '<':
            dx, dy = -1, 0
        elif cmd == '^':
            dx, dy = 0, -1
        elif cmd == 'v':
            dx, dy = 0, 1
        elif cmd == '?':
            d = random.choices([(1,0), (-1,0), (0,1), (0,-1)], weights=[0.3, 0.2, 0.3, 0.2], k=1)[0]
            dx, dy = d
        elif cmd == '_':
            dx, dy = (1,0) if pop() == 0 else (-1,0)
        elif cmd == '|':
            dx, dy = (0,1) if pop() == 0 else (0,-1)
        elif cmd == '"':
            string_mode = True
        elif cmd in '0123456789':
            stack.append(int(cmd))
        elif cmd == '+':
            stack.append(pop() + pop())
        elif cmd == '-':
            a, b = pop(), pop()
            stack.append(b - a)
        elif cmd == '*':
            stack.append(pop() * pop())
        elif cmd == '/':
            a, b = pop(), pop()
            stack.append(0 if a == 0 else b // a)
        elif cmd == '%':
            a, b = pop(), pop()
            stack.append(0 if a == 0 else b % a)
        elif cmd == '!':
            stack.append(0 if pop() else 1)
        elif cmd == '`':
            a, b = pop(), pop()
            stack.append(1 if b > a else 0)
        elif cmd == ':':
            stack.append(stack[-1] if stack else 0)
        elif cmd == '\\':
            a = pop()
            b = pop()
            stack.append(a)
            stack.append(b)
        elif cmd == '$':
            pop()
        elif cmd == '.':
            print(f"Output(int): {pop()}")
        elif cmd == ',':
            output_buffer += chr(pop())
        elif cmd == '#':
            x = (x + dx) % WIDTH
            y = (y + dy) % HEIGHT
        elif cmd == 'g':
            a = pop()
            b = pop()
            stack.append(ord(program[b % HEIGHT][a % WIDTH]))
        elif cmd == 'p':
            a = pop()
            b = pop()
            v = pop()
            program[b % HEIGHT][a % WIDTH] = chr(v % 256)
        elif cmd == '&':
            val = 0
            try:
                val = int(input("Input(int): "))
            except:
                pass
            stack.append(val)
        elif cmd == '~':
            s = input("Input(char): ")
            stack.append(ord(s[0]) if s else 0)
        elif cmd == '@':
            print("Final Output:", output_buffer)
            #print("End of Program")
            break

    x = (x + dx) % WIDTH
    y = (y + dy) % HEIGHT
    step += 1
