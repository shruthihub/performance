from prometheus_client import start_http_server, Metric, REGISTRY
import json
import requests
import sys
import time

class JsonCollector(object):
  def __init__(self, endpoint):
    self._endpoint = endpoint
  def collect(self):
    # Fetch the JSON
    response = json.loads(requests.get(self._endpoint).content.decode('UTF-8'))

    # Metrics for CPU usage
    metric = Metric('cpu_usage',
        'CPU usage at a particular time', 'gauge')
    metric.add_sample('cpu_usage',
        value=response['cpu_usage_millicores'], labels={})
    yield metric

    # Counter for the memory allocatated
    metric = Metric('memory_allocated',
       'Memory allocation at a particular time', 'summary')
    metric.add_sample('memory_allocated',
       value=response['memory_allocated_millibytes'], labels={})
    yield metric

    # Metrics for timestamp
    metric = Metric('timestamp',
        'Timestamp of the event', 'summary')
    metric.add_sample('timestamp',
        value=response['accurate_timestamp'], labels={})
    yield metric

if __name__ == '__main__':
  # Usage: json_exporter.py port endpoint
  start_http_server(int(sys.argv[1]))
  REGISTRY.register(JsonCollector(sys.argv[2]))

  while True: time.sleep(1)

