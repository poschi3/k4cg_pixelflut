class Util:

    def hex_to_rgb(self, value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv / 3], 16) for i in range(0, lv, lv / 3))