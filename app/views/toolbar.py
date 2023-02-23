from kivymd.uix.button import MDTextButton, MDIconButton
from kivymd.uix.screen import MDScreen


def tool_bar(controller_object: object, app_object: object):
    return MDScreen(
        MDTextButton(
            text = 'Добавить запись',
            pos_hint = {'center_x':0.1 ,'center_y':0.95},
            padding = [10,10],
            font_style = 'Button',
        ),
        MDTextButton(
            text = 'Удалить запись',
            pos_hint = {'center_x':0.3, 'center_y':0.95},
            padding = [10,10],
            font_style = 'Button',
        ),
        MDTextButton(
            text = 'Найти запись',
            pos_hint = {'center_x':0.5, 'center_y':0.95},
            padding = [10,10],
            font_style = 'Button',
        ),
        
        MDIconButton(
            icon = 'white-balance-sunny',
            on_release = app_object.switch_theme_style,
            pos_hint = {'center_y':0.95, 'center_x':0.95},
            padding = [10,10],
        ),
    )