import pickle

class MemoAdmin:#主体程序类  
    def __init__(self):
        pass

    def add(self):#增
        thing=input('待办事项：')
        time=input('待办时间：')
        interval=input('待办事项耗时：')
        memo=Memo(thing,time,interval)
        pklMemo=self.load_pkl()
        pklMemo.update(memo.dic)
        self.write_pkl(pklMemo)
        
    def delete(self,id): #删
        pklMemo=self.load_pkl() 
        pklMemo.pop(id)
        self.write_pkl(pklMemo)

    def modify(self,id):#改
        pklMemo=self.load_pkl() 
        thing=input('待办事项：')
        time=input('待办时间：')
        interval=input('待办事项耗时（分钟）：')
        pklMemo[id]=[thing,time,interval]
        self.write_pkl(pklMemo)

    def query(self):#查
        memos=self.load_pkl()
        print(memos)

    def load_pkl(self):#获取最新字典数据，封装为方法
        with open('./db.pkl','rb') as f:
            pklMemos=pickle.loads(f.read()) 
            return pklMemos

    def write_pkl(self,memos):#数据写入，封装为方法
        with open('./db.pkl','wb') as f:
            f.write(pickle.dumps(memos))
    

class Memo:#备忘录类
    

    def __init__(self,thing,time,interval):
        admin=MemoAdmin()
        pklMemo=admin.load_pkl()
        maxid=max(int(k) for k in pklMemo.keys())
        self.__id=maxid+1
        self.thing=thing #待办事项
        self.time=time #待办时间
        self.interval=interval #待办事项耗时
        self.dic={str(self.__id):[self.thing,self.time,self.interval]} #新记录

    def getId(self): #获取id方法
        return str(self.__id)


if __name__=="__main__":#程序入口
    welcome='欢迎使用备忘录'.center(30,'-')
    print(welcome) 
    admin=MemoAdmin()
    
    while True: 
        oper=input('请选择操作类型：1.增；2.删；3.改；4.查 任意键退出...')
        if oper=='1':
            oper1=''
            while oper1!='q':
                admin.add()
                oper1=input('任意键继续添加，q退出')
        elif oper=='2':
            oper2=''
            while oper2!='q':
                try:
                    id=input('请输入要删除的记录id：')
                    admin.delete(id)
                    print('删除成功')
                    oper2=input('任意键继续删除，q退出')
                except:
                    print('没有该id数据，请重新输入！')
        elif oper=='3':
            oper3=''
            while oper3!='q':
                try:
                    id=input('请输入要修改的记录id：')
                    admin.modify(id)
                    print('修改成功')
                    oper3=input('任意键继续修改，q退出')
                except:
                    print('没有该id数据，请重新输入！')
        elif oper=='4':
            admin.query()
        else:
            break
    
