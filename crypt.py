import re

def crypt(message):
    """ en/decript messages with given code:
            {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
        
        examples of input/output:
            input = "th3s 3s 1 m2ss1g2."
            output = "this is a message."

            input = "another message here!"
            output = "1n4th2r m2ss1g2 h2r2!"
    """
    codes = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
    revert_codes = {y: x for x, y in codes.items()}
    codes = {**codes, **revert_codes}

    pattern = re.compile("|".join(codes.keys()))
    return pattern.sub(lambda m: codes[re.escape(m.group(0))], message)
