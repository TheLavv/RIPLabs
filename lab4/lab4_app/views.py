from django.shortcuts import render
from datetime import date
from enum import Enum

parrots = [
    {
        'name': 'Веерный',
        'id': 1,
        'url': '/parrot/1',
        'info': 'Свое название веерные попугаи получили из-за расположения перьев на затылочной части в форме опахала.',
        'image_src': 'img/fan.jpeg'
    },
    {
        'name': 'Розелла',
        'id': 2,
        'url': '/parrot/2',
        'info': 'Свое название веерные попугаи получили из-за расположения перьев на затылочной части в форме опахала.',
        'image_src': 'img/fan.jpeg'
    },
    {
        'name': 'Эклектус',
        'id': 3,
        'url': '/parrot/3',
        'info': 'Свое название веерные попугаи получили из-за расположения перьев на затылочной части в форме опахала.',
        'image_src': 'img/fan.jpeg'
    },
    {
        'name': 'Японские амадины',
        'id': 4,
        'url': '/parrot/4',
        'info': 'Свое название веерные попугаи получили из-за расположения перьев на затылочной части в форме опахала.',
        'image_src': 'img/fan.jpeg'
    },
    {
        'name': 'Ара',
        'id': 5,
        'url': '/parrot/5',
        'info': 'Свое название веерные попугаи получили из-за расположения перьев на затылочной части в форме опахала.',
        'image_src': 'img/fan.jpeg'
    },
    {
        'name': 'Кольчатый',
        'id': 6,
        'url': '/parrot/6',
        'info': 'Свое название веерные попугаи получили из-за расположения перьев на затылочной части в форме опахала.',
        'image_src': 'img/fan.jpeg'
    },
]


class ParrotNames(Enum):
    fan = 0
    rosella = 1
    eclectus = 2
    japan_finches = 3
    ara = 4
    annular = 5


def get_parrots(request):
    return render(request, 'main.html', {'data': {
        'current_date': date.today(),
        'parrots': parrots
    }})


def get_parrot_info(request, id):
    return render(request, 'parrot_info.html', parrots[id - 1])
