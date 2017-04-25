from model import schedule_optimize

weights=[10, 10, 10, 10, 14, 14, 5, 5, 6, 6, 6, 6, 5, 5, 5, 1, 1, 1, 1, 11, 11, 11, 9, 9, 13, 13, 13]
length=len(weights)
print(length)
schedule_optimize(weights)