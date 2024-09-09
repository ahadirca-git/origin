import time
from datetime import datetime
from clickhouse_driver import Client
timestamp = time.time()
counts = int(input("Insert Row count: "))
client = Client(host='127.0.0.1', port='9000', database='irp', user='default', password='')
id_report = int(input("Insert Report ID 1|2|3|4: "))
id_data = int(input("Insert ID DATA 14|16|116|114: "))
for i in range (1,counts):
    time_past_previous_5_min = 300*i
    ts= datetime.fromtimestamp(timestamp - time_past_previous_5_min - timestamp % 300)
    ret_show = client.execute("insert into irp.report_data_5m (ts, id_report, id_data, data_int ) values ('%s', %s, %s, 1234);" %(ts,id_report, id_data))

# copy script on eval, use commands on eval:
# apt install python3-pip
# pip install clickhouse_driver