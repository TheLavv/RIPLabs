from lab2.lab_python_oop.figure import Figure
from lab2.lab_python_oop.color import FigureColor
import pymorphy2


class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, width_param, height_param):
        self.width = width_param
        self.height = height_param
        self.figure_color = FigureColor()
        self.figure_color.colorproperty = color_param

    def square(self):
        return self.width * self.height

    def __repr__(self):
        figure_color_gent = pymorphy2.MorphAnalyzer().parse(self.figure_color.colorproperty)[0].inflect({'gent'}).word
        return '{} {} цвета, шириной = {}, высотой = {} и площадью = {}.'.format(
            Rectangle.get_figure_type(),
            figure_color_gent,
            self.width,
            self.height,
            self.square()
        )