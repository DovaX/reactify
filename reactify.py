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


class Div(Tag):
    def __init__(self,class_name):
        self.class_name=class_name
        
        
