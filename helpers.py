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

alphabet_encode = {
    'A': '01000001',
    'B': '01000010',
    'C': '01000011',
    'D': '01000100',
    'E': '01000101',
    'F': '01000110',
    'G': '01000111',
    'H': '01001000',
    'I': '01001001',
    'J': '01001010',
    'K': '01001011',
    'L': '01001100',
    'M': '01001101',
    'N': '01001110',
    'O': '01001111',
    'P': '01010000',
    'Q': '01010001',
    'R': '01010010',
    'S': '01010011',
    'T': '01010100',
    'U': '01010101',
    'V': '01010110',
    'W': '01010111',
    'X': '01011000',
    'Y': '01011001',
    'Z': '01011010',

    'a': '01100001',
    'b': '01100010',
    'c': '01100011',
    'd': '01100100',
    'e': '01100101',
    'f': '01100110',
    'g': '01100111',
    'h': '01101000',
    'i': '01101001',
    'j': '01101010',
    'k': '01101011',
    'l': '01101100',
    'm': '01101101',
    'n': '01101110',
    'o': '01101111',
    'p': '01110000',
    'q': '01110001',
    'r': '01110010',
    's': '01110011',
    't': '01110100',
    'u': '01110101',
    'v': '01110110',
    'w': '01110111',
    'x': '01111000',
    'y': '01111001',
    'z': '01111010',

    ' ': '00100000',
    '!': '00100001',
    '"': '00100010',
    '#': '00100011',
    '$': '00100100',
    '%': '00100101',
    '&': '00100110',
    "'": '00100111',
    '(': '00101000',
    ')': '00101001',
    '*': '00101010',
    '+': '00101011',
    ',': '00101100',
    '-': '00101101',
    '.': '00101110',
    '/': '00101111',
    '0': '00110000',
    '1': '00110001',
    '2': '00110010',
    '3': '00110011',
    '4': '00110100',
    '5': '00110101',
    '6': '00110110',
    '7': '00110111',
    '8': '00111000',
    '9': '00111001',
    ':': '00111010',
    ';': '00111011',
    '<': '00111100',
    '=': '00111101',
    '>': '00111110',
    '?': '00111111',
    '@': '01000000',
    '[': '01011011',
    ']': '01011100',
    '^': '01011110',
    '_': '01011111',
    '`': '01100000',
    '{': '01111011',
    '}': '01111101',
    '|': '01111100',
    '~': '01111110'
}

alphabet_decode = swap(alphabet_encode)


def close_error():
    window.destroy()


def create_error():
    global window

    window = CTkToplevel()
    window.minsize(width=400, height=200)
    window.title('Erreur')
    window.iconbitmap('assets/nice-pencil-logo-transparent.ico')

    error = CTkLabel(window, text='Une erreur est survenue', text_font=('arial', 22), bg_color='#EA4242', padx=10, pady=10)
    error.pack(pady=20)

    close_error_button = CTkButton(window, text='Fermer', command=close_error)
    close_error_button.pack(pady=20)