# 列表的用法(append/remove/max/min/sorted)

# 实现购物清单
shopping_list = []
shopping_list.append("键盘")
shopping_list.append("键帽")
print(shopping_list)
print(len(shopping_list))
shopping_list.remove("键盘")
print(shopping_list)
print(len(shopping_list))

# 实现价格表
price_list=[50, 52, 450, 312, 1024]
max_pr = max(price_list)
min_pr = min(price_list)
sort_pr = sorted(price_list)
print(max_pr)
print(min_pr)
print(sort_pr)