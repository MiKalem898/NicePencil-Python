from customtkinter import *
from pint import UnitRegistry

ureg = UnitRegistry()


def swap(json):
    ret = {}
    for key in json:
        ret[json[key]] = key

    return ret


codes = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '5', '6', '7', '8', '9']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

text_to_emoji_codes = {
    'a': '🅰',
    'b': '🅱',
    'c': '©',
    'd': 'Ď',
    'e': '€',
    'f': '₣',
    'g': 'Ɠ',
    'h': 'Ħ',
    'i': 'Ī',
    'j': 'ʖ',
    'k': 'Ҝ',
    'l': 'Ƚ',
    'm': 'Ⓜ',
    'n': 'Ñ',
    'o': '🅾',
    'p': 'ק',
    'q': 'Գ',
    'r': '®',
    's': '$',
    't': 'Ŧ',
    'u': 'µ',
    'v': 'Ɣ',
    'w': '￦',
    'x': '❌',
    'y': 'Ỵ',
    'z': '乙'
}

emoji_to_text_codes = swap(text_to_emoji_codes)

unities = {
    "distance": ['km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm'],
    "time": ['ns', 'μs', 'ms', 's', 'min'],
    "mass": ['ng', 'μg', 'mg', 'cg', 'dg', 'g', 'dag', 'hg', 'kg', 't'],
    "speed": ['m/s', 'km/s', 'km/min', 'km/h'],
    "passing-band": ['bit/s', 'Kb/s', 'Mb/s', 'Gb/s', 'Tb/s', 'B/s'],
}

unities_codes = {
    'Distances': {
        'km': ureg.kilometers,
        'hm': ureg.hectometers,
        'dam': ureg.decameters,
        'm': ureg.meter,
        'dm': ureg.decimeters,
        'cm': ureg.centimeters,
        'mm': ureg.millimeter,
    },
    'Durées': {
        'ns': ureg.nanoseconds,
        'μs': ureg.microseconds,
        'ms': ureg.milliseconds,
        's': ureg.seconds,
        'min': ureg.minutes,
    },
    'Masses': {
        'ng': ureg.nanograms,
        'μg': ureg.micrograms,
        'mg': ureg.milligrams,
        'cg': ureg.centigrams,
        'dg': ureg.decigrams,
        'g': ureg.grams,
        'dag': ureg.decagrams,
        'hg': ureg.hectograms,
        'kg': ureg.kilograms,
        't': ureg.tons,
    },
    "Bande Passante": {
        "bit": ureg.bit,
        "Kb": ureg.kilobit,
        "Mb": ureg.megabit,
        "Gb": ureg.gigabit,
        "Tb": ureg.terabit,
        "B": ureg.byte,
    }
}


def close_error():
    window.destroy()


def create_error():
    global window

    window = CTkToplevel()
    window.minsize(width=400, height=200)
    window.title('Erreur')
    window.iconbitmap('outils.ico')

    error = CTkLabel(window, text='Une erreur est survenue', text_font=('arial', 22), bg_color='#EA4242', padx=10, pady=10)
    error.pack(pady=20)

    close_error_button = CTkButton(window, text='Fermer', command=close_error)
    close_error_button.pack(pady=20)