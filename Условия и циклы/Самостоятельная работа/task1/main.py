src = not False and True or False and not True
#src = True or False and not True
# TODO расписать упрощение выражения

result = True and True or False and False
result = True or False
result = True# TODO подставить результат выражения

print(src == result)
