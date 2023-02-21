import json
with open('Lab4\json\sample-data.json', 'r') as smp:
    s = json.load(smp)
    print('Interface Status')
    print("================================================================================")
    print('DN                                                 Description           Speed     MTU  ')
    print('-------------------------------------------------- --------------------  -------  ------')
    for i in s['imdata']:
        print("{:50} {:20}  {:7}  {:6}".format(i['l1PhysIf']['attributes']['dn'], i['l1PhysIf']['attributes']['descr'], i['l1PhysIf']['attributes']['speed'], i['l1PhysIf']['attributes']['mtu']))

