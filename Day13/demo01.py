# python 有 單繼承、多繼承 
#此為單繼承
# from typing import overload
class XClass(object):
    #繼承(def，屬性)
    def getMethod(self):
        # 同名方法  調用，覆寫
        print("def")

class YClass(XClass):
    # 同名方法  覆寫
    # @overload      #註解父類別
    def getMethod(self):
        print("def2.0")

    # 同名方法  調用
    def getMethod01(self):
        self.getMethod01()    #調用離最近的，調不到才往外調用

y=YClass()      #建立子類別的實體
y.getMethod()   #呼叫子類別(def)
                
