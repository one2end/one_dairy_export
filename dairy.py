import json,time,os
import xml.etree.ElementTree as ET

def split_json(addr,dir=True):
    '''split the text from one dairy'''
    if os.path.isfile(addr) == False or addr[-4:] !='json':
        print('not a json file')
        return
    my_dairy = json.loads(open(addr,encoding = 'utf8').read())
    all_text_dairy = json.loads(my_dairy['json']) 
    for txt in all_text_dairy:
        timestamp = txt['createTime']
        time_local = time.localtime(timestamp /1000)
        dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local) #2019-09-29 08:59:18
        content = txt['content']
        if dir == True:
            addr = '.\\'+dt[:4]+'\\'+dt[5:7]
            title ='\\'+dt[:10]+'.txt'
            if os.path.isdir(addr) == False:
                os.makedirs(addr)  
        else:
            addr = '.\\'
            title = dt[:10]+'.txt'
        with open(addr + title,'w',encoding = 'utf8') as f:
            f.write(content)
        print('output'+addr+title)

def change_enex(addr):
    '''fix title and create time in enex file for dairy'''
    if os.path.isfile(addr) == False or addr[-4:] !='enex':
        print('not a enex file')
        return
    tree = ET.parse(addr)
    root = tree.getroot()
    for i in range(len(root)):
        root[i][0].text = root[i][0].text.replace('.txt','')
        date = root[i][0].text.replace('/','').replace('-','')
        create_date = root[i][2].text[:8]
        tail = root[i][2].text[8:]
        if date != create_date:
            root[i][3].text = date+tail
    tree2 = ET.ElementTree(root)
    tree2.write('finash.enex',encoding = 'utf-8')
    print('change over')

if __name__ == '__main__':
    path = os.getcwd()
    print('''The script have been launched
     current file directory:{0}.
     find for dairy json and enex.....
    '''.format(path))
    file_list = []
    for file in os.listdir(path):
        if file.endswith('.enex'):
            file_list.append(file)
        elif file.endswith('.json'):
             file_list.append(file)
    if file_list != []:
        for i,v in enumerate(file_list):
            print('index:'+':'+str(i),'name'+':'+v)
        num = input('input index to execute script,split json to text and fix title and create time in enex'
        )
        addr = path+'\\'+file_list[int(num)]
        if addr.endswith('.enex'):
            change_enex(addr)
        elif addr.endswith('.json'):
            print(addr[-4:])
            dir = bool(input('spilt order with directory? True or False'))
            split_json(addr,dir)
    else:
        print('no thing find,please move script to the directory that have your dairy files')
        
    


