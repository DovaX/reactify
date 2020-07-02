import os

def npm_start():
    try:
        os.chdir(".//my-app")
    except:
        print("Already in right folder")
    os.system("npm start")
    os.chdir("..")
    
def npm_install():
    os.system("npm install")
    
    
def npx_create_react_app():
    os.system("npx create-react-app my-app")

        
############ DOGUI ##############        
import dogui.dogui_core as dg


#gui1=dg.GUI()

#btn1=dg.Button(gui1.window,"npm start",npm_start,1,1)
#btn2=dg.Button(gui1.window,"npx create react app",npx_create_react_app,1,2)
#btn2=dg.Button(gui1.window,"npm install",npm_install,1,3)
#gui1.build_gui()


########### Parsing ##############

def read_file(filename):
    with open(filename,"r") as file:
        rows=file.readlines()
    return(rows)
    
rows=read_file(".//my-app//src//App.js")


for i in range(len(rows)-1,-1,-1):    
    rows[i]=rows[i].strip()
    if rows[i]=="":
        
        rows.pop(i)
        
  

########### Objects ###############      

class Tag:
    def __init__(self,tag_name,class_name=None):
        self.tag_name=tag_name
        self.class_name=class_name
        self.tag_tree=[]
        
    def __str__(self):
        if self.class_name is not None:
            statement='<'+self.tag_name+' className="'+self.class_name+'">'
        else:
            statement="<"+self.tag_name+">"
        return(statement)
    
    def end(self):
        print("</"+self.tag_name+">")
        return("</"+self.tag_name+">")
    
    
    
class Div(Tag):
    def __init__(self,class_name=None):
        super().__init__("div")
    
    



class JSFunction:
    def __init__(self,function_name):
        self.statement="function "+function_name+"() {"
    
    def __str__(self):
        return(self.statement)
        
    def end(self):
        print("}")
        return("}")
    
    def export(self):
        print("export default App;")
        return("export default App;")
    
    
    
        
    
class JSReturn:
    def __init__(self):
        self.statement="return ("
        
    def __str__(self):
        return(self.statement)
    
    def end(self):
        print(");")
        return(");")

        
class Import:
    def __init__(self,what,from_where=None):
        if from_where is not None:
            self.statement="import "+what+" from "+from_where+";"
        else:
            self.statement="import "+what+";"
            
    def __str__(self):
        return(self.statement)
            





imports=[]
imports.append(Import("React","'react'"))
imports.append(Import("logo","'./logo.svg'"))
imports.append(Import("'./App.css'"))





for i,imp in enumerate(imports):
    print(imp)

func=JSFunction("App")
print(func)

ret=JSReturn()
print(ret)
    
div1=Div("Apppp")
print(div1)

header=Tag("header","App-header")
print(header)
img1=Tag("img","App-logo")
print(img1)
img1.end()
p=Tag("p")
print(p)
print("Edit")
p.end()

a=Tag("a","App-link")
print(a)
print("Learn React")

a.end()


header.end()



div1.end()
ret.end()    
func.end()
func.export()
