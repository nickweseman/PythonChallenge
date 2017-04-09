import xmlrpc.client

url = 'http://www.pythonchallenge.com/pc/phonebook.php'
conn = xmlrpc.client.ServerProxy(url)

print(conn.system.listMethods())

print(conn.system.methodHelp('phone'))
print(conn.system.methodSignature('phone'))

print(conn.phone('blah'))
print(conn.phone('Bert'))
