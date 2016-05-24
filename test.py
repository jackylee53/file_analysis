
str = '|30CP230120140408871400|2500000\nseq'
print str.split('\n')[0]


cnt = 0
while True:
    #read records
    if cnt > 1000:
        #write records to db
        cnt = 0

    cnt = cnt + 1



import os

work_dir = '/Users/jacky'

new_dir = os.path.join(work_dir,'test')

os.mkdir(new_dir)

for i in range(0,10,1):
    os.mkdir(os.path.join(new_dir,str(i)))



import cPickle as pickle

d = dict( a = 1, b = 2, c = 3)

f = open('/Users/jacky/test/1/hello.txt','wb')

pickle.dump(d,f)

f.close()




