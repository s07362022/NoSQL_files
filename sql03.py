from operator import imod
from traceback import print_tb
from influxdb import InfluxDBClient
import time
client = InfluxDBClient('192.168.13.22', 8086, '', '', 'smoke_ids01')
def get_sql():
    result = client.query('select Level from smoke_level') 
    insql_list=list(result.get_points())
    return insql_list[-1]

re=get_sql()
print(re)