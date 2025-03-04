Project Path: getting_started

Source Tree:

```
getting_started
├── introduction.md
├── basics.md
├── chat_tutorial_utils.py
├── installation.md
├── dashboard_tutorial.md
├── chat_tutorial_style.py
├── chatapp_tutorial.md
└── project-structure.md

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/getting_started/introduction.md`:

```md

<!-- TODO how do we consistently rename page title? -->

# Introduction

**Reflex** is an open-source framework for quickly building beautiful, interactive web applications in **pure Python**.

## Goals

```md section
### Pure Python

Use Python for everything. Don't worry about learning a new language.

### Easy to Learn

Build and share your first app in minutes. No web development experience required.

### Full Flexibility

Remain as flexible as traditional web frameworks. Reflex is easy to use, yet allows for advanced use cases.

Build anything from small data science apps to large, multi-page websites. **This entire site was built and deployed with Reflex!**

### Batteries Included

No need to reach for a bunch of different tools. Reflex handles the user interface, server-side logic, and deployment of your app.
```

## An example: Make it count

Here, we go over a simple counter app that lets the user count up or down.


```python demo box id=counter
rx.hstack(
    rx.button(
        "Decrement",
        color_scheme="ruby",
        on_click=CounterExampleState.decrement,
    ),
    rx.heading(CounterExampleState.count, font_size="2em"),
    rx.button(
        "Increment",
        color_scheme="grass",
        on_click=CounterExampleState.increment,
    ),
    spacing="4",
)
```

Here is the full code for this example:

```python eval
tabs()
```

```python demo box
rx.box(
    rx._x.code_block(
        """import reflex as rx """,
        class_name="code-block !bg-transparent !border-none",
    ),
    rx._x.code_block(
        """class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1""",
        background=rx.cond(
            IntroTabsState.value == "tab2",
            "var(--c-violet-3) !important",
            "transparent",
        ),
        border=rx.cond(
            IntroTabsState.value == "tab2",
            "1px solid var(--c-violet-5)",
            "none !important"
        ),
        class_name="code-block",
    ),
    rx._x.code_block(
        """def index():
    return rx.hstack(
        rx.button(
            "Decrement",
            color_scheme="ruby",
            on_click=State.decrement,
        ),
        rx.heading(State.count, font_size="2em"),
        rx.button(
            "Increment",
            color_scheme="grass",
            on_click=State.increment,
        ),
        spacing="4",
    )""",
        border=rx.cond(
            IntroTabsState.value == "tab1",
            "1px solid var(--c-violet-5)",
            "none !important",
        ),
        background=rx.cond(
            IntroTabsState.value == "tab1",
            "var(--c-violet-3) !important",
            "transparent",
        ),
        class_name="code-block",
    ),
    rx._x.code_block(
        """app = rx.App()
app.add_page(index)""",
        background=rx.cond(
            IntroTabsState.value == "tab3",
            "var(--c-violet-3) !important",
            "transparent",
        ),
        border=rx.cond(
            IntroTabsState.value == "tab3",
            "1px solid var(--c-violet-5)",
            "none !important",
        ),
        class_name="code-block",
    ),
    class_name="w-full flex flex-col",
)
```

## The Structure of a Reflex App

Let's break this example down.

### Import

```python
import reflex as rx
```

We begin by importing the `reflex` package (aliased to `rx`). We reference Reflex objects as `rx.*` by convention.

### State

```python
class State(rx.State):
    count: int = 0
```

The state defines all the variables (called **[vars]({vars.base_vars.path})**) in an app that can change, as well as the functions (called **[event_handlers](#event-handlers)**) that change them.

Here our state has a single var, `count`, which holds the current value of the counter. We initialize it to `0`.

### Event Handlers

```python
def increment(self):
    self.count += 1

def decrement(self):
    self.count -= 1
```

Within the state, we define functions, called **event handlers**, that change the state vars.

Event handlers are the only way that we can modify the state in Reflex.
They can be called in response to user actions, such as clicking a button or typing in a text box.
These actions are called **events**.

Our counter app has two event handlers, `increment` and `decrement`.

### User Interface (UI)

```python
def index():
    return rx.hstack(
        rx.button(
            "Decrement",
            color_scheme="ruby",
            on_click=State.decrement,
        ),
        rx.heading(State.count, font_size="2em"),
        rx.button(
            "Increment",
            color_scheme="grass",
            on_click=State.increment,
        ),
        spacing="4",
    )
```

This function defines the app's user interface.

We use different components such as `rx.hstack`, `rx.button`, and `rx.heading` to build the frontend. Components can be nested to create complex layouts, and can be styled using the full power of CSS.

Reflex comes with [50+ built-in components]({library.path}) to help you get started.
We are actively adding more components. Also, it's easy to [wrap your own React components]({wrapping_react.overview.path}).

```python
rx.heading(State.count, font_size="2em"),
```

Components can reference the app's state vars.
The `rx.heading` component displays the current value of the counter by referencing `State.count`.
All components that reference state will reactively update whenever the state changes.

```python
rx.button(
    "Decrement",
    color_scheme="ruby",
    on_click=State.decrement,
),
```

Components interact with the state by binding events triggers to event handlers.
For example, `on_click` is an event that is triggered when a user clicks a component.

The first button in our app binds its `on_click` event to the `State.decrement` event handler. Similarly the second button binds `on_click` to `State.increment`.

In other words, the sequence goes like this:

- User clicks "increment" on the UI.
- `on_click` event is triggered.
- Event handler `State.increment` is called.
- `State.count` is incremented.
- UI updates to reflect the new value of `State.count`.

### Add pages

Next we define our app and add the counter component to the base route.

```python
app = rx.App()
app.add_page(index)
```

## Next Steps

🎉 And that's it!

We've created a simple, yet fully interactive web app in pure Python.

By continuing with our documentation, you will learn how to building awesome apps with Reflex.

For a glimpse of the possibilities, check out these resources:

* For a more real-world example, check out either the [dashboard tutorial]({getting_started.dashboard_tutorial.path}) or the [chatapp tutorial]({getting_started.chatapp_tutorial.path}).
* We have bots that can answer questions and generate Reflex code for you. Check them out in #ask-ai in our [Discord]({constants.DISCORD_URL})!
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/getting_started/basics.md`:

```md

# Reflex Basics

This page gives an introduction to the most common concepts that you will use to build Reflex apps.

```md section
# You will learn how to:

- Create and nest components
- Customize and style components
- Distinguish between compile-time and runtime
- Display data that changes over time
- Respond to events and update the screen
- Render conditions and lists
- Create pages and navigate between them
```

[Install]({docs.getting_started.installation.path}) `reflex` using pip.

```bash
pip install reflex
```

Import the `reflex` library to get started.

```python
import reflex as rx
```

## Creating and nesting components

[Components]({docs.ui.overview.path}) are the building blocks for your app's user interface (UI). They are the visual elements that make up your app, like buttons, text, and images. Reflex has a wide selection of [built-in components]({library.path}) to get you started quickly.

Components are created using functions that return a component object.

```python demo exec
def my_button():
    return rx.button("Click Me")
```

Components can be nested inside each other to create complex UIs.

To nest components as children, pass them as positional arguments to the parent component. In the example below, the `rx.text` and `my_button` components are children of the `rx.box` component.

```python demo exec
def my_page():
    return rx.box(
        rx.text("This is a page"),
        # Reference components defined in other functions.
        my_button()
    )
```

You can also use any base HTML element through the [`rx.el`]({docs.library.other.html.path}) namespace.

```python demo exec
def my_div():
    return rx.el.div(
        rx.el.p("Use base html!"),
    )
```

If you need a component not provided by Reflex, you can check the [3rd party ecosystem]({custom_components.path}) or [wrap your own React component]({docs.wrapping_react.guide.path}).

## Customizing and styling components

Components can be customized using [props]({docs.components.props.path}), which are passed in as keyword arguments to the component function.

Each component has props that are specific to that component. Check the docs for the component you are using to see what props are available.

```python demo exec
def half_filled_progress():
    return rx.progress(value=50)
```

In addition to component-specific props, components can also be styled using CSS properties passed as props.

```python demo exec
def round_button():
    return rx.button("Click Me", border_radius="15px", font_size="18px")
```

```md alert
Use the `snake_case` version of the CSS property name as the prop name.
```

See the [styling guide]({docs.styling.overview.path}) for more information on how to style components

In summary, components are made up of children and props.

```md definition
# Children

- Text or other Reflex components nested inside a component.
- Passed as **positional arguments**.

# Props

- Attributes that affect the behavior and appearance of a component.
- Passed as **keyword arguments**.
```

## Displaying data that changes over time

Apps need to store and display data that changes over time. Reflex handles this through [State]({docs.state.overview.path}), which is a Python class that stores variables that can change when the app is running, as well as the functions that can change those variables.

To define a state class, subclass `rx.State` and define fields that store the state of your app. The state variables ([vars]({docs.vars.base_vars.path})) should have a type annotation, and can be initialized with a default value.

```python
class MyState(rx.State):
    count: int = 0
```

### Referencing state vars in components

To reference a state var in a component, you can pass it as a child or prop. The component will automatically update when the state changes.

Vars are referenced through class attributes on your state class. For example, to reference the `count` var in a component, use `MyState.count`.

```python demo exec
class MyState(rx.State):
    count: int = 0
    color: str = "red"

def counter():
    return rx.hstack(
        # The heading `color` prop is set to the `color` var in MyState.
        rx.heading("Count: ", color=MyState.color),
        # The `count` var in `MyState` is passed as a child to the heading component.
        rx.heading(MyState.count),
    )
```

Vars can be referenced in multiple components, and will automatically update when the state changes.

## Responding to events and updating the screen

So far, we've defined state vars but we haven't shown how to change them. All state changes are handled through functions in the state class, called [event handlers]({docs.events.events_overview.path}).

```md alert
Event handlers are the ONLY way to change state in Reflex.
```

Components have special props, such as `on_click`, called event triggers that can be used to make components interactive. Event triggers connect components to event handlers, which update the state.

```python demo exec
class CounterState(rx.State):
    count: int = 0

    @rx.event
    def increment(self):
        self.count += 1

def counter_increment():
    return rx.hstack(
        rx.heading(CounterState.count),
        rx.button("Increment", on_click=CounterState.increment)
    )
```

When an event trigger is activated, the event handler is called, which updates the state. The UI is automatically re-rendered to reflect the new state. 


```md alert info
# What is the `@rx.event` decorator?
Adding the `@rx.event` decorator above the event handler is strongly recommended. This decorator enables proper static type checking, which ensures event handlers receive the correct number and types of arguments. This was introduced in Reflex version 0.6.5.
```

### Event handlers with arguments

Event handlers can also take in arguments. For example, the `increment` event handler can take an argument to increment the count by a specific amount.

```python demo exec
class CounterState2(rx.State):
    count: int = 0

    @rx.event
    def increment(self, amount: int):
        self.count += amount

def counter_variable():
    return rx.hstack(
        rx.heading(CounterState2.count),
        rx.button("Increment by 1", on_click=lambda: CounterState2.increment(1)),
        rx.button("Increment by 5", on_click=lambda: CounterState2.increment(5)),
    )
```

The `on_click` event trigger doesn't pass any arguments here, but some event triggers do. For example, the `on_blur` event trigger passes the text of an input as an argument to the event handler.

```python demo exec
class TextState(rx.State):
    text: str = ""

    @rx.event
    def update_text(self, new_text: str):
        self.text = new_text

def text_input():
    return rx.vstack(
        rx.heading(TextState.text),
        rx.input(default_value=TextState.text, on_blur=TextState.update_text),
    )
```

```md alert
Make sure that the event handler has the same number of arguments as the event trigger, or an error will be raised.
```

## Compile-time vs. runtime (IMPORTANT)

Before we dive deeper into state, it's important to understand the difference between compile-time and runtime in Reflex.

When you run your app, the frontend gets compiled to Javascript code that runs in the browser (compile-time). The backend stays in Python and runs on the server during the lifetime of the app (runtime).

### When can you not use pure Python?

We cannot compile arbitrary Python code, only the components that you define. What this means importantly is that you cannot use arbitrary Python operations and functions on state vars in components.

However, since any event handlers in your state are on the backend, you **can use any Python code or library** within your state.

### Examples that work

Within an event handler, use any Python code or library.

```python demo exec
def check_even(num: int):
    return num % 2 == 0

class MyState3(rx.State):
    count: int = 0
    text: str = "even"

    @rx.event
    def increment(self):
        # Use any Python code within state.
        # Even reference functions defined outside the state.
        if check_even(self.count):
            self.text = "even"
        else:
            self.text = "odd"
        self.count += 1

def count_and_check():
    return rx.box(
        rx.heading(MyState3.text),
        rx.button("Increment", on_click=MyState3.increment)
    )
```

Use any Python function within components, as long as it is defined at compile time (i.e. does not reference any state var)

```python demo exec
def show_numbers():
    return rx.vstack(
        *[
            rx.hstack(i, check_even(i))
            for i in range(10)
        ]
    )
```

### Examples that don't work

You cannot do an `if` statement on vars in components, since the value is not known at compile time.

```python
class BadState(rx.State):
    count: int = 0

def count_if_even():
    return rx.box(
        rx.heading("Count: "),
        # This will raise a compile error, as BadState.count is a var and not known at compile time.
        rx.text(BadState.count if BadState.count % 2 == 0 else "Odd"),
        # Using an if statement with a var as a prop will NOT work either.
        rx.text("hello", color="red" if BadState.count % 2 == 0 else "blue"),
    )
```

You cannot do a `for` loop over a list of vars.

```python
class BadState(rx.State):
    items: list[str] = ["Apple", "Banana", "Cherry"]

def loop_over_list():
    return rx.box(
        # This will raise a compile error, as BadState.items is a list and not known at compile time.
        *[rx.text(item) for item in BadState.items]
    )
```

You cannot do arbitrary Python operations on state vars in components.

```python
class BadTextState(rx.State):
    text: str = "Hello world"

def format_text():
    return rx.box(
        # Python operations such as `len` will not work on state vars.
        rx.text(len(BadTextState.text)),
    )
```

In the next sections, we will show how to handle these cases.

## Conditional rendering

As mentioned above, you cannot use Python `if/else` statements with state vars in components. Instead, use the [`rx.cond`]({docs.components.conditional_rendering.path}) function to conditionally render components.

```python demo exec
class LoginState(rx.State):
    logged_in: bool = False

    @rx.event
    def toggle_login(self):
        self.logged_in = not self.logged_in

def show_login():
    return rx.box(
        rx.cond(
            LoginState.logged_in,
            rx.heading("Logged In"),
            rx.heading("Not Logged In"),
        ),
        rx.button("Toggle Login", on_click=LoginState.toggle_login)
    )
```

## Rendering lists

To iterate over a var that is a list, use the [`rx.foreach`]({docs.components.rendering_iterables.path}) function to render a list of components.

Pass the list var and a function that returns a component as arguments to `rx.foreach`.

```python demo exec
class ListState(rx.State):
    items: list[str] = ["Apple", "Banana", "Cherry"]

def render_item(item: rx.Var[str]):
    """Render a single item."""
    # Note that item here is a Var, not a str!
    return rx.list.item(item)

def show_fruits():
    return rx.box(
        rx.foreach(ListState.items, render_item),
    )
```

The function that renders each item takes in a `Var`, since this will get compiled up front.

## Var Operations

You can't use arbitrary Python operations on state vars in components, but Reflex has [var operations]({docs.vars.var_operations.path}) that you can use to manipulate state vars.

For example, to check if a var is even, you can use the `%` and `==` var operations.

```python demo exec
class CountEvenState(rx.State):
    count: int = 0

    @rx.event
    def increment(self):
        self.count += 1

def count_if_even():
    return rx.box(
        rx.heading("Count: "),
        rx.cond(
            # Here we use the `%` and `==` var operations to check if the count is even.
            CountEvenState.count % 2 == 0,
            rx.text("Even"),
            rx.text("Odd"),
        ),
        rx.button("Increment", on_click=CountEvenState.increment),
    )
```

## App and Pages

Reflex apps are created by instantiating the `rx.App` class. Pages are linked to specific URL routes, and are created by defining a function that returns a component.

```python
def index():
    return rx.text('Root Page')

rx.app = rx.App()
app.add_page(index, route="/")
```

## Next Steps

Now that you have a basic understanding of how Reflex works, the next step is to start coding your own apps. Try one of the following tutorials:

- [Dashboard Tutorial]({getting_started.dashboard_tutorial.path})
- [Chatapp Tutorial]({getting_started.chatapp_tutorial.path})

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/getting_started/chat_tutorial_utils.py`:

```py
from __future__ import annotations

import os

import openai
import reflex as rx

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


class ChatappState(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self) -> None:
        # Our chatbot is not very smart right now...
        answer = "I don't know!"
        self.chat_history.append((self.question, answer))

    def answer2(self) -> None:
        # Our chatbot is not very smart right now...
        answer = "I don't know!"
        self.chat_history.append((self.question, answer))
        # Clear the question input.
        self.question = ""

    async def answer3(self):
        import asyncio

        # Our chatbot is not very smart right now...
        answer = "I don't know!"
        self.chat_history.append((self.question, ""))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        for i in range(len(answer)):
            await asyncio.sleep(0.1)
            self.chat_history[-1] = (self.chat_history[-1][0], answer[: i + 1])
            yield

    async def answer4(self):
        # Our chatbot has some brains now!
        client = openai.AsyncOpenAI(api_key=OPENAI_API_KEY)
        session = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": self.question}],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        # Add to the answer as the chatbot responds.
        answer = ""
        self.chat_history.append((self.question, answer))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        async for item in session:
            if hasattr(item.choices[0].delta, "content"):
                if item.choices[0].delta.content is None:
                    # presence of 'None' indicates the end of the response
                    break
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (self.chat_history[-1][0], answer)
                yield

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/getting_started/installation.md`:

```md

# Installation

Reflex requires Python 3.8+.


```md video https://youtube.com/embed/ITOZkzjtjUA?start=758&end=1206
# Video: Installation
```


## Virtual Environment

We **highly recommend** creating a virtual environment for your project.

[venv]({constants.VENV_URL}) is the standard option. [conda]({constants.CONDA_URL}) and [poetry]({constants.POETRY_URL}) are some alternatives.

# Install Reflex on your system

---md tabs

--tab macOS/Linux
## Install on macOS/Linux

We will go with [venv]({constants.VENV_URL}) here.


### Prerequisites
macOS (Apple Silicon) users should install [Rosetta 2](https://support.apple.com/en-us/HT211861). Run this command:
    
`/usr/sbin/softwareupdate --install-rosetta --agree-to-license`


### Create the project directory 

Replace `{app_name}` with your project name. Switch to the new directory.

```bash
mkdir {app_name}
cd {app_name}
```

### Setup virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```


```md alert info
# Getting `No module named venv`?

While Python typically ships with `venv` it is not installed by default on some systems.
If so, please install it manually. E.g. on Ubuntu Linux, run `sudo apt-get install python3-venv`.
```

### Install Reflex package

Reflex is available as a [pip]({constants.PIP_URL}) package.

```bash
pip install reflex
```

```md alert info
# Getting `command not found: pip`?

While Python typically ships with `pip` as the standard package management tool, it is not installed by default on some systems.
You may need to install it manually. E.g. on Ubuntu Linux, run `apt-get install python3-pip`
```

## Initialize the project

```bash
reflex init
```

```md alert warning
# Error `command not found: reflex` Mac / Linux
If you install Reflex with no virtual environment and get this error it means your `PATH` cannot find the reflex package. 
A virtual environment should solve this problem, or you can try running `python3 -m` before the reflex command.
```

--
--tab Windows
## Install on Windows

### Prerequisites
For Windows users, we recommend using [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/about) for optimal performance.

WSL users should refer to instructions for Linux above.

For the rest of this section we will work with native Windows (non-WSL).

We will go with [venv]({constants.VENV_URL}) here, for virtual environments.

### Create the project directory 

Replace `{app_name}` with your project name. Switch to the new directory.

```bash
mkdir {app_name}
cd {app_name}
```

### Setup virtual environment

```bash
py -3 -m venv .venv
.venv\\Scripts\\activate
```

### Install Reflex package

Reflex is available as a [pip](constants.PIP_URL) package.

```bash
pip install reflex
```

## Initialize the project

```bash
reflex init
```

```md alert warning
# Error `command not found: reflex` Windows

The Reflex framework includes the `reflex` command line (CLI) tool. Using a virtual environment is highly recommended for a seamless experience.",
```

```md alert warning
# Error `Install Failed - You are missing a DLL required to run bun.exe` Windows
Bun requires runtime components of Visual C++ libraries to run on windows. This issue is fixed by installing [Microsoft Visual C++ 2015 Redistributable](https://www.microsoft.com/en-us/download/details.aspx?id=53840).
```
--

---


The command will return four template options to choose from as shown below.

```bash
Initializing the web directory.

Get started with a template:
(0) blank (https://blank-template.reflex.run) - A minimal template
(1) dashboard (https://dashboard-new.reflex.run/) - A dashboard with tables and graphs
(2) sales (https://sales-new.reflex.run/) - An app to manage sales and customers
(3) ai_image_gen (https://ai-image-gen.reflex.run/) - An app to generate images using AI
(4) ci_template (https://cijob.reflex.run/) - A template for continuous integration
(5) api_admin_panel (https://api-admin-panel.reflex.run/) - An admin panel for an api.
(6) nba (https://nba-new.reflex.run/) - A data visualization app for NBA data.
(7) customer_data_app (https://customer-data-app.reflex.run/) - An app to manage customer data.
Which template would you like to use? (0): 
```

From here select a template. 


## Run the App

Run it in development mode:

```bash
reflex run
```

Your app runs at [http://localhost:3000](http://localhost:3000).

Reflex prints logs to the terminal. To increase log verbosity to help with debugging, use the `--loglevel` flag:

```bash
reflex run --loglevel debug
```

Reflex will *hot reload* any code changes in real time when running in development mode. Your code edits will show up on [http://localhost:3000](http://localhost:3000) automatically.
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/getting_started/dashboard_tutorial.md`:

```md

# Tutorial: Data Dashboard

During this tutorial you will build a small data dashboard, where you can input data and it will be rendered in table and a graph. This tutorial does not assume any existing Reflex knowledge, but we do recommend checking out the quick [Basics Guide]({docs.getting_started.basics.path}) first. 

The techniques you’ll learn in the tutorial are fundamental to building any Reflex app, and fully understanding it will give you a deep understanding of Reflex.


This tutorial is divided into several sections:

- **Setup for the Tutorial**: A starting point to follow the tutorial
- **Overview**: The fundamentals of Reflex UI (components and props)
- **Showing Dynamic Data**: How to use State to render data that will change in your app.
- **Add Data to your App**: Using a Form to let a user add data to your app and introduce event handlers.
- **Plotting Data in a Graph**: How to use Reflex's graphing components.
- **Final Cleanup and Conclusion**: How to further customize your app and add some extra styling to it.

### What are you building?

In this tutorial, you are building an interactive data dashboard with Reflex.

You can see what the finished app and code will look like here:



```python eval
rx.vstack(
        add_customer_button5(),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Gender"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    State5.users, show_user5
                ),
            ),
            variant="surface",
            size="3",
            width="100%",
        ),
        graph5(),
        align="center",
        width="100%",
        on_mouse_enter=State5.transform_data,
        border_width="2px",
        border_radius="10px",
        padding="1em",
    )
```

```python
import reflex as rx
from collections import Counter

class User(rx.Base):
    """The user model."""

    name: str
    email: str
    gender: str


class State(rx.State):
    users: list[User] = [
        User(name="Danilo Sousa", email="danilo@example.com", gender="Male"),
        User(name="Zahra Ambessa", email="zahra@example.com", gender="Female"),
    ]
    users_for_graph: list[dict] = []

    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))
        self.transform_data()
    
    def transform_data(self):
        """Transform user gender group data into a format suitable for visualization in graphs."""
        # Count users of each gender group
        gender_counts = Counter(user.gender for user in self.users)
        
        # Transform into list of dict so it can be used in the graph
        self.users_for_graph = [
            {
                "name": gender_group,
                "value": count
            }
            for gender_group, count in gender_counts.items()
        ]
        

def show_user(user: User):
    """Show a user in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
        style=\{"_hover": 
            \{"bg": rx.color("gray", 3)}
        },
        align="center",
    )

def add_customer_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Add User", size="4"),
            ),
        ),
        rx.dialog.content(
            rx.dialog.title(
                "Add New User",
            ),
            rx.dialog.description(
                "Fill the form with the user's info",
            ),
            rx.form(
                rx.flex(
                    rx.input(
                        placeholder="User Name", name="name", required=True
                    ),
                    rx.input(
                        placeholder="user@reflex.dev",
                        name="email",
                    ),
                    rx.select(
                        ["Male", "Female"],
                        placeholder="male",
                        name="gender",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.dialog.close(
                            rx.button(
                                "Submit", type="submit"
                            ),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=State.add_user,
                reset_on_submit=False,
            ),
            max_width="450px",
        ),
    )

def graph():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="value",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=State.users_for_graph,
        width="100%",
        height=250,
    )

def index() -> rx.Component:
    return rx.vstack(
        add_customer_button(),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Gender"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    State.users, show_user
                ),
            ),
            variant="surface",
            size="3",
            width="100%",
        ),
        graph(),
        align="center",
        width="100%",
    )


app = rx.App(
    theme=rx.theme(
        radius="full", accent_color="grass"
    ),
)

app.add_page(
    index,
    title="Customer Data App",
    description="A simple app to manage customer data.",
    on_load=State.transform_data,
)
```

Don't worry if you don't understand the code above, in this tutorial we are going to walk you through the whole thing step by step.


## Setup for the tutorial

Check out the [installation docs]({docs.getting_started.installation.path}) to get Reflex set up on your machine. Follow these to create a folder called `dashboard_tutorial`, which you will `cd` into and `pip install reflex`.

We will choose template `0` when we run `reflex init` to get the blank template. Finally run `reflex run` to start the app and confirm everything is set up correctly.


## Overview

Now that you’re set up, let’s get an overview of Reflex!

### Inspecting the starter code

Within our `dashboard_tutorial` folder we just `cd`'d into, there is a `rxconfig.py` file that contains the configuration for our Reflex app. (Check out the [config docs]({docs.advanced_onboarding.configuration.path}) for more information)

There is also an `assets` folder where static files such as images and stylesheets can be placed to be referenced within your app. ([asset docs]({docs.assets.overview.path}) for more information)

Most importantly there is a folder also called `dashboard_tutorial` which contains all the code for your app. Inside of this folder there is a file named `dashboard_tutorial.py`. To begin this tutorial we will delete all the code in this file so that we can start from scratch and explain every step as we go.

The first thing we need to do is import `reflex`. Once we have done this we can create a component, which is a reusable piece of user interface code. Components are used to render, manage, and update the UI elements in your application. 

Let's look at the example below. Here we have a function called `index` that returns a `text` component (an in-built Reflex UI component) that displays the text "Hello World!".

Next we define our app using `app = rx.App()` and add the component we just defined (`index`) to a page using `app.add_page(index)`. The function name (in this example `index`) which defines the component, must be what we pass into the `add_page`. The definition of the app and adding a component to a page are required for every Reflex app.

```python
import reflex as rx


def index() -> rx.Component:
    return rx.text("Hello World!")

app = rx.App()
app.add_page(index)
```

This code will render a page with the text "Hello World!" when you run your app like below:

```python eval
rx.text("Hello World!", 
    border_width="2px",
    border_radius="10px",
    padding="1em"
)
```

```md alert info
For the rest of the tutorial the `app=rx.App()` and `app.add_page` will be implied and not shown in the code snippets.
```

### Creating a table

Let's create a new component that will render a table. We will use the `table` component to do this. The `table` component has a `root`, which takes in a `header` and a `body`, which in turn take in `row` components. The `row` component takes in `cell` components which are the actual data that will be displayed in the table.

```python eval
rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.table.row(
                rx.table.cell("Danilo Sousa"),
                rx.table.cell("danilo@example.com"),
                rx.table.cell("Male"),
            ),
            rx.table.row(
                rx.table.cell("Zahra Ambessa"),
                rx.table.cell("zahra@example.com"),
                rx.table.cell("Female"),
            ),
        ),
        border_width="2px",
        border_radius="10px",
        padding="1em",
    )
```

```python
def index() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.table.row(
                rx.table.cell("Danilo Sousa"),
                rx.table.cell("danilo@example.com"),
                rx.table.cell("Male"),
            ),
            rx.table.row(
                rx.table.cell("Zahra Ambessa"),
                rx.table.cell("zahra@example.com"),
                rx.table.cell("Female"),
            ),
        ),
    )
```

Components in Reflex have `props`, which can be used to customize the component and are passed in as keyword arguments to the component function. 

The `rx.table.root` component has for example the `variant` and `size` props, which customize the table as seen below.

```python eval
rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.table.row(
                rx.table.cell("Danilo Sousa"),
                rx.table.cell("danilo@example.com"),
                rx.table.cell("Male"),
            ),
            rx.table.row(
                rx.table.cell("Zahra Ambessa"),
                rx.table.cell("zahra@example.com"),
                rx.table.cell("Female"),
            ),
        ),
        variant="surface",
        size="3",
        border_width="2px",
        border_radius="10px",
        padding="1em",
    )
```

```python
def index() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.table.row(
                rx.table.cell("Danilo Sousa"),
                rx.table.cell("danilo@example.com"),
                rx.table.cell("Male"),
            ),
            rx.table.row(
                rx.table.cell("Zahra Ambessa"),
                rx.table.cell("zahra@example.com"),
                rx.table.cell("Female"),
            ),
        ),
        variant="surface",
        size="3",
    )
```

## Showing dynamic data (State)

Up until this point all the data we are showing in the app is static. This is not very useful for a data dashboard. We need to be able to show dynamic data that can be added to and updated.

This is where `State` comes in. `State` is a Python class that stores variables that can change when the app is running, as well as the functions that can change those variables.

To define a state class, subclass `rx.State` and define fields that store the state of your app. The state variables (vars) should have a type annotation, and can be initialized with a default value. Check out the [basics]({docs.getting_started.basics.path}) section for a simple example of how state works.


In the example below we define a `State` class called `State` that has a variable called `users` that is a list of lists of strings. Each list in the `users` list represents a user and contains their name, email and gender.

```python
class State(rx.State):
    users: list[list[str]] = [
        ["Danilo Sousa", "danilo@example.com", "Male"],
        ["Zahra Ambessa", "zahra@example.com", "Female"],
    ]
```

To iterate over a state var that is a list, we use the [`rx.foreach`]({docs.components.rendering_iterables.path}) function to render a list of components. The `rx.foreach` component takes an `iterable` (list, tuple or dict) and a `function` that renders each item in the `iterable`.

```md alert info
# Why can we not just splat this in a `for` loop
You might be wondering why a `foreach` is even needed to render this state variable and why we cannot just splat a `for` loop. Check out this [documentation]({docs.getting_started.basics.path}#compile-time-vs.-runtime-(important)) to learn why.
```

Here the render function is `show_user` which takes in a single user and returns a `table.row` component that displays the users name, email and gender.


```python eval
rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                State1.users, show_user1
            ),
        ),
        variant="surface",
        size="3",
        border_width="2px",
        border_radius="10px",
        padding="1em",
)
```


```python
class State(rx.State):
    users: list[list[str]] = [
        ["Danilo Sousa", "danilo@example.com", "Male"],
        ["Zahra Ambessa", "zahra@example.com", "Female"],
    ]

def show_user(person: list):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(person[0]),
        rx.table.cell(person[1]),
        rx.table.cell(person[2]),
    )

def index() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                State.users, show_user
            ),
        ),
        variant="surface",
        size="3",
)
```

As you can see the output above looks the same as before, except now the data is no longer static and can change with user input to the app.

### Using a proper class structure for our data

So far our data has been defined in a list of lists, where the data is accessed by index i.e. `user[0]`, `user[1]`. This is not very maintainable as our app gets bigger. 

A better way to structure our data in Reflex is to use a class to represent a user. This way we can access the data using attributes i.e. `user.name`, `user.email`.

In Reflex when we create these classes to showcase our data, the class must inherit from `rx.Base`.

`rx.Base` is also necessary if we want to have a state var that is an iterable with different types. For example if we wanted to have `age` as an `int` we would have to use `rx.base` as we could not do this with a state var defined as `list[list[str]]`. 

The `show_user` render function is also updated to access the data by named attributes, instead of indexing.


```python eval
rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                State2.users, show_user2
            ),
        ),
        variant="surface",
        size="3",
        border_width="2px",
        border_radius="10px",
        padding="1em",
)
```


```python
class User(rx.Base):
    """The user model."""

    name: str
    email: str
    gender: str


class State(rx.State):
    users: list[User] = [
        User(name="Danilo Sousa", email="danilo@example.com", gender="Male"),
        User(name="Zahra Ambessa", email="zahra@example.com", gender="Female"),
    ]

def show_user(user: User):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
    )

def index() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                State.users, show_user
            ),
        ),
        variant="surface",
        size="3",
)
```


Next let's add a form to the app so we can add new users to the table.


## Using a Form to Add Data 

We build a form using `rx.form`, which takes several components such as `rx.input` and `rx.select`, which represent the form fields that allow you to add information to submit with the form. Check out the [form]({docs.library.forms.form.path}) docs for more information on form components.

The `rx.input` component takes in several props. The `placeholder` prop is the text that is displayed in the input field when it is empty. The `name` prop is the name of the input field, which gets passed through in the dictionary when the form is submitted. The `required` prop is a boolean that determines if the input field is required.

The `rx.select` component takes in a list of options that are displayed in the dropdown. The other props used here are identical to the `rx.input` component.

```python demo
rx.form(
    rx.input(
        placeholder="User Name", name="name", required=True
    ),
    rx.input(
        placeholder="user@reflex.dev",
        name="email",
    ),
    rx.select(
        ["Male", "Female"],
        placeholder="Male",
        name="gender",
    ),
)
```

This form is all very compact as you can see from the example, so we need to add some styling to make it look better. We can do this by adding a `vstack` component around the form fields. The `vstack` component stacks the form fields vertically. Check out the [layout]({docs.styling.layout.path}) docs for more information on how to layout your app.


```python demo
rx.form(
    rx.vstack(
        rx.input(
            placeholder="User Name", name="name", required=True
        ),
        rx.input(
            placeholder="user@reflex.dev",
            name="email",
        ),
        rx.select(
            ["Male", "Female"],
            placeholder="Male",
            name="gender",
        ),
    ),
)
```

Now you have probably realised that we have all the form fields, but we have no way to submit the form. We can add a submit button to the form by adding a `rx.button` component to the `vstack` component. The `rx.button` component takes in the text that is displayed on the button and the `type` prop which is the type of button. The `type` prop is set to `submit` so that the form is submitted when the button is clicked. 

In addition to this we need a way to update the `users` state variable when the form is submitted. All state changes are handled through functions in the state class, called [event handlers]({docs.events.events_overview.path}).

Components have special props called event triggers, such as `on_submit`, that can be used to make components interactive. Event triggers connect components to event handlers, which update the state. Different event triggers expect the event handler that you hook them up to, to take in different arguments (and some do not take in any arguments).

The `on_submit` event trigger of `rx.form` is hooked up to the `add_user` event handler that is defined in the `State` class. This event trigger expects to pass a `dict`, containing the form data, to the event handler that it is hooked up to. The `add_user` event handler takes in the form data as a dictionary and appends it to the `users` state variable. 


```python
class State(rx.State):
    
    ...

    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))


def form():
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="User Name", name="name", required=True
            ),
            rx.input(
                placeholder="user@reflex.dev",
                name="email",
            ),
            rx.select(
                ["Male", "Female"],
                placeholder="Male",
                name="gender",
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit=State.add_user,
        reset_on_submit=True,
    )
```

Finally we must add the new `form()` component we have defined to the `index()` function so that the form is rendered on the page.

Below is the full code for the app so far. If you try this form out you will see that you can add new users to the table by filling out the form and clicking the submit button. The form data will also appear as a toast (a small window in the corner of the page) on the screen when submitted.



```python eval
rx.vstack(
    form(),
    rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                State3.users, show_user
            ),
        ),
        variant="surface",
        size="3",
    ),
    border_width="2px",
    border_radius="10px",
    padding="1em",
)
```

```python
class State(rx.State):
    users: list[User] = [
        User(name="Danilo Sousa", email="danilo@example.com", gender="Male"),
        User(name="Zahra Ambessa", email="zahra@example.com", gender="Female"),
    ]

    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))


def show_user(user: User):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
    )

def form():
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="User Name", name="name", required=True
            ),
            rx.input(
                placeholder="user@reflex.dev",
                name="email",
            ),
            rx.select(
                ["Male", "Female"],
                placeholder="Male",
                name="gender",
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit=State.add_user,
        reset_on_submit=True,
    )

def index() -> rx.Component:
    return rx.vstack(
        form(),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Gender"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    State.users, show_user
                ),
            ),
            variant="surface",
            size="3",
        ),
    )
```


### Putting the Form in an Overlay

In Reflex, we like to make the user interaction as intuitive as possible. Placing the form we just constructed in an overlay creates a focused interaction by dimming the background, and ensures a cleaner layout when you have multiple action points such as editing and deleting as well.

We will place the form inside of a `rx.dialog` component (also called a modal). The `rx.dialog.root` contains all the parts of a dialog, and the `rx.dialog.trigger` wraps the control that will open the dialog. In our case the trigger will be an `rx.button` that says "Add User" as shown below.

```python
rx.dialog.trigger(
    rx.button(
        rx.icon("plus", size=26),
        rx.text("Add User", size="4"),
    ),
)
```

After the trigger we have the `rx.dialog.content` which contains everything within our dialog, including a title, a description and our form. The first way to close the dialog is without submitting the form and the second way is to close the dialog by submitting the form as shown below. This requires two `rx.dialog.close` components within the dialog.

```python
rx.dialog.close(
    rx.button(
        "Cancel",
        variant="soft",
        color_scheme="gray",
    ),
),
rx.dialog.close(
    rx.button(
        "Submit", type="submit"
    ),
)
```

The total code for the dialog with the form in it is below.

```python demo
rx.dialog.root(
    rx.dialog.trigger(
        rx.button(
            rx.icon("plus", size=26),
            rx.text("Add User", size="4"),
        ),
    ),
    rx.dialog.content(
        rx.dialog.title(
            "Add New User",
        ),
        rx.dialog.description(
            "Fill the form with the user's info",
        ),
        rx.form(
            # flex is similar to vstack and used to layout the form fields
            rx.flex(
                rx.input(
                    placeholder="User Name", name="name", required=True
                ),
                rx.input(
                    placeholder="user@reflex.dev",
                    name="email",
                ),
                rx.select(
                    ["Male", "Female"],
                    placeholder="Male",
                    name="gender",
                ),
                rx.flex(
                    rx.dialog.close(
                        rx.button(
                            "Cancel",
                            variant="soft",
                            color_scheme="gray",
                        ),
                    ),
                    rx.dialog.close(
                        rx.button(
                            "Submit", type="submit"
                        ),
                    ),
                    spacing="3",
                    justify="end",
                ),
                direction="column",
                spacing="4",
            ),
            on_submit=State3.add_user,
            reset_on_submit=False,
        ),
        # max_width is used to limit the width of the dialog
        max_width="450px",
    ),
)
```

At this point we have an app that allows you to add users to a table by filling out a form. The form is placed in a dialog that can be opened by clicking the "Add User" button. We change the name of the component from `form` to `add_customer_button` and update this in our `index` component. The full app so far and code are below.



```python eval
rx.vstack(
    add_customer_button(),
    rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                State3.users, show_user
            ),
        ),
        variant="surface",
        size="3",
    ),
    border_width="2px",
    border_radius="10px",
    padding="1em",
)
```

```python
class User(rx.Base):
    """The user model."""

    name: str
    email: str
    gender: str


class State(rx.State):
    users: list[User] = [
        User(name="Danilo Sousa", email="danilo@example.com", gender="Male"),
        User(name="Zahra Ambessa", email="zahra@example.com", gender="Female"),
    ]

    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))

        

def show_user(user: User):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
    )

def add_customer_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Add User", size="4"),
            ),
        ),
        rx.dialog.content(
            rx.dialog.title(
                "Add New User",
            ),
            rx.dialog.description(
                "Fill the form with the user's info",
            ),
            rx.form(
                rx.flex(
                    rx.input(
                        placeholder="User Name", name="name", required=True
                    ),
                    rx.input(
                        placeholder="user@reflex.dev",
                        name="email",
                    ),
                    rx.select(
                        ["Male", "Female"],
                        placeholder="Male",
                        name="gender",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.dialog.close(
                            rx.button(
                                "Submit", type="submit"
                            ),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=State.add_user,
                reset_on_submit=False,
            ),
            max_width="450px",
        ),
    )

def index() -> rx.Component:
    return rx.vstack(
        add_customer_button(),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Gender"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    State.users, show_user
                ),
            ),
            variant="surface",
            size="3",
        ),
    )
```


## Plotting Data in a Graph

The last part of this tutorial is to plot the user data in a graph. We will use Reflex's built-in graphing library recharts to plot the number of users of each gender. 

### Transforming the data for the graph

The graphing components in Reflex expect to take in a list of dictionaries. Each dictionary represents a data point on the graph and contains the x and y values. We will create a new event handler in the state called `transform_data` to transform the user data into the format that the graphing components expect. We must also create a new state variable called `users_for_graph` to store the transformed data, which will be used to render the graph.


```python
from collections import Counter

class State(rx.State):
    users: list[User] = []
    users_for_graph: list[dict] = []

    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))
        self.transform_data()
    
    def transform_data(self):
        """Transform user gender group data into a format suitable for visualization in graphs."""
        # Count users of each gender group
        gender_counts = Counter(user.gender for user in self.users)
        
        # Transform into list of dict so it can be used in the graph
        self.users_for_graph = [
            {
                "name": gender_group,
                "value": count
            }
            for gender_group, count in gender_counts.items()
        ]
```

As we can see above the `transform_data` event handler uses the `Counter` class from the `collections` module to count the number of users of each gender. We then create a list of dictionaries from this which we set to the state var `users_for_graph`. 

Finally we can see that whenever we add a new user through submitting the form and running the `add_user` event handler, we call the `transform_data` event handler to update the `users_for_graph` state variable.

### Rendering the graph

We use the `rx.recharts.bar_chart` component to render the graph. We pass through the state variable for our graphing data as `data=State.users_for_graph`. We also pass in a `rx.recharts.bar` component which represents the bars on the graph. The `rx.recharts.bar` component takes in the `data_key` prop which is the key in the data dictionary that represents the y value of the bar. The `stroke` and `fill` props are used to set the color of the bars.

The `rx.recharts.bar_chart` component also takes in `rx.recharts.x_axis` and `rx.recharts.y_axis` components which represent the x and y axes of the graph. The `data_key` prop of the `rx.recharts.x_axis` component is set to the key in the data dictionary that represents the x value of the bar. Finally we add `width` and `height` props to set the size of the graph.

```python
def graph():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="value",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=State.users_for_graph,
        width="100%",
        height=250,
    )
```

Finally we add this `graph()` component to our `index()` component so that the graph is rendered on the page. The code for the full app with the graph included is below. If you try this out you will see that the graph updates whenever you add a new user to the table.


```python eval
rx.vstack(
    add_customer_button(),
    rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                State4.users, show_user
            ),
        ),
        variant="surface",
        size="3",
    ),
    graph(),
    border_width="2px",
    border_radius="10px",
    padding="1em",
)
```

```python
from collections import Counter

class State(rx.State):
    users: list[User] = [
        User(name="Danilo Sousa", email="danilo@example.com", gender="Male"),
        User(name="Zahra Ambessa", email="zahra@example.com", gender="Female"),
    ]
    users_for_graph: list[dict] = []

    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))
        self.transform_data()
    
    def transform_data(self):
        """Transform user gender group data into a format suitable for visualization in graphs."""
        # Count users of each gender group
        gender_counts = Counter(user.gender for user in self.users)
        
        # Transform into list of dict so it can be used in the graph
        self.users_for_graph = [
            {
                "name": gender_group,
                "value": count
            }
            for gender_group, count in gender_counts.items()
        ]
        

def show_user(user: User):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
    )

def add_customer_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Add User", size="4"),
            ),
        ),
        rx.dialog.content(
            rx.dialog.title(
                "Add New User",
            ),
            rx.dialog.description(
                "Fill the form with the user's info",
            ),
            rx.form(
                rx.flex(
                    rx.input(
                        placeholder="User Name", name="name", required=True
                    ),
                    rx.input(
                        placeholder="user@reflex.dev",
                        name="email",
                    ),
                    rx.select(
                        ["Male", "Female"],
                        placeholder="male",
                        name="gender",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.dialog.close(
                            rx.button(
                                "Submit", type="submit"
                            ),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=State.add_user,
                reset_on_submit=False,
            ),
            max_width="450px",
        ),
    )

def graph():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="value",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=State.users_for_graph,
        width="100%",
        height=250,
    )

def index() -> rx.Component:
    return rx.vstack(
        add_customer_button(),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Gender"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    State.users, show_user
                ),
            ),
            variant="surface",
            size="3",
        ),
        graph(),
    )
```

One thing you may have noticed about your app is that the graph does not appear initially when you run the app, and that you must add a user to the table for it to first appear. This occurs because the `transform_data` event handler is only called when a user is added to the table. In the next section we will explore a solution to this.


## Final Cleanup

### Revisiting app.add_page

At the beginning of this tutorial we mentioned that the `app.add_page` function is required for every Reflex app. This function is used to add a component to a page. 

The `app.add_page` currently looks like this `app.add_page(index)`. We could change the route that the page renders on by setting the `route` prop such as `route="/custom-route"`, this would change the route to `http://localhost:3000/custom-route` for this page.

We can also set a `title` to be shown in the browser tab and a `description` as shown in search results. 

To solve the problem we had above about our graph not loading when the page loads, we can use `on_load` inside of `app.add_page` to call the `transform_data` event handler when the page loads. This would look like `on_load=State.transform_data`. Below see what our `app.add_page` would look like with some of the changes above added.

```python eval
rx.vstack(
    add_customer_button(),
    rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                State4.users, show_user
            ),
        ),
        variant="surface",
        size="3",
    ),
    graph(),
    on_mouse_enter=State4.transform_data,
    border_width="2px",
    border_radius="10px",
    padding="1em",
)
```

```python
app.add_page(
    index,
    title="Customer Data App",
    description="A simple app to manage customer data.",
    on_load=State.transform_data,
)
```

### Revisiting app=rx.App()

At the beginning of the tutorial we also mentioned that we defined our app using `app=rx.App()`. We can also pass in some props to the `rx.App` component to customize the app.

The most important one is `theme` which allows you to customize the look and feel of the app. The `theme` prop takes in an `rx.theme` component which has several props that can be set. 

The `radius` prop sets the global radius value for the app that is inherited by all components that have a `radius` prop. It can be overwritten locally for a specific component by manually setting the `radius` prop.

The `accent_color` prop sets the accent color of the app. Check out other options for the accent color [here]({docs.library.other.theme.path}).

To see other props that can be set at the app level check out this [documentation](docs.styling.theming.path)

```python
app = rx.App(
    theme=rx.theme(
        radius="full", accent_color="grass"
    ),
)
```

Unfortunately in this tutorial here we cannot actually apply this to the live example on the page, but if you copy and paste the code below into a reflex app locally you can see it in action.



## Conclusion

Finally let's make some final styling updates to our app. We will add some hover styling to the table rows and center the table inside the `show_user` with `style=\{"_hover": \{"bg": rx.color("gray", 3)}}, align="center"`.

In addition, we will add some `width="100%"` and `align="center"` to the `index()` component to center the items on the page and ensure they stretch the full width of the page.

Check out the full code and interactive app below:

```python eval
rx.vstack(
        add_customer_button5(),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Gender"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    State5.users, show_user5
                ),
            ),
            variant="surface",
            size="3",
            width="100%",
        ),
        graph5(),
        align="center",
        width="100%",
        on_mouse_enter=State5.transform_data,
        border_width="2px",
        border_radius="10px",
        padding="1em",
    )
```


```python
import reflex as rx
from collections import Counter

class User(rx.Base):
    """The user model."""

    name: str
    email: str
    gender: str


class State(rx.State):
    users: list[User] = [
        User(name="Danilo Sousa", email="danilo@example.com", gender="Male"),
        User(name="Zahra Ambessa", email="zahra@example.com", gender="Female"),
    ]
    users_for_graph: list[dict] = []

    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))
        self.transform_data()
    
    def transform_data(self):
        """Transform user gender group data into a format suitable for visualization in graphs."""
        # Count users of each gender group
        gender_counts = Counter(user.gender for user in self.users)
        
        # Transform into list of dict so it can be used in the graph
        self.users_for_graph = [
            {
                "name": gender_group,
                "value": count
            }
            for gender_group, count in gender_counts.items()
        ]
        

def show_user(user: User):
    """Show a user in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
        style=\{"_hover": 
            \{"bg": rx.color("gray", 3)}
        },
        align="center",
    )

def add_customer_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Add User", size="4"),
            ),
        ),
        rx.dialog.content(
            rx.dialog.title(
                "Add New User",
            ),
            rx.dialog.description(
                "Fill the form with the user's info",
            ),
            rx.form(
                rx.flex(
                    rx.input(
                        placeholder="User Name", name="name", required=True
                    ),
                    rx.input(
                        placeholder="user@reflex.dev",
                        name="email",
                    ),
                    rx.select(
                        ["Male", "Female"],
                        placeholder="male",
                        name="gender",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.dialog.close(
                            rx.button(
                                "Submit", type="submit"
                            ),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=State.add_user,
                reset_on_submit=False,
            ),
            max_width="450px",
        ),
    )

def graph():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="value",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=State.users_for_graph,
        width="100%",
        height=250,
    )

def index() -> rx.Component:
    return rx.vstack(
        add_customer_button(),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Gender"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    State.users, show_user
                ),
            ),
            variant="surface",
            size="3",
            width="100%",
        ),
        graph(),
        align="center",
        width="100%",
    )


app = rx.App(
    theme=rx.theme(
        radius="full", accent_color="grass"
    ),
)

app.add_page(
    index,
    title="Customer Data App",
    description="A simple app to manage customer data.",
    on_load=State.transform_data,
)
```

And that is it for your first dashboard tutorial. In this tutorial we have created 

- a table to display user data
- a form to add new users to the table
- a dialog to showcase the form
- a graph to visualize the user data

In addition to the above we have we have 

- explored state to allow you to show dynamic data that changes over time
- explored events to allow you to make your app interactive and respond to user actions
- added styling to the app to make it look better



## Advanced Section (Hooking this up to a Database)

Coming Soon!
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/getting_started/chat_tutorial_style.py`:

```py
# Common styles for questions and answers.
import reflex as rx

shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    background_color=rx.color("gray", 4), margin_left=chat_margin
)
answer_style = message_style | dict(
    background_color=rx.color("accent", 8), margin_right=chat_margin
)

# Styles for the action bar.
input_style = dict(border_width="1px", box_shadow=shadow, width="350px")
button_style = dict(background_color=rx.color("accent", 10), box_shadow=shadow)

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/getting_started/chatapp_tutorial.md`:

```md

# Interactive Tutorial: AI Chat App

This tutorial will walk you through building an AI chat app with Reflex. This app is fairly complex, but don't worry - we'll break it down into small steps.

You can find the full source code for this app [here]({CHAT_APP_URL}).

### What You'll Learn

In this tutorial you'll learn how to:

1. Install `reflex` and set up your development environment.
2. Create components to define and style your UI.
3. Use state to add interactivity to your app.
4. Deploy your app to share with others.




## Setting up Your Project

```md video https://youtube.com/embed/ITOZkzjtjUA?start=175&end=445
# Video: Example of Setting up the Chat App
```

We will start by creating a new project and setting up our development environment. First, create a new directory for your project and navigate to it.

```bash
~ $ mkdir chatapp
~ $ cd chatapp
```

Next, we will create a virtual environment for our project. This is optional, but recommended. In this example, we will use [venv]({constants.VENV_URL}) to create our virtual environment.

```bash
chatapp $ python3 -m venv venv
$ source venv/bin/activate
```

Now, we will install Reflex and create a new project. This will create a new directory structure in our project directory.

> **Note:** When prompted to select a template, choose option 0 for a blank project.


```bash
chatapp $ pip install reflex
chatapp $ reflex init
────────────────────────────────── Initializing chatapp ───────────────────────────────────
Success: Initialized chatapp
chatapp $ ls
assets          chatapp         rxconfig.py     venv
```

```python eval
rx.box(height="20px")
```
You can run the template app to make sure everything is working.

```bash
chatapp $ reflex run
─────────────────────────────────── Starting Reflex App ───────────────────────────────────
Compiling:  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 1/1 0:00:00
─────────────────────────────────────── App Running ───────────────────────────────────────
App running at: http://localhost:3000
```

```python eval
rx.box(height="20px")
```

You should see your app running at [http://localhost:3000]({"http://localhost:3000"}).

Reflex also starts the backend server which handles all the state management and communication with the frontend. You can test the backend server is running by navigating to [http://localhost:8000/ping]({"http://localhost:8000/ping"}).

Now that we have our project set up, in the next section we will start building our app!




## Basic Frontend

Let's start with defining the frontend for our chat app. In Reflex, the frontend can be broken down into independent, reusable components. See the [components docs]({components.props.path}) for more information.

### Display A Question And Answer

We will modify the `index` function in `chatapp/chatapp.py` file to return a component that displays a single question and answer.

```python demo box
rx.container(
    rx.box(
        "What is Reflex?",
        # The user's question is on the right.
        text_align="right",
    ),
    rx.box(
        "A way to build web apps in pure Python!",
        # The answer is on the left.
        text_align="left",
    ),
)
```

```python
# chatapp.py

import reflex as rx

def index() -> rx.Component:
    return rx.container(
        rx.box(
            "What is Reflex?",
            # The user's question is on the right.
            text_align="right",
        ),
        rx.box(
            "A way to build web apps in pure Python!",
            # The answer is on the left.
            text_align="left",
        ),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
```

Components can be nested inside each other to create complex layouts. Here we create a parent container that contains two boxes for the question and answer.

We also add some basic styling to the components. Components take in keyword arguments, called [props]({components.props.path}), that modify the appearance and functionality of the component. We use the `text_align` prop to align the text to the left and right.

### Reusing Components

Now that we have a component that displays a single question and answer, we can reuse it to display multiple questions and answers. We will move the component to a separate function `question_answer` and call it from the `index` function.


```python demo box
rx.container(chat())
```

```python
def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align="right"),
        rx.box(answer, text_align="left"),
        margin_y="1em",
    )


def chat() -> rx.Component:
    qa_pairs = [
        ("What is Reflex?", "A way to build web apps in pure Python!"),
        ("What can I make with it?", "Anything from a simple website to a complex web app!"),
    ]
    return rx.box(*[qa(question, answer) for question, answer in qa_pairs])


def index() -> rx.Component:
    return rx.container(chat())
```

### Chat Input

Now we want a way for the user to input a question. For this, we will use the [input]({library.forms.input.path}) component to have the user add text and a [button]({library.forms.button.path}) component to submit the question.


```python demo box
rx.container(
    chat(),
    action_bar(),
)
```

```python
def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Ask a question"),
        rx.button("Ask"),
    )

def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
    )
```

### Styling

Let's add some styling to the app. More information on styling can be found in the [styling docs]({styling.overview.path}). To keep our code clean, we will move the styling to a separate file `chatapp/style.py`.

```python
# style.py
import reflex as rx

# Common styles for questions and answers.
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(margin_left=chat_margin, background_color=rx.color("gray", 4))
answer_style = message_style | dict(margin_right=chat_margin, background_color=rx.color("accent", 8))

# Styles for the action bar.
input_style = dict(
    border_width="1px", padding="0.5em", box_shadow=shadow,width="350px"
)
button_style = dict(background_color=rx.color("accent", 10), box_shadow=shadow)
```

We will import the styles in `chatapp.py` and use them in the components. At this point, the app should look like this:


```python demo box
rx.center(
    rx.vstack(
        chat4(),
        action_bar4(),
        align="center",
    )
)
```

```python
# chatapp.py
import reflex as rx

from chatapp import style


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(rx.text(question, style=style.question_style), text_align="right"),
        rx.box(rx.text(answer, style=style.answer_style), text_align="left"),
        margin_y="1em",
        width="100%",
    )

def chat() -> rx.Component:
    qa_pairs = [
        ("What is Reflex?", "A way to build web apps in pure Python!"),
        ("What can I make with it?", "Anything from a simple website to a complex web app!"),
    ]
    return rx.box(*[qa(question, answer) for question, answer in qa_pairs])


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Ask a question", style=style.input_style),
        rx.button("Ask", style=style.button_style),
    )


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            chat(),
            action_bar(),
            align="center",
        )
    )


app = rx.App()
app.add_page(index)
```

The app is looking good, but it's not very useful yet! In the next section, we will add some functionality to the app.






## State

Now let’s make the chat app interactive by adding state. The state is where we define all the variables that can change in the app and all the functions that can modify them. You can learn more about state in the [state docs]({state.overview.path}).

### Defining State

We will create a new file called `state.py` in the `chatapp` directory. Our state will keep track of the current question being asked and the chat history. We will also define an event handler `answer` which will process the current question and add the answer to the chat history.

```python
# state.py
import reflex as rx


class State(rx.State):

    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    @rx.event
    def answer(self):
        # Our chatbot is not very smart right now...
        answer = "I don't know!"
        self.chat_history.append((self.question, answer))

```

### Binding State to Components

Now we can import the state in `chatapp.py` and reference it in our frontend components. We will modify the `chat` component to use the state instead of the current fixed questions and answers.


```python demo box
rx.container(
    chat1(),
    action_bar1(),
)
```

```python
# chatapp.py
from chatapp.state import State
...

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1])
        )
    )

...

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Ask a question", on_change=State.set_question, style=style.input_style),
        rx.button("Ask", on_click=State.answer, style=style.button_style),
    )
```

Normal Python `for` loops don't work for iterating over state vars because these values can change and aren't known at compile time. Instead, we use the [foreach]({library.dynamic_rendering.foreach.path}) component to iterate over the chat history.

We also bind the input's `on_change` event to the `set_question` event handler, which will update the `question` state var while the user types in the input. We bind the button's `on_click` event to the `answer` event handler, which will process the question and add the answer to the chat history. The `set_question` event handler is a built-in implicitly defined event handler. Every base var has one. Learn more in the [events docs]({events.setters.path}) under the Setters section.

### Clearing the Input

Currently the input doesn't clear after the user clicks the button. We can fix this by binding the value of the input to `question`, with `value=State.question`, and clear it when we run the event handler for `answer`, with `self.question = ''`.


```python demo box
rx.container(
    chat1(),
    action_bar2(),
)
```

```python
# chatapp.py
def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Ask a question",
            on_change=State.set_question,
            style=style.input_style),
        rx.button("Ask", on_click=State.answer, style=style.button_style),
    )
```

```python
# state.py

@rx.event
def answer(self):
    # Our chatbot is not very smart right now...
    answer = "I don't know!"
    self.chat_history.append((self.question, answer))
    self.question = ""
```

### Streaming Text

Normally state updates are sent to the frontend when an event handler returns. However, we want to stream the text from the chatbot as it is generated. We can do this by yielding from the event handler. See the [yield events docs]({events.yield_events.path}) for more info.


```python demo box
rx.container(
    chat1(),
    action_bar3(),
)
```

```python
# state.py
import asyncio

...
async def answer(self):
    # Our chatbot is not very smart right now...
    answer = "I don't know!"
    self.chat_history.append((self.question, ""))

    # Clear the question input.
    self.question = ""
    # Yield here to clear the frontend input before continuing.
    yield

    for i in range(len(answer)):
        # Pause to show the streaming effect.
        await asyncio.sleep(0.1)
        # Add one letter at a time to the output.
        self.chat_history[-1] = (self.chat_history[-1][0], answer[:i + 1])
        yield
```

In the next section, we will finish our chatbot by adding AI!



## Final App

We will use OpenAI's API to give our chatbot some intelligence.

### Configure the OpenAI API Key

Ensure you have an active OpenAI subscription. Save your API key as an environment variable named `OPENAI_API_KEY`:

    ```bash
    export OPENAI_API_KEY="your-api-key-here"
    ```

Install the `openai` pypi package:

    ```bash
    pip install openai
    ```

### Using the API

We need to modify our event handler to send a request to the API.


```python demo box
rx.center(
    rx.vstack(
        chat1(),
        action_bar3(),
        align="center",
        width="100%",
    )
)
```

```python
# state.py
import os

from openai import AsyncOpenAI

@rx.event
async def answer(self):
    # Our chatbot has some brains now!
    client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

    session = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            \{"role": "user", "content": self.question}
        ],
        stop=None,
        temperature=0.7,
        stream=True,
    )

    # Add to the answer as the chatbot responds.
    answer = ""
    self.chat_history.append((self.question, answer))

    # Clear the question input.
    self.question = ""
    # Yield here to clear the frontend input before continuing.
    yield

    async for item in session:
        if hasattr(item.choices[0].delta, "content"):
            if item.choices[0].delta.content is None:
                # presence of 'None' indicates the end of the response
                break
            answer += item.choices[0].delta.content
            self.chat_history[-1] = (self.chat_history[-1][0], answer)
            yield
```

Finally, we have our chatbot!

### Final Code

We wrote all our code in three files, which you can find below.

```python
# chatapp.py
import reflex as rx

from chatapp import style
from chatapp.state import State


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(rx.text(question, style=style.question_style),text_align="right"),
        rx.box(rx.text(answer, style=style.answer_style),text_align="left"),
        margin_y="1em",
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Ask a question",
            on_change=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=style.button_style,
        ),
    )


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            chat(),
            action_bar(),
            align="center",
        )
    )


app = rx.App()
app.add_page(index)
```

```python
# state.py
import os

from openai import AsyncOpenAI

import reflex as rx

class State(rx.State):

    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    async def answer(self):
        # Our chatbot has some brains now!
        client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

        session = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[\{"role": "user", "content": self.question}],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        # Add to the answer as the chatbot responds.
        answer = ""
        self.chat_history.append((self.question, answer))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        async for item in session:
            if hasattr(item.choices[0].delta, "content"):
                if item.choices[0].delta.content is None:
                    # presence of 'None' indicates the end of the response
                    break
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (
                    self.chat_history[-1][0],
                    answer,
                )
                yield
```

```python
# style.py
import reflex as rx

# Common styles for questions and answers.
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    margin_left=chat_margin,
    background_color=rx.color("gray", 4),
)
answer_style = message_style | dict(
    margin_right=chat_margin,
    background_color=rx.color("accent", 8),
)

# Styles for the action bar.
input_style = dict(border_width="1px", padding="0.5em", box_shadow=shadow, width="350px")
button_style = dict(
    background_color=rx.color("accent", 10), box_shadow=shadow
)

```

### Next Steps

Congratulations! You have built your first chatbot. From here, you can read through the rest of the documentations to learn about Reflex in more detail. The best way to learn is to build something, so try to build your own app using this as a starting point!

### One More Thing

With our hosting service, you can deploy this app with a single command within minutes. Check out our [Hosting Quick Start]({hosting.deploy_quick_start.path}).

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/getting_started/project-structure.md`:

```md
# Project Structure


## Directory Structure


Let's create a new app called `{app_name}`

```bash
mkdir {app_name}
cd {app_name}
reflex init
```

This will create a directory structure like this:

```bash
{app_name}
├── .web
├── assets
├── {app_name}
│   ├── __init__.py
│   └── {app_name}.py
└── rxconfig.py
```

Let's go over each of these directories and files.

## .web

This is where the compiled Javascript files will be stored. You will never need to touch this directory, but it can be useful for debugging.

Each Reflex page will compile to a corresponding `.js` file in the `.web/pages` directory.

## Assets

The `assets` directory is where you can store any static assets you want to be publicly available. This includes images, fonts, and other files.

For example, if you save an image to `assets/image.png` you can display it from your app like this:

```python
rx.image(src="image.png")
```

## Main Project

Initializing your project creates a directory with the same name as your app. This is where you will write your app's logic.

Reflex generates a default app within the `{app_name}/{app_name}.py` file. You can modify this file to customize your app.

## Configuration

The `rxconfig.py` file can be used to configure your app. By default it looks something like this:

```python
import reflex as rx


config = rx.Config(
    app_name="{app_name}",
)
```

We will discuss project structure and configuration in more detail in the [advanced project structure]({advanced_onboarding.code_structure.path}) documentation.
```