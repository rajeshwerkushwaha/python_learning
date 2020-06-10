from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'janus-tier1_snc1',
     # bootstrap_servers=['localhost:9092'],
     bootstrap_servers=['kafka.dub1:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     # group_id='janus-tier1_snc1',
     # topic='janus-tier1_snc1',
     value_deserializer=lambda x: loads(x.decode('utf-8'))


for message in consumer:
    message = message.value
    # print('read {} from numtest kafka topic'.format(message))
    print(message)