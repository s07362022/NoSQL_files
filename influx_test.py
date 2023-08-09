from operator import imod
from influxdb import InfluxDBClient
import time
client = InfluxDBClient('localhost', 8086, '', '', 'smoke_ids01') 

level_value = [0,1,2,3,4,5]


#DB########################################
def sql(level_value):
    data = [
        {
            "measurement": "smoke_level",
            "tags": {
                "topic": "Sensor/level"
            },
            "fields": {
                "Level": level_value[-1]
            }
        }
    ]
    data2 = [
        {
            "measurement": "smoke_level",
            "tags": {
                "topic": "Sensor/data"
            },
            "fields": {
                "value": level_value[1]
            }
        }
    ]
    client.write_points(data)
############db############
#for i in range(10):
    #level_value.append(0)
for i in range(10):    
    sql(level_value)
    #time.sleep(2)

result = client.query('select Level from smoke_level') 
print(list(result.get_points()))
