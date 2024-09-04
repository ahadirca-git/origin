import time
from datetime import datetime
timestamp = time.time()
counts =5000
for i in range (1,counts):
    time_past_previous_5_min = 300*i
    ts= datetime.fromtimestamp(timestamp - time_past_previous_5_min - timestamp % 300)
    print("insert into irp.report_data_5m (ts, id_report, id_data, data_int ) values ('%s', 2, 14, 1234);" %(ts))