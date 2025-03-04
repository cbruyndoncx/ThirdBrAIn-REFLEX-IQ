Project Path: vars

Source Tree:

```
vars
├── base_vars.md
├── custom_vars.md
├── var-operations.md
└── computed_vars.md

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/vars/base_vars.md`:

```md

# Base Vars

Vars are any fields in your app that may change over time. A Var is directly
rendered into the frontend of the app.

Base vars are defined as fields in your State class.

They can have a preset default value. If you don't provide a default value, you
must provide a type annotation.

```md alert warning
# State Vars should provide type annotations.

Reflex relies on type annotations to determine the type of state vars during the compilation process.
```

```python demo exec
class TickerState(rx.State):
    ticker: str ="AAPL"
    price: str = "$150"


def ticker_example():
    return rx.center(
          rx.vstack(
                rx.heading(TickerState.ticker, size="3"),
                rx.text(f"Current Price: {TickerState.price}", font_size="md"),
                rx.text("Change: 4%", color="green"),
            ),

    )
```

In this example `ticker` and `price` are base vars in the app, which can be modified at runtime.

```md alert warning
# Vars must be JSON serializable.

Vars are used to communicate between the frontend and backend. They must be primitive Python types, Plotly figures, Pandas dataframes, or [a custom defined type]({vars.custom_vars.path}).
```

## Accessing state variables on different pages

State is just a python class and so can be defined on one page and then imported and used on another. Below we define `TickerState` class on the page `state.py` and then import it and use it on the page `index.py`.

```python
# state.py

class TickerState(rx.State):
    ticker: str = "AAPL"
    price: str = "$150"
```

```python
# index.py
from .state import TickerState

def ticker_example():
    return rx.center(
          rx.vstack(
                rx.heading(TickerState.ticker, size="3"),
                rx.text(f"Current Price: {TickerState.price}", font_size="md"),
                rx.text("Change: 4%", color="green"),
            ),

    )
```

## Backend-only Vars

Any Var in a state class that starts with an underscore is considered backend
only and will not be synchronized with the frontend. Data associated with a
specific session that is not directly rendered on the frontend should be stored
in a backend-only var to reduce network traffic and improve performance.

They have the advantage that they don't need to be JSON serializable, however
they must still be cloudpickle-able to be used with redis in prod mode. They are
not directly renderable on the frontend, and may be used to store sensitive
values that should not be sent to the client.

For example, a backend-only var is used to store a large data structure which is
then paged to the frontend using cached vars.

```python demo exec
import numpy as np


class BackendVarState(rx.State):
    _backend: np.ndarray = np.array([random.randint(0, 100) for _ in range(100)])
    offset: int = 0
    limit: int = 10

    @rx.var(cache=True)
    def page(self) -> list[int]:
        return [
            int(x)  # explicit cast to int
            for x in self._backend[self.offset : self.offset + self.limit]
        ]

    @rx.var(cache=True)
    def page_number(self) -> int:
        return (self.offset // self.limit) + 1 + (1 if self.offset % self.limit else 0)

    @rx.var(cache=True)
    def total_pages(self) -> int:
        return len(self._backend) // self.limit + (1 if len(self._backend) % self.limit else 0)

    @rx.event
    def prev_page(self):
        self.offset = max(self.offset - self.limit, 0)

    @rx.event
    def next_page(self):
        if self.offset + self.limit < len(self._backend):
            self.offset += self.limit

    @rx.event
    def generate_more(self):
        self._backend = np.append(self._backend, [random.randint(0, 100) for _ in range(random.randint(0, 100))])

    @rx.event
    def set_limit(self, value: str):
        self.limit = int(value)

def backend_var_example():
    return rx.vstack(
        rx.hstack(
            rx.button(
                "Prev",
                on_click=BackendVarState.prev_page,
            ),
            rx.text(f"Page {BackendVarState.page_number} / {BackendVarState.total_pages}"),
            rx.button(
                "Next",
                on_click=BackendVarState.next_page,
            ),
            rx.text("Page Size"),
            rx.input(
                width="5em",
                value=BackendVarState.limit,
                on_change=BackendVarState.set_limit,
            ),
            rx.button("Generate More", on_click=BackendVarState.generate_more),
        ),
        rx.list(
            rx.foreach(
                BackendVarState.page,
                lambda x, ix: rx.text(f"_backend[{ix + BackendVarState.offset}] = {x}"),
            ),
        ),
    )
```


## Using rx.field / rx.Field to improve type hinting for vars

When defining state variables you can use `rx.Field[T]` to annotate the variable's type. Then, you can initialize the variable using `rx.field(default_value)`, where `default_value` is an instance of type `T`. 

This approach makes the variable's type explicit, aiding static analysis tools in type checking. In addition, it shows you what methods are allowed to modify the variable in your frontend code, as they are listed in the type hint.

Below are two examples:

```python
import reflex as rx

app = rx.App()


class State(rx.State):
    x: rx.Field[bool] = rx.field(False)

    def flip(self):
        self.x = not self.x


@app.add_page
def index():
    return rx.vstack(
        rx.button("Click me", on_click=State.flip),
        rx.text(State.x),
        rx.text(~State.x),
    )
```

Here `State.x`, as it is typed correctly as a `boolean` var, gets better code completion, i.e. here we get options such as `to_string()` or `equals()`.


```python
import reflex as rx

app = rx.App()


class State(rx.State):
    x: rx.Field[dict[str, list[int]]] = rx.field(\{})


@app.add_page
def index():
    return rx.vstack(
        rx.text(State.x.values()[0][0]),
    )
```

Here `State.x`, as it is typed correctly as a `dict` of `str` to `list` of `int` var, gets better code completion, i.e. here we get options such as `contains()`, `keys()`, `values()`, `items()` or `merge()`.
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/vars/custom_vars.md`:

```md

# Custom Vars

As mentioned in the [vars page]({vars.base_vars.path}), Reflex vars must be JSON serializable.

This means we can support any Python primitive types, as well as lists, dicts, and tuples. However, you can also create more complex var types by inheriting from `rx.Base` or decorating them as dataclasses with `@dataclasses.dataclass`.

## Defining a Type

In this example, we will create a custom var type for storing translations.

Once defined, we can use it as a state var, and reference it from within a component.

```python demo exec
import googletrans

class Translation(rx.Base):
    original_text: str
    translated_text: str

class TranslationState(rx.State):
    input_text: str = "Hola Mundo"
    current_translation: Translation = Translation(original_text="", translated_text="")

    @rx.event
    def translate(self):
        self.current_translation.original_text = self.input_text
        self.current_translation.translated_text = googletrans.Translator().translate(self.input_text, dest="en").text

def translation_example():
    return rx.vstack(
        rx.input(on_blur=TranslationState.setvar("input_text"), default_value=TranslationState.input_text, placeholder="Text to translate...",),
        rx.button("Translate", on_click=TranslationState.translate),
        rx.text(TranslationState.current_translation.translated_text),
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/vars/var-operations.md`:

```md

# Var Operations

Var operations transform the placeholder representation of the value on the
frontend and provide a way to perform basic operations on the Var without having
to define a computed var.

Within your frontend components, you cannot use arbitrary Python functions on
the state vars. For example, the following code will **not work.**

```python
class State(rx.State):
    number: int

def index():
    # This will be compiled before runtime, before `State.number` has a known value.
    # Since `float` is not a valid var operation, this will throw an error.
    rx.text(float(State.number))
```

This is because we compile the frontend to Javascript, but the value of `State.number`
is only known at runtime.

In this example below we use a var operation to concatenate a `string` with a `var`, meaning we do not have to do in within state as a computed var.

```python demo exec
coins = ["BTC", "ETH", "LTC", "DOGE"]

class VarSelectState(rx.State):
    selected: str = "DOGE"

def var_operations_example():
    return rx.vstack(
        # Using a var operation to concatenate a string with a var.
        rx.heading("I just bought a bunch of " + VarSelectState.selected),
        # Using an f-string to interpolate a var.
        rx.text(f"{VarSelectState.selected} is going to the moon!"),
        rx.select(
            coins,
            value=VarSelectState.selected,
            on_change=VarSelectState.set_selected,
        )
    )
```

```md alert success
# Vars support many common operations.

They can be used for arithmetic, string concatenation, inequalities, indexing, and more. See the [full list of supported operations](/docs/api-reference/var/).
```

## Supported Operations

Var operations allow us to change vars on the front-end without having to create more computed vars on the back-end in the state.

Some simple examples are the `==` var operator, which is used to check if two vars are equal and the `to_string()` var operator, which is used to convert a var to a string.

```python demo exec

fruits = ["Apple", "Banana", "Orange", "Mango"]

class EqualsState(rx.State):
    selected: str = "Apple"
    favorite: str = "Banana"


def var_equals_example():
    return rx.vstack(
        rx.text(EqualsState.favorite.to_string() + "is my favorite fruit!"),
        rx.select(
            fruits,
            value=EqualsState.selected,
            on_change=EqualsState.set_selected,
        ),
        rx.cond(
            EqualsState.selected == EqualsState.favorite,
            rx.text("The selected fruit is equal to the favorite fruit!"),
            rx.text("The selected fruit is not equal to the favorite fruit."),
        ),
    )

```

### Negate, Absolute and Length

The `-` operator is used to get the negative version of the var. The `abs()` operator is used to get the absolute value of the var. The `.length()` operator is used to get the length of a list var.

```python demo exec
import random

class OperState(rx.State):
    number: int
    numbers_seen: list = []

    @rx.event
    def update(self):
        self.number = random.randint(-100, 100)
        self.numbers_seen.append(self.number)

def var_operation_example():
    return rx.vstack(
        rx.heading(f"The number: {OperState.number}", size="3"),
        rx.hstack(
            rx.text("Negated:", rx.badge(-OperState.number, variant="soft", color_scheme="green")),
            rx.text(f"Absolute:", rx.badge(abs(OperState.number), variant="soft", color_scheme="blue")),
            rx.text(f"Numbers seen:", rx.badge(OperState.numbers_seen.length(), variant="soft", color_scheme="red")),
        ),
        rx.button("Update", on_click=OperState.update),
    )
```

### Comparisons and Mathematical Operators

All of the comparison operators are used as expected in python. These include `==`, `!=`, `>`, `>=`, `<`, `<=`.

There are operators to add two vars `+`, subtract two vars `-`, multiply two vars `*` and raise a var to a power `pow()`.

```python demo exec
import random

class CompState(rx.State):
    number_1: int
    number_2: int

    @rx.event
    def update(self):
        self.number_1 = random.randint(-10, 10)
        self.number_2 = random.randint(-10, 10)

def var_comparison_example():

    return rx.vstack(
                rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Integer 1"),
                    rx.table.column_header_cell("Integer 2"),
                    rx.table.column_header_cell("Operation"),
                    rx.table.column_header_cell("Outcome"),
                ),
            ),
            rx.table.body(
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("Int 1 == Int 2"),
                    rx.table.cell((CompState.number_1 == CompState.number_2).to_string()),
                ),
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("Int 1 != Int 2"),
                    rx.table.cell((CompState.number_1 != CompState.number_2).to_string()),
                ),
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("Int 1 > Int 2"),
                    rx.table.cell((CompState.number_1 > CompState.number_2).to_string()),
                ),
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("Int 1 >= Int 2"),
                    rx.table.cell((CompState.number_1 >= CompState.number_2).to_string()),
                ),
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2, ),
                    rx.table.cell("Int 1 < Int 2 "),
                    rx.table.cell((CompState.number_1 < CompState.number_2).to_string()),
                ),
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("Int 1 <= Int 2"),
                    rx.table.cell((CompState.number_1 <= CompState.number_2).to_string()),
                ),

                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("Int 1 + Int 2"),
                    rx.table.cell(f"{(CompState.number_1 + CompState.number_2)}"),
                ),
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("Int 1 - Int 2"),
                    rx.table.cell(f"{CompState.number_1 - CompState.number_2}"),
                ),
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("Int 1 * Int 2"),
                    rx.table.cell(f"{CompState.number_1 * CompState.number_2}"),
                ),
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("pow(Int 1, Int2)"),
                    rx.table.cell(f"{pow(CompState.number_1, CompState.number_2)}"),
                ),
            ),
            width="100%",
        ),
        rx.button("Update", on_click=CompState.update),
    )
```

### True Division, Floor Division and Remainder

The operator `/` represents true division. The operator `//` represents floor division. The operator `%` represents the remainder of the division.

```python demo exec
import random

class DivState(rx.State):
    number_1: float = 3.5
    number_2: float = 1.4

    @rx.event
    def update(self):
        self.number_1 = round(random.uniform(5.1, 9.9), 2)
        self.number_2 = round(random.uniform(0.1, 4.9), 2)

def var_div_example():
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Integer 1"),
                    rx.table.column_header_cell("Integer 2"),
                    rx.table.column_header_cell("Operation"),
                    rx.table.column_header_cell("Outcome"),
                ),
            ),
            rx.table.body(
                rx.table.row(
                    rx.table.row_header_cell(DivState.number_1),
                    rx.table.cell(DivState.number_2),
                    rx.table.cell("Int 1 / Int 2"),
                    rx.table.cell(f"{DivState.number_1 / DivState.number_2}"),
                ),
                rx.table.row(
                    rx.table.row_header_cell(DivState.number_1),
                    rx.table.cell(DivState.number_2),
                    rx.table.cell("Int 1 // Int 2"),
                    rx.table.cell(f"{DivState.number_1 // DivState.number_2}"),
                ),
                rx.table.row(
                    rx.table.row_header_cell(DivState.number_1),
                    rx.table.cell(DivState.number_2),
                    rx.table.cell("Int 1 % Int 2"),
                    rx.table.cell(f"{DivState.number_1 % DivState.number_2}"),
                ),
            ),
            width="100%",
        ),
        rx.button("Update", on_click=DivState.update),
    )
```

### And, Or and Not

In Reflex the `&` operator represents the logical AND when used in the front end. This means that it returns true only when both conditions are true simultaneously.
The `|` operator represents the logical OR when used in the front end. This means that it returns true when either one or both conditions are true.
The `~` operator is used to invert a var. It is used on a var of type `bool` and is equivalent to the `not` operator.

```python demo exec
import random

class LogicState(rx.State):
    var_1: bool = True
    var_2: bool = True

    @rx.event
    def update(self):
        self.var_1 = random.choice([True, False])
        self.var_2 = random.choice([True, False])

def var_logical_example():
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Var 1"),
                    rx.table.column_header_cell("Var 2"),
                    rx.table.column_header_cell("Operation"),
                    rx.table.column_header_cell("Outcome"),
                ),
            ),
            rx.table.body(
                rx.table.row(
                    rx.table.row_header_cell(LogicState.var_1.to_string()),
                    rx.table.cell(LogicState.var_2.to_string()),
                    rx.table.cell("Logical AND (&)"),
                    rx.table.cell((LogicState.var_1 & LogicState.var_2).to_string()),
                ),
                rx.table.row(
                    rx.table.row_header_cell(LogicState.var_1.to_string()),
                    rx.table.cell(LogicState.var_2.to_string()),
                    rx.table.cell("Logical OR (|)"),
                    rx.table.cell((LogicState.var_1 | LogicState.var_2).to_string()),
                ),
                rx.table.row(
                    rx.table.row_header_cell(LogicState.var_1.to_string()),
                    rx.table.cell(LogicState.var_2.to_string()),
                    rx.table.cell("The invert of Var 1 (~)"),
                    rx.table.cell((~LogicState.var_1).to_string()),
                ),

            ),
            width="100%",
        ),
        rx.button("Update", on_click=LogicState.update),
    )
```

### Contains, Reverse and Join

The 'in' operator is not supported for Var types, we must use the `Var.contains()` instead. When we use `contains`, the var must be of type: `dict`, `list`, `tuple` or `str`.
`contains` checks if a var contains the object that we pass to it as an argument.

We use the `reverse` operation to reverse a list var. The var must be of type `list`.

Finally we use the `join` operation to join a list var into a string.

```python demo exec
class ListsState(rx.State):
    list_1: list = [1, 2, 3, 4, 6]
    list_2: list = [7, 8, 9, 10]
    list_3: list = ["p","y","t","h","o","n"]

def var_list_example():
    return rx.hstack(
        rx.vstack(
            rx.heading(f"List 1: {ListsState.list_1}", size="3"),
            rx.text(f"List 1 Contains 3: {ListsState.list_1.contains(3)}"),
        ),
        rx.vstack(
            rx.heading(f"List 2: {ListsState.list_2}", size="3"),
            rx.text(f"Reverse List 2: {ListsState.list_2.reverse()}"),
        ),
        rx.vstack(
            rx.heading(f"List 3: {ListsState.list_3}", size="3"),
            rx.text(f"List 3 Joins: {ListsState.list_3.join()}"),
        ),
    )
```

### Lower, Upper, Split

The `lower` operator converts a string var to lowercase. The `upper` operator converts a string var to uppercase. The `split` operator splits a string var into a list.

```python demo exec
class StringState(rx.State):
    string_1: str = "PYTHON is FUN"
    string_2: str = "react is hard"


def var_string_example():
    return rx.hstack(
        rx.vstack(
            rx.heading(f"List 1: {StringState.string_1}", size="3"),
            rx.text(f"List 1 Lower Case: {StringState.string_1.lower()}"),
        ),
        rx.vstack(
            rx.heading(f"List 2: {StringState.string_2}", size="3"),
            rx.text(f"List 2 Upper Case: {StringState.string_2.upper()}"),
            rx.text(f"Split String 2: {StringState.string_2.split()}"),
        ),
    )
```

## Get Item (Indexing)

Indexing is only supported for strings, lists, tuples, dicts, and dataframes. To index into a state var strict type annotations are required.

```python
class GetItemState1(rx.State):
    list_1: list = [50, 10, 20]

def get_item_error_1():
    return rx.progress(value=GetItemState1.list_1[0])
```

In the code above you would expect to index into the first index of the list_1 state var. In fact the code above throws the error: `Invalid var passed for prop value, expected type <class 'int'>, got value of type typing.Any.` This is because the type of the items inside the list have not been clearly defined in the state. To fix this you change the list_1 definition to `list_1: list[int] = [50, 10, 20]`

```python demo exec
class GetItemState1(rx.State):
    list_1: list[int] = [50, 10, 20]

def get_item_error_1():
    return rx.progress(value=GetItemState1.list_1[0])
```

### Using with Foreach

Errors frequently occur when using indexing and `foreach`.

```python
class ProjectsState(rx.State):
    projects: List[dict] = [
        {
            "technologies": ["Next.js", "Prisma", "Tailwind", "Google Cloud", "Docker", "MySQL"]
        },
        {
            "technologies": ["Python", "Flask", "Google Cloud", "Docker"]
        }
    ]

def get_badge(technology: str) -> rx.Component:
    return rx.badge(technology, variant="soft", color_scheme="green")

def project_item(project: dict):
    return rx.box(
        rx.hstack(
            rx.foreach(project["technologies"], get_badge)
        ),
    )

def failing_projects_example() -> rx.Component:
    return rx.box(rx.foreach(ProjectsState.projects, project_item))
```

The code above throws the error `TypeError: Could not foreach over var of type Any. (If you are trying to foreach over a state var, add a type annotation to the var.)`

We must change `projects: list[dict]` => `projects: list[dict[str, list]]` because while projects is annotated, the item in project["technologies"] is not.

```python demo exec
class ProjectsState(rx.State):
    projects: list[dict[str, list]] = [
        {
            "technologies": ["Next.js", "Prisma", "Tailwind", "Google Cloud", "Docker", "MySQL"]
        },
        {
            "technologies": ["Python", "Flask", "Google Cloud", "Docker"]
        }
    ]


def projects_example() -> rx.Component:
    def get_badge(technology: str) -> rx.Component:
        return rx.badge(technology, variant="soft", color_scheme="green")

    def project_item(project: dict) -> rx.Component:

        return rx.box(
            rx.hstack(
                rx.foreach(project["technologies"], get_badge)
            ),
        )
    return rx.box(rx.foreach(ProjectsState.projects, project_item))
```

The previous example had only a single type for each of the dictionaries `keys` and `values`. For complex multi-type data, you need to use a dataclass, as shown below.

```python demo exec
import dataclasses

@dataclasses.dataclass
class ActressType:
    actress_name: str
    age: int
    pages: list[dict[str, str]]

class MultiDataTypeState(rx.State):
    """The app state."""
    actresses: list[ActressType] = [
        ActressType(
            actress_name="Ariana Grande",
            age=30,
            pages=[
                {"url": "arianagrande.com"}, {"url": "https://es.wikipedia.org/wiki/Ariana_Grande"}
            ]
        ),
        ActressType(
            actress_name="Gal Gadot",
            age=38,
            pages=[
                {"url": "http://www.galgadot.com/"}, {"url": "https://es.wikipedia.org/wiki/Gal_Gadot"}
            ]
        )
    ]

def actresses_example() -> rx.Component:
    def showpage(page: dict[str, str]):
        return rx.vstack(
            rx.text(page["url"]),
        )

    def showlist(item: ActressType):
        return rx.vstack(
            rx.hstack(
                rx.text(item.actress_name),
                rx.text(item.age),
            ),
            rx.foreach(item.pages, showpage),
        )
    return rx.box(rx.foreach(MultiDataTypeState.actresses, showlist))

```

Setting the type of `actresses` to be `actresses: list[dict[str,str]]` would fail as it cannot be understood that the `value` for the `pages key` is actually a `list`.

## Combine Multiple Var Operations

You can also combine multiple var operations together, as seen in the next example.

```python demo exec
import random

class VarNumberState(rx.State):
    number: int

    @rx.event
    def update(self):
        self.number = random.randint(0, 100)

def var_number_example():
    return rx.vstack(
        rx.heading(f"The number is {VarNumberState.number}", size="5"),
        # Var operations can be composed for more complex expressions.
        rx.cond(
            VarNumberState.number % 2 == 0,
            rx.text("Even", color="green"),
            rx.text("Odd", color="red"),
        ),
        rx.button("Update", on_click=VarNumberState.update),
    )
```

We could have made a computed var that returns the parity of `number`, but
it can be simpler just to use a var operation instead.

Var operations may be generally chained to make compound expressions, however
some complex transformations not supported by var operations must use computed vars
to calculate the value on the backend.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/vars/computed_vars.md`:

```md

# Computed Vars

Computed vars have values derived from other properties on the backend. They are
defined as methods in your State class with the `@rx.var` decorator. A computed
var is recomputed every time an event is processed in your app.

Try typing in the input box and clicking out.

```python demo exec id=upper
class UppercaseState(rx.State):
    text: str = "hello"

    @rx.var
    def upper_text(self) -> str:
        # This will be recomputed whenever `text` changes.
        return self.text.upper()


def uppercase_example():
    return rx.vstack(
        rx.heading(UppercaseState.upper_text),
        rx.input(on_blur=UppercaseState.set_text, placeholder="Type here..."),
    )
```

Here, `upper_text` is a computed var that always holds the upper case version of `text`.

We recommend always using type annotations for computed vars.

## Cached Vars

A cached var, decorated as `@rx.var(cache=True)` is a special type of computed var
that is only recomputed when the other state vars it depends on change. This is
useful for expensive computations, but in some cases it may not update when you
expect it to.
Previous versions of Reflex had a `@rx.cached_var` decorator, which is now replaced
by the new `cache` argument of `@rx.var`.

```python demo exec
class CachedVarState(rx.State):
    counter_a: int = 0
    counter_b: int = 0

    @rx.var
    def last_touch_time(self) -> str:
        # This is updated anytime the state is updated.
        return time.strftime("%H:%M:%S")

    @rx.event
    def increment_a(self):
        self.counter_a += 1

    @rx.var(cache=True)
    def last_counter_a_update(self) -> str:
        # This is updated only when `counter_a` changes.
        return f"{self.counter_a} at {time.strftime('%H:%M:%S')}"

    @rx.event
    def increment_b(self):
        self.counter_b += 1

    @rx.var(cache=True)
    def last_counter_b_update(self) -> str:
        # This is updated only when `counter_b` changes.
        return f"{self.counter_b} at {time.strftime('%H:%M:%S')}"


def cached_var_example():
    return rx.vstack(
        rx.text(f"State touched at: {CachedVarState.last_touch_time}"),
        rx.text(f"Counter A: {CachedVarState.last_counter_a_update}"),
        rx.text(f"Counter B: {CachedVarState.last_counter_b_update}"),
        rx.hstack(
            rx.button("Increment A", on_click=CachedVarState.increment_a),
            rx.button("Increment B", on_click=CachedVarState.increment_b),
        ),
    )
```

In this example `last_touch_time` is a normal computed var, which updates any
time the state is modified. `last_counter_a_update` is a computed var that only
depends on `counter_a`, so it only gets recomputed when `counter_a` has changes.
Similarly `last_counter_b_update` only depends on `counter_b`, and thus is
updated only when `counter_b` changes.

```