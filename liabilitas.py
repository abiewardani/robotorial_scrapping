
from utils import cleansingValue


def liabilitasCalculation(data, historyYear, quartal, index, typeLiability):
    liabilitasNow = 0
    liabilitasLastQuartal = 0
    liabilitasNowRaw = 0
    liabilitasLastQuartalRaw = 0
    for i, row in enumerate(data[index]):
        if quartal > 3:
            if i == 1:
                liabilitasNowRaw = row
                liabilitasNow = cleansingValue(row)
        else:
            if i == 2:
                liabilitasNowRaw = row
                liabilitasNow = cleansingValue(row)

        if i == 3:
            liabilitasLastQuartalRaw = row
            liabilitasLastQuartal = cleansingValue(row)

    typeLiabilityStr = 'Hutang Jangka Pendek'
    if typeLiability == 'long':
        typeLiabilityStr = 'Hutang Jangka Panjang'


    marginAsset = ((liabilitasNow - liabilitasLastQuartal)/liabilitasNow) * 100
    if liabilitasNow > liabilitasLastQuartal:
        print('Total '+typeLiabilityStr+' sd kuartal ' + str(quartal) + ' tahun ini adalah '+liabilitasNowRaw+'. Terjadi peningkatan '+typeLiabilityStr+' sebesar ' +
              str(round(marginAsset, 2))+' persen daripada kuartal ' + str(quartal) + ' tahun kemarin sebesar ' + liabilitasLastQuartalRaw)
    else:
        print('Total '+typeLiabilityStr+' sd kuartal ' + str(quartal) + ' tahun ini adalah '+liabilitasNowRaw+'. Terjadi penurunan '+typeLiabilityStr+' sebesar ' +
              str(round(marginAsset, 2))+' persen daripada kuartal ' + str(quartal) + ' tahun kemarin sebesar ' + liabilitasLastQuartalRaw)
