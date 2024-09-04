from clickhouse_driver import Client
client = Client(host='t1.dev.noction.com', port='9000', database='irp', user='', password='')
ret_show = client.execute('SHOW TABLES')
print(ret_show)
