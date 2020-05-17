#Value Added Tax (VAT)

#VAT is not charged on supplies outside the scope of VAT (e.g. wages/dividends), nor on exempt supplies (e.g. land, insurance and post)

taxableSupplyValue = 500
vatInclusivePrice = False
vatExclusivePrice = True
zeroRated = False
reducedRated = True
standardRated = False
valueAddedTax = 0
#VAT is charged on value of taxable supplies (i.e. output VAT is chargeable and input VAT can be recovered)
#3 x categories of taxable supplies:
#Zero Rated (0% output VAT - but VAT can be recovered) - e.g. Food, books, drugs
#Reduced rate (5% output VAT) - e.g. fuel
#Standard rated (20% output VAT) - any taxable supply that isn't zero rated or reduced rate
vatRate = 0
if zeroRated == True:
    vatRate = 0
if reducedRated == True:
    vatRate = 0.05
if standardRated == True:
    vatRate = 0.2

if vatInclusivePrice == True:
    valueAddedTax = taxableSupplyValue * vatRate/(1 + vatRate)
elif vatExclusivePrice == True:
    valueAddedTax = taxableSupplyValue * vatRate
print(f"VAT charged is £{valueAddedTax}")