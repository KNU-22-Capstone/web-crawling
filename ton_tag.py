

def tagging(hsv):
    h, s, v = hsv

    if s < 11 or v < 11: # 무채색
        result = dark(v)
    else:                # 유채색
        result = [color(h), level(s), level(v)]
    return result

def dark(v):    # 무채색
    if 0 <= v <= 10:
        return ('BK', 0, 0)
    elif 11 <= v <= 43:
        return ('BK', 0, 1)
    elif 43 <= v <= 75:
        return ('BK', 0, 2)
    elif 76 <= v <= 100:
        return ('BK', 0, 3)

def color(h):
    if 345 <= h or h <= 15:
        return 'R'
    elif 16 <= h <= 45:
        return 'O'
    elif 46 <= h <= 75:
        return 'Y'
    elif 76 <= h <= 105:
        return 'GA'
    elif 106 <= h <= 135:
        return 'GB'
    elif 136 <= h <= 165:
        return 'GC'
    elif 166 <= h <= 195:
        return 'BA'
    elif 196 <= h <= 225:
        return 'BB'
    elif 226 <= h <= 255:
        return 'BC'
    elif 256 <= h <= 285:
        return 'PA'
    elif 286 <= h <= 315:
        return 'PB'
    elif 316 <= h <= 344:
        return 'PC'

def level(sv):
    if 11 <= sv <= 43:
        return 0
    elif 44 <= sv <= 75:
        return 1
    elif 76 <= sv <= 100:
        return 2

if __name__ == '__main__':
    pass