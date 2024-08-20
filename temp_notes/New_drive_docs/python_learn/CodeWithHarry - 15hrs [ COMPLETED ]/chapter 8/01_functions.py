def percent(marks):
    return (sum(marks)/400)*100


marks = [45, 78, 86, 77]
percentage1 = percent(marks)

marks2 = [75, 98, 88, 78]
percentage2 = percent(marks2)

print(percentage1, percentage2)