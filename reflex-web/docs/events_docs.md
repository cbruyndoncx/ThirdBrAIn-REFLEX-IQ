Project Path: events

Source Tree:

```
events
├── background_events.md
├── special_events.md
├── event_actions.md
├── events_overview.md
├── chaining_events.md
├── setters.md
├── event_arguments.md
├── yield_events.md
└── page_load_events.md

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/events/background_events.md`:

```md

# Background Tasks

A background task is a special type of `EventHandler` that may run
concurrently with other `EventHandler` functions. This enables long-running
tasks to execute without blocking UI interactivity.

A background task is defined by decorating an async `State` method with
`@rx.event(background=True)`.

```md alert warning
# `@rx.event(background=True)` used to be called `@rx.background`.
In Reflex version 0.6.5 and later, the `@rx.background` decorator has been renamed to `@rx.event(background=True)`.
```

Whenever a background task needs to interact with the state, **it must enter an
`async with self` context block** which refreshes the state and takes an
exclusive lock to prevent other tasks or event handlers from modifying it
concurrently. Because other `EventHandler` functions may modify state while the
task is running, **outside of the context block, Vars accessed by the background
task may be _stale_**. Attempting to modify the state from a background task
outside of the context block will raise an `ImmutableStateError` exception.

In the following example, the `my_task` event handler is decorated with
`@rx.event(background=True)` and increments the `counter` variable every half second, as
long as certain conditions are met. While it is running, the UI remains
interactive and continues to process events normally.

```md alert info
# Background events are similar to simple Task Queues like [Celery](https://www.fullstackpython.com/celery.html) allowing asynchronous events.
```

```python demo exec id=background_demo
import asyncio
import reflex as rx


class MyTaskState(rx.State):
    counter: int = 0
    max_counter: int = 10
    running: bool = False
    _n_tasks: int = 0

    @rx.event
    def set_max_counter(self, value: str):
        self.max_counter = int(value)

    @rx.event(background=True)
    async def my_task(self):
        async with self:
            # The latest state values are always available inside the context
            if self._n_tasks > 0:
                # only allow 1 concurrent task
                return

            # State mutation is only allowed inside context block
            self._n_tasks += 1

        while True:
            async with self:
                # Check for stopping conditions inside context
                if self.counter >= self.max_counter:
                    self.running = False
                if not self.running:
                    self._n_tasks -= 1
                    return

                self.counter += 1

            # Await long operations outside the context to avoid blocking UI
            await asyncio.sleep(0.5)

    @rx.event
    def toggle_running(self):
        self.running = not self.running
        if self.running:
            return MyTaskState.my_task

    @rx.event
    def clear_counter(self):
        self.counter = 0


def background_task_example():
    return rx.hstack(
        rx.heading(MyTaskState.counter, " /"),
        rx.input(
            value=MyTaskState.max_counter,
            on_change=MyTaskState.set_max_counter,
            width="8em",
        ),
        rx.button(
            rx.cond(~MyTaskState.running, "Start", "Stop"),
            on_click=MyTaskState.toggle_running,
        ),
        rx.button(
            "Reset",
            on_click=MyTaskState.clear_counter,
        ),
    )
```

## Task Lifecycle

When a background task is triggered, it starts immediately, saving a reference to
the task in `app.background_tasks`. When the task completes, it is removed from
the set.

Multiple instances of the same background task may run concurrently, and the
framework makes no attempt to avoid duplicate tasks from starting.

It is up to the developer to ensure that duplicate tasks are not created under
the circumstances that are undesirable. In the example above, the `_n_tasks`
backend var is used to control whether `my_task` will enter the increment loop,
or exit early.

## Background Task Limitations

Background tasks mostly work like normal `EventHandler` methods, with certain exceptions:

- Background tasks must be `async` functions.
- Background tasks cannot modify the state outside of an `async with self` context block.
- Background tasks may read the state outside of an `async with self` context block, but the value may be stale.
- Background tasks may not be directly called from other event handlers or background tasks. Instead use `yield` or `return` to trigger the background task.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/events/special_events.md`:

```md

# Special Events

Reflex also has built-in special events can be found in the [reference]({api_reference.special_events.path}).

For example, an event handler can trigger an alert on the browser.

```python demo exec
class SpecialEventsState(rx.State):
    @rx.event
    def alert(self):
        return rx.window_alert("Hello World!")

def special_events_example():
    return rx.button("Alert", on_click=SpecialEventsState.alert)
```

Special events can also be triggered directly in the UI by attaching them to an event trigger.

```python
def special_events_example():
    return rx.button("Alert", on_click=rx.window_alert("Hello World!"))
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/events/event_actions.md`:

```md

# Event Actions

In Reflex, an event action is a special behavior that occurs during or after
processing an event on the frontend.

Event actions can modify how the browser handles DOM events or throttle and
debounce events before they are processed by the backend.

An event action is specified by accessing attributes and methods present on all
EventHandlers and EventSpecs.

## DOM Event Propagation

_Added in v0.3.2_

### prevent_default

The `.prevent_default` action prevents the default behavior of the browser for
the action. This action can be added to any existing event, or it can be used on its own by
specifying `rx.prevent_default` as an event handler.

A common use case for this is to prevent navigation when clicking a link.

```python demo
rx.link("This Link Does Nothing", href="https://reflex.dev/", on_click=rx.prevent_default)
```

```python demo exec
class LinkPreventDefaultState(rx.State):
    status: bool = False

    @rx.event
    def toggle_status(self):
        self.status = not self.status

def prevent_default_example():
    return rx.vstack(
        rx.heading(f"The value is {LinkPreventDefaultState.status}"),
        rx.link(
            "Toggle Value",
            href="https://reflex.dev/",
            on_click=LinkPreventDefaultState.toggle_status.prevent_default,
        ),
    )
```

### stop_propagation

The `.stop_propagation` action stops the event from propagating to parent elements.

This action is often used when a clickable element contains nested buttons that
should not trigger the parent element's click event.

In the following example, the first button uses `.stop_propagation` to prevent
the click event from propagating to the outer vstack. The second button does not
use `.stop_propagation`, so the click event will also be handled by the on_click
attached to the outer vstack.

```python demo exec
class StopPropagationState(rx.State):
    where_clicked: list[str] = []

    @rx.event
    def handle_click(self, where: str):
        self.where_clicked.append(where)

    @rx.event
    def handle_reset(self):
        self.where_clicked = []

def stop_propagation_example():
    return rx.vstack(
        rx.button(
            "btn1 - Stop Propagation",
            on_click=StopPropagationState.handle_click("btn1").stop_propagation,
        ),
        rx.button(
            "btn2 - Normal Propagation",
            on_click=StopPropagationState.handle_click("btn2"),
        ),
        rx.foreach(StopPropagationState.where_clicked, rx.text),
        rx.button(
            "Reset",
            on_click=StopPropagationState.handle_reset.stop_propagation,
        ),
        padding="2em",
        border=f"1px dashed {rx.color('accent', 5)}",
        on_click=StopPropagationState.handle_click("outer")
    )
```

## Throttling and Debounce

_Added in v0.5.0_

For events that are fired frequently, it can be useful to throttle or debounce
them to avoid network latency and improve performance. These actions both take a
single argument which specifies the delay time in milliseconds.

### throttle

The `.throttle` action limits the number of times an event is processed within a
a given time period. It is useful for `on_scroll` and `on_mouse_move` events which are
fired very frequently, causing lag when handling them in the backend.

```md alert warning
# Throttled events are discarded.

There is no eventual delivery of any event that is triggered while the throttle
period is active. Throttle is not appropriate for events when the final payload
contains data that must be processed, like `on_change`.
```

In the following example, the `on_scroll` event is throttled to only fire every half second.

```python demo exec
class ThrottleState(rx.State):
    last_scroll: datetime.datetime | None

    @rx.event
    def handle_scroll(self):
        self.last_scroll = datetime.datetime.now(datetime.timezone.utc)

def scroll_box():
    return rx.scroll_area(
        rx.heading("Scroll Me"),
        *[rx.text(f"Item {i}") for i in range(100)],
        height="75px",
        width="50%",
        border=f"1px solid {rx.color('accent', 5)}",
        on_scroll=ThrottleState.handle_scroll.throttle(500),
    )

def throttle_example():
    return (
        scroll_box(),
        rx.text(
            f"Last Scroll Event: ",
            rx.moment(ThrottleState.last_scroll, format="HH:mm:ss.SSS"),
        ),
    )
```

```md alert info
# Event Actions are Chainable

Event actions can be chained together to create more complex event handling
behavior. For example, you can throttle an event and prevent its default
behavior in the same event handler: `on_click=MyState.handle_click.throttle(500).prevent_default`.
```

### debounce

The `.debounce` action delays the processing of an event until the specified
timeout occurs. If another event is triggered during the timeout, the timer is
reset and the original event is discarded.

Debounce is useful for handling the final result of a series of events, such as
moving a slider.

```md alert warning
# Debounced events are discarded.

When a new event is triggered during the debounce period, the original event is
discarded. Debounce is not appropriate for events where each payload contains
unique data that must be processed, like `on_key_down`.
```

In the following example, the slider's `on_change` handler, `update_value`, is
only triggered on the backend when the slider value has not changed for half a
second.

```python demo exec
class DebounceState(rx.State):
    settled_value: int = 50

    @rx.event
    def update_value(self, value: list[int]):
        self.settled_value = value[0]


def debounced_slider():
    return rx.slider(
        key=rx.State.router.session.session_id,
        default_value=[DebounceState.settled_value],
        on_change=DebounceState.update_value.debounce(500),
        width="100%",
    )

def debounce_example():
    return rx.vstack(
        debounced_slider(),
        rx.text(f"Settled Value: {DebounceState.settled_value}"),
    )
```

```md alert info
# Why set key on the slider?

Setting `key` to the `session_id` with a dynamic `default_value` ensures that
when the page is refreshed, the component will be re-rendered to reflect the
updated default_value from the state.

Without the `key` set, the slider would always display the original
`settled_value` after a page reload, instead of its current value.
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/events/events_overview.md`:

```md

# Events Overview

Events are composed of two parts: Event Triggers and Event Handlers.

- **Events Handlers** are how the State of a Reflex application is updated. They are triggered by user interactions with the UI, such as clicking a button or hovering over an element. Events can also be triggered by the page loading or by other events.

- **Event triggers** are component props that create an event to be sent to an event handler.
Each component supports a set of events triggers. They are described in each [component's documentation]({library.path}) in the event trigger section.


## Example 
Lets take a look at an example below. Try mousing over the heading to change the word.

```python demo exec
class WordCycleState(rx.State):
    # The words to cycle through.
    text: list[str] = ["Welcome", "to", "Reflex", "!"]

    # The index of the current word.
    index: int = 0

    @rx.event
    def next_word(self):
        self.index = (self.index + 1) % len(self.text)

    @rx.var
    def get_text(self) -> str:
        return self.text[self.index]

def event_triggers_example():
    return rx.heading(
        WordCycleState.get_text,
        on_mouse_over=WordCycleState.next_word,
        color="green",
    )

```

In this example, the heading component has the **event trigger**, `on_mouse_over`.
Whenever the user hovers over the heading, the `next_word` **event handler** will be called to cycle the word. Once the handler returns, the UI will be updated to reflect the new state.

Adding the `@rx.event` decorator above the event handler is strongly recommended. This decorator enables proper static type checking, which ensures event handlers receive the correct number and types of arguments.

# What in this section?

In the event section of the documentation, you will explore the different types of events supported by Reflex, along with the different ways to call them.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/events/chaining_events.md`:

```md

# Chaining events

## Calling Event Handlers From Event Handlers

You can call other event handlers from event handlers to keep your code modular. Just use the `self.call_handler` syntax to run another event handler. As always, you can yield within your function to send incremental updates to the frontend.

```python demo exec id=call-handler
import asyncio

class CallHandlerState(rx.State):
    count: int = 0
    progress: int = 0

    @rx.event
    async def run(self):
        # Reset the count.
        self.set_progress(0)
        yield

        # Count to 10 while showing progress.
        for i in range(10):
            # Wait and increment.
            await asyncio.sleep(0.5)
            self.count += 1

            # Update the progress.
            self.set_progress(i + 1)

            # Yield to send the update.
            yield


def call_handler_example():
    return rx.vstack(
        rx.badge(CallHandlerState.count, font_size="1.5em", color_scheme="green"),
        rx.progress(value=CallHandlerState.progress, max=10, width="100%"),
        rx.button("Run", on_click=CallHandlerState.run),
    )
```

## Returning Events From Event Handlers

So far, we have only seen events that are triggered by components. However, an event handler can also return events.

In Reflex, event handlers run synchronously, so only one event handler can run at a time, and the events in the queue will be blocked until the current event handler finishes.The difference between returning an event and calling an event handler is that returning an event will send the event to the frontend and unblock the queue.

```md alert info
# Be sure to use the class name `State` (or any substate) rather than `self` when returning events.
```

Try entering an integer in the input below then clicking out.

```python demo exec id=collatz
class CollatzState(rx.State):
    count: int = 1

    @rx.event
    def start_collatz(self, count: str):
        """Run the collatz conjecture on the given number."""
        self.count = abs(int(count if count else 1))
        return CollatzState.run_step

    @rx.event
    async def run_step(self):
        """Run a single step of the collatz conjecture."""

        while self.count > 1:

            await asyncio.sleep(0.5)

            if self.count % 2 == 0:
                # If the number is even, divide by 2.
                self.count /= 2
            else:
                # If the number is odd, multiply by 3 and add 1.
                self.count = self.count * 3 + 1
            yield


def collatz_example():
    return rx.vstack(
        rx.badge(CollatzState.count, font_size="1.5em", color_scheme="green"),
        rx.input(on_blur=CollatzState.start_collatz),
    )

```

In this example, we run the [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) on a number entered by the user.

When the `on_blur` event is triggered, the event handler `start_collatz` is called. It sets the initial count, then calls `run_step` which runs until the count reaches `1`.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/events/setters.md`:

```md

# Setters

Every base var has a built-in event handler to set it's value for convenience, called `set_VARNAME`.

Say you wanted to change the value of the select component. You could write your own event handler to do this:

```python demo exec

options: list[str] = ["1", "2", "3", "4"]
class SetterState1(rx.State):
    selected: str = "1"

    @rx.event
    def change(self, value):
        self.selected = value


def code_setter():
    return rx.vstack(
        rx.badge(SetterState1.selected, color_scheme="green"),
        rx.select(
            options,
            on_change= lambda value: SetterState1.change(value),
        )
    )

```

Or you could could use a built-in setter for conciseness.

```python demo exec

options: list[str] = ["1", "2", "3", "4"]
class SetterState2(rx.State):
    selected: str = "1"

def code_setter_2():
    return rx.vstack(
        rx.badge(SetterState2.selected, color_scheme="green"),
        rx.select(
            options,
            on_change= SetterState2.set_selected,
        )
    )
```

In this example, the setter for `selected` is `set_selected`. Both of these examples are equivalent.

Setters are a great way to make your code more concise. But if you want to do something more complicated, you can always write your own function in the state.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/events/event_arguments.md`:

```md

# Event Arguments

The event handler signature needs to match the event trigger definition argument count. If the event handler takes two arguments, the event trigger must be able to provide two arguments.

Here is a simple example:

```python demo exec

class EventArgStateSlider(rx.State):
    value: int = 50

    @rx.event
    def set_end(self, value: list[int]):
        self.value = value[0]


def slider_max_min_step():
    return rx.vstack(
        rx.heading(EventArgStateSlider.value),
        rx.slider(
            default_value=40,
            on_value_commit=EventArgStateSlider.set_end,
        ),
        width="100%",
    )

```

The event trigger here is `on_value_commit` and it is called when the value changes at the end of an interaction. This event trigger passes one argument, which is the value of the slider. The event handler which is triggered by the event trigger must therefore take one argument, which is `value` here.

Here is a form example:

```python demo exec

class EventArgState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def event_arg_example():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Name",
                    name="name",
                ),
                rx.checkbox("Checked", name="check"),
                rx.button("Submit", type="submit"),
            ),
            on_submit=EventArgState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(EventArgState.form_data.to_string()),
    )
```

In this example the event trigger is the `on_submit` event of the form. The event handler is `handle_submit`. The `on_submit` event trigger passes one argument, the form data as a dictionary, to the `handle_submit` event handler. The `handle_submit` event handler must take one argument because the `on_submit` event trigger passes one argument.

When the number of args accepted by an EventHandler differs from that provided by the event trigger, an `EventHandlerArgMismatch` error will be raised.

## Pass Additional Arguments to Event Handlers

In some use cases, you want to pass additional arguments to your event handlers. To do this you can bind an event trigger to a lambda, which can call your event handler with the arguments you want.

Try typing a color in an input below and clicking away from it to change the color of the input.

```python demo exec
class ArgState(rx.State):
    colors: list[str] = ["rgba(245,168,152)", "MediumSeaGreen", "#DEADE3"]

    @rx.event
    def change_color(self, color: str, index: int):
        self.colors[index] = color

def event_arguments_example():
    return rx.hstack(
        rx.input(default_value=ArgState.colors[0], on_blur=lambda c: ArgState.change_color(c, 0), bg=ArgState.colors[0]),
        rx.input(default_value=ArgState.colors[1], on_blur=lambda c: ArgState.change_color(c, 1), bg=ArgState.colors[1]),
        rx.input(default_value=ArgState.colors[2], on_blur=lambda c: ArgState.change_color(c, 2), bg=ArgState.colors[2]),
    )

```

In this case, in we want to pass two arguments to the event handler `change_color`, the color and the index of the color to change.

The `on_blur` event trigger passes the text of the input as an argument to the lambda, and the lambda calls the `change_color` event handler with the text and the index of the input.

When the number of args accepted by a lambda differs from that provided by the event trigger, an `EventFnArgMismatch` error will be raised.

```md alert warning
# Event Handler Parameters should provide type annotations.

Like state vars, be sure to provide the right type annotations for the parameters in an event handler.
```

## Events with Partial Arguments (Advanced)

_Added in v0.5.0_

Event arguments in Reflex are passed positionally. Any additional arguments not
passed to an EventHandler will be filled in by the event trigger when it is
fired.

The following two code samples are equivalent:

```python
# Use a lambda to pass event trigger args to the EventHandler.
rx.text(on_blur=lambda v: MyState.handle_update("field1", v))

# Create a partial that passes event trigger args for any args not provided to the EventHandler.
rx.text(on_blur=MyState.handle_update("field1"))
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/events/yield_events.md`:

```md

# Yielding Updates

A regular event handler will send a `StateUpdate` when it has finished running. This works fine for basic event, but sometimes we need more complex logic. To update the UI multiple times in an event handler, we can `yield` when we want to send an update.

To do so, we can use the Python keyword `yield`. For every yield inside the function, a `StateUpdate` will be sent to the frontend with the changes up to this point in the execution of the event handler.

This example below shows how to yield 100 updates to the UI.

```python demo exec

class MultiUpdateState(rx.State):
    count: int = 0

    @rx.event
    def timed_update(self):
        for i in range(100):
            self.count += 1
            yield


def multi_update():
    return rx.vstack(
    rx.text(MultiUpdateState.count),
    rx.button("Start", on_click=MultiUpdateState.timed_update)
)

```

Here is another example of yielding multiple updates with a loading icon.

```python demo exec

import asyncio

class ProgressExampleState(rx.State):
    count: int = 0
    show_progress: bool = False

    @rx.event
    async def increment(self):
        self.show_progress = True
        yield
        # Think really hard.
        await asyncio.sleep(0.5)
        self.count += 1
        self.show_progress = False

def progress_example():
    return rx.button(
        ProgressExampleState.count,
        on_click=ProgressExampleState.increment,
        loading=ProgressExampleState.show_progress,
    )

```

```md video https://youtube.com/embed/ITOZkzjtjUA?start=6463&end=6835
# Video: Asyncio with Yield
```

## Yielding Other Events

Events can also yield other events. This is useful when you want to chain events together. To do this, you can yield the event handler function itself.

```md alert
# Reference other Event Handler via class

When chaining another event handler with `yield`, access it via the state class, not `self`.
```

```python demo exec

import asyncio

class YieldEventsState(rx.State):
    count: int = 0
    show_progress: bool = False

    @rx.event
    async def add_five(self):
        self.show_progress = True
        yield
        # Think really hard.
        await asyncio.sleep(1)
        self.count += 5
        self.show_progress = False

    @rx.event
    async def increment(self):
        yield YieldEventsState.add_five
        yield YieldEventsState.add_five
        yield YieldEventsState.add_five


def multiple_yield_example():
    return rx.button(
        YieldEventsState.count,
        on_click=YieldEventsState.increment,
        loading=YieldEventsState.show_progress,
    )

```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/events/page_load_events.md`:

```md

# Page Load Events

You can also specify a function to run when the page loads. This can be useful for fetching data once vs on every render or state change.
In this example, we fetch data when the page loads:

```python
class State(rx.State):
    data: Dict[str, Any]

    @rx.event
    def get_data(self):
        # Fetch data
        self.data = fetch_data()

@rx.page(on_load=State.get_data)
def index():
    return rx.text('A Beautiful App')
```

Another example would be checking if the user is authenticated when the page loads. If the user is not authenticated, we redirect them to the login page. If they are authenticated, we don't do anything, letting them access the page. This `on_load` event would be placed on every page that requires authentication to access.

```python
class State(rx.State):
    authenticated: bool

    @rx.event
    def check_auth(self):
        # Check if user is authenticated
        self.authenticated = check_auth()
        if not self.authenticated:
            return rx.redirect('/login')

@rx.page(on_load=State.check_auth)
def index():
    return rx.text('A Beautiful App')
```

```