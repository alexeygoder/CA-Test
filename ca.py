'''
CA Test

Alexey Goder
(408)306-2013
'''

cmd = ' '
inst = []
dep = {}

def list_cmd(l):
    global inst
    for x in inst:
        print x
        
def inst_with_dep(x,flag=True):

    if x in dep:
        for y in dep[x]:
            inst_with_dep(y,False)
            
    if x in inst:
        if flag: print x,' is already installed.'
    else: 
        inst.append(x)
        print 'Installing ',x

        
def install_cmd(l):
    for x in l:
        inst_with_dep(x)

            
def inst_dep(x):
    if x in dep:
        for y in dep[x]:
            if y not in inst:
                inst.append(y)
                print 'Installing ',y
                
                
def add_depend(l):
    global dep
    dep[l[0]] = l[1:]
    
def check_depend(x):
    global dep
    for y in dep:
        if x in dep[y]:
            return True
    return False

def remove_cmd(l):
    for x in l:
        if check_depend(x):
            print x, ' is still needed.'
        else:
            inst.remove(x)
            print 'Removing ',x
            

d = {'DEPEND':add_depend, 'INSTALL':install_cmd, 'REMOVE':remove_cmd, 'LIST':list_cmd }

while True:
    line = raw_input().replace('\n',' ').strip()
    print line
    #print dep
    if line == 'END':
        break

    cmd = line.split(' ')[0]
    l = []
    if len(line.split(' ')) > 1:
        l = line.split(' ')[1:]
    
    d[cmd](l)
