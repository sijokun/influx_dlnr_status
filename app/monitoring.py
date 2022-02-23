from influxdb import InfluxDBClient
from settings import settings
import datetime


client = InfluxDBClient(host=settings.INFLUX_HOST, port=settings.INFLUX_PORT, database=settings.INFLUX_DB)


async def append_measurement(results: list):
    json_body = []
    for res in results:
        json_body.append({
            "measurement": "ping",
            "time": datetime.datetime.utcnow().isoformat(),
            "fields": {
                "ip": str(res.server.ip),
                "name": res.server.name,
                "result": res.result,
                "node": settings.NODE_NAME
            }
        })
    client.write_points(json_body)
