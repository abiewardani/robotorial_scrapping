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
        print('Total asset sd kuartal ' + str(quartal) + ' tahun ini adalah '+assetNowRaw +'. '
              'Asset Meningkat Sebesar ' +
              str(round(marginAsset, 2))+' persen, yaitu  ' +
              "{:,}".format(assetNow - assetLastQuartal))
    else:   
        print('Total asset sd kuartal ' + str(quartal) + ' tahun ini adalah '+assetNowRaw + '. '
              'Asset Menurun Sebesar ' +
              str(round(marginAsset, 2))+' persen, yaitu  ' +
              "{:,}".format(assetNow - assetLastQuartal))
  

def cleansingValue(valueAccount):
    rest = 0

    if 'T' in valueAccount:
        val = valueAccount.replace('T', '')
        rest = float(val) * 1000000000000
    
    if 'B' in valueAccount:
        val = valueAccount.replace('B', '')
        rest = float(val) * 1000000000
    
    if 'M' in valueAccount:
        val = valueAccount.replace('M', '')
        rest = float(val) * 1000000

   
    return rest
