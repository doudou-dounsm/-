date="2020-4-21"

class Databox():
    def __init__(self,value=""):
        self.value=value
        self.kw={}
    def set(self,value,key=None,back=True):
        if key==None:
            self.value=value  
        else:
            self.kw[key]=value
        if back:
            return {"key":key,"value":value}
    def get(self, key=None):
        if key==None:
            return self.value
        else:
            try:
                return self.kw[key]
            except:
                return ''
    def get_all(self):
        return {'value':self.value,"kw":self.kw}
    def delete(self,key=None,back=True):
        if key==None:
            sth=self.value
            self.value=''
        else:
            try:
                sth=self.kw[key]
            except:
                sth=''
            self.kw[key]='delete'
            del self.kw[key]
        if back:
            return {'key':key,"value":sth}

if __name__=="__main__":
    a=Databox(123)
    print(a.get())
    print(a.get("name"))
    print(a.set("Python","name"))
    print(a.set("cmd"))
    print(a.set("Chinese", "L", back=False))
    print(a.get_all())
    print(a.delete('L'))
    print(a.delete())
    print(a.delete("N"))
    print(a.get_all())
    print(a.get())
    print(a.get("L"))
