import ipywidgets as widgets

import react_ipywidgets as react
import react_ipywidgets.ipywidgets as w


def test_find_by_class():
    @react.component
    def Test():
        with w.VBox() as main:
            with w.HBox():
                w.Button(description="test")
        return main

    box, rc = react.render(Test())
    assert rc._find(widgets.Button).single.description == "test"


def test_find_by_class_and_attr():
    @react.component
    def Test():
        with w.VBox() as main:
            with w.HBox():
                w.Button(description="1")
                with w.VBox():
                    w.Button(description="2")
        return main

    box, rc = react.render(Test())
    assert rc._find(widgets.Button, description="1").single.description == "1"
    assert rc._find(widgets.Button, description="2").single.description == "2"


def test_find_by_class_and_attr_nested():
    @react.component
    def Test():
        with w.VBox() as main:
            with w.HBox(box_style="SUCCESS"):
                w.Button(description="1", disabled=True)
                with w.VBox():
                    w.Button(description="2", disabled=False)
            with w.HBox(box_style="info"):
                w.Button(description="1", disabled=True)
                with w.VBox():
                    w.Button(description="2", disabled=False)
        return main

    box, rc = react.render(Test())
    rc._find(widgets.HBox, box_style="success").find(widgets.Button, description="1").matches(description="1", disabled=True)
    rc._find(widgets.HBox, box_style="info").find(widgets.Button, description="2").matches(description="2", disabled=False)
