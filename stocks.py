from bs4 import BeautifulSoup
from per import perCalculation, showHistoryTable
from asset import assetCalculation
from equity import equityCalculation
from calculation import accountCalculation
from money_management import moneyManagement
import requests

stockCode = 'sido'
quartal = 4
totalStock = 5
totalMoney = 10000000

websiterUrl = requests.get(
    "https://www.indopremier.com/module/saham/include/fundamental.php?code="+stockCode+"&quarter="+str(quartal)).text
print("https://www.indopremier.com/module/saham/include/fundamental.php?code="+stockCode+"&quarter="+str(quartal))
soup = BeautifulSoup(websiterUrl, "html.parser")

table = []

myTable = soup.find("table", {"class": "table-fundamental"})
headers = myTable.find('thead').findAll('tr')
header = []
for row in headers:
    thList = row.find_all('th', {"align": "right"})
    header.append('akun')
    for rowTh in thList:
        header.append(rowTh.text)
        
table.append(header)

datas = myTable.find('tbody').findAll("tr")
for row in datas:
    td_list = row.find_all("td")
    account=[]
    for rowTd in td_list:
        account.append(rowTd.text)
    if len(account) > 2:
        table.append(account)

print(" ")

#Define Account
per = []

index = 0
pbvNow = 0
epsNow = 0
perNow = 0
averagePer = 0
averagePbv = 0
averageRoe = 0
bvpsNow = 0
lastPrice = 0
der = 0
roe = 0

perArr = []
pbvArr = []
roeArr = []
score = 0
scoreBlueChip = 0

dateKuartal = []

print('Stock Code:', stockCode)
print('')

while index < len(table):
    if table[index][0] == 'akun':
        dateKuartal = table[index]
    if table[index][0] == 'Total Asset':
        print('===================== Balance Sheet ========================')
        assetCalculation(table, dateKuartal, quartal, index)
    if table[index][0] == 'Total Equity':
        equityCalculation(table, dateKuartal, quartal, index)
        print('')
    if table[index][0] == 'S.T.Borrowing':
        accountCalculation(table, dateKuartal, quartal, index, 'Hutang Jangka Pendek')
    if table[index][0] == 'L.T.Borrowing':
        accountCalculation(table, dateKuartal, quartal, index, 'Hutang Jangka Panjang')
    if table[index][0] == 'Revenue':
        print('===================== Income Statement ========================')
        accountCalculation(table, dateKuartal, quartal, index, 'Pendapatan')
    if table[index][0] == 'Operating Profit':
        accountCalculation(table, dateKuartal, quartal, index, 'Pendapatan Operasional')
    if table[index][0] == 'Net.Profit':
        accountCalculation(table, dateKuartal, quartal,
                           index, 'Net.Profit')
        print('')
    if table[index][0] == 'PER':
        print('===================== PER ========================')
        perArr, perNow, totalPer = perCalculation(table,dateKuartal,quartal, index)      
    if table[index][0] == 'PBV':
        print('')
        print('===================== PBV ========================')
        totalPbv = 0
        for i, row in enumerate(table[index]):
            if quartal > 3:
                if i != 0 and i != 2:
                    pbvInt = row.replace(' x', '')
                    if i == 1:
                        pbvNow = float(pbvInt)
                    pbvArr.append(float(pbvInt))
                    totalPbv = totalPbv + float(pbvInt)
            else: 
                if i > 1:
                    pbvInt = row.replace(' x', '')
                    if i == 2:
                        pbvNow = float(pbvInt)
                    pbvArr.append(float(pbvInt))
                    totalPbv = totalPbv + float(pbvInt)

        averagePbv = totalPbv/(len(table[index])-2)
        marginPbv = ((averagePbv - pbvNow)/averagePbv) * 100

        print('PBV saat ini :', round(pbvNow,2))
        print('PBV rata rata :', round(averagePbv,2))
        print('Margin PBV :', round(marginPbv,2), '%')
        if float(pbvNow) > averagePbv:
            print('PBV diatas rata rata')
        else:
            score +=1
            scoreBlueChip +=1
            print('PBV dibawah rata rata')

    if table[index][0] == 'EPS':
        for i, row in enumerate(table[index]):
            if quartal > 3:
                if i != 0 and i != 2:
                    epsInt = row.replace(' x', '')
                    epsInt = row.replace(',', '')
                    if i == 1:
                        epsNow = float(epsInt)
            else :
                if i > 1:
                    epsInt = row.replace(' x', '')
                    epsInt = row.replace(',', '')
                    if i == 2:
                        epsNow = float(epsInt)
            

    if table[index][0] == 'BVPS':
        for i, row in enumerate(table[index]):
            if quartal > 3:
                if i != 0 and i != 2:
                    bvpsInt = row.replace(',', '')
                    if i == 1:
                        bvpsNow = float(bvpsInt)
            else :
                if i > 1:
                    bvpsInt = row.replace(',', '')
                    if i == 2:
                        bvpsNow = float(bvpsInt)

    if table[index][0] == 'Last Price':
        for i, row in enumerate(table[index]):
            if quartal > 3:
                if i != 0 and i != 2:
                    lastPriceInt = row.replace(',', '')
                    if i == 1:
                        lastPrice = float(lastPriceInt)
            else:
                if i > 1:
                    lastPriceInt = row.replace(',', '')
                    if i == 2:
                        lastPrice = float(lastPriceInt)

    if table[index][0] == 'Debt/Equity':
        for i, row in enumerate(table[index]):
            if quartal > 3:
                if i != 0 and i != 2:
                    derInt = row.replace(',', '')
                    if i == 1:
                        der = float(derInt)
            else:
                if i > 1:
                    derInt = row.replace(',', '')
                    if i == 1:
                        der = float(derInt)
    
    if table[index][0] == 'ROE':
        totalRoe = 0
        for i, row in enumerate(table[index]):
            if quartal > 3:
                if i != 0 and i != 2:
                    roeStr = row.replace(',', '')
                    roeStr = row.replace('%', '')
                    if i == 1:
                        roe = roeStr
                    totalRoe = totalRoe + float(roeStr)
                    roeArr.append(float(roeStr))
            else:
                if i > 1:
                    roeStr = row.replace(',', '')
                    roeStr = row.replace('%', '')
                    if i == 2:
                        roe = roeStr

                    totalRoe = totalRoe + float(roeStr)
                    roeArr.append(float(roeStr))

            averageRoe = totalRoe/(len(table[index])-2)

    index += 1
print('')
print('===================== Info ======================')
print('Harga Saat ini :', round(lastPrice, 2))
print('ROE :', roe)
print('Average Roe:', round(averageRoe,2))

initialReturn = (epsNow/lastPrice)*100
if initialReturn > 7.5 :
    score +=1
    print('Initial Return:', round(initialReturn,2), "Diatas Rata rata")
else:
    print('Initial Return:', round(initialReturn,2), "Dibawah Rata")


statusDer = ''
if der > 1:
    statusDer = ' Hutang diatas rata rata'
else:
    statusDer = ' Hutang dibawah rata rata'


print('DER:', der, statusDer)

print('')
print('===================== PRICE AVERAGE ======================')

fairPriceByPBV = bvpsNow * averagePbv
print('Harga Wajar By PBV Average :', round(fairPriceByPBV, 2))

marginPrice = ((fairPriceByPBV - lastPrice)/fairPriceByPBV) * 100
print('Margin Of Safety Average :', round(marginPrice, 2), '%')

if float(marginPrice) > 15:
    score +=1

print('')
print('===================== PRICE RANGE ======================')

perArr.sort()
pbvArr.sort()

#Teori baca saham
fairPriceByPERTerkecil = epsNow * float(perArr[0])
fairPriceByPERTerbesar = epsNow * float(perArr[len(perArr)-1])

fairPriceByPERRange = (fairPriceByPERTerkecil + fairPriceByPERTerbesar) / 2

#Teori baca saham
fairPriceByPBVTerkecil = bvpsNow * float(pbvArr[0])
fairPriceByPBVTerbesar = bvpsNow * float(pbvArr[len(pbvArr)-1])

fairPriceByPBVRange = (fairPriceByPBVTerkecil + fairPriceByPBVTerbesar) / 2
print('Harga Wajar By PBV Range:', round(fairPriceByPBVRange, 2))

averagePriceRange = (fairPriceByPERRange + fairPriceByPBVRange)/2
marginPrice = ((averagePriceRange - lastPrice)/averagePriceRange) * 100

if float(marginPrice) > 15:
    score +=1

print('')
print('===================== BEST BUY ======================')
print('Best Buy PBV :', round(fairPriceByPBVTerkecil, 2), ' PVB terkecil 6 tahun terakhir')
print('Best Sell PBV :', round(fairPriceByPBVTerbesar, 2),' PVB terbesar 6 tahun terakhir')

print('')
print('===================== MONEY MANAGEMENT ======================')
if fairPriceByPBV > lastPrice:
    priceMoneyManagement = lastPrice
else:
    priceMoneyManagement = fairPriceByPBV

moneyManagement(priceMoneyManagement, totalMoney, totalStock, lastPrice)
print('')

print('===================== AVERAGE DOWN RATA2 ======================')

##average down
count = 1
averageDown = fairPriceByPBV
while (count < 6):     
    averageDown = averageDown -(averageDown * 0.10) 
    print('Avareage Down ',count, ':', round(averageDown, 2))
    count = count + 1

print('')
print('===================== Harga Wajar Krisis ======================')

##average down
count = 1
averageDown = fairPriceByPBV
averageDown = averageDown - (averageDown * 0.30)
while (count < 6):
    averageDown = averageDown - (averageDown * 0.10)
    print('Pembelian krisis ', count, ':', round(averageDown, 2))
    count = count + 1

print('')
print('===================== AVERAGE UP  ======================')

##average UP
averageUpRange = averagePriceRange
averageUpRange = averageUpRange + (averageUpRange * 0.03) 
print('Avareage Up ', ':', round(averageUpRange, 2))
print('')
print('===================== Price Earning Growth ======================')
##average down
peg = (float(pbvNow) * 10) / float(roe)
print('PEG ', ':', round(peg, 2))
print('')

