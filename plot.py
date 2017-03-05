import numpy as np
import math as math
import matplotlib as matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

matplotlib.interactive(True)

fig, ax = plt.subplots(figsize=(7, 7))

x0 = 200
y0 = 200

d1 = 185
d2 = 98

ax.set_ylim(-100, 500)
ax.set_xlim(-100, 500)
ax.plot([0, 400, 400, 0, 0], [0, 0, 400, 400, 0], "-", linestyle='dashed')
ax.plot([100, 300, 300, 100, 100], [100, 100, 300, 300, 100], "-", linestyle='dashed')

def cosine_law(a, b, c):
  val = (c**2 - b**2 - a**2) / (-2.0 * a * b)
  if val > 1:
    val = 1 
  elif val < -1:
    val = -1
  return math.acos(val)


def arctan(x, y, q2):
  return math.atan2(y, x) - math.atan2(d2 * math.sin(q2), d1 + (d2 * math.cos(q2)))


def plot_position(ax, a1, a2):
  p1 = a1
  p2 = p1 + a2

  x1 = x0 + math.cos(p1) * d1
  y1 = y0 + math.sin(p1) * d1

  x2 = x1 + math.cos(p2) * d2
  y2 = y1 + math.sin(p2) * d2

  ax.plot([x0, x1, x2], [y0, y1, y2], "o-", color='red')


def calculate_angles(x2, y2):
  x = x2 - x0
  y = y2 - y0
  d3 = (x**2 + y**2) ** 0.5

  beta = cosine_law(d1, d2, d3)
  q2 = math.pi - beta
  q1 = arctan(x, y, q2)

  return q1, q2


def on_move(event):
  x2 = event.xdata
  y2 = event.ydata
  q1, q2 = calculate_angles(x2, y2)

  if len(ax.lines) > 2:
    ax.lines.remove(ax.lines[-1])

  plot_position(ax, q1, q2)


fig = plt.gcf()
cid_up = fig.canvas.mpl_connect('motion_notify_event', on_move)

input('Press enter to exit')