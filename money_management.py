def moneyManagement(fairPriceByPBV, totalMoney, totalStock, lastPrice):
    amount = totalMoney / totalStock
    print('Total Dana : ', round(amount, 2))
    print(' ')

    count = 1
    while (count < 4):
        print('Price ', count, ':', round(fairPriceByPBV, 2))
        if count == 1:
            firstAmount = amount * (0.2)
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

        fairPriceByPBV = fairPriceByPBV - (fairPriceByPBV * 0.10)
       
        count = count + 1

