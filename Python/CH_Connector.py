from clickhouse_driver import Client
client = Client(host='t1.dev.noction.com', port='9000', database='irp', user='', password='')
ret_show = client.execute('SHOW databases')
print(ret_show)
