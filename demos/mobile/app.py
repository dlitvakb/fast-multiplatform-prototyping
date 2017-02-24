import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

import contentful


client = contentful.Client(
    '1t8fkm227wii',
    'db4920ea9db282ed36c6728dcd153575c6aafc35958dccbbf3fb02801b8e8f21'
)

class BlogLayout(BoxLayout):
    def __init__(self, **kwargs):
        BoxLayout.__init__(self, orientation='vertical', **kwargs)

        entry = client.entry('minecraft_agiles', {'include': 3})

        title = Label(text="[b]{0}[/b]".format(entry.title), font_size='40sp', markup=True)
        subtitle = Label(text="[i]{0}[/i]".format(entry.subtitle), font_size='15sp', markup=True)
        content = Label(text="{0}...".format(entry.author.name))

        self.add_widget(title)
        self.add_widget(subtitle)
        self.add_widget(content)

class DemoApp(App):
    def build(self):
        return BlogLayout()


if __name__ == '__main__':
    DemoApp().run()
