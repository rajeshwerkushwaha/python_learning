import json
import time
import sys
# read line by line when file is big
#filepath = 'pizza_20191212_1'
path = '/Users/rkumar/Downloads/temp/'
filepath = ['logs_14012020/pizza_logstash.log-20200114','logs_14012020/pizza_logstash.log-20200114_2']
#filepath = '/Users/rkumar/Downloads/temp/pizza_logstash.log-20191212'
# chatid = sys.argv[1]
# eventdate = sys.argv[2]
# eventtype = sys.argv[3]

#print(type(chatid), type(eventdate), type(eventtype))

for f in filepath:
    print(path+f)
    with open(path+f) as fp:
        for cnt, line in enumerate(fp):
            jsonObj = json.loads(line)
            dt = time.strftime('%Y-%m-%d', time.localtime(int(jsonObj['data']['eventTime'])/1000))
            #print(chatid, eventdate, eventtype)
#            if jsonObj['data']['chatId']==chatid and jsonObj['data']['segment']==eventtype and dt==eventdate:
            if jsonObj['data']['chatId']=='882031715903048632' and jsonObj['data']['segment']=='boldchat_message_sent' and dt=='2020-01-14':
#                 print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(jsonObj['data']['eventTime'])/1000)), jsonObj['data']['titleId'], jsonObj['data']['eventTime'])
                print("=================================================")
                print(jsonObj)