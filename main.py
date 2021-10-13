from newList import new_list
#1. Total sales
new = new_list
total = 0
for i in range(len(new)):
  total = total + int(new[i][4])
print(f'1. Total sales of the store = ₹ {total}')

#2. Month wise Sales Totals
# January sales
sum = []
new_sum = 0
for i in range(len(new)):
    sum = new[i][0]
    for j in range(1,32):
      if sum == f'2019-01-{f"{j:02d}"}':
          sum = str(new[i][4])
          new_sum += int(sum)
          january = int(new_sum)
print(f'2.a Total sales in january = ₹ {january}')

# Fabruary sales
sum = []
new_sum = 0
for i in range(len(new)):
    sum = new[i][0]
    for j in range(1,29):
      if sum == f'2019-02-{f"{j:02d}"}':
          sum = str(new[i][4])
          new_sum += int(sum)
          fab = int(new_sum)
print(f'2.b Total sales in Fabruary = ₹ {fab}')

# March sales
sum = []
new_sum = 0
for i in range(len(new)):
    sum = new[i][0]
    for j in range(1,32):
      if sum == f'2019-03-{f"{j:02d}"}':
          sum = str(new[i][4])
          new_sum += int(sum)
          march = int(new_sum)
print(f'2.c Total sales in March = ₹ {march}')

# Total Item Quantity
sum = 0
for i in range(len(new)):
  total_item_quantity = sum + int(new[i][3])      
total_item_list = [['Almond Fudge'], ['Banana Split'], ['Butterscotch Double Scoop'], ['Butterscotch Single Scoop'], ['Cafe Caramel'], ['Cake Fudge'], ['Caramel Crunch Double Scoop'], ['Caramel Crunch Single Scoop'], ['Chocolate Europa Double Scoop'], ['Chocolate Europa Single Scoop'], ['Death by Chocolate'], ['Dew Drop Sundae'], ['Dry Fruit Double Scoop'], ['Dry Fruit Single Scoop'], ['Fig and Honey Double Scoop'], ['Fig and Honey Single Scoop'], ['Hot Chocolate Fudge'], ['Mint Fudge'], ['Pista Double Scoop'], ['Pista Single Scoop'], ['Rocky Road Double Scoop'], ['Rocky Road Single Scoop'], ['Trilogy'], ['Vanilla Double Scoop'], ['Vanilla Single Scoop']]

# bnew = []
# for a,b,c,d,e in new: 
#       bnew.append(b)

# def total_items(x):
#     x2=sorted(x)
#     List_Of_Repeated=[]
#     for i in x2:
#         if x2.count(i)>1:
#             List_Of_Repeated.append([i])
#             for c in range(x2.count(i)):
#                 for j in x2:
#                     if i==j and x2.count(i)>1:
#                         x2.remove(i)
#     List_Of_Repeated.sort()
#     return List_Of_Repeated

# List=bnew
# print(total_items(List),"\n") 

# 3.Most popular item (most quantity sold) in each month
sorted_new_list = sorted(new)
index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[0].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity1 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity1 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[1].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity2 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity2 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[2].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity3 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity3 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[3].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity4 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity4 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[4].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity5 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity5 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[5].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity6 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity6 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[6].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity7 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity7 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[7].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity8 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity8 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[8].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity9 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity9 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[9].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity10 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity10 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[10].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity11 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity11 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[11].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity12 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity12 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[12].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity13 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity13 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[13].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity14 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity14 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[14].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity15 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity15 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[15].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity16 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity16 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[16].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity17 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity17 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[17].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity18 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity18 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[18].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity19 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity19 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[19].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity20 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity20 += list_of_index[i]

index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[20].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity21 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity21 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[21].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity22 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity22 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[22].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity23 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity23 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[23].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity24 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity24 += list_of_index[i]

index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[24].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][3] for i in index]

item_quantity25 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity25 += list_of_index[i]

list_of_item_quantity = [item_quantity25,item_quantity24,item_quantity23,item_quantity22,item_quantity21,item_quantity20,item_quantity19,item_quantity18,item_quantity17,item_quantity16,item_quantity15,item_quantity14,item_quantity13,item_quantity12,item_quantity11,item_quantity9,item_quantity8,item_quantity7,item_quantity6,item_quantity5,item_quantity4,item_quantity3,item_quantity2,item_quantity1]

list_of_item_quantity.reverse()

max_quantity_of_an_item = max(list_of_item_quantity)
# print(max_quantity_of_an_item)
# Getting index of item(sold max quantity)
max_item_index = list_of_item_quantity.index(max_quantity_of_an_item)

most_popular_item = total_item_list[max_item_index +1]
print(f'3. Most popular item (most quantity sold) in each month = {most_popular_item[0]} and Qunatity sold = {max_quantity_of_an_item}')

# def most_revenue():
index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[0].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity1 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity1 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[1].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity2 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity2 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[2].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity3 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity3 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[3].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity4 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity4 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[4].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity5 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity5 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[5].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity6 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity6 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[6].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity7 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity7 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[7].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity8 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity8 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[8].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity9 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity9 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[9].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity10 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity10 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[10].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity11 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity11 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[11].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity12 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity12 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[12].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity13 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity13 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[13].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity14 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity14 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[14].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity15 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity15 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[15].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity16 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity16 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[16].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity17 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity17 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[17].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity18 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity18 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[18].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity19 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity19 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[19].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity20 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity20 += list_of_index[i]

index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[20].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity21 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity21 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[21].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity22 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity22 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[22].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity23 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity23 += list_of_index[i]


index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[23].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity24 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity24 += list_of_index[i]

index_of_item = []
i = 0
while (i < len(new)):
    if ( total_item_list[24].count(sorted_new_list[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [sorted_new_list[i][4] for i in index]

item_quantity25 = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity25 += list_of_index[i]
    
list_of_item_revenue = [item_quantity25,item_quantity24,item_quantity23,item_quantity22,item_quantity21,item_quantity20,item_quantity19,item_quantity18,item_quantity17,item_quantity16,item_quantity15,item_quantity14,item_quantity13,item_quantity12,item_quantity11,item_quantity9,item_quantity8,item_quantity7,item_quantity6,item_quantity5,item_quantity4,item_quantity3,item_quantity2,item_quantity1]
# print(list_of_item_revenue)

# max_revenue = maxr.max()
# print(max_revenue)

list_of_item_revenue.reverse()

max_revenue_of_an_item = max(list_of_item_revenue)
# print(max_quantity_of_an_item)
# Getting index of item(sold max quantity)
max_item_revenue_index = list_of_item_revenue.index(max_revenue_of_an_item)

most_popular_item_by_revenue = total_item_list[max_item_revenue_index +1]
print(f'4. Items generating most revenue in each month = {most_popular_item_by_revenue[0]} and Total Revenue = ₹ {max_revenue_of_an_item}')

#5.For the most popular item, find the min, max and average number of orders each month.

# January sales
# jan_date = []
# new_sum = 0
# count = 0
# for i in range(len(new)):
#     jan_date = new[i][0]
#     for j in range(1,32):
#       if jan_date == f'2019-03-{f"{j:02d}"}':
#           count+= 1
#           jan_date = str(new[i][4])
#           new_sum += int(jan_date)
#           january = int(new_sum)
# print(f'2.a Total sales in january = ₹ {january}and {count}')

index_of_item = []
i = 0
while (i < 4326):
    if ( total_item_list[16].count(new[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [new[i][3] for i in index]

item_quantity_in_jan = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity_in_jan += list_of_index[i]

index_of_item = []
i = 4326
while ( i < 8658):
    if ( total_item_list[16].count(new[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [new[i][3] for i in index]

item_quantity_in_fab = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity_in_fab += list_of_index[i]

index_of_item = []
i = 8658
while ( i < 13939):
    if ( total_item_list[16].count(new[i][1]) > 0):
        index_of_item.append(i)
    i += 1
index = index_of_item

list_of_index = [new[i][3] for i in index]

item_quantity_in_march = 0
for i in range(0, len(list_of_index)):
    list_of_index[i] = int(list_of_index[i])
    item_quantity_in_march += list_of_index[i]

min_max_avg = [item_quantity_in_jan, item_quantity_in_fab, item_quantity_in_march]
# print(min_max_avg)
print('5. For the most popular item, find the min, max and average number of orders each month')

minimum = min(min_max_avg)
print(f'5.a Mim of most popular item (most quantity sold) in each month = {minimum} in Fabruary')

maximum = max(min_max_avg)
print(f'5.b Mim of most popular item (most quantity sold) in each month = {maximum} in March')

avg = round((item_quantity_in_jan+ item_quantity_in_fab+ item_quantity_in_march)/2)
print(f'5.c Average of most popular item (most quantity sold) in each month = {avg}')
