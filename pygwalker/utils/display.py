from typing import Union

from IPython.display import display, HTML
import ipywidgets

DISPLAY_HANDLER = {}


def display_on_streamlit(html: str):
    import streamlit.components.v1 as components
    components.html(html, height=1000, scrolling=True)


def display_html(
    html: Union[str, HTML, ipywidgets.Widget],
    *,
    slot_id: str = None
):
    """Judge the presentation method to be used based on the context

    Args:
        - html (str): html string to display.
        - env: (Literal['Widgets' | 'Streamlit' | 'Jupyter'], optional): The enviroment using pygwalker
        *
        - slot_id(str): display with given id.
    """
    widget = HTML(html) if isinstance(html, str) else html
    if slot_id is None:
        display(widget)
    else:
        handler = DISPLAY_HANDLER.get(slot_id)
        if handler is None:
            handler = display(widget, display_id=slot_id)
            DISPLAY_HANDLER[slot_id] = handler
        else:
            handler.update(widget)
