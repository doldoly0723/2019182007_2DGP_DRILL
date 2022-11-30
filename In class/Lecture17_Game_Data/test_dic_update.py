data = {'name':'yuri', 'x':100, 'y':200}
data['name'] = 'tom'
data['x'] = 200
data['y'] = 100
print(data)
new_data = {'name':'jeny', 'x':300, 'y':400}
data.update(new_data)
print(data)
data.update({'name':'jhon'})
