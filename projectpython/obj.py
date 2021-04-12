#program to demonstrate class and method
# class pythontraining(object):#new model class, classic class wit no object
#     def listen(self,name):
#         print("im an object and im listening"+str(name))
# # creating object or instance
# x=pythontraining()#constructor
# # invoke or execute
# x.listen(10)
# y=pythontraining()#constructor
# # invoke or execute
# y.listen(20)
#new model class, classic class wit no object
#==========classvariables,object variables and class/static method==========
# class pythontraining(object):
#     board='whiteboard' #class variables
#     def bookwriting(self,name):
#         print('im writing in my book:'+str(name))
#     def listening(self,name):
#         print('im listening perfectly :' + str(name))
#     def understanding(self,percentage):
#         print('im understood perfectly :' + str(percentage))
#     @classmethod
#     def boardreading(cls): #CLASS/STATIC METHOD
#         print('all read the board')
# x=pythontraining()
# x.pen='parker'
# x.book='rule'
# x.bookwriting(x.pen)
# y=pythontraining()
# y.understanding('90%:y')
# x.pen='reynolds'
# x.book='whitepage book'
# print(pythontraining.board)
# pythontraining.boardreading()
#=================== constructors in python =====================
# class training:
#     def __init__(self,a,b):
#         print('im constructor mtd')
#         self.pen=a
#         self.book=b
#     def display(self):
#         print('my pen is '+self.pen)
#         print('my book is ' + self.book)
# x=training('parker','white notebook')
# x.display()

# class grandparent:#======single inheritance=======
#     def __init__(self,h):
#         self.house=h
#     def displaygpproperties(self):
#         print('grandparent house is: '+self.house)
# class parent(grandparent):
#     def __init__(self,h,c):
#         self.house=h
#         self.car=c
#     def displaypproperties(self):
#         print('parent house is :'+self.house)
#         print('parent car is :'+self.car)
# sub1=parent('duplex','hondacity')
# sub1.displaypproperties()
# class grandparent:#multi inheritance copying superclass var's to sub calss=======
#     def __init__(self,h):
#         self.house=h
#     def displaygpproperties(self):
#         print('grandparent house is: '+self.house)
# class parent(grandparent):
#     def __init__(self,h,c):
#         self.car=c
#         super().__init__(h)
#     def displaypproperties(self):
#         print('parent house is :'+self.house)
#         print('parent car is :'+self.car)
# class child(parent):
#     def __init__(self,h,c,b):
#         self.bike=b
#         super().__init__(h,c)
#     def displaychildproperties(self):
#         print('child house is :'+self.house)
#         print('child car is :'+self.car)
#         print('child bike is :' + self.bike)
# sub1=child('duplex','hondacity','harley davidson')#constructor
# sub1.displaypproperties()
# sub1.displaychildproperties()
# sub1.displaygpproperties()
#=======program to demonstrate sets in python======
# s1={1,'a',5.6}
# print(s1)
# # s2={2,'f',7.6}
# # s1.add(5)
# # print(s1)
# # s1.update(s2)
# # print(s1)
# # s1.remove(1)
# s1.discard(14)
# print(s1)
#==============================
# s1={2,1,'a',5.6}
# s2={2,1,'f',7.6}
# print(s1 | s2)#union
# print(s1 & s2)#intersection
# print(s1-s2)#difference
# print(s1 ^ s2)#symmetric difference
