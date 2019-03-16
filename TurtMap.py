import turtle as t
NAME = 0
POINTS = 1
POP = 2

state = ['colorado',[[-109,37],[-109,41],[-102,41],[-102,37]],5187582]
cities = []
cities.append(['denver',[-104.98,39.74],634265])
cities.append(['boulder',[-105.27,40.02],98889])
cities.append(['durango',[-107.8,37.28],170691])
map_width = 500
map_height = 300
minx = 180
maxx = -180
miny = 90
maxy = -90
for x,y in state[POINTS]:
    if x < minx : minx = x
    elif x > maxx : maxx = x
    if y < miny : miny = y
    elif y > maxy : maxy = y

dist_x = maxx- minx
dist_y = maxy - miny

x_radio = map_width/dist_x
y_radio = map_height/dist_y

def convert(point):
    lon = point[0]
    lat = point[1]
    x = map_width - ((maxx - lon)*x_radio)
    y = map_height - ((maxy - lat)*y_radio)
    x = x - (map_width/2)
    y = y - (map_height/2)
    return [x,y]

t.up()
first_pixel = None
for point in state[POINTS]:
    pixel = convert(point)
    print(pixel)
    if not first_pixel:
        first_pixel = pixel
    t.goto(pixel)
    t.down()

t.goto(first_pixel)
t.up()
t.goto([0,0])
t.write(state[NAME],align='center',font = ('arial',16,'bold'))

for city in cities:
    pixel = convert(city[POINTS])
    t.up()
    t.goto(pixel)
    #绘制城市位置
    t.dot(10)
    #标记城市
    t.write(city[NAME] + ", Pop.:" + str(city[POP]), align="left")
    t.up()

biggest_city = max(cities, key=lambda city:city[POP])
t.goto(0, -200)
t.write("The Biggest city is:" + biggest_city[NAME])

western_city = min(cities, key=lambda city:city[POINTS])
t.goto(0, -220)
t.write("The western - most city is:" + western_city[NAME])

t.pen(show=False)
t.done()