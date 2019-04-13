#!/usr/bin/env python
# encoding: utf-8
"""
@author: xiaohui
@contact: xiaohui1295371450@163.com
@file: die.py
@time: 2019-04-13 15:47
@desc: 使用Pygal模拟掷两个骰子
"""


from random import randint
import pygal


class Die:
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)


# 创建一个D6骰子
die1 = Die()
die2 = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

print(results)

# 分析结果
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Results"
# hist.y.title = "Frequency of Results"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
