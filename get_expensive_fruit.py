def get_expensive_fruit(data:str)->str:
    """
    This function returns the name of the most expensive fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the most expensive fruit
    """
    # your code here
    row=data.split('\n')[1:]
    price=[]
    name=[]
    exp=0
    for i in row:
        price.append(float(i.split(',')[1]))
    for i in row:
        name.append(i.split(',')[0])
    for i in price:
        
        if i>exp:
            exp=i
   
    

    return name[price.index(exp)]
data=open('fruits.csv').read()
print(get_expensive_fruit(data))

    


