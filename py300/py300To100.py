# 딕셔너리 : 품명, [가격, 재고]
inventory = {"메로나":[300,20],
             "비비빅":[400,3],
             "죠스바":[250,100]

}
print(inventory)

# 가격 인덱싱
inventory = {"메로나":[300,20],
             "비비빅":[400,3],
             "죠스바":[250,100]

}
print(inventory["메로나"][0])

#  메로나의 재고 
inventory = {"메로나":[300,20],
             "비비빅":[400,3],
             "죠스바":[250,100]

}
print(inventory["메로나"][1])

# 데이터 추가 
inventory = {"메로나":[300,20],
             "비비빅":[400,3],
             "죠스바":[250,100]

}

inventory["월드코"]=[500,7]
print(inventory)

#키 값 얻어오기
inventory = {"메로나":[300,20],
             "비비빅":[400,3],
             "죠스바":[250,100]

}
print(list(inventory.keys()))

# value만 얻기 
inventory = {"메로나":[300,20],
             "비비빅":[400,3],
             "죠스바":[250,100]

}
print(list(inventory.values()))

# 총합 
inventory = {"메로나":300,
             "비비빅":400,
             "죠스바":250

}
price = inventory.values()
print(sum(price))

# new product 추가 : update
inventory = {"메로나":300,
             "비비빅":400,
             "죠스바":250
}
new_product = {"팥빙수":2700, "아맛나":1000}
inventory.update(new_product)
print(inventory)

# zip과 dict : 쌍으로 묶어주기 zip
keys = ("apple","pear","peach")
vals = (300,200,400)
fruits = zip(keys,vals)
print(dict(fruits))

# zip과 dict : 쌍으로 묶어주기 zip
keys = ("apple","pear","peach")
vals = (300,200,400)
fruits = zip(keys,vals)
print(dict(fruits))

# zip과 tuple : 쌍으로 묶어주기 zip (tuple안에 tuple)
keys = ("apple","pear","peach")
vals = (300,200,400)
fruits = zip(keys,vals)
print(tuple(fruits))

# zip과 list : 쌍으로 묶어주기 zip 
keys = ("apple","pear","peach")
vals = (300,200,400)
fruits = zip(keys,vals)
print(list(fruits))

# 날짜와 종가 
date = ['09/05','09/06','09/08','09/09']
close_price = [10500,10300,10100,10800,11000]
print(dict(zip(date,close_price)))
