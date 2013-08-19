#-*- coding: utf-8 -*-
from binascii import hexlify, unhexlify
import re
import json
import tempfile
def formatPortSettins(settings):
    assert type(settings) is dict
    try:
        settings["baund"] = int(settings.get("baund", 9600))
        settings["bytesize"] = int(settings.get("bytesize", 8))
        settings["stopbits"] = int(settings.get("stopbits", 1))
    except Exception, msg:
        return False, msg
    
    return True, "success"
        
def checkData(data, _type):
    if data == '':
        return False, u"数据不能为空"

    errch, msg = None, "success"
    if _type == "hex":
        data = ''.join(data.split())
        if len(data) % 2 != 0:
            errch, msg = True, u"HEX模式下，数据长度必须为偶数"
        else:
            for ch in data.upper():
                if not ('0' <= ch <= '9' or 'A' <= ch <= 'F'):
                    errch, msg = ch, u"数据中含有非法的HEX字符"
                    break
                    
    return not errch, msg

def filterData(data,regex):
    if data == '':
        return ''
    try:
        re_filter=re.compile(regex,re.DOTALL)
        if re_filter.search(data):
            return data
    except Exception, e:
        raise

def configSave(jsondata):
    with open('config.json','w+') as jsonFile:
        try:
            #configData=json.dumps([{"list":"1","2":"2"}],indent=4)
            #jsonFile.write(str(configData))
            #f = tempfile.NamedTemporaryFile(mode='w+')
            json.dump(jsondata,jsonFile,indent=4)
            #f.flush()
            #print open(f.name,"r").read()
        except Exception, e:
            raise
        finally:
            jsonFile.close()
        

def configRead():
    with open('config.json','a+') as jsonFile:
        data=jsonFile.read()
        try:
            configData=json.loads(data)
            print configData
            return configData
        except Exception, e:
            print 'Config file no found,create default'
            configSave({"list":"1","2":"2"})
        finally:
            jsonFile.close()


toVisualHex = lambda data: ' '.join([hexlify(c) for c in data]).upper()
toHex = lambda data: ''.join([unhexlify(data[i:i+2]) for i in xrange(0, len(data), 2)])

if __name__=="__main__":
    configRead()
    #configSave("1")
