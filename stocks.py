from bs4 import BeautifulSoup
import requests

stockCode = 'myor'
quartal = 4
websiterUrl = requests.get(
    "https://www.indopremier.com/module/saham/include/fundamental.php?code="+stockCode+"&quarter="+str(quartal)).text
print("https://www.indopremier.com/module/saham/include/fundamental.php?code="+stockCode+"&quarter="+str(quartal))
soup = BeautifulSoup(websiterUrl, "html5lib")

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
bvpsNow = 0
lastPrice = 0
der = 0
roe = 0

perArr = []
pbvArr = []


while index < len(table):
    if table[index][0] == 'PER':
        print('===================== PER ========================')
        
        totalPer = 0
        for i, row in enumerate(table[index]):
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

        
        averagePer = totalPer/(len(table[index])-2)
        marginPer = ((averagePer - perNow)/averagePer) * 100

        print('PER saat ini :', round(perNow,2))
        print('PER rata rata :', round(averagePer,2))
        print('Margin PER :', round(marginPer,2), '%')
        if float(perNow) > averagePer:
            print('PER diatas rata rata')
        else:
            print('PER dibawah rata rata')

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
        for i, row in enumerate(table[index]):
            if quartal > 3:
                if i != 0 and i != 2:
                    roeStr = row.replace(',', '')
                    if i == 1:
                        roe = roeStr
            else:
                if i > 1:
                    roeStr = row.replace(',', '')
                    if i == 2:
                        roe = roeStr

    index += 1
print('')
print('===================== Info ======================')

print('Stock Code:', stockCode)
print('Harga Saat ini :', round(lastPrice, 2))
print('ROE :', roe)
statusDer = ''
if der > 1:
    statusDer = ' Hutang diatas rata rata'
else:
    statusDer = ' Hutang dibawah rata rata'

print('DER:', der, statusDer)

print('')
print('===================== PRICE AVERAGE ======================')

fairPriceByPER = epsNow * averagePer
print('Harga Wajar By PER Average :', round(fairPriceByPER, 2))

fairPriceByPBV = bvpsNow * averagePbv
print('Harga Wajar By PBV Average :', round(fairPriceByPBV, 2))
averagePrice = (fairPriceByPER + fairPriceByPBV)/2

print('Harga Wajar Average :', round(averagePrice, 2))

marginPrice = ((averagePrice - lastPrice)/averagePrice) * 100
print('Margin Of Safety Average :', round(marginPrice, 2), '%')

print('')
print('===================== PRICE RANGE ======================')

perArr.sort()
pbvArr.sort()

#Teori baca saham
fairPriceByPERTerkecil = epsNow * float(perArr[0])
fairPriceByPERTerbesar = epsNow * float(perArr[len(perArr)-1])

fairPriceByPERRange = (fairPriceByPERTerkecil + fairPriceByPERTerbesar) / 2
print('Harga Wajar By PER Range:', round(fairPriceByPERRange, 2))

#Teori baca saham
fairPriceByPBVTerkecil = bvpsNow * float(pbvArr[0])
fairPriceByPBVTerbesar = bvpsNow * float(pbvArr[len(pbvArr)-1])

fairPriceByPBVRange = (fairPriceByPBVTerkecil + fairPriceByPBVTerbesar) / 2
print('Harga Wajar By PBV Range:', round(fairPriceByPBVRange, 2))

averagePriceRange = (fairPriceByPERRange + fairPriceByPBVRange)/2

print('Harga Wajar Range :', round(averagePriceRange, 2))
marginPrice = ((averagePriceRange - lastPrice)/averagePriceRange) * 100
print('Margin Of Safety Range :', round(marginPrice, 2), '%')

print('')
print('===================== PRICE RANGE ======================')
print('Best Buy PER :', round(fairPriceByPERTerkecil, 2), ' PER terkecil 6 tahun terakhir')
print('Best Buy PBV :', round(fairPriceByPBVTerkecil, 2), ' PVB terkecil 6 tahun terakhir')

print('Best Sell PER :', round(fairPriceByPERTerbesar, 2),
      ' PER terbesar 6 tahun terakhir')
print('Best Sell PBV :', round(fairPriceByPBVTerbesar, 2),
      ' PVB terbesar 6 tahun terakhir')

print('')
print('===================== AVERAGE DOWN RANGE ======================')

##average down
count = 1
averageDownRange = averagePriceRange
while (count < 6):     
    averageDownRange = averageDownRange -(averageDownRange * 0.05) 
    print('Avareage Down ',count, ':', round(averageDownRange, 2))
    count = count + 1

print('')

print('===================== AVERAGE DOWN RATA2 ======================')

##average down
count = 1
averageDown = averagePrice
while (count < 6):     
    averageDown = averageDown -(averageDown * 0.05) 
    print('Avareage Down ',count, ':', round(averageDown, 2))
    count = count + 1

print('')

print('===================== AVERAGE UP RANGE ======================')

##average UP
averageUpRange = averagePriceRange
averageUpRange = averageUpRange + (averageUpRange * 0.03) 
print('Avareage Up ', ':', round(averageUpRange, 2))


print('')

print('===================== AVERAGE DOWN RATA2 ======================')
##average down
averageUp = averagePrice
averageUp = averageUp +(averageUp * 0.03) 
print('Avareage Up ', ':', round(averageUp, 2))

print('')





