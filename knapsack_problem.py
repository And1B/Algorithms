print("KNAPSACK PROBLEM:\n")

capacity = int(input("Enter capacity:\n"))

item_ratio = list()
items = [(25, 3), (24, 2), (15, 2), (40, 5)]
for item in items:
    item_ratio.append((item[0] / item[1], item[0], item[1]))

profit = 0
solution = list()
for i in range(len(items)):
    solution.append(0)

item_ratio.sort(reverse=True)

for i in range(len(item_ratio)):
    if capacity - item_ratio[i][-1] < 0:
        ratio = capacity / item_ratio[i][-1]
        profit += item_ratio[i][1] * ratio
        solution[items.index((item_ratio[i][1], item_ratio[i][-1]))] = ratio
        break
    capacity -= item_ratio[i][-1]
    profit += item_ratio[i][1]
    solution[items.index((item_ratio[i][1], item_ratio[i][-1]))] = 1
print(profit)
print(solution)
