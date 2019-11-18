plan = {}

with open("text_6.txt") as f:
    for subjects in f:
        subjects_split = subjects.split()
        subjects_name = subjects_split[0]
        all_hours = subjects_split[1:]
        plan[subjects_name] = 0
        for types in all_hours:
            try:
                plan[subjects_name] += int(types[:types.find("(")])
            except ValueError:
                pass
print(plan)

# Мозг поломал себе с этой задачей. Так и не разобрался самостоятельно.
# Когда ДЗ проверили - оказалось что очень рядом ходиил - бродил.




