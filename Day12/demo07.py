# 繼承(單、多、多層)

class A():
    def info(self):
        print("A info")

class B(A):     # B繼承A
    pass

class C(B):     # C繼承B
    # 同名方法，雖然繼承前面的def，但本身也有值，會優先取用。
    def info(self):
        print("C info")

x=C()
x.info()