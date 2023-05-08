def get_cheapest_fruit(data:str)->str:
    """
    This function returns the name of the cheapest fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the cheapest fruit
    """
    row=data.split('\n')[1:]
    price=[]
    name=[]
    for i in row:
        price.append(float(i.split(',')[1]))
    for i in row:
        name.append(i.split(',')[0])
    for i in price:
        min=price[0]
        
        if i<min:
            min=i
    

    return name[price.index(min)]
data=open('fruits.csv').read()
print(get_cheapest_fruit(data))
   
   