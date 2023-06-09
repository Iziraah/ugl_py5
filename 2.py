# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов, вида "10,25%". В результате получаем словарь
# с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка,
# умноженная на процент премии.


names = ['Иванов','Петров','Сидоров']
salary = [10000 , 20000 , 30000]
premium = ['10.25%','15.3%','21.5%']

# w = [float(x[:-1]) for x in premium] # делает список чисел !!! без %
# print(w)

# rezult = [x * float(y[:-1]) for x, y in zip(salary, premium)] # получает список итоговых зарплат * премию
# print(rezult)

result = dict(zip(names,(x + x * (float(y[:-1])/100) for x, y in zip(salary, premium))))
print(result)