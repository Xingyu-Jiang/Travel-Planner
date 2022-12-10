routedata = open("routedata.txt", "r")
route = []
airlinedata = open("airlinedata.txt", "r", encoding='utf-8')
airlines = []

for i in range(6161):
    airlines.append(airlinedata.readline().split(','))
for i in range(67663):
    route.append(routedata.readline().split(','))

+for i in route:
    for y in airlines:
        if str(i[0]) == y[3].strip('"') or str(i[0]) == y[4].strip('"'):
            i[0] = y[6]

print(route)

