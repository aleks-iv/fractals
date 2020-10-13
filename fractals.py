import turtle
from math import sqrt


def rule_applying(axiom, rules, num_iter):
    frac_instr = axiom
    for _ in range(num_iter):
        for ch in rules:
            frac_instr = frac_instr.replace(ch, rules[ch])
    return frac_instr


def instr_applying(turt, instr, angle, forw_len):
    if instr == "F":
        turt.forward(forw_len)
    elif instr == "+":
        turt.left(angle)
    elif instr == "-":
        turt.right(angle)


axiom = 'F'
rules = {'F': 'F+F---FFF+++F-F'}
angle = 45
forw_len = 40

win = turtle.Screen()
win.setup(width=800, height=600)

curs = turtle.Turtle()
curs.hideturtle()

turtle.tracer(0, 0)

curs.color('white')
curs.goto(330, 30)
curs.color('black')

frac_instructions = rule_applying(axiom, rules, 2)

for instruction in frac_instructions:
    instr_applying(curs, instruction, angle, forw_len)


