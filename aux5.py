SLOVAR = {
    "glasnie": tuple("аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouyAEIOUY"),
    "soglasnie": tuple("бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"),
}

def f1(s):
    first_index = next(
        (i for i, char in enumerate(s) if char in SLOVAR["glasnie"]),
        None
    )
    last_index = next(
        (i for i, char in enumerate(reversed(s)) if char in SLOVAR["soglasnie"]),
        None
    )
    if first_index is None or last_index is None:
        return None
    last_index = len(s) - 1 - last_index
    return s[first_index + 1:last_index]  # между первой гласной и последней согласной

def f2(d):
    return {k: f1(v) for k, v in d.items() if f1(v) is not None}
