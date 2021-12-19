from lab2.lab_python_oop.figure import Figure
from lab2.lab_python_oop.color import FigureColor
import math
import pymorphy2


class Circle(Figure):
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, r_param):
        self.r = r_param
        self.figure_color = FigureColor()
        self.figure_color.colorproperty = color_param

    def square(self):
        return math.pi * (self.r ** 2)

    def __repr__(self):
        figure_color_gent = pymorphy2.MorphAnalyzer().parse(self.figure_color.colorproperty)[0].inflect({'gent'}).word
        return '{} {} цвета, радиусом = {}, площадью = {}.'.format(
            Circle.get_figure_type(),
            figure_color_gent,
            self.r,
            self.square()
        )
