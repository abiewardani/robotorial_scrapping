def perCalculation(data, historyYear, quartal, index):
    perArr = []
    totalPer = 0
    for i, row in enumerate(data[index]):
        if quartal > 3:
            if i != 0 and i != 2:
                perInt = row.replace(' x', '')
                if i == 1:
                    perNow = float(perInt)
                totalPer = totalPer + float(perInt)
                perArr.append(float(perInt))
              
        else:
            if i > 1:
                perInt = row.replace(' x', '')
                if i == 2:
                    perNow = float(perInt)
                totalPer = totalPer + float(perInt)
                perArr.append(float(perInt))

    averagePer = totalPer/(len(data[index])-2)
    marginPer = ((averagePer - perNow)/averagePer) * 100

    resultString = 'Dari data diatas PER average adalah ' + \
        str(round(averagePer, 2)) + \
        ' . Dapat kita simpulkan bahwa PER saat ini ' + str(round(perNow, 2))

  
    if float(perNow) > averagePer:
        resultString += ' diatas PER average'
    else:
        # score += 1
        # scoreBlueChip += 1
        resultString += ' dibawah PER average'
    
    resultString += ', dengan perbedaan margin sebesar ' + str(round(marginPer, 2))+ '%'
    print(resultString)

    return perArr, perNow, totalPer


def showHistoryTable(data, historyYear, quartal, index):
    print('<p> Data PER 7 tahun terakhir </p>')
    print('<table id="jurnalTable">')
    print('<tr>')
    for i, row in enumerate(historyYear):
        if i != 0 and i != 2:
            print('<td>'+row+'<td>')
    print('</tr>')
    print('<tr>')
    for i, row in enumerate(data[index]):
        if quartal > 3:
            if i != 0 and i != 2:
                perInt = row.replace(' x', '')
                print('<td>'+perInt+'<td>')
        else:
            if i > 1:
                perInt = row.replace(' x', '')
                print('<td>'+perInt+'<td>')

    print('</tr>')
    print('</table>')
    print('')
