from nicegui import ui

from .screen import Screen


def test_with_strings(screen: Screen):
    with ui.tabs() as tabs:
        ui.tab('One')
        ui.tab('Two')

    with ui.tab_panels(tabs, value='One') as panels:
        with ui.tab_panel('One'):
            ui.label('First tab')
        with ui.tab_panel('Two'):
            ui.label('Second tab')

    screen.open('/')
    screen.should_contain('First tab')
    screen.click('Two')
    screen.should_contain('Second tab')


def test_with_tab_objects(screen: Screen):
    with ui.tabs() as tabs:
        tab1 = ui.tab('One')
        tab2 = ui.tab('Two')

    with ui.tab_panels(tabs, value=tab2):
        with ui.tab_panel(tab1):
            ui.label('First tab')
        with ui.tab_panel(tab2):
            ui.label('Second tab')

    screen.open('/')
    screen.should_contain('One')
    screen.should_contain('Two')
    # TODO initial value selects tab but does not show its content
    # screen.should_contain('Second tab')
    screen.click('One')
    screen.should_contain('First tab')
