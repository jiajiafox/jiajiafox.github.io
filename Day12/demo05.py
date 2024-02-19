class MyDemo(object):

    def __init__(self):
        #加入屬性
        self.age=1      #  不可變的值放在預設

    def print_info(self):
        print(f"剛出生的年紀為{self.age}歲")

c=MyDemo         # 沒有給回傳值就不一定要加"()"。
c.print_info()   # 呼叫