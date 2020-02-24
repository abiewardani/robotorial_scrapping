def assetCalculation(data, historyYear, quartal, index):
    assetNow = 0
    assetLastQuartal = 0
    assetNowRaw = 0
    assetLastQuartalRaw = 0
    for i, row in enumerate(data[index]):
        if quartal > 3:
            if i == 1:
                assetNowRaw = row
                assetNow = cleansingValue(row)
        else:
            if i == 2:
                assetNowRaw = row
                assetNow = cleansingValue(row)
           
        if i == 3:
            assetLastQuartalRaw = row
            assetLastQuartal = cleansingValue(row)
    
    marginAsset = ((assetNow - assetLastQuartal)/assetNow) * 100
    if assetNow > assetLastQuartal:
        print('Total asset sd kuartal ' + str(quartal) + ' tahun ini adalah '+assetNowRaw+'. Terjadi peningkatan asset sebesar ' +
              str(round(marginAsset, 2))+' persen daripada kuartal ' + str(quartal) + ' tahun kemarin sebesar ' + assetLastQuartalRaw)
    
   
    print('Margin Asset :', round(marginAsset, 2))


def cleansingValue(valueAccount):
    rest = 0
    if valueAccount.find('T'):
        val = valueAccount.replace('T', '')
        rest = float(val) * 1000000000000
    elif valueAccount.find('B'):
        val = valueAccount.replace('B', '')
        rest = float(val) * 1000000000

    return rest
