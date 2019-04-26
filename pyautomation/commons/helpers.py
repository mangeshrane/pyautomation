

def expand_escape_sequence(string):
    return bytes(string, "utf-8").decode("unicode_escape")