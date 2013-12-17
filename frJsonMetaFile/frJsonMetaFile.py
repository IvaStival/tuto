import maya.cmds as cmds
import json


class MetaFile:
    ''' Save lasdasdas
    '''
    def saveData(self, name, objects_list):
        json_list = {}
        all_list=[]
         
        for obj in objects_list:
            data_dict={}
            for field in cmds.listAttr(obj, keyable=True, unlocked=True):
                #print field,
                value=cmds.getAttr(obj+'.'+field)
                #print value
                data_dict.setdefault(field,value)
             
             
            all_list.append(data_dict)
         
        json_list.setdefault(name,{"data_list":data_dict})
         
        auxFile = open('/Users/ivastival/Desktop/'+name+'.rp', 'w')
        auxFile.write(json.dumps(json_list))
        auxFile.close()



    def loadData(self, nameFile):
        auxFile = open('/Users/ivastival/Desktop/'+nameFile+'.rp','r')
        
        json_list = auxFile.readlines()
        auxFile.close()
        
        all_list=json.loads(json_list[0])
        
        data_list = all_list[nameFile]['data_list']
        
        print data_list
        return data_list
        
    
    def changeObject(self, data_list, obj):
        for field in data_list:
            cmds.setAttr(obj+'.'+field,data_list[field])
            print data_list[field]

