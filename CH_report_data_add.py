from datetime import time
year =2024
month=1
for month in range (1, 12):
    month = month +1
    for date in range (1, 28):
        date=date+1
        for hour in range (0, 12):
            if hour==0:
                hour=00
            hour = hour +1
            for minute in range (0, 60):
                if minute % 5 == 0:
                    print("insert into irp.report_data_5m (ts, id_report, id_data, data_int ) values ('%s-%s-%s %s:%s:00' , 2, 14, 1234);" %( year, month, date, hour,minute))
                    minute+=5