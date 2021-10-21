from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty, ListProperty
#from kivymd.uix.screen import MDScreen
#from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import Screen
# ^ It must be from screenmanager!
#   See KivyMD/demos/kitchen_sink/libs/baseclass/navigation_drawer.py


class ContentNavDrawer(BoxLayout):
    pass


class NavDrawerScreen(Screen):
    pass
    '''
    def __init__(self, **kw):
        super(NavDrawerScreen, self).__init__(**kw)
        Clock.schedule_once(self.__post_init__)

    def __post_init__(self, *args):
        pass
    '''


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "My Material Application"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_file('navigation_drawer.kv')
        # self.nav_drawer = NavDrawer()


if __name__ == "__main__":
    MainApp().run()
