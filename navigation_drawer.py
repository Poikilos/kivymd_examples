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
from kivymd.uix.list import (
    OneLineAvatarListItem,
)


class ContentNavDrawer(BoxLayout):
    pass


class OneLineLeftIconItem(OneLineAvatarListItem):
    icon = StringProperty()


class NavDrawer(Screen):
    def __init__(self, **kw):
        super(NavDrawer, self).__init__(**kw)
        Clock.schedule_once(self.__post_init__)

    def __post_init__(self, *args):
        pass
    #def on_enter(self):
        print("on_enter...")
        if not self.ids.content_drawer.ids.box_item.children:
            for icon, text in {
                "home-circle-outline": "Home",
                "update": "Check for Update",
                "cog-outline": "Settings",
                "exit-to-app": "Exit",
            }.items():
                self.ids.content_drawer.ids.box_item.add_widget(
                    OneLineLeftIconItem(
                        text=text, icon=icon, divider=None
                    )
                )


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Navigation Drawer (kivymd_examples)"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_file('navigation_drawer.kv')
        # self.nav_drawer = NavDrawer()


if __name__ == "__main__":
    MainApp().run()
