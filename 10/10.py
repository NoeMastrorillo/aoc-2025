import sys
import numpy as np
from pyscipopt import Model
import itertools


def parse_light(s):
    return (np.array(list(s)[1:-1]) == '#').astype(int)

def parse_button(s, n):
    btn = np.zeros(n, dtype=int)
    btn[[int(x) for x in s[1:-1].split(',')]] = 1
    return btn

def parse_buttons(ls, n):
    return np.array([parse_button(x, n) for x in ls])

def parse_joltage(s):
    return np.array(s[1:-1].split(','), dtype=int)

input = open(sys.argv[1], 'r').read().strip()
lines = input.split('\n')

lights = []
buttons = []
joltage = []
for l in lines:
    splits = l.split()
    light = parse_light(splits[0])
    n = light.shape[0]
    lights.append(light)
    buttons.append(parse_buttons(splits[1:-1], n))
    joltage.append(parse_joltage(splits[-1]))


def lights_model(lights, buttons):
    n = lights.shape[0]
    k = buttons.shape[0]

    N = list(range(n))
    K = list(range(k))

    model = Model()

    x = {i: model.addVar(f"x{i}", vtype='B') for i in K}
    y = {j: model.addVar(f"y{j}", vtype='I') for j in N}

    model.setObjective(sum(x[i] for i in K), 'minimize')

    for j in N:
        model.addCons(sum(x[i]*buttons[i,j] for i in K) - 2*y[j] == lights[j])

    return model

def solve_lights_instance(lights, buttons):
    model = lights_model(lights, buttons)
    model.hideOutput(True)
    model.optimize()
    return model.getObjVal()

print(sum(solve_lights_instance(l,b) for l,b in zip(lights, buttons)))

    
def joltage_model(joltage, buttons):
    n = joltage.shape[0]
    k = buttons.shape[0]

    N = list(range(n))
    K = list(range(k))

    model = Model()

    x = {i: model.addVar(f"x{i}", vtype='I') for i in K}

    model.setObjective(sum(x[i] for i in K), 'minimize')

    for i in K:
        model.addCons(x[i] >= 0)

    for j in N:
        model.addCons(sum(x[i]*buttons[i,j] for i in K) == joltage[j])

    return model

def solve_joltage_instance(joltage, buttons):
    model = joltage_model(joltage, buttons)
    model.hideOutput(True)
    model.optimize()
    return model.getObjVal()

print(sum(solve_joltage_instance(j,b) for j,b in zip(joltage, buttons)))

