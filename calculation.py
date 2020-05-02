from asset import cleansingValue


def accountCalculation(data, historyYear, quartal, index, accountType):
    equityNow = 0
    equityLastQuartal = 0
    equityNowRaw = 0
    equityLastQuartalRaw = 0
    for i, row in enumerate(data[index]):
        if quartal > 3:
            if i == 1:
                equityNowRaw = row
                equityNow = cleansingValue(row)
        else:
            if i == 2:
                equityNowRaw = row
                equityNow = cleansingValue(row)

        if i == 3:
            equityLastQuartalRaw = row
            equityLastQuartal = cleansingValue(row)

    marginAsset = ((equityNow - equityLastQuartal)/equityNow) * 100
    if equityNow > equityLastQuartal:
        print('Total '+accountType+' sd kuartal ' + str(quartal) + ' tahun ini adalah '+equityNowRaw + '. ' +accountType+' Meningkat Sebesar ' +str(round(marginAsset, 2))+' persen, yaitu  ' +
              "{:,}".format(equityNow - equityLastQuartal))
    elif equityNow == equityLastQuartal:
        print('Total '+accountType+' sama dengan kuartal sebelumnya')
    else:
       print('Total '+accountType+' sd kuartal ' + str(quartal) + ' tahun ini adalah '+equityNowRaw + '. '
             + accountType+' Menurun Sebesar ' +
             str(round(marginAsset, 2))+' persen, yaitu  ' +
             "{:,}".format(equityNow - equityLastQuartal))

