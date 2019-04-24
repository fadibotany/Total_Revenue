
def total_revenue(original_quantity, original_price, other_quantity, other_price):
    change_in_quantity = other_quantity - original_quantity
    
    total_quantity = float(change_in_quantity) / float(original_quantity) 
    change_in_price = other_price - original_price
   
    total_price = float(change_in_price)/float(original_price)
    
    
    total_ratio = abs(total_quantity / total_price)
    
    if(total_ratio < 1):
        print("")
        print("Demand curve is inelastic")
        print("The ratio was " + str(total_ratio))
    if(total_ratio > 1):
        print("")
        print("Demand curve is elastic")
        print("The ratio was " + str(total_ratio))
    if(total_ratio == 1):
        print("")
        print("Demand curve is unit elastic")
        print("The ratio was " + str(total_ratio))
        
    revenue_original= original_quantity * original_price    
    print("")
    print('The total revenue for the original price and quantity was ' + str(revenue_original))
    
    revenue_other = other_quantity * other_price
    print('The total revenue for the new price and quantity was ' + str(revenue_other))
    
    change_in_revenue = revenue_original - revenue_other
    print("")
    print("The change in revenue was " + str(change_in_revenue))
    
    if(change_in_revenue > 0.0000001):
        print("Therefore, more money was made with the ORIGINAL price than the new price")
    if(change_in_revenue < -0.0000001):
        print("Therefore, more money was made with the NEW price than the original price")