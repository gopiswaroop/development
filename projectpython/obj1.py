# for i in range(10):
#     print(i)
# for i in range(0,10,3):
#   print(i)
# s='my name is gopi swaroop'
# print(max(s))
# s=[1,2]
# print(34 not in s)
# s={'country':'india','religion':'hindu'}
# del s['country']
# s['state']='Ap'
# print(s)
#========================================functions
# def sayhello(name='gopi'):
#     print('hello..'+str(name)+'welcome to functions concept')
# sayhello('swaroop')
#========================================functions lambda
# f= lambda a, b : a+b
# print(f(20,.5))
#========================================files
# f=open('pratice.txt','w')
# f.close()
# print(f)
#========================================files
# f=open('practice.txt','r')
# a=f.read(5)   #reads first 5 bites and stores in variable a
# f.close()
# print(a)
#========================================files
# f=open('practice.txt','r')
# a=f.readlines(5)   #reads all lines and stores in variable a
# f.close()
# print(a)
#========================================errors(syntax,logical) and exceptions
# x={'first':'python','second':'java'}
# y=[10,20]
# try:
#     print(x['first'])
#     print(y[11])
# except KeyError:
#     print('PR
#     INT KEY not exists')
# except IndexError:
#     print('index does not exist')
# print('hi')
# ==========================
#program to demonstrate threads
#stp-1:create thread
import threading
class thread1(threading.Thread):# step-1:create run mtd
    def run(self):
        for i in range(10):
            print(i)
#step-3 create object & call run mtd by using start method
t1=thread1()
t1.start()






