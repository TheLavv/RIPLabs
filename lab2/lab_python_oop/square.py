from lab2.lab_python_oop.rectangle import Rectangle
import pymorphy2


class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, side_param):
        self.side = side_param
        super().__init__(color_param, self.side, self.side)

    def __repr__(self):
        figure_color_gent = pymorphy2.MorphAnalyzer().parse(self.figure_color.colorproperty)[0].inflect({'gent'}).word
        return '{} {} цвета, стороной - {}, площадью - {}.'.format(
            Square.get_figure_type(),
            figure_color_gent,
            self.side,
            self.square()
        )
