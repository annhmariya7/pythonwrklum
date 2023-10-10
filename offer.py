item_price=45
offer_perc=5                                      #offer price in percentage

#selling price? 

discount_price=(item_price*offer_perc)/100        #offer price in digit
act_price=(item_price-discount_price)             #selling price

print(act_price)