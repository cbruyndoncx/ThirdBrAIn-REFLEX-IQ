Project Path: components

Source Tree:

```
components
├── html_to_reflex.md
├── conditional_rendering.md
├── props.md
├── rendering_iterables.md
└── conditional_props.md

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/components/html_to_reflex.md`:

```md
# Convert HTML to Reflex


To convert HTML to Reflex code use this live converter tool: https://flexgen.reflex.run/reverse-compiler/

## Convert Figma file to Reflex

Check out this [Notion doc](https://www.notion.so/reflex-dev/Convert-HTML-to-Reflex-fe22d0641dcd4d5c91c8404ca41c7e77) for a walk through on how to convert a Figma file into Reflex code.
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/components/conditional_rendering.md`:

```md

# Conditional Rendering

Recall from the [basics]({docs.getting_started.basics.path}) that we cannot use Python `if/else` statements when referencing state vars in Reflex. Instead, use the `rx.cond` component to conditionally render components or set props based on the value of a state var.

```md video https://youtube.com/embed/ITOZkzjtjUA?start=6040&end=6463
# Video: Conditional Rendering
```

```md alert
# Check out the API reference for [cond docs]({library.dynamic_rendering.cond.path}).
```

```python eval
rx.box(height="2em")
```

Below is a simple example showing how to toggle between two text components by checking the value of the state var `show`.

```python demo exec
class CondSimpleState(rx.State):
    show: bool = True

    @rx.event
    def change(self):
        self.show = not (self.show)


def cond_simple_example():
    return rx.vstack(
        rx.button("Toggle", on_click=CondSimpleState.change),
        rx.cond(
            CondSimpleState.show,
            rx.text("Text 1", color="blue"),
            rx.text("Text 2", color="red"),
        ),
    )
```

If `show` is `True` then the first component is rendered (in this case the blue text). Otherwise the second component is rendered (in this case the red text).

## Conditional Props

You can also set props conditionally using `rx.cond`. In this example, we set the `color` prop of a text component based on the value of the state var `show`.

```python demo exec
class PropCondState(rx.State):

    value: int
    
    @rx.event
    def set_end(self, value: list[int]):
        self.value = value[0]


def cond_prop():
    return rx.slider(
        default_value=[50],
        on_value_commit=PropCondState.set_end,
        color_scheme=rx.cond(PropCondState.value > 50, "green", "pink"),
        width="100%",
    )
```


## Var Operations

You can use [var operations]({docs.vars.var_operations.path}) with the `cond` component for more complex conditions. See the full [cond reference]({library.dynamic_rendering.cond.path}) for more details.


## Multiple Conditional Statements

The [`rx.match`]({library.dynamic_rendering.match.path}) component in Reflex provides a powerful alternative to`rx.cond` for handling multiple conditional statements and structural pattern matching. This component allows you to handle multiple conditions and their associated components in a cleaner and more readable way compared to nested `rx.cond` structures.

```python demo exec
from typing import List

import reflex as rx


class MatchState(rx.State):
    cat_breed: str = ""
    animal_options: List[str] = [
        "persian",
        "siamese",
        "maine coon",
        "ragdoll",
        "pug",
        "corgi",
    ]


def match_demo():
    return rx.flex(
        rx.match(
            MatchState.cat_breed,
            ("persian", rx.text("Persian cat selected.")),
            ("siamese", rx.text("Siamese cat selected.")),
            (
                "maine coon",
                rx.text("Maine Coon cat selected."),
            ),
            ("ragdoll", rx.text("Ragdoll cat selected.")),
            rx.text("Unknown cat breed selected."),
        ),
        rx.select(
            [
                "persian",
                "siamese",
                "maine coon",
                "ragdoll",
                "pug",
                "corgi",
            ],
            value=MatchState.cat_breed,
            on_change=MatchState.set_cat_breed,
        ),
        direction="column",
        gap="2",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/components/props.md`:

```md

# Props

Props modify the behavior and appearance of a component. They are passed in as keyword arguments to a component.

## Component Props

There are props that are shared between all components, but each component can also define its own props.

For example, the `rx.image` component has a `src` prop that specifies the URL of the image to display and an `alt` prop that specifies the alternate text for the image.

```python demo
rx.image(
    src="https://reflex.dev/logo.jpg",
    alt="Reflex Logo",
)
```

Check the docs for the component you are using to see what props are available and how they affect the component (see the `rx.image` [reference]({docs.library.media.image.path}#api-reference) page for example).


## Common Props

Components support many standard HTML properties as props. For example: the HTML [id]({"https://www.w3schools.com/html/html_id.asp"}) property is exposed directly as the prop `id`. The HTML [className]({"https://www.w3schools.com/jsref/prop_html_classname.asp"}) property is exposed as the prop `class_name` (note the Pythonic snake_casing!).

```python demo
rx.box(
    "Hello World",
    id="box-id",
    class_name=["class-name-1", "class-name-2",],
)
```

In the example above, the `class_name` prop of the `rx.box` component is assigned a list of class names. This means the `rx.box` component will be styled with the CSS classes `class-name-1` and `class-name-2`.

## Style Props

In addition to component-specific props, most built-in components support a full range of style props. You can use any [CSS property](https://www.w3schools.com/cssref/index.php) to style a component.

```python demo
rx.button(
    "Fancy Button",
    border_radius="1em",
    box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
    background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
    box_sizing="border-box",
    color="white",
    opacity= 1,
)
```

See the [styling docs]({docs.styling.overview.path}) to learn more about customizing the appearance of your app.


## Binding Props to State

```md alert warning
# Optional: Learn all about [State]({docs.state.overview.path}) first.
```

Reflex apps define [State]({docs.state.overview.path}) classes that hold variables that can change over time.

State may be modified in response to things like user input like clicking a button, or in response to events like loading a page.

State vars can be bound to component props, so that the UI always reflects the current state of the app.

Try clicking the badge below to change its color.

```python demo exec
class PropExampleState(rx.State):
    text: str = "Hello World"
    color: str = "red"

    @rx.event
    def flip_color(self):
        if self.color == "red":
            self.color = "blue"
        else:
            self.color = "red"


def index():
    return rx.button(
        PropExampleState.text,
        color_scheme=PropExampleState.color,
        on_click=PropExampleState.flip_color,
    )
```

In this example, the `color_scheme` prop is bound to the `color` state var.

When the `flip_color` event handler is called, the `color` var is updated, and the `color_scheme` prop is updated to match.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/components/rendering_iterables.md`:

```md

# Rendering Iterables

Recall again from the [basics]({docs.getting_started.basics.path}) that we cannot use Python `for` loops when referencing state vars in Reflex. Instead, use the `rx.foreach` component to render components from a collection of data.

```python demo exec
class IterState(rx.State):
    color: list[str] = [
        "red",
        "green",
        "blue",
    ]


def colored_box(color: str):
    return rx.button(color, background_color=color)


def dynamic_buttons():
    return rx.vstack(
        rx.foreach(IterState.color, colored_box),
    )

```

Here's the same example using a lambda function.

```python
def dynamic_buttons():
    return rx.vstack(
        rx.foreach(IterState.color, lambda color: colored_box(color)),
    )
```

You can also use lambda functions directly with components without defining a separate function.

```python
def dynamic_buttons():
    return rx.vstack(
        rx.foreach(IterState.color, lambda color: rx.button(color, background_color=color)),
    )
```

In this first simple example we iterate through a `list` of colors and render a dynamic number of buttons.

The first argument of the `rx.foreach` function is the state var that you want to iterate through. The second argument is a function that takes in an item from the data and returns a component. In this case, the `colored_box` function takes in a color and returns a button with that color.

## For vs Foreach

```md definition
# Regular For Loop
* Use when iterating over constants.

# Foreach
* Use when iterating over state vars.
```

The above example could have been written using a regular Python `for` loop, since the data is constant.

```python demo exec
colors = ["red", "green", "blue"]
def dynamic_buttons_for():
    return rx.vstack(
        [colored_box(color) for color in colors],
    )
```

However, as soon as you need the data to be dynamic, you must use `rx.foreach`.

```python demo exec
class DynamicIterState(rx.State):
    color: list[str] = [
        "red",
        "green",
        "blue",
    ]

    def add_color(self, form_data):
        self.color.append(form_data["color"])

def dynamic_buttons_foreach():
    return rx.vstack(
        rx.foreach(DynamicIterState.color, colored_box),
        rx.form(
            rx.input(name="color", placeholder="Add a color"),
            rx.button("Add"),
            on_submit=DynamicIterState.add_color,
        )
    )
```

## Render Function

The function to render each item can be defined either as a separate function or as a lambda function. In the example below, we define the function `colored_box` separately and pass it to the `rx.foreach` function. 

```python demo exec
class IterState2(rx.State):
    color: list[str] = [
        "red",
        "green",
        "blue",
    ]

def colored_box(color: rx.Var[str]):
    return rx.button(color, background_color=color)

def dynamic_buttons2():
    return rx.vstack(
        rx.foreach(IterState2.color, colored_box),
    )

```

Notice that the type annotation for the `color` parameter in the `colored_box` function is `rx.Var[str]` (rather than just `str`). This is because the `rx.foreach` function passes the item as a `Var` object, which is a wrapper around the actual value. This is what allows us to compile the frontend without knowing the actual value of the state var (which is only known at runtime).

## Enumerating Iterables

The function can also take an index as a second argument, meaning that we can enumerate through data as shown in the example below.

```python demo exec
class IterIndexState(rx.State):
    color: list[str] = [
        "red",
        "green",
        "blue",
    ]


def create_button(color: rx.Var[str], index: int):
    return rx.box(
        rx.button(f"{index + 1}. {color}"),
        padding_y="0.5em",
    )

def enumerate_foreach():
    return rx.vstack(
        rx.foreach(
            IterIndexState.color,
            create_button
        ),
    )
```

Here's the same example using a lambda function.

```python
def enumerate_foreach():
    return rx.vstack(
        rx.foreach(
            IterIndexState.color,
            lambda color, index: create_button(color, index)
        ),
    )
```

## Iterating Dictionaries

We can iterate through a `dict` using a `foreach`. When the dict is passed through to the function that renders each item, it is presented as a list of key-value pairs `[("sky", "blue"), ("balloon", "red"), ("grass", "green")]`.

```python demo exec
class SimpleDictIterState(rx.State):
    color_chart: dict[str, str] = {
        "sky": "blue",
        "balloon": "red",
        "grass": "green",
    }


def display_color(color: list):
    # color is presented as a list key-value pairs [("sky", "blue"), ("balloon", "red"), ("grass", "green")]
    return rx.box(rx.text(color[0]), bg=color[1], padding_x="1.5em")


def dict_foreach():
    return rx.grid(
        rx.foreach(
            SimpleDictIterState.color_chart,
            display_color,
        ),
        columns="3",
    )

```

```md alert warning
# Dict Type Annotation.
It is essential to provide the correct full type annotation for the dictionary in the state definition (e.g., `dict[str, str]` instead of `dict`) to ensure `rx.foreach` works as expected. Proper typing allows Reflex to infer and validate the structure of the data during rendering.
```

## Nested examples

`rx.foreach` can be used with nested state vars. Here we use nested `foreach` components to render the nested state vars. The `rx.foreach(project["technologies"], get_badge)` inside of the `project_item` function, renders the `dict` values which are of type `list`. The `rx.box(rx.foreach(NestedStateFE.projects, project_item))` inside of the `projects_example` function renders each `dict` inside of the overall state var `projects`.

```python demo exec
class NestedStateFE(rx.State):
    projects: list[dict[str, list]] = [
        {
            "technologies": ["Next.js", "Prisma", "Tailwind", "Google Cloud", "Docker", "MySQL"]
        },
        {
            "technologies": ["Python", "Flask", "Google Cloud", "Docker"]
        }
    ]

def get_badge(technology: rx.Var[str]) -> rx.Component:
    return rx.badge(technology, variant="soft", color_scheme="green")

def project_item(project: rx.Var[dict[str, list]]) -> rx.Component:
    return rx.box(
        rx.hstack(            
            rx.foreach(project["technologies"], get_badge)
        ),
    )

def projects_example() -> rx.Component:
    return rx.box(rx.foreach(NestedStateFE.projects, project_item))
```

If you want an example where not all of the values in the dict are the same type then check out the example on [var operations using foreach]({docs.vars.var_operations.path}).

Here is a further example of how to use `foreach` with a nested data structure.

```python demo exec
class NestedDictIterState(rx.State):
    color_chart: dict[str, list[str]] = {
        "purple": ["red", "blue"],
        "orange": ["yellow", "red"],
        "green": ["blue", "yellow"],
    }


def display_colors(color: rx.Var[tuple[str, list[str]]]):
    return rx.vstack(
        rx.text(color[0], color=color[0]),
        rx.hstack(
            rx.foreach(
                color[1],
                lambda x: rx.box(
                    rx.text(x, color="black"), bg=x
                ),
            )
        ),
    )


def nested_dict_foreach():
    return rx.grid(
        rx.foreach(
            NestedDictIterState.color_chart,
            display_colors,
        ),
        columns="3",
    )

```

## Foreach with Cond

We can also use `foreach` with the `cond` component.

In this example we define the function `render_item`. This function takes in an `item`, uses the `cond` to check if the item `is_packed`. If it is packed it returns the `item_name` with a `✔` next to it, and if not then it just returns the `item_name`. We use the `foreach` to iterate over all of the items in the `to_do_list` using the `render_item` function.

```python demo exec
import dataclasses

@dataclasses.dataclass
class ToDoListItem:
    item_name: str
    is_packed: bool

class ForeachCondState(rx.State):
    to_do_list: list[ToDoListItem] = [
        ToDoListItem(item_name="Space suit", is_packed=True), 
        ToDoListItem(item_name="Helmet", is_packed=True),
        ToDoListItem(item_name="Back Pack", is_packed=False),
        ]


def render_item(item: rx.Var[ToDoListItem]):
    return rx.cond(
        item.is_packed, 
        rx.list.item(item.item_name + ' ✔'),
        rx.list.item(item.item_name),
    )

def packing_list():
    return rx.vstack(
        rx.text("Sammy's Packing List"),
        rx.list(rx.foreach(ForeachCondState.to_do_list, render_item)),
    )

```

```