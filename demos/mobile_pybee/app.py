import toga
import contentful


client = contentful.Client(
    '1t8fkm227wii',
    'db4920ea9db282ed36c6728dcd153575c6aafc35958dccbbf3fb02801b8e8f21'
)

def build(app):
    box = toga.Box()
    entry = client.entry('minecraft_agiles', {'include': 3})

    title_font = toga.Font('Helvetica Neue Bold', 16)
    subtitle_font = toga.Font('Helvetica Neue Italic', 12)

    title = toga.Label(entry.title, alignment=toga.CENTER_ALIGNED)
    subtitle = toga.Label(entry.subtitle, alignment=toga.CENTER_ALIGNED)
    content = toga.Label('{0}...'.format(entry.content[:1000]), alignment=toga.CENTER_ALIGNED)

    title.style.set(height=40, width=640, margin=10)
    title.set_font(title_font)
    subtitle.style.set(height=30,margin=10, width=640)
    subtitle.set_font(subtitle_font)
    content.style.set(margin=10, width=640)

    box.add(title)
    box.add(subtitle)
    box.add(content)

    return box

if __name__ == '__main__':
    app = toga.App('Demo', 'demo.pycaribbean.com', startup=build)
    app.main_loop()
