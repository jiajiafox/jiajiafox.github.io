class Other():
    def __init__(self,age):
        self.age=age
        #(任意參數(可變))

    def __str__(self):
        return "歡迎登入"
    
    def __del__(self):
        print("刪除這個class")

    def print_inf(self):
        print(f"{self.age}")

o=Other(18) # 需要給回傳值才加"()"
# del o       # 刪除這個class，後面的程式無法運行。
print(o)    
o.print_inf()
