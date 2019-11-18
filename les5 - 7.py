import json

dict_firm = {}
profit = []
average_profit = []
dict_profit = {}


with open("text_7.txt") as f:
    for el in f:
        el_split = el.split()
        firm_name = el_split[0]
        profit_firm = int(el_split[2]) - int(el_split[3])
        dict_firm[firm_name] = profit_firm
        average_profit.append(int(profit_firm))
        if profit_firm > 0:
            profit.append(int(profit_firm))
    dict_profit['avarage_profit'] = sum(average_profit) / len(average_profit)
    total_list = [dict_firm, dict_profit]
    print(f'Средняя прибыль компаний: {sum(profit) / len(profit) :.2f} рублей.')
print (total_list)

with open("text_7.json", 'w') as f_1:
    json.dump(total_list, f_1)

