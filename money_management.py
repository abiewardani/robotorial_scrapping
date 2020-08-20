def moneyManagement(fairPriceByPBV, totalMoney, totalStock, lastPrice):
    amount = totalMoney / totalStock
    print('Total Dana : ', round(amount, 2))
    print(' ')

    totalBill = 0
    totalAllLot = 0

    count = 1
    while (count < 4):
        print('Price ', count, ':', round(fairPriceByPBV, 2))
        if count == 1:
            firstAmount = amount * (0.4)
            totalLot = (firstAmount/fairPriceByPBV)/100
        if count == 2:
            secondAmount = amount * (0.3)
            totalLot = (secondAmount/fairPriceByPBV)/100
        if count == 3:
            thirdAmount = amount * (0.3)
            totalLot = (thirdAmount/fairPriceByPBV)/100
        
        print('Jumlah Lot ' ':', round(totalLot, 0))
        if fairPriceByPBV >= lastPrice:
            print('====> (Signal Buy) <====')
        print('')

        totalAllLot = totalAllLot + totalLot
        totalBill = totalBill + (fairPriceByPBV * totalLot)

        fairPriceByPBV = fairPriceByPBV - (fairPriceByPBV * 0.08)
        count = count + 1
    
    averagePrice = totalBill/totalAllLot
    print('Average Price :', round(averagePrice, 2))

    cutLoss = averagePrice - (averagePrice * 0.30)
    print('Cut Loss :', round(cutLoss, 2))

    targetPrice = averagePrice + (averagePrice * 0.15)
    print('Target Price:', round(targetPrice, 2))
