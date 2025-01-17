
class mate:
    def __init__(self,name,number,chinese,math,english):
        self.name=name
        self.number=number
        self.chinese=chinese
        self.math=math
        self.english=english

    def set(self,subject,score):
        if subject=="语文":
            self.chinese=score
        elif subject=="数学":
            self.math=score
        else:
            self.english=score

    def fprint(self):
        print(f"{self.name}同学(学号{self.number})的成绩分别是，语文{self.chinese},数学{self.math}+英语+{self.english} ")

mate1=mate("张三","22009102114",99,100,100)
mate1.fprint()
mate1.set("语文",100)
mate1.fprint()

#类继承
class dzr(mate):
    def __init__(self,chinese,math,english):
        super().__init__(chinese,math,english)
        self.nam="小小张"
        self.numbe="22009202114"

    def sprint(self):
        print(f"{self.nam}同学(学号{self.numbe})的成绩分别是，语文{self.chinese},数学{self.math}+英语+{self.english} ")
