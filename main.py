import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
#Config.set('graphics', 'width', '1200')
#Config.set('graphics', 'height', '600')

Window.size = (310, 500)


#Builder.load_file('tictactoe.kv')

global x_wins, o_wins, turn
x_wins = 0
o_wins = 0

turn = 'X'
class MyGridLayout(GridLayout):
    global slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, turn, winner
    slot1 = ' '
    slot2 = ' '
    slot3 = ' '
    slot4 = ' '
    slot5 = ' '
    slot6 = ' '
    slot7 = ' '
    slot8 = ' '
    slot9 = ' '
    winner = ''
    def __init__(self, **kwargs):
        #Call grid layout Constructor
        super(MyGridLayout, self).__init__(**kwargs)


        #Set Columns
        self.cols = 1

        #Create a second layout
        self.top_grid = GridLayout()
        self.top_grid.cols=3
        global b1, b2, b3, b4, b5, b6, b7, b8, b9, l1, e1, e2, l2, b10, b11, t1, winner, x_wins, o_wins, turn
        self.add_widget(Label(text="[u][b]Tic Tac Toe[/b][/u]", markup=True,
                             font_size = 32,
                             size_hint_y = None,
                             height =50,
                             size_hint_x = None,
                             width = 300))

        #add widgets
        self.top_grid.add_widget(Label(text = "[u]Player X: [/u]",markup=True, font_size = 20))

        self.wins_by_x = Label(text = f"{x_wins}", font_size = 20)
        self.top_grid.add_widget(self.wins_by_x)

        self.top_grid.add_widget((Button(text="Reset", font_size = 20,
                             size_hint_y = None,
                             height =50,
                             size_hint_max_x = 100,
                             width = 100,
                             on_release=self.reset)))
                         #background_normal= '',
                         #background_color=(48/255, 84/255, 150/255,1))))



        self.top_grid.add_widget(Label(text="[u]Player O: [/u]",markup=True, font_size = 20))

        self.wins_by_o = Label(text=f"{o_wins}", font_size = 20)
        self.top_grid.add_widget(self.wins_by_o)

        self.t1= Label(text=f"Turn: {turn}", font_size = 20,
                             #size_hint_y = None,
                             #height =35,
                             size_hint_x = None,
                             width = 100)
        self.top_grid.add_widget(self.t1)
#Adding the 3x3
        self.b1= Button(text=f"{slot1}",
                             font_size = 32,
                             size_hint_y = None,
                             height =100,
                             size_hint_x = None,
                             width = 100)

                         #background_normal= '',
                         #background_color=(48/255, 84/255, 150/255,1))
        self.b1.bind(on_press=self.b1click)
        self.top_grid.add_widget(self.b1)
        self.b2 = Button(text=f"{slot2}",
                             font_size = 32,
                             size_hint_y = None,
                             height =100,
                             size_hint_x = None,
                             width = 100)
                         #background_normal= '',
                         #background_color=(48/255, 84/255, 150/255,1))
        self.b2.bind(on_press=self.b2click)
        self.top_grid.add_widget(self.b2)
        self.b3 = Button(text=f"{slot3}",
                             font_size = 32,
                             size_hint_y = None,
                             height =100,
                             size_hint_x = None,
                             width = 100)
                         #background_normal= '',
                         #background_color=(48/255, 84/255, 150/255,1))
        self.b3.bind(on_press=self.b3click)
        self.top_grid.add_widget(self.b3)
        self.top_grid.add_widget((Label(text="",
                                         size_hint_y=None,
                                         height=5,
                                         size_hint_x=None,
                                         width=100)))
        self.top_grid.add_widget((Label(text="",
                                         size_hint_y=None,
                                         height=5,
                                         size_hint_x=None,
                                         width=100)))
        self.top_grid.add_widget((Label(text="",
                                         size_hint_y=None,
                                         height=5,
                                         size_hint_x=None,
                                         width=100)))
        self.b4 = Button(text=f"{slot4}",
                             font_size = 32,
                             size_hint_y = None,
                             height =100,
                             size_hint_x = None,
                             width = 100)
                         #background_normal= '',
                         #background_color=(48/255, 84/255, 150/255,1))
        self.b4.bind(on_press=self.b4click)
        self.top_grid.add_widget(self.b4)
        self.b5 = Button(text=f"{slot5}",
                             font_size = 32,
                             size_hint_y = None,
                             height =100,
                             size_hint_x = None,
                             width = 100)
                         #background_normal= '',
                         #background_color=(48/255, 84/255, 150/255,1))
        self.b5.bind(on_press=self.b5click)
        self.top_grid.add_widget(self.b5)
        self.b6 = Button(text=f"{slot6}",
                             font_size = 32,
                             size_hint_y = None,
                             height =100,
                             size_hint_x = None,
                             width = 100)
                         #background_normal= '',
                         #background_color=(48/255, 84/255, 150/255,1))
        self.b6.bind(on_press=self.b6click)
        self.top_grid.add_widget(self.b6)
        self.top_grid.add_widget((Label(text="",
                                        size_hint_y=None,
                                        height=5,
                                        size_hint_x=None,
                                        width=100)))
        self.top_grid.add_widget((Label(text="",
                                        size_hint_y=None,
                                        height=5,
                                        size_hint_x=None,
                                        width=100)))
        self.top_grid.add_widget((Label(text="",
                                        size_hint_y=None,
                                        height=5,
                                        size_hint_x=None,
                                        width=100)))
        self.b7 = Button(text=f"{slot7}",
                             font_size = 32,
                             size_hint_y = None,
                             height =100,
                             size_hint_x = None,
                             width = 100)
                         #background_normal= '',
                         #background_color=(48/255, 84/255, 150/255,1))
        self.b7.bind(on_press=self.b7click)
        self.top_grid.add_widget(self.b7)
        self.b8 = Button(text=f"{slot8}",
                             font_size = 32,
                             size_hint_y = None,
                             height =100,
                             size_hint_x = None,
                             width = 100)
                         #background_normal= '',
                         #background_color=(48/255, 84/255, 150/255,1))
        self.b8.bind(on_press=self.b8click)
        self.top_grid.add_widget(self.b8)
        self.b9 = Button(text=f"{slot9}",
                             font_size = 32,
                             size_hint_y = None,
                             height = 100,
                             size_hint_x = None,
                             width = 100)
                         #background_normal= '',
                         #background_color=(48/255, 84/255, 150/255,1))
        self.b9.bind(on_press=self.b9click)
        self.top_grid.add_widget(self.b9)





        #add the new top grid
        self.add_widget(self.top_grid)






    def checkingIfWon(self):
        global  b1, b2, b3, b4, b5, b6, b7, b8, b9, l1, e1, e2, l2, b10, b11, t1, winner, x_wins, o_wins, turn, popupwindow

        #### X Win Possibilities #####
        # Horizontal
        global slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, turn, winner
        if (slot1 == 'X' and slot2 == 'X' and slot3 == 'X'):
            self.b1.background_normal=''
            self.b2.background_normal = ''
            self.b3.background_normal = ''
            self.b1.background_color=(1/255, 102/255, 21/255)
            self.b2.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b3.background_color = (1 / 255, 102 / 255, 21 / 255)
            x_wins += 1
            self.wins_by_x.text = f'{x_wins}'
            turn = 'X'
            self.t1.text = f'Turn : {turn}'
            #self.reset()
            winner = 'X'
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(text=f"'{winner}' won this round !!!"))
            btn1 = Button(text="Close")

            popupwindow = Popup(title="Winner!!", content=box,pos_hint={"x":0.1, "top":0.97}, size_hint=(None,None), size=(250,150), auto_dismiss=False)
            popupwindow.open()
            btn1.bind(on_release=self.resetafterwin)
            box.add_widget(btn1)


        elif (slot4 == 'X' and slot5 == 'X' and slot6 == 'X'):
            self.b4.background_normal = ''
            self.b5.background_normal = ''
            self.b6.background_normal = ''
            self.b4.background_color=(1/255, 102/255, 21/255)
            self.b5.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b6.background_color = (1 / 255, 102 / 255, 21 / 255)
            x_wins += 1
            self.wins_by_x.text = f'{x_wins}'
            turn = 'X'
            self.t1.text = f'Turn : {turn}'
            #self.reset()
            winner = 'X'
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(text=f"'{winner}' won this round !!!"))
            btn1 = Button(text="Close")

            popupwindow = Popup(title="Winner!!", content=box,pos_hint={"x":0.1, "top":0.97}, size_hint=(None,None), size=(250,150), auto_dismiss=False)
            popupwindow.open()
            btn1.bind(on_release=self.resetafterwin)
            box.add_widget(btn1)

        elif (slot7 == 'X' and slot8 == 'X' and slot9 == 'X'):
            self.b7.background_normal = ''
            self.b8.background_normal = ''
            self.b9.background_normal = ''
            self.b7.background_color=(1/255, 102/255, 21/255)
            self.b8.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b9.background_color = (1 / 255, 102 / 255, 21 / 255)
            x_wins += 1
            self.wins_by_x.text = f'{x_wins}'
            turn = 'X'
            self.t1.text = f'Turn : {turn}'
            #self.reset()
            winner = 'X'
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(text=f"'{winner}' won this round !!!"))
            btn1 = Button(text="Close")

            popupwindow = Popup(title="Winner!!", content=box,pos_hint={"x":0.1, "top":0.97}, size_hint=(None,None), size=(250,150), auto_dismiss=False)
            popupwindow.open()
            btn1.bind(on_release=self.resetafterwin)
            box.add_widget(btn1)

        #Vertically
        elif (slot1 == 'X' and slot4 == 'X' and slot7 == 'X'):
            self.b1.background_normal = ''
            self.b4.background_normal = ''
            self.b7.background_normal = ''
            self.b1.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b4.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b7.background_color = (1 / 255, 102 / 255, 21 / 255)
            x_wins += 1
            self.wins_by_x.text = f'{x_wins}'
            turn = 'X'
            self.t1.text = f'Turn : {turn}'
            # self.reset()
            winner = 'X'
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(text=f"'{winner}' won this round !!!"))
            btn1 = Button(text="Close")

            popupwindow = Popup(title="Winner!!", content=box, pos_hint={"x": 0.1, "top": 0.97}, size_hint=(None, None),
                                size=(250, 150), auto_dismiss=False)
            popupwindow.open()
            btn1.bind(on_release=self.resetafterwin)
            box.add_widget(btn1)


        elif (slot2 == 'X' and slot5 == 'X' and slot8 == 'X'):
            self.b2.background_normal = ''
            self.b5.background_normal = ''
            self.b8.background_normal = ''
            self.b2.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b5.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b8.background_color = (1 / 255, 102 / 255, 21 / 255)
            x_wins += 1
            self.wins_by_x.text = f'{x_wins}'
            turn = 'X'
            self.t1.text = f'Turn : {turn}'
            # self.reset()
            winner = 'X'
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(text=f"'{winner}' won this round !!!"))
            btn1 = Button(text="Close")

            popupwindow = Popup(title="Winner!!", content=box, pos_hint={"x": 0.1, "top": 0.97}, size_hint=(None, None),
                                size=(250, 150), auto_dismiss=False)
            popupwindow.open()
            btn1.bind(on_release=self.resetafterwin)
            box.add_widget(btn1)

        elif (slot3 == 'X' and slot6 == 'X' and slot9 == 'X'):
            self.b3.background_normal = ''
            self.b6.background_normal = ''
            self.b9.background_normal = ''
            self.b3.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b6.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b9.background_color = (1 / 255, 102 / 255, 21 / 255)
            x_wins += 1
            self.wins_by_x.text = f'{x_wins}'
            turn = 'X'
            self.t1.text = f'Turn : {turn}'
            # self.reset()
            winner = 'X'
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(text=f"'{winner}' won this round !!!"))
            btn1 = Button(text="Close")

            popupwindow = Popup(title="Winner!!", content=box, pos_hint={"x": 0.1, "top": 0.97}, size_hint=(None, None),
                                size=(250, 150), auto_dismiss=False)
            popupwindow.open()
            btn1.bind(on_release=self.resetafterwin)
            box.add_widget(btn1)

        #Diagonally
        elif (slot1 == 'X' and slot5 == 'X' and slot9 == 'X'):
            self.b1.background_normal = ''
            self.b5.background_normal = ''
            self.b9.background_normal = ''
            self.b1.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b5.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b9.background_color = (1 / 255, 102 / 255, 21 / 255)
            x_wins += 1
            self.wins_by_x.text = f'{x_wins}'
            turn = 'X'
            self.t1.text = f'Turn : {turn}'
            # self.reset()
            winner = 'X'
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(text=f"'{winner}' won this round !!!"))
            btn1 = Button(text="Close")

            popupwindow = Popup(title="Winner!!", content=box, pos_hint={"x": 0.1, "top": 0.97}, size_hint=(None, None),
                                size=(250, 150), auto_dismiss=False)
            popupwindow.open()
            btn1.bind(on_release=self.resetafterwin)
            box.add_widget(btn1)

        elif (slot3 == 'X' and slot5 == 'X' and slot7 == 'X'):
            self.b3.background_normal = ''
            self.b5.background_normal = ''
            self.b7.background_normal = ''
            self.b3.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b5.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b7.background_color = (1 / 255, 102 / 255, 21 / 255)
            x_wins += 1
            self.wins_by_x.text = f'{x_wins}'
            turn = 'X'
            self.t1.text = f'Turn : {turn}'
            # self.reset()
            winner = 'X'
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(text=f"'{winner}' won this round !!!"))
            btn1 = Button(text="Close")

            popupwindow = Popup(title="Winner!!", content=box, pos_hint={"x": 0.1, "top": 0.97}, size_hint=(None, None),
                                size=(250, 150), auto_dismiss=False)
            popupwindow.open()
            btn1.bind(on_release=self.resetafterwin)
            box.add_widget(btn1)

        #### O Win Possibilities #####
        # Horizontal
        if (slot1 == 'O' and slot2 == 'O' and slot3 == 'O'):
            self.b1.background_normal = ''
            self.b2.background_normal = ''
            self.b3.background_normal = ''
            self.b1.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b2.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b3.background_color = (1 / 255, 102 / 255, 21 / 255)
            o_wins += 1
            self.wins_by_o.text = f'{o_wins}'
            turn = 'O'
            self.t1.text = f'Turn : {turn}'
            # self.reset()
            winner = 'O'
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(text=f"'{winner}' won this round !!!"))
            btn1 = Button(text="Close")

            popupwindow = Popup(title="Winner!!", content=box, pos_hint={"x": 0.1, "top": 0.97},
                                    size_hint=(None, None), size=(250, 150), auto_dismiss=False)
            popupwindow.open()
            btn1.bind(on_release=self.resetafterwin)
            box.add_widget(btn1)


        elif (slot4 == 'O' and slot5 == 'O' and slot6 == 'O'):
            self.b4.background_normal = ''
            self.b5.background_normal = ''
            self.b6.background_normal = ''
            self.b4.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b5.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b6.background_color = (1 / 255, 102 / 255, 21 / 255)
            o_wins += 1
            self.wins_by_o.text = f'{o_wins}'
            turn = 'O'
            self.t1.text = f'Turn : {turn}'
            # self.reset()
            winner = 'O'
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(text=f"'{winner}' won this round !!!"))
            btn1 = Button(text="Close")

            popupwindow = Popup(title="Winner!!", content=box, pos_hint={"x": 0.1, "top": 0.97},
                                size_hint=(None, None), size=(250, 150), auto_dismiss=False)
            popupwindow.open()
            btn1.bind(on_release=self.resetafterwin)
            box.add_widget(btn1)

        elif (slot7 == 'O' and slot8 == 'O' and slot9 == 'O'):
            self.b7.background_normal = ''
            self.b8.background_normal = ''
            self.b9.background_normal = ''
            self.b7.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b8.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b9.background_color = (1 / 255, 102 / 255, 21 / 255)
            o_wins += 1
            self.wins_by_o.text = f'{o_wins}'
            turn = 'O'
            self.t1.text = f'Turn : {turn}'
            # self.reset()
            winner = 'O'
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(text=f"'{winner}' won this round !!!"))
            btn1 = Button(text="Close")

            popupwindow = Popup(title="Winner!!", content=box, pos_hint={"x": 0.1, "top": 0.97},
                                size_hint=(None, None), size=(250, 150), auto_dismiss=False)
            popupwindow.open()
            btn1.bind(on_release=self.resetafterwin)
            box.add_widget(btn1)

        # Vertically
        elif (slot1 == 'O' and slot4 == 'O' and slot7 == 'O'):
            self.b1.background_normal = ''
            self.b4.background_normal = ''
            self.b7.background_normal = ''
            self.b1.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b4.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b7.background_color = (1 / 255, 102 / 255, 21 / 255)
            o_wins += 1
            self.wins_by_o.text = f'{o_wins}'
            turn = 'O'
            self.t1.text = f'Turn : {turn}'
            # self.reset()
            winner = 'O'
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(text=f"'{winner}' won this round !!!"))
            btn1 = Button(text="Close")

            popupwindow = Popup(title="Winner!!", content=box, pos_hint={"x": 0.1, "top": 0.97},
                                size_hint=(None, None),
                                size=(250, 150), auto_dismiss=False)
            popupwindow.open()
            btn1.bind(on_release=self.resetafterwin)
            box.add_widget(btn1)


        elif (slot2 == 'O' and slot5 == 'O' and slot8 == 'O'):
            self.b2.background_normal = ''
            self.b5.background_normal = ''
            self.b8.background_normal = ''
            self.b2.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b5.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b8.background_color = (1 / 255, 102 / 255, 21 / 255)
            o_wins += 1
            self.wins_by_o.text = f'{o_wins}'
            turn = 'O'
            self.t1.text = f'Turn : {turn}'
            # self.reset()
            winner = 'O'
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(text=f"'{winner}' won this round !!!"))
            btn1 = Button(text="Close")

            popupwindow = Popup(title="Winner!!", content=box, pos_hint={"x": 0.1, "top": 0.97},
                                size_hint=(None, None),
                                size=(250, 150), auto_dismiss=False)
            popupwindow.open()
            btn1.bind(on_release=self.resetafterwin)
            box.add_widget(btn1)

        elif (slot3 == 'O' and slot6 == 'O' and slot9 == 'O'):
            self.b3.background_normal = ''
            self.b6.background_normal = ''
            self.b9.background_normal = ''
            self.b3.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b6.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b9.background_color = (1 / 255, 102 / 255, 21 / 255)
            o_wins += 1
            self.wins_by_o.text = f'{o_wins}'
            turn = 'O'
            self.t1.text = f'Turn : {turn}'
            # self.reset()
            winner = 'O'
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(text=f"'{winner}' won this round !!!"))
            btn1 = Button(text="Close")

            popupwindow = Popup(title="Winner!!", content=box, pos_hint={"x": 0.1, "top": 0.97},
                                size_hint=(None, None),
                                size=(250, 150), auto_dismiss=False)
            popupwindow.open()
            btn1.bind(on_release=self.resetafterwin)
            box.add_widget(btn1)

        # Diagonally
        elif (slot1 == 'O' and slot5 == 'O' and slot9 == 'O'):
            self.b1.background_normal = ''
            self.b5.background_normal = ''
            self.b9.background_normal = ''
            self.b1.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b5.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b9.background_color = (1 / 255, 102 / 255, 21 / 255)
            o_wins += 1
            self.wins_by_o.text = f'{o_wins}'
            turn = 'O'
            self.t1.text = f'Turn : {turn}'
            # self.reset()
            winner = 'O'
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(text=f"'{winner}' won this round !!!"))
            btn1 = Button(text="Close")

            popupwindow = Popup(title="Winner!!", content=box, pos_hint={"x": 0.1, "top": 0.97},
                                size_hint=(None, None),
                                size=(250, 150), auto_dismiss=False)
            popupwindow.open()
            btn1.bind(on_release=self.resetafterwin)
            box.add_widget(btn1)

        elif (slot3 == 'O' and slot5 == 'O' and slot7 == 'O'):
            self.b3.background_normal = ''
            self.b5.background_normal = ''
            self.b7.background_normal = ''
            self.b3.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b5.background_color = (1 / 255, 102 / 255, 21 / 255)
            self.b7.background_color = (1 / 255, 102 / 255, 21 / 255)
            o_wins += 1
            self.wins_by_o.text = f'{o_wins}'
            turn = 'O'
            self.t1.text = f'Turn : {turn}'
            # self.reset()
            winner = 'O'
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(text=f"'{winner}' won this round !!!"))
            btn1 = Button(text="Close")

            popupwindow = Popup(title="Winner!!", content=box, pos_hint={"x": 0.1, "top": 0.97},
                                size_hint=(None, None),
                                size=(250, 150), auto_dismiss=False)
            popupwindow.open()
            btn1.bind(on_release=self.resetafterwin)
            box.add_widget(btn1)

        elif (slot1 == 'X' or slot1 == 'O') and (slot2 == 'X' or slot2 == 'O') and (slot3 == 'X' or slot3 == 'O') \
                and (slot4 == 'X' or slot4 == 'O') and (slot5 == 'X' or slot5 == 'O') and (slot6 == 'X' or slot6 == 'O') \
                and (slot7 == 'X' or slot7 == 'O') and (slot8 == 'X' or slot8 == 'O') and (
                slot9 == 'X' or slot9 == 'O') and winner == '':
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(text=f"This Round was a Tie.. \n(Whose turn is first will be selected at random)\n", font_size=12))
            btn1 = Button(text="Close")

            popupwindow = Popup(title="Winner!!", content=box, pos_hint={"x": 0.03, "top": 0.97},
                                size_hint=(None, None),
                                size=(300, 150), auto_dismiss=False)
            popupwindow.open()
            btn1.bind(on_release=self.resetafterwin)
            box.add_widget(btn1)



    def reset(self, instance):
        global slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, turn, winner,reset_turn_divisible, t1
        


        reset_turn_divisible=0
        if slot1!=' ':
            reset_turn_divisible+=1

        if slot2!=' ':
            reset_turn_divisible+=1

        if slot3!=' ':
            reset_turn_divisible+=1

        if slot4!=' ':
            reset_turn_divisible+=1

        if slot5!=' ':
            reset_turn_divisible+=1

        if slot6!=' ':
            reset_turn_divisible+=1

        if slot7 != ' ':
            reset_turn_divisible += 1

        if slot8 != ' ':
            reset_turn_divisible += 1

        if slot9 != ' ':
            reset_turn_divisible += 1

        slot1 = ' '
        slot2 = ' '
        slot3 = ' '
        slot4 = ' '
        slot5 = ' '
        slot6 = ' '
        slot7 = ' '
        slot8 = ' '
        slot9 = ' '
        winner = ''
        if (reset_turn_divisible==1 or reset_turn_divisible==3 or reset_turn_divisible==5 or reset_turn_divisible==7 or reset_turn_divisible==9) and turn=='X':
            turn='O'
            self.t1.text = f'Turn : {turn}'
        elif (reset_turn_divisible==1 or reset_turn_divisible==3 or reset_turn_divisible==5 or reset_turn_divisible==7 or reset_turn_divisible==9) and turn=='O':

            turn='X'
            self.t1.text = f'Turn : {turn}'
        elif (reset_turn_divisible==2 or reset_turn_divisible==4 or reset_turn_divisible==6 or reset_turn_divisible==8 ) and turn=='X':

            turn='X'
            self.t1.text = f'Turn : {turn}'
        elif (reset_turn_divisible==2 or reset_turn_divisible==4 or reset_turn_divisible==6 or reset_turn_divisible==8) and turn=='O':

            turn='O'
            self.t1.text = f'Turn : {turn}'


        self.b1.text = slot1
        self.b2.text = slot2
        self.b3.text = slot3
        self.b4.text = slot4
        self.b5.text = slot5
        self.b6.text = slot6
        self.b7.text = slot7
        self.b8.text = slot8
        self.b9.text = slot9
        self.b1.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b2.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b3.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b4.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b5.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b6.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b7.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b8.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b9.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b1.background_color=(1,1,1,1)
        self.b2.background_color = (1,1,1,1)
        self.b3.background_color = (1,1,1,1)
        self.b4.background_color = (1,1,1,1)
        self.b5.background_color = (1,1,1,1)
        self.b6.background_color = (1,1,1,1)
        self.b7.background_color = (1,1,1,1)
        self.b8.background_color = (1,1,1,1)
        self.b9.background_color = (1,1,1,1)

    def resetafterwin(self, instance):
        global slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, turn, winner, popupwindow
        popupwindow.dismiss()
        slot1 = ' '
        slot2 = ' '
        slot3 = ' '
        slot4 = ' '
        slot5 = ' '
        slot6 = ' '
        slot7 = ' '
        slot8 = ' '
        slot9 = ' '
        winner = ''
        self.b1.text = slot1
        self.b2.text = slot2
        self.b3.text = slot3
        self.b4.text = slot4
        self.b5.text = slot5
        self.b6.text = slot6
        self.b7.text = slot7
        self.b8.text = slot8
        self.b9.text = slot9
        self.b1.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b2.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b3.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b4.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b5.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b6.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b7.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b8.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b9.background_normal = 'atlas://data/images/defaulttheme/button'
        self.b1.background_color=(1,1,1,1)
        self.b2.background_color = (1,1,1,1)
        self.b3.background_color = (1,1,1,1)
        self.b4.background_color = (1,1,1,1)
        self.b5.background_color = (1,1,1,1)
        self.b6.background_color = (1,1,1,1)
        self.b7.background_color = (1,1,1,1)
        self.b8.background_color = (1,1,1,1)
        self.b9.background_color = (1,1,1,1)


    def b1click(self, instance):
        global slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, turn, winner
        if slot1 == ' ' and turn == 'X':
            slot1 = 'X'
            turn = 'O'
            self.b1.text=slot1
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()

        if slot1 == ' ' and turn == 'O':
            slot1 = 'O'
            turn = 'X'
            self.b1.text=slot1
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()


    def b2click(self, instance):
        global slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, turn, winner
        if slot2 == ' ' and turn == 'X':
            slot2 = 'X'
            turn = 'O'
            self.b2.text=slot2
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()

        if slot2 == ' ' and turn == 'O':
            slot2 = 'O'
            turn = 'X'
            self.b2.text=slot2
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()


    def b3click(self, instance):
        global slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, turn, winner
        if slot3 == ' ' and turn == 'X':
            slot3 = 'X'
            turn = 'O'
            self.b3.text=slot3
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()

        if slot3 == ' ' and turn == 'O':
            slot3 = 'O'
            turn = 'X'
            self.b3.text=slot3
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()


    def b4click(self, instance):
        global slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, turn, winner
        if slot4 == ' ' and turn == 'X':
            slot4 = 'X'
            turn = 'O'
            self.b4.text=slot4
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()
        if slot4 == ' ' and turn == 'O':
            slot4 = 'O'
            turn = 'X'
            self.b4.text=slot4
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()


    def b5click(self, instance):
        global slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, turn, winner
        if slot5 == ' ' and turn == 'X':
            slot5 = 'X'
            turn = 'O'
            self.b5.text=slot5
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()

        if slot5 == ' ' and turn == 'O':
            slot5 = 'O'
            turn = 'X'
            self.b5.text=slot5
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()


    def b6click(self, instance):
        global slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, turn, winner
        if slot6 == ' ' and turn == 'X':
            slot6 = 'X'
            turn = 'O'
            self.b6.text=slot6
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()

        if slot6 == ' ' and turn == 'O':
            slot6 = 'O'
            turn = 'X'
            self.b6.text=slot6
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()


    def b7click(self, instance):
        global slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, turn, winner
        if slot7 == ' ' and turn == 'X':
            slot7 = 'X'
            turn = 'O'
            self.b7.text=slot7
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()
        if slot7 == ' ' and turn == 'O':
            slot7 = 'O'
            turn = 'X'
            self.b7.text=slot7
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()


    def b8click(self, instance):
        global slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, turn, winner
        if slot8 == ' ' and turn == 'X':
            slot8 = 'X'
            turn = 'O'
            self.b8.text=slot8
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()

        if slot8 == ' ' and turn == 'O':
            slot8 = 'O'
            turn = 'X'
            self.b8.text=slot8
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()


    def b9click(self, instance):
        global slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, turn, winner
        if slot9 == ' ' and turn == 'X':
            slot9 = 'X'
            turn = 'O'
            self.b9.text=slot9
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()

        if slot9 == ' ' and turn == 'O':
            slot9 = 'O'
            turn = 'X'
            self.b9.text=slot9
            self.t1.text=f'Turn : {turn}'
            self.checkingIfWon()







class XandOApp(App):
    def build(self):
        self.icon='presplash.png'
        return MyGridLayout()

if __name__ == '__main__':
    XandOApp().run()