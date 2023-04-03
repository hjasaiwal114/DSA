names = ['himanshu' , 'jasaiwal' , 'shadi' , 'party']

countMap = {}
for name in names:
    if name not in countMap:
        countMap[name] = 1
    else:
        countMap[name] += 1