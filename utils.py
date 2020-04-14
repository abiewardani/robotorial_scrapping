def cleansingValue(valueAccount):
    rest = 0
    if valueAccount.find('T'):
        val = valueAccount.replace('T', '')
        rest = float(val) * 1000000000000
    elif valueAccount.find('B'):
        val = valueAccount.replace('B', '')
        rest = float(val) * 1000000000

    return rest
