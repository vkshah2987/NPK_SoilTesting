from kivymd.app import MDApp
from kivy.lang import Builder
from sheet_to_app import NPK_DATA as nd
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.size = (300, 500)

data = nd()


def indx(a,b):
    a_list = a.split("/")
    b_list = b.split("/")
    print("printing b split", b_list)

    if (int(b_list[0]) == 28) and (b_list[1] == "02"):
        b_list[0] = str(int(b_list[1]) + 1)
        b_list.insert(1, "1")
        b = "/".join(b_list)
        a_list[0], a_list[1] = a_list[1], a_list[0]
        a = "/".join(a_list)
    elif (int(b_list[0]) == 30) and (b_list[1] in ["04", "06", "09", "11"]):
        b_list[0] = str(int(b_list[1]) + 1)
        b_list.insert(1, "1")
        b = "/".join(b_list)
        a_list[0], a_list[1] = a_list[1], a_list[0]
        a = "/".join(a_list)
    elif (int(b_list[0]) == 31) and (b_list[1] in ["01", "03", "05", "07", "08", "10", "12"]):
        print("Entered in to this loop")
        b_list[0] = str(int(b_list[1]) + 1)
        b_list.insert(1, "1")
        b = "/".join(b_list)
        a_list[0], a_list[1] = a_list[1], a_list[0]
        a = "/".join(a_list)
    elif (int(b_list[0]) == 31) and (b_list[1] == "12"):
        b_list.insert(0, "1")
        b_list.insert(1, "1")
        b_list[2] = str(int(b_list[2]) + 1)
        b = "/".join(b_list)
        a_list[0], a_list[1] = a_list[1], a_list[0]
        a = "/".join(a_list)
    else:
        print("Entered into else block")
        a_list[0], a_list[1] = a_list[1], a_list[0]
        a = "/".join(a_list)
        print(a)
        b_list[0] = str(int(b_list[0])+1)
        b_list[0], b_list[1] = b_list[1], b_list[0]
        b = "/".join(b_list)
        print(b)

    try:
        f = data[0].index(a)
        l = data[0].index(b)
    except:
        f = 0
        l = 0

    return [f, l]



def percent(inp, mini, maxi):
    print("in per")
    try:
        print("in per try")
        return (((inp - mini)*100)/(maxi-mini))
    except:
        return 0


def calculate(x):
    cal = []
    print(x)
    try:
        if x == 1001:
            print("In 1001")
            cal = [percent(int(data[2][-1]), 145, 370), percent(int(data[3][-1]), 12, 55), percent(int(data[4][-1]), 160, 570), int(data[5][-1])]
        elif x == 1002:
            cal = [percent(int(data[2][-1]), 100, 250), percent(int(data[3][-1]), 5, 75), percent(int(data[4][-1]), 125, 475), int(data[5][-1])]
        elif x == 1003:
            cal = [percent(int(data[2][-1]), 140, 350), percent(int(data[3][-1]), 10, 50), percent(int(data[4][-1]), 150, 430), int(data[5][-1])]
        elif x == 1004:
            cal = [percent(int(data[2][-1]), 120, 300), percent(int(data[3][-1]), 10, 52), percent(int(data[4][-1]), 200, 700), int(data[5][-1])]
        elif x == 1005:
            cal = [percent(int(data[2][-1]), 150, 400), percent(int(data[3][-1]), 10, 60), percent(int(data[4][-1]), 150, 650), int(data[5][-1])]
        elif x == 1006:
            cal = [percent(int(data[2][-1]), 75, 400), percent(int(data[3][-1]), 10, 75), percent(int(data[4][-1]), 150, 800), int(data[5][-1])]
        elif x == 1007:
            cal = [percent(int(data[2][-1]), 200, 600), percent(int(data[3][-1]), 10, 90), percent(int(data[4][-1]), 200, 600), int(data[5][-1])]
        elif x == 1008:
            cal = [percent(int(data[2][-1]), 125, 235), percent(int(data[3][-1]), 5, 115), percent(int(data[4][-1]), 175, 450), int(data[5][-1])]
        elif x == 1009:
            cal = [percent(int(data[2][-1]), 190, 410), percent(int(data[3][-1]), 3, 36), percent(int(data[4][-1]), 180, 510), int(data[5][-1])]
        elif x == 1010:
            cal = [percent(int(data[2][-1]), 100, 425), percent(int(data[3][-1]), 10, 75), percent(int(data[4][-1]), 200, 525), int(data[5][-1])]
        elif x == 1011:
            cal = [percent(int(data[2][-1]), 75, 425), percent(int(data[3][-1]), 10, 80), percent(int(data[4][-1]), 150, 850), int(data[5][-1])]
        elif x == 1012:
            cal = [percent(int(data[2][-1]), 100, 200), percent(int(data[3][-1]), 5, 50), percent(int(data[4][-1]), 125, 350), int(data[5][-1])]
        elif x == 1013:
            cal = [percent(int(data[2][-1]), 100, 360), percent(int(data[3][-1]), 10, 80), percent(int(data[4][-1]), 150, 475), int(data[5][-1])]
        elif x == 1014:
            cal = [percent(int(data[2][-1]), 100, 300), percent(int(data[3][-1]), 10, 110), percent(int(data[4][-1]), 100, 350), int(data[5][-1])]
        else:
            cal = [0,0,0,0]
    except:
        cal = [0, 0, 0, 0]

    return cal

class InfoScreen(Screen):
    pass


class HomeScreen(Screen):
    def display_value(self):
        try:
            x = int(self.code.text)
            print(x)
            val = calculate(x)
            print(val)
        except:
            val = [0, 0, 0, 0]
        self.ntpb.value = val[0]
        self.phpb.value = val[1]
        self.popb.value = val[2]
        self.mopb.value = val[3]




class DataScreen(Screen):

    dialog = None
    def data(self):
        try:
            self.nitro.text = data[2][-1]
            self.phos.text = data[3][-1]
            self.potas.text = data[4][-1]
            self.moist.text = data[5][-1]
        except:
            self.nitro.text = "Error"
            self.phos.text = "Error"
            self.potas.text = "Error"
            self.moist.text = "Error"


    def find_date(self):

        d1 = self.date1.text
        d2 = self.date2.text
        print(d1,d2)

        self.l = indx(str(d1), str(d2))
        self.m = self.l[0]
        print(self.l)

        try:
            self.nitro.text = data[2][self.l[0]]
            self.phos.text = data[3][self.l[0]]
            self.potas.text = data[4][self.l[0]]
            self.moist.text = data[5][self.l[0]]
        except:
            self.nitro.text = "Error"
            self.phos.text = "Error"
            self.potas.text = "Error"
            self.moist.text = "Error"


    def next_data(self):
        try:
                if self.l[0]<(self.l[1]-1):
                    self.l[0] = self.l[0]+1
                    try:
                        self.nitro.text = data[2][self.l[0]]
                        self.phos.text = data[3][self.l[0]]
                        self.potas.text = data[4][self.l[0]]
                        self.moist.text = data[5][self.l[0]]
                    except:
                        self.nitro.text = "Error"
                        self.phos.text = "Error"
                        self.potas.text = "Error"
                        self.moist.text = "Error"
        except:
                self.nitro.text = "Error"
                self.phos.text = "Error"
                self.potas.text = "Error"
                self.moist.text = "Error"


    def prev_data(self):
        try:
            if self.l[0]>self.m:
                self.l[0] = self.l[0]-1
                try:
                    self.nitro.text = data[2][self.l[0]]
                    self.phos.text = data[3][self.l[0]]
                    self.potas.text = data[4][self.l[0]]
                    self.moist.text = data[5][self.l[0]]
                except:
                    self.nitro.text = "Error"
                    self.phos.text = "Error"
                    self.potas.text = "Error"
                    self.moist.text = "Error"
        except:
            self.nitro.text = "Error"
            self.phos.text = "Error"
            self.potas.text = "Error"
            self.moist.text = "Error"




class GraphScreen(Screen):
    pass



class MyApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.title = 'FarmTech'
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(DataScreen(name='data'))
        self.sm.add_widget(GraphScreen(name='graph'))
        self.sm.add_widget(InfoScreen(name='info'))
        screen = Builder.load_file("GUI.kv")

        return screen

    def change_screen(self, scr, dir):
        self.root.transition.direction = dir
        self.root.current = scr


MyApp().run()