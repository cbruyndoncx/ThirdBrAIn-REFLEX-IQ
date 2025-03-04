Project Path: datatable_tutorial

Source Tree:

```
datatable_tutorial
├── simple_table.md
├── __init__.py
├── live_stream.md
├── add_interactivity.md
├── add_styling.md
└── datatable_tutorial_utils.py

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/datatable_tutorial/simple_table.md`:

```md

# Data Table (Editable) Tutorial

```md alert info
#There is another [datatable component]({library.tables_and_data_grids.data_table.path}), which is only used for displaying data and does not support user interactivity or editing.
```

```python eval
rx.box(height="2em")
```

We need to start by defining our columns that describe the shape of our data. The column var should be typed as a `list` of `dict` (`list[dict]`), where each item describes the attributes of a single column in the table.

Each column dict recognizes the keys below:

1. `title`: The text to display in the header of the column
2. `id`: An id for the column, if not defined, will default to a lower case of title
3. `width`: The width of the column (in pixels)
4. `type`: The type of the columns, default to "str"

Below we define `DataTableState` with columns definitions in the `cols` var, and data about Harry Potter characters in the `data` var..

```python
class DataTableState(rx.State):
    """The app state."""
    cols: list[dict] = [
        {\"title": "Title", "type": "str"},
        {
            "title": "Name",
            "type": "str",
            "width": 300,
        },
        {
            "title": "Birth",
            "type": "str",
            "width": 150,
        },
        {
            "title": "Human",
            "type": "bool",
            "width": 80,
        },
        {
            "title": "House",
            "type": "str",
        },
        {
            "title": "Wand",
            "type": "str",
            "width": 250,
        },
        {
            "title": "Patronus",
            "type": "str",
        },
        {
            "title": "Blood status",
            "type": "str",
            "width": 200,
        },
    ]
    data = [
        ["1", "Harry James Potter", "31 July 1980", True, "Gryffindor", "11'  Holly  phoenix feather", "Stag", "Half-blood"],
        ["2", "Ronald Bilius Weasley", "1 March 1980", True,"Gryffindor", "12' Ash unicorn tail hair", "Jack Russell terrier", "Pure-blood"],
        ["3", "Hermione Jean Granger", "19 September, 1979", True, "Gryffindor", "10¾'  vine wood dragon heartstring", "Otter", "Muggle-born"], 
        ["4", "Albus Percival Wulfric Brian Dumbledore", "Late August 1881", True, "Gryffindor", "15' Elder Thestral tail hair core", "Phoenix", "Half-blood"], 
        ["5", "Rubeus Hagrid", "6 December 1928", False, "Gryffindor", "16'  Oak unknown core", "None", "Part-Human (Half-giant)"], 
        ["6", "Fred Weasley", "1 April, 1978", True, "Gryffindor", "Unknown", "Unknown", "Pure-blood"], 
        ["7", "George Weasley", "1 April, 1978", True, "Gryffindor", "Unknown", "Unknown", "Pure-blood"],
    ]
```

We then define a basic table by passing the previously defined state vars as props `columns` and `data` to the `rx.data_editor()` component,

```python demo
rx.data_editor(
    columns=DataTableState.cols,
    data=DataTableState.data,
)
```

This is enough to display the data, but there is no way to interact with it. On the next page we will explore how to add interactivity to our datatable.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/datatable_tutorial/live_stream.md`:

```md

# Live Streaming example

Lastly let's add in an API so we can live stream data into our datatable.

Here we use a [Background Task]({events.background_events.path}) to stream the data into the table without blocking UI interactivity. We call an advice API using `httpx` and then append that data to the `self.table_data` state var. We also create a button that allows us to start and pause the streaming of the data by changing the value of the boolean state var `running` using the event handler `toggle_pause`. If the `running` state var is set to `True` we stream the API data, when it is set to `False` we break out of the `while` loop and end the background event.

```python
class DataTableLiveState(BaseState):
    "The app state."

    running: bool = False
    table_data: list[dict[str, Any]] = []
    rate: int = 0.4
    columns: list[dict[str, str]] = [
        {
            "title": "id",
            "id": "v1",
            "type": "int",
            "width": 100,
        },
        {
            "title": "advice",
            "id": "v2",
            "type": "str",
            "width": 750,
        },

    ]

    @rx.event(background=True)
    async def live_stream(self):
        while True:
            await asyncio.sleep(1 / self.rate)
            if not self.running:
                break

            async with self:
                if len(self.table_data) > 50:
                    self.table_data.pop(0)

                res = httpx.get('https://api.adviceslip.com/advice')
                data = res.json()
                self.table_data.append(\{"v1": data["slip"]["id"], "v2": data["slip"]["advice"]})

    @rx.event
    def toggle_pause(self):
        self.running = not self.running
        if self.running:
            return DataTableLiveState.live_stream
```

```python demo
rx.vstack(
    rx.stack(
        rx.cond(
            ~DataTableLiveState.running,
            rx.button("Start", on_click=DataTableLiveState.toggle_pause, color_scheme='green'),
            rx.button("Pause", on_click=DataTableLiveState.toggle_pause, color_scheme='red'),
        ),
    ),
    rx.data_editor(
        columns=DataTableLiveState.columns,
        data=DataTableLiveState.table_data,
        draw_focus_ring=True,
        row_height=50,
        smooth_scroll_x=True,
        smooth_scroll_y=True,
        column_select="single",
        # style
        theme=darkTheme,
        ),
    overflow_x="auto",
    width="100%",
    height="30vh",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/datatable_tutorial/add_interactivity.md`:

```md

# Adding Interactivity to our DataTable

Now we will add interactivity to our datatable. We do this using event handlers and event triggers.

The first example implements a handler for the `on_cell_clicked` event trigger, which is called when the user clicks on a cell of the data editor. The event trigger receives the coordinates of the cell.

```python
class DataTableState(rx.State):
    clicked_cell: str = "Cell clicked: "

    ...

    @rx.event
    def get_clicked_data(self, pos: tuple[int, int]) -> str:
        self.clicked_cell = f"Cell clicked: \{pos}"

```

The state has a var called `clicked_cell` that will store a message about which cell was clicked. We define an event handler `get_clicked_data` that updates the value of the `clicked_cell` var when it is called. In essence, we have clicked on a cell, called the `on_cell_clicked` event trigger which calls the `get_clicked_data` event handler, which updates the `clicked_cell` var.

```python demo
rx.text(DataTableState.clicked_cell)
```

```python demo
rx.data_editor(
    columns=DataTableState.cols,
    data=DataTableState.data,
    on_cell_clicked=DataTableState.get_clicked_data,
)
```

The event handler `on_cell_context_menu` can be used in the same way as `on_cell_clicked`, except here the event trigger is called when the user right clicks, i.e. when the cell should show a context menu.

## Editing cells

Another important type of interactivity we will showcase is how to edit cells. Here we use the `on_cell_edited` event trigger to update the data based on what the user entered.

```python
class DataTableState(rx.State):
    clicked_cell: str = "Cell clicked: "
    edited_cell: str = "Cell edited: "

    ...


    @rx.event
    def get_clicked_data(self, pos):
        self.clicked_cell = f"Cell clicked: \{pos}"

    @rx.event
    def get_edited_data(self, pos, val):
        col, row = pos
        self.data[row][col] = val["data"]
        self.edited_cell = f"Cell edited: \{pos}, Cell value: \{val["data"]}"

```

The `on_cell_edited` event trigger is called when the user modifies the content of a cell. It receives the coordinates of the cell and the modified content. We pass these into the `get_edited_data` event handler and use them to update the `data` state var at the appropriate position. We then update the `edited_cell` var value.

```python demo
rx.text(DataTableState.edited_cell)
```

```python demo
rx.data_editor(
    columns=DataTableState.cols,
    data=DataTableState.data,
    on_cell_clicked=DataTableState.get_clicked_data,
    on_cell_edited=DataTableState.get_edited_data,
)
```

## Group Header

We can define group headers which are headers that encompass a group of columns. We define these in the `columns` using the `group` property such as `"group": "Data"`. The `columns` would now be defined as below. Only the `Title` does not fall under a group header, all the rest fall under the `Data` group header.

```python
class DataTableState2(rx.State):
    """The app state."""

    ...

    cols: list[dict] = [
        {\"title": "Title", "type": "str"},
        {
            "title": "Name",
            "type": "str",
            "group": "Data",
            "width": 300,
        },
        {
            "title": "Birth",
            "type": "str",
            "group": "Data",
            "width": 150,
        },
        {
            "title": "Human",
            "type": "bool",
            "group": "Data",
            "width": 80,
        },
        {
            "title": "House",
            "type": "str",
            "group": "Data",
        },
        {
            "title": "Wand",
            "type": "str",
            "group": "Data",
            "width": 250,
        },
        {
            "title": "Patronus",
            "type": "str",
            "group": "Data",
        },
        {
            "title": "Blood status",
            "type": "str",
            "group": "Data",
            "width": 200,
        },
    ]

    ...
```

The table now has a header as below.

```python demo
rx.data_editor(
    columns=DataTableState2.cols,
    data=DataTableState2.data,
    on_cell_clicked=DataTableState2.get_clicked_data,
    on_cell_edited=DataTableState2.get_edited_data,
)
```

There are several event triggers we can apply to the group header.

```python
class DataTableState2(rx.State):
    """The app state."""

    right_clicked_group_header : str = "Group header right clicked: "

    ...

    @rx.event
    def get_group_header_right_click(self, index, val):
        self.right_clicked_group_header = f"Group header right clicked at index: \{index}, Group header value: \{val['group']}"

```

```python demo
rx.text(DataTableState2.right_clicked_group_header)
```

```python demo
rx.data_editor(
    columns=DataTableState2.cols,
    data=DataTableState2.data,
    on_cell_clicked=DataTableState2.get_clicked_data,
    on_cell_edited=DataTableState2.get_edited_data,
    on_group_header_context_menu=DataTableState2.get_group_header_right_click,
)
```

In this example we use the `on_group_header_context_menu` event trigger which is called when the user right-clicks on a group header. It returns the `index` and the `data` of the group header. We can also use the `on_group_header_clicked` and `on_group_header_renamed` event triggers which are called when the user left-clicks on a group header and when a user renames a group header respectively.

## More Event Triggers

There are several other event triggers that are worth exploring. The `on_item_hovered` event trigger is called whenever the user hovers over an item in the datatable. The `on_delete` event trigger is called when the user deletes a cell from the datatable.

The final event trigger to check out is `on_column_resize`. `on_column_resize` allows us to respond to the user dragging the handle between columns. The event trigger returns the `col` we are adjusting and the new `width` we have defined. The `col` that is returned is a dictionary for example: `\{'title': 'Name', 'type': 'str', 'group': 'Data', 'width': 198, 'pos': 1}`. We then index into `self.cols` defined in our state and change the `width` of that column using this code: `self.cols[col['pos']]['width'] = width`.

```python
class DataTableState2(rx.State):
    """The app state."""

    ...

    item_hovered: str = "Item Hovered: "
    deleted: str = "Deleted: "

    ...


    @rx.event
    def get_item_hovered(self, pos):
        self.item_hovered = f"Item Hovered type: \{pos['kind']}, Location: \{pos['location']}"

    @rx.event
    def get_deleted_item(self, selection):
        self.deleted = f"Deleted cell: \{selection['current']['cell']}"

    @rx.event
    def column_resize(self, col, width):
        self.cols[col['pos']]['width'] = width
```

```python demo
rx.text(DataTableState2.item_hovered)
```

```python demo
rx.text(DataTableState2.deleted)
```

```python demo
rx.data_editor(
    columns=DataTableState2.cols,
    data=DataTableState2.data,
    on_cell_clicked=DataTableState2.get_clicked_data,
    on_cell_edited=DataTableState2.get_edited_data,
    on_group_header_context_menu=DataTableState2.get_group_header_right_click,
    on_item_hovered=DataTableState2.get_item_hovered,
    on_delete=DataTableState2.get_deleted_item,
    on_column_resize=DataTableState2.column_resize,
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/datatable_tutorial/add_styling.md`:

```md

# DataTable Styling

There are props that we can explore to ensure the datatable is shaped correctly and reacts in the way we expect. We can set `on_paste` to `True`, which allows us to paste directly into a cell. We can use `draw_focus_ring` to draw a ring around the cells when selected, this defaults to `True` so can be turned off if we do not want it. The `rows` prop can be used to hard code the number of rows that we show.

`freeze_columns` is used to keep a certain number of the left hand columns frozen when scrolling horizontally. `group_header_height` and `header_height` define the height of the group header and the individual headers respectively. `max_column_width` and `min_column_width` define how large or small the columns are allowed to be with the manual column resizing. We can also define the `row_height` to make the rows more nicely spaced.

We can add `row_markers`, which appear on the furthest left side of the table. They can take values of `'none', 'number', 'checkbox', 'both', 'clickable-number'`. We can set `smooth_scroll_x` and `smooth_scroll_y`, which allows us to smoothly scroll along the columns and rows.

By default there is a `vertical_border` between the columns, we can turn it off by setting this prop to `False`. We can define how many columns a user can select at a time by setting the `column_select` prop. It can take values of `"none", "single", "multi"`.

We can allow `overscroll_x`, which allows users to scroll past the limit of the actual horizontal content. There is an equivalent `overscroll_y`.

Check out [these docs]({library.tables_and_data_grids.data_editor.path}) for more information on these props.

```python demo
rx.data_editor(
    columns=DataTableState2.cols,
    data=DataTableState2.data,

    #rows=4,
    on_paste=True,
    draw_focus_ring=False,
    freeze_columns=2,
    group_header_height=50,
    header_height=60,
    max_column_width=300,
    min_column_width=100,
    row_height=50,
    row_markers='clickable-number',
    smooth_scroll_x=True,
    vertical_border=False,
    column_select="multi",
    overscroll_x=100,


    on_cell_clicked=DataTableState2.get_clicked_data,
    on_cell_edited=DataTableState2.get_edited_data,
    on_group_header_context_menu=DataTableState2.get_group_header_right_click,
    on_item_hovered=DataTableState2.get_item_hovered,
    on_delete=DataTableState2.get_deleted_item,
    on_column_resize=DataTableState2.column_resize,
)
```

## Theming

Lastly there is a `theme` prop that allows us to pass in all color and font information for the data table.

```python
darkTheme = {
    "accentColor": "#8c96ff",
    "accentLight": "rgba(202, 206, 255, 0.253)",
    "textDark": "#ffffff",
    "textMedium": "#b8b8b8",
    "textLight": "#a0a0a0",
    "textBubble": "#ffffff",
    "bgIconHeader": "#b8b8b8",
    "fgIconHeader": "#000000",
    "textHeader": "#a1a1a1",
    "textHeaderSelected": "#000000",
    "bgCell": "#16161b",
    "bgCellMedium": "#202027",
    "bgHeader": "#212121",
    "bgHeaderHasFocus": "#474747",
    "bgHeaderHovered": "#404040",
    "bgBubble": "#212121",
    "bgBubbleSelected": "#000000",
    "bgSearchResult": "#423c24",
    "borderColor": "rgba(225,225,225,0.2)",
    "drilldownBorder": "rgba(225,225,225,0.4)",
    "linkColor": "#4F5DFF",
    "headerFontStyle": "bold 14px",
    "baseFontStyle": "13px",
    "fontFamily": "Inter, Roboto, -apple-system, BlinkMacSystemFont, avenir next, avenir, segoe ui, helvetica neue, helvetica, Ubuntu, noto, arial, sans-serif",
}
```


```python demo
rx.data_editor(
    columns=DataTableState2.cols,
    data=DataTableState2.data,

    on_paste=True,
    draw_focus_ring=False,
    freeze_columns=2,
    group_header_height=50,
    header_height=60,
    max_column_width=300,
    min_column_width=100,
    row_height=50,
    row_markers='clickable-number',
    smooth_scroll_x=True,
    vertical_border=False,
    column_select="multi",
    overscroll_x=100,
    theme=darkTheme,


    on_cell_clicked=DataTableState2.get_clicked_data,
    on_cell_edited=DataTableState2.get_edited_data,
    on_group_header_context_menu=DataTableState2.get_group_header_right_click,
    on_item_hovered=DataTableState2.get_item_hovered,
    on_delete=DataTableState2.get_deleted_item,
    on_column_resize=DataTableState2.column_resize,
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/datatable_tutorial/datatable_tutorial_utils.py`:

```py
from __future__ import annotations

import asyncio
from typing import Any

import httpx
import reflex as rx


class DataTableState(rx.State):
    """The app state."""

    clicked_cell: str = "Cell clicked: "
    edited_cell: str = "Cell edited: "

    cols: list[dict] = [
        {"title": "Title", "type": "str"},
        {
            "title": "Name",
            "type": "str",
            "width": 300,
        },
        {
            "title": "Birth",
            "type": "str",
            "width": 150,
        },
        {
            "title": "Human",
            "type": "bool",
            "width": 80,
        },
        {
            "title": "House",
            "type": "str",
        },
        {
            "title": "Wand",
            "type": "str",
            "width": 250,
        },
        {
            "title": "Patronus",
            "type": "str",
        },
        {
            "title": "Blood status",
            "type": "str",
            "width": 200,
        },
    ]

    data = [
        [
            "1",
            "Harry James Potter",
            "31 July 1980",
            True,
            "Gryffindor",
            "11'  Holly  phoenix feather",
            "Stag",
            "Half-blood",
        ],
        [
            "2",
            "Ronald Bilius Weasley",
            "1 March 1980",
            True,
            "Gryffindor",
            "12' Ash unicorn tail hair",
            "Jack Russell terrier",
            "Pure-blood",
        ],
        [
            "3",
            "Hermione Jean Granger",
            "19 September, 1979",
            True,
            "Gryffindor",
            "10¾'  vine wood dragon heartstring",
            "Otter",
            "Muggle-born",
        ],
        [
            "4",
            "Albus Percival Wulfric Brian Dumbledore",
            "Late August 1881",
            True,
            "Gryffindor",
            "15' Elder Thestral tail hair core",
            "Phoenix",
            "Half-blood",
        ],
        [
            "5",
            "Rubeus Hagrid",
            "6 December 1928",
            False,
            "Gryffindor",
            "16'  Oak unknown core",
            "None",
            "Part-Human (Half-giant)",
        ],
        [
            "6",
            "Fred Weasley",
            "1 April, 1978",
            True,
            "Gryffindor",
            "Unknown",
            "Unknown",
            "Pure-blood",
        ],
        [
            "7",
            "George Weasley",
            "1 April, 1978",
            True,
            "Gryffindor",
            "Unknown",
            "Unknown",
            "Pure-blood",
        ],
    ]

    def get_clicked_data(self, pos) -> str:
        self.clicked_cell = f"Cell clicked: {pos}"

    def get_edited_data(self, pos, val) -> str:
        col, row = pos
        self.data[row][col] = val["data"]
        self.edited_cell = f"Cell edited: {pos}, Cell value: {val['data']}"


class DataTableState2(rx.State):
    """The app state."""

    clicked_cell: str = "Cell clicked: "
    edited_cell: str = "Cell edited: "
    right_clicked_group_header: str = "Group header right clicked: "
    item_hovered: str = "Item Hovered: "
    deleted: str = "Deleted: "

    cols: list[dict] = [
        {
            "title": "Title",
            "type": "str",
            "width": 100,
        },
        {
            "title": "Name",
            "type": "str",
            "group": "Data",
            "width": 200,
        },
        {
            "title": "Birth",
            "type": "str",
            "group": "Data",
            "width": 150,
        },
        {
            "title": "Human",
            "type": "bool",
            "group": "Data",
            "width": 80,
        },
        {
            "title": "House",
            "type": "str",
            "group": "Data",
        },
        {
            "title": "Wand",
            "type": "str",
            "group": "Data",
            "width": 250,
        },
        {
            "title": "Patronus",
            "type": "str",
            "group": "Data",
        },
        {
            "title": "Blood status",
            "type": "str",
            "group": "Data",
            "width": 200,
        },
    ]

    data = [
        [
            "1",
            "Harry James Potter",
            "31 July 1980",
            True,
            "Gryffindor",
            "11'  Holly  phoenix feather",
            "Stag",
            "Half-blood",
        ],
        [
            "2",
            "Ronald Bilius Weasley",
            "1 March 1980",
            True,
            "Gryffindor",
            "12' Ash unicorn tail hair",
            "Jack Russell terrier",
            "Pure-blood",
        ],
        [
            "3",
            "Hermione Jean Granger",
            "19 September, 1979",
            True,
            "Gryffindor",
            "10¾'  vine wood dragon heartstring",
            "Otter",
            "Muggle-born",
        ],
        [
            "4",
            "Albus Percival Wulfric Brian Dumbledore",
            "Late August 1881",
            True,
            "Gryffindor",
            "15' Elder Thestral tail hair core",
            "Phoenix",
            "Half-blood",
        ],
        [
            "5",
            "Rubeus Hagrid",
            "6 December 1928",
            False,
            "Gryffindor",
            "16'  Oak unknown core",
            "None",
            "Part-Human (Half-giant)",
        ],
        [
            "6",
            "Fred Weasley",
            "1 April, 1978",
            True,
            "Gryffindor",
            "Unknown",
            "Unknown",
            "Pure-blood",
        ],
        [
            "7",
            "George Weasley",
            "1 April, 1978",
            True,
            "Gryffindor",
            "Unknown",
            "Unknown",
            "Pure-blood",
        ],
    ]

    def get_clicked_data(self, pos) -> str:
        self.clicked_cell = f"Cell clicked: {pos}"

    def get_edited_data(self, pos, val) -> str:
        col, row = pos
        self.data[row][col] = val["data"]
        self.edited_cell = f"Cell edited: {pos}, Cell value: {val['data']}"

    def get_group_header_right_click(self, index, val) -> None:
        self.right_clicked_group_header = f"Group header right clicked at index: {index}, Group header value: {val['group']}"

    def get_item_hovered(self, pos) -> str:
        self.item_hovered = (
            f"Item Hovered type: {pos['kind']}, Location: {pos['location']}"
        )

    def get_deleted_item(self, selection) -> None:
        self.deleted = f"Deleted cell: {selection['current']['cell']}"

    def column_resize(self, col, width) -> None:
        self.cols[col["pos"]]["width"] = width


class DataTableLiveState(rx.State):
    """The app state."""

    running: bool = False
    table_data: list[dict[str, Any]] = []
    rate: int = 0.4
    columns: list[dict[str, str]] = [
        {
            "title": "id",
            "id": "v1",
            "type": "int",
            "width": 100,
        },
        {
            "title": "advice",
            "id": "v2",
            "type": "str",
            "width": 750,
        },
    ]

    @rx.event(background=True)
    async def live_stream(self) -> None:
        while True:
            await asyncio.sleep(1 / self.rate)
            if not self.running:
                break

            async with self:
                if len(self.table_data) > 50:
                    self.table_data.pop(0)

                res = httpx.get("https://api.adviceslip.com/advice")
                data = res.json()
                self.table_data.append(
                    {
                        "v1": data["slip"]["id"],
                        "v2": data["slip"]["advice"],
                    },
                )

    def toggle_pause(self):
        self.running = not self.running
        if self.running:
            return DataTableLiveState.live_stream

        return None

```