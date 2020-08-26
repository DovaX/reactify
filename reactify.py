import os


class JSProgram:
    def __init__(self):
        self.list_of_statements=[]
        
    def activate(self):
        global active_js_program
        active_js_program=self
        
    def generate_file(self,filename):
        with open(filename,"w") as file:
            for i,line in enumerate(self.list_of_statements):
                file.write(line+"\n")
        

app_js=JSProgram()
app_js.activate()


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
    def __init__(self,tag_name,class_name=None,attributes=None):
        global active_js_program
        self.active_js_program=active_js_program
        self.tag_name=tag_name
        self.class_name=class_name
        self.tag_tree=[]
        self.attributes=attributes #dict
        
        
        
        attribute_string=""
        if self.attributes is not None:
            attribute_string=" "
            for k,v in self.attributes.items():
                attribute_string+=k+'="'+v+'"'
                
        
        if self.class_name is not None:
            statement='<'+self.tag_name+' className="'+self.class_name+'"'+attribute_string+'>'
        else:
            statement="<"+self.tag_name+attribute_string+">"
        
        self.statement=statement
        
        active_js_program.list_of_statements.append(self.statement)
        
    
    def __str__(self):
        return(self.statement)
    
    def end(self):
        end_statement="</"+self.tag_name+">"
        active_js_program.list_of_statements.append(end_statement)
        return(end_statement)
    
    
    
class Div(Tag):
    def __init__(self,class_name=None,attributes=None):
        super().__init__("div")
    
    



class JSFunction:
    def __init__(self,function_name):
        global active_js_program
        self.active_js_program=active_js_program
        self.statement="function "+function_name+"() {"
        active_js_program.list_of_statements.append(self.statement)
    
    def __str__(self):
        return(self.statement)
        
    def end(self):
        end_statement="}"
        active_js_program.list_of_statements.append(end_statement)
        return(end_statement)
    
    def export(self):
        export_statement="export default App;"
        active_js_program.list_of_statements.append(export_statement)
        return(export_statement)
    
    
    
        
    
class JSReturn:
    def __init__(self):
        global active_js_program
        self.active_js_program=active_js_program
        self.statement="return ("
        active_js_program.list_of_statements.append(self.statement)
        
    def __str__(self):
        return(self.statement)
    
    def end(self):
        end_statement=");"
        active_js_program.list_of_statements.append(end_statement)
        return(end_statement)
        
class Import:
    def __init__(self,what,from_where=None):
        global active_js_program
        self.active_js_program=active_js_program
        if from_where is not None:
            self.statement="import "+what+" from "+from_where+";"
        else:
            self.statement="import "+what+";"
        active_js_program.list_of_statements.append(self.statement)
            
    def __str__(self):
        return(self.statement)
            


Import("React","'react'")
Import("logo","'./logo.svg'")
Import("'./App.css'")

func=JSFunction("App")

ret=JSReturn()
    
div1=Div("App")

header=Tag("header","App-header")

img1=Tag("img","App-logo",{"src":"{logo}",
                           "alt":"logo"                           
                           })
img1.end()
p=Tag("p")
p.end()

a=Tag("a","App-link",{"href":'https://reactjs.org',"target":'_blank','rel':'noopener noreferrer'})
a.end()

header.end()
div1.end()
ret.end()
func.end()
func.export()

print(app_js.list_of_statements)

app_js.generate_file("test.js")


print(app_js.list_of_statements)

#local_variables=locals()
#items=local_variables.items()
#for k,v in items:
#    if type(exec(k))==type(Tag):
#        print(k,v)



