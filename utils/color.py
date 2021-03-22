#### A list that sest long non-sensical ANSI characters to short synonyms
COLORS = {
    "blu": "\u001b[34;1m",
    "r": "\u001b[31;1m",
    "g": "\u001b[32m",
    "y": "\u001b[33;1m",
    "b": "\u001b[30;1m",
    "m": "\u001b[35m",
    "c": "\u001b[36m",
    "w": "\u001b[37m",
    "y-bg": "\u001b[43m",
    "b-bg": "\u001b[40m",
    "c-bg": "\u001b[46;1m",
}


#### All the colors must be prefixed and suffixed with a "[[" "color" "]]"
def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text
