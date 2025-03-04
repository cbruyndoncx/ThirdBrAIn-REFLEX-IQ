Project Path: substates

Source Tree:

```
substates
├── overview.md
└── component_state.md

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/substates/overview.md`:

```md

# Substates

Substates allow you to break up your state into multiple classes to make it more manageable. This is useful as your app
grows, as it allows you to think about each page as a separate entity. Substates also allow you to share common state
resources, such as variables or event handlers.

When a particular state class becomes too large, breaking it up into several substates can bring performance
benefits by only loading parts of the state that are used to handle a certain event.

## Multiple States

One common pattern is to create a substate for each page in your app.
This allows you to think about each page as a separate entity, and makes it easier to manage your code as your app grows.

To create a substate, simply inherit from `rx.State` multiple times:

```python
# index.py
import reflex as rx

class IndexState(rx.State):
    """Define your main state here."""
    data: str = "Hello World"


@rx.page()
def index():
    return rx.box(rx.text(IndexState.data)

# signup.py
import reflex as rx


class SignupState(rx.State):
    """Define your signup state here."""
    username: str = ""
    password: str = ""

    def signup(self):
        ...


@rx.page()
def signup_page():
    return rx.box(
        rx.input(value=SignupState.username),
        rx.input(value=SignupState.password),
    )

# login.py
import reflex as rx

class LoginState(rx.State):
    """Define your login state here."""
    username: str = ""
    password: str = ""

    def login(self):
        ...

@rx.page()
def login_page():
    return rx.box(
        rx.input(value=LoginState.username),
        rx.input(value=LoginState.password),
    )
```

Separating the states is purely a matter of organization. You can still access the state from other pages by importing the state class.

```python
# index.py

import reflex as rx

from signup import SignupState

...

def index():
    return rx.box(
        rx.text(IndexState.data),
        rx.input(value=SignupState.username),
        rx.input(value=SignupState.password),
    )
```

## State Inheritance

A substate can also inherit from another substate other than `rx.State`, allowing you to create a hierarchy of states.

For example, you can create a base state that defines variables and event handlers that are common to all pages in your app, such as the current logged in user.

```python
class BaseState(rx.State):
    """Define your base state here."""

    current_user: str = ""

    def logout(self):
        self.current_user = ""


class LoginState(BaseState):
    """Define your login state here."""

    username: str = ""
    password: str = ""

    def login(self, username, password):
        # authenticate
        authenticate(...)

        # Set the var on the parent state.
        self.current_user = username
```

You can access the parent state properties from a child substate automatically.

## Accessing Arbitrary States

An event handler in a particular state can access and modify vars in another state instance by calling
the `get_state` async method and passing the desired state class. If the requested state is not already loaded,
it will be loaded and deserialized on demand.

In the following example, the `GreeterState` accesses the `SettingsState` to get the `salutation` and uses it
to update the `message` var.

Notably, the widget that sets the salutation does NOT have to load the `GreeterState` when handling the
input `on_change` event, which improves performance.

```python demo exec
class SettingsState(rx.State):
     salutation: str = "Hello"


def set_salutation_popover():
    return rx.popover.root(
        rx.popover.trigger(
            rx.icon_button(rx.icon("settings")),
        ),
        rx.popover.content(
            rx.input(
                value=SettingsState.salutation,
                on_change=SettingsState.set_salutation
            ),
        ),
    )


class GreeterState(rx.State):
    message: str = ""

    @rx.event
    async def handle_submit(self, form_data: dict[str, Any]):
        settings = await self.get_state(SettingsState)
        self.message = f"{settings.salutation} {form_data['name']}"


def index():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(placeholder="Name", id="name"),
                    set_salutation_popover(),
                ),
                rx.button("Submit"),
            ),
            reset_on_submit=True,
            on_submit=GreeterState.handle_submit,
        ),
        rx.text(GreeterState.message),
    )
```

## Performance Implications

When an event handler is called, Reflex will load the data not only for the substate containing
the event handler, but also all of its substates and parent states as well.
If a state has a large number of substates or contains a large amount of data, it can slow down processing
of events associated with that state.

For optimal performance, keep a flat structure with most substate classes directly inheriting from `rx.State`.
Only inherit from another state when the parent holds data that is commonly used by the substate.
Implementing different parts of the app with separate, unconnected states ensures that only the necessary
data is loaded for processing events for a particular page or component.

Avoid defining computed vars inside a state that contains a large amount of data, as
states with computed vars are always loaded to ensure the values are recalculated.
When using computed vars, it better to define them in a state that directly inherits from `rx.State` and
does not have other states inheriting from it, to avoid loading unnecessary data.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/substates/component_state.md`:

```md

# Component State

_New in version 0.4.6_.

Defining a subclass of `rx.ComponentState` creates a special type of state that is tied to an
instance of a component, rather than existing globally in the app. A Component State combines
[UI code]({ui.overview.path}) with state [Vars]({vars.base_vars.path}) and
[Event Handlers]({events.events_overview.path}),
and is useful for creating reusable components which operate independently of each other.

## Using ComponentState

```python demo exec
class ReusableCounter(rx.ComponentState):
    count: int = 0

    @rx.event
    def increment(self):
        self.count += 1

    @rx.event
    def decrement(self):
        self.count -= 1

    @classmethod
    def get_component(cls, **props):
        return rx.hstack(
            rx.button("Decrement", on_click=cls.decrement),
            rx.text(cls.count),
            rx.button("Increment", on_click=cls.increment),
            **props,
        )

reusable_counter = ReusableCounter.create

def multiple_counters():
    return rx.vstack(
        reusable_counter(),
        reusable_counter(),
        reusable_counter(),
    )
```

The vars and event handlers defined on the `ReusableCounter`
class are treated similarly to a normal State class, but will be scoped to the component instance. Each time a
`reusable_counter` is created, a new state class for that instance of the component is also created.

The `get_component` classmethod is used to define the UI for the component and link it up to the State, which
is accessed via the `cls` argument. Other states may also be referenced by the returned component, but
`cls` will always be the instance of the `ComponentState` that is unique to the component being returned.

## Passing Props

Similar to a normal Component, the `ComponentState.create` classmethod accepts the arbitrary
`*children` and `**props` arguments, and by default passes them to your `get_component` classmethod.
These arguments may be used to customize the component, either by applying defaults or
passing props to certain subcomponents.

```python eval
rx.divider()
```

In the following example, we implement an editable text component that allows the user to click on
the text to turn it into an input field. If the user does not provide their own `value` or `on_change`
props, then the defaults defined in the `EditableText` class will be used.

```python demo exec
class EditableText(rx.ComponentState):
    text: str = "Click to edit"
    original_text: str
    editing: bool = False

    @rx.event
    def start_editing(self, original_text: str):
        self.original_text = original_text
        self.editing = True

    @rx.event
    def stop_editing(self):
        self.editing = False
        self.original_text = ""

    @classmethod
    def get_component(cls, **props):
        # Pop component-specific props with defaults before passing **props
        value = props.pop("value", cls.text)
        on_change = props.pop("on_change", cls.set_text)
        cursor = props.pop("cursor", "pointer")

        # Set the initial value of the State var.
        initial_value = props.pop("initial_value", None)
        if initial_value is not None:
            # Update the pydantic model to use the initial value as default.
            cls.__fields__["text"].default = initial_value

        # Form elements for editing, saving and reverting the text.
        edit_controls = rx.hstack(
            rx.input(
                value=value,
                on_change=on_change,
                **props,
            ),
            rx.icon_button(
                rx.icon("x"),
                on_click=[
                    on_change(cls.original_text),
                    cls.stop_editing,
                ],
                type="button",
                color_scheme="red",
            ),
            rx.icon_button(rx.icon("check")),
            align="center",
            width="100%",
        )

        # Return the text or the form based on the editing Var.
        return rx.cond(
            cls.editing,
            rx.form(
                edit_controls,
                on_submit=lambda _: cls.stop_editing(),
            ),
            rx.text(
                value,
                on_click=cls.start_editing(value),
                cursor=cursor,
                **props,
            ),
        )


editable_text = EditableText.create


def editable_text_example():
    return rx.vstack(
        editable_text(),
        editable_text(initial_value="Edit me!", color="blue"),
        editable_text(initial_value="Reflex is fun", font_family="monospace", width="100%"),
    )
```

```python eval
rx.divider()
```

Because this `EditableText` component is designed to be reusable, it can handle the case
where the `value` and `on_change` are linked to a normal global state.


```python demo exec
class EditableTextDemoState(rx.State):
    value: str = "Global state text"


def editable_text_with_global_state():
    return rx.vstack(
        editable_text(value=EditableTextDemoState.value, on_change=EditableTextDemoState.set_value),
        rx.text(EditableTextDemoState.value.upper()),
    )
```

## Accessing the State

The underlying state class of a `ComponentState` is accessible via the `.State` attribute. To use it,
assign an instance of the component to a local variable, then include that instance in the page.


```python demo exec
def counter_sum():
    counter1 = reusable_counter()
    counter2 = reusable_counter()
    return rx.vstack(
        rx.text(f"Total: {counter1.State.count + counter2.State.count}"),
        counter1,
        counter2,
    )
```

```python eval
rx.divider()
```

Other components can also affect a `ComponentState` by referencing its event handlers or vars
via the `.State` attribute.


```python demo exec
def extended_counter():
    counter1 = reusable_counter()
    return rx.vstack(
        counter1,
        rx.hstack(
            rx.icon_button(rx.icon("step_back"), on_click=counter1.State.set_count(0)),
            rx.icon_button(rx.icon("plus"), on_click=counter1.State.increment),
            rx.button("Double", on_click=counter1.State.set_count(counter1.State.count * 2)),
            rx.button("Triple", on_click=counter1.State.set_count(counter1.State.count * 3)),
        ),
    )
```

```