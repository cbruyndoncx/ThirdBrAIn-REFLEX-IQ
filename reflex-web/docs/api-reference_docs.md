Project Path: api-reference

Source Tree:

```
api-reference
├── var_system.md
├── special_events.md
├── cli.md
├── event_triggers.md
├── browser_javascript.md
└── browser_storage.md

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/api-reference/var_system.md`:

```md
# Reflex's Var System

## Motivation

Reflex supports some basic operations in state variables on the frontend.
Reflex automatically converts variable operations from Python into a JavaScript equivalent.

Here's an example of a Reflex conditional in Python that returns "Pass" if the threshold is equal to or greater than 50 and "Fail" otherwise:

```py
rx.cond(
    State.threshold >= 50,
    "Pass",
    "Fail",
)
```

 The conditional to roughly the following in Javascript:

```js
state.threshold >= 50 ? "Pass" : "Fail";
```

## Overview

Simply put, a `Var` in Reflex represents a Javascript expression.
If the type is known, it can be any of the following:

- `NumberVar` represents an expression that evaluates to a Javascript `number`. `NumberVar` can support both integers and floating point values
- `BooleanVar` represents a boolean expression. For example: `false`, `3 > 2`.
- `StringVar` represents an expression that evaluates to a string. For example: `'hello'`, `(2).toString()`.
- `ArrayVar` represents an expression that evaluates to an array object. For example: `[1, 2, 3]`, `'words'.split()`.
- `ObjectVar` represents an expression that evaluates to an object. For example: `\{a: 2, b: 3}`, `\{deeply: \{nested: \{value: false}}}`.
- `NoneVar` represent null values. These can be either `undefined` or `null`.

## Creating Vars

State fields are converted to `Var` by default. Additionally, you can create a `Var` from Python values using `rx.Var.create()`:

```py
rx.Var.create(4) # NumberVar
rx.Var.create("hello") # StringVar
rx.Var.create([1, 2, 3]) # ArrayVar
```

If you want to explicitly create a `Var` from a raw Javascript string, you can instantiate `rx.Var` directly:

```py
rx.Var("2", _var_type=int).guess_type() # NumberVar
```

In the example above, `.guess_type()` will attempt to downcast from a generic `Var` type into `NumberVar`.
For this example, calling the function `.to(int)` can also be used in place of `.guess_type()`.

## Operations

The `Var` system also supports some other basic operations.
For example, `NumberVar` supports basic arithmetic operations like `+` and `-`, as in Python.
It also supports comparisons that return a `BooleanVar`.

Custom `Var` operations can also be defined:

```py
from reflex.vars import var_operation, var_operation_return, ArrayVar, NumberVar

@var_operation
def multiply_array_values(a: ArrayVar):
    return var_operation_return(
        js_expression=f"\{a}.reduce((p, c) => p * c, 1)",
        var_type=int,
    )

def factorial(value: NumberVar):
    return rx.cond(
        value <= 1,
        1,
        multiply_array_values(rx.Var.range(1, value+1))
    )
```

Use `js_expression` to pass explicit JavaScript expressions; in the `multiply_array_values` example, we pass in a JavaScript expression that calculates the product of all elements in an array called `a` by using the reduce method to multiply each element with the accumulated result, starting from an initial value of 1.
Later, we leverage `rx.cond` in the' factorial' function, we instantiate an array using the `range` function, and pass this array to `multiply_array_values`.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/api-reference/special_events.md`:

```md

# Special Events

Reflex includes a set of built-in special events that can be utilized as event triggers
or returned from event handlers in your applications. These events enhance interactivity and user experience.
Below are the special events available in Reflex, along with explanations of their functionality:

## rx.console_log

Perform a console.log in the browser's console.

```python demo
rx.button('Log', on_click=rx.console_log('Hello World!'))
```

When triggered, this event logs a specified message to the browser's developer console.
It's useful for debugging and monitoring the behavior of your application.

## rx.scroll_to

scroll to an element in the page

```python demo
rx.button(
    "Scroll to download button",
    on_click=rx.scroll_to("download button")

)
```

When this is triggered, it scrolls to an element passed by id as parameter. Click on button to scroll to download button (rx.download section) at the bottom of the page

## rx.redirect

Redirect the user to a new path within the application.

### Parameters

- `path`: The destination path or URL to which the user should be redirected.
- `external`: If set to True, the redirection will open in a new tab. Defaults to `False`.

```python demo
rx.vstack(
    rx.button("open in tab", on_click=rx.redirect("/docs/api-reference/special-events")),
    rx.button("open in new tab", on_click=rx.redirect('https://github.com/reflex-dev/reflex/', is_external=True))
)
```

When this event is triggered, it navigates the user to a different page or location within your Reflex application.
By default, the redirection occurs in the same tab. However, if you set the external parameter to True, the redirection
will open in a new tab or window, providing a seamless user experience.

This event can also be run from an event handler in State. It is necessary to `return` the `rx.redirect()`.

```python demo exec
class RedirectExampleState(rx.State):
    """The app state."""

    @rx.event
    def change_page(self):
        return rx.redirect('https://github.com/reflex-dev/reflex/', is_external=True)

def redirect_example():
    return rx.vstack(
        rx.button("Change page in State", on_click=RedirectExampleState.change_page),
    )
```

## rx.set_clipboard

Set the specified text content to the clipboard.

```python demo
rx.button('Copy "Hello World" to clipboard',on_click=rx.set_clipboard('Hello World'),)
```

This event allows you to copy a given text or content to the user's clipboard.
It's handy when you want to provide a "Copy to Clipboard" feature in your application,
allowing users to easily copy information to paste elsewhere.

## rx.set_value

Set the value of a specified reference element.

```python demo
rx.hstack(
    rx.input(id='input1'),
    rx.button(
        'Erase', on_click=rx.set_value('input1', '')
    ),
)
```

With this event, you can modify the value of a particular HTML element, typically an input field or another form element.

## rx.window_alert

Create a window alert in the browser.

```python demo
rx.button('Alert', on_click=rx.window_alert('Hello World!'))
```

## rx.download

Download a file at a given path.

Parameters:

- `url`: The URL of the file to be downloaded.
- `data`: The data to be downloaded. Should be `str` or `bytes`, `data:` URI, `PIL.Image`, or any state Var (to be converted to JSON).
- `filename`: The desired filename of the downloaded file.

```md alert
# `url` and `data` args are mutually exclusive, and at least one of them must be provided.
```

```python demo
rx.button("Download", on_click=rx.download(url="/reflex_banner.png", filename="different_name_logo.png"), id="download button")
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/api-reference/cli.md`:

```md
# CLI

The `reflex` command line interface (CLI) is a tool for creating and managing Reflex apps.

To see a list of all available commands, run `reflex --help`.

```bash
$ reflex --help

Usage: reflex [OPTIONS] COMMAND [ARGS]...

  Reflex CLI to create, run, and deploy apps.

Options:
  -v, --version  Get the Reflex version.
  --help         Show this message and exit.

Commands:
  db           Subcommands for managing the database schema.
  demo         Run the demo app.
  deploy       Deploy the app to the Reflex hosting service.
  deployments  Subcommands for managing the Deployments.
  export       Export the app to a zip file.
  init         Initialize a new Reflex app in the current directory.
  login        Authenticate with Reflex hosting service.
  logout       Log out of access to Reflex hosting service.
  run          Run the app in the current directory.
```

## Init

The `reflex init` command creates a new Reflex app in the current directory.
If an `rxconfig.py` file already exists already, it will re-initialize the app with the latest template.

```bash
$ reflex init --help
Usage: reflex init [OPTIONS]

  Initialize a new Reflex app in the current directory.

Options:
  --name APP_NAME                 The name of the app to initialize.
  --template [demo|sidebar|blank]
                                  The template to initialize the app with.
  --loglevel [debug|info|warning|error|critical]
                                  The log level to use.  [default:
                                  LogLevel.INFO]
  --help                          Show this message and exit.
```

## Run

The `reflex run` command runs the app in the current directory.

By default it runs your app in development mode.
This means that the app will automatically reload when you make changes to the code.
You can also run in production mode which will create an optimized build of your app.

You can configure the mode, as well as other options through flags.

```bash
$ reflex run --help
Usage: reflex run [OPTIONS]

  Run the app in the current directory.

Options:
  --env [dev|prod]                The environment to run the app in.
                                  [default: Env.DEV]
  --frontend-only                 Execute only frontend.
  --backend-only                  Execute only backend.
  --frontend-port TEXT            Specify a different frontend port.
                                  [default: 3000]
  --backend-port TEXT             Specify a different backend port.  [default:
                                  8000]
  --backend-host TEXT             Specify the backend host.  [default:
                                  0.0.0.0]
  --loglevel [debug|info|warning|error|critical]
                                  The log level to use.  [default:
                                  LogLevel.INFO]
  --help                          Show this message and exit.
```

## Export

You can export your app's frontend and backend to zip files using the `reflex export` command.

The frontend is a compiled NextJS app, which can be deployed to a static hosting service like Github Pages or Vercel.
However this is just a static build, so you will need to deploy the backend separately.
See the self-hosting guide for more information.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/api-reference/event_triggers.md`:

```md

# Event Triggers

Components can modify the state based on user events such as clicking a button or entering text in a field.
These events are triggered by event triggers.

Event triggers are component specific and are listed in the documentation for each component.

```python eval
rx.box(
    rx.divider(),
    component_grid(),
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/api-reference/browser_javascript.md`:

```md

# Browser Javascript

Reflex compiles your frontend code, defined as python functions, into a Javascript web application
that runs in the user's browser. There are instances where you may need to supply custom javascript
code to interop with Web APIs, use certain third-party libraries, or wrap low-level functionality
that is not exposed via Reflex's Python API.

```md alert
# Avoid Custom Javascript

Custom Javascript code in your Reflex app presents a maintenance challenge, as it will be harder to debug and may be unstable across Reflex versions.

Prefer to use the Python API whenever possible and file an issue if you need additional functionality that is not currently provided.
```

## Executing Script

There are four ways to execute custom Javascript code into your Reflex app:

- `rx.script` - Injects the script via `next/script` for efficient loading of inline and external Javascript code. Described further in the [component library]({library.other.script.path}).
  - These components can be directly included in the body of a page, or they may
    be passed to `rx.App(head_components=[rx.script(...)])` to be included in
    the `<Head>` tag of all pages.
- `rx.call_script` - An event handler that evaluates arbitrary Javascript code,
  and optionally returns the result to another event handler.

These previous two methods can work in tandem to load external scripts and then
call functions defined within them in response to user events.

The following two methods are geared towards wrapping components and are
described with examples in the [Wrapping React]({wrapping_react.overview.path})
section.

- `_get_hooks` and `_get_custom_code` in an `rx.Component` subclass
- `Var.create` with `_var_is_local=False`

## Inline Scripts

The `rx.script` component is the recommended way to load inline Javascript for greater control over
frontend behavior.

The functions and variables in the script can be accessed from backend event
handlers or frontend event triggers via the `rx.call_script` interface.

```python demo exec
class SoundEffectState(rx.State):
    @rx.event(background=True)
    async def delayed_play(self):
        await asyncio.sleep(1)
        return rx.call_script("playFromStart(button_sfx)")


def sound_effect_demo():
    return rx.hstack(
        rx.script("""
            var button_sfx = new Audio("/vintage-button-sound-effect.mp3")
            function playFromStart (sfx) {sfx.load(); sfx.play()}"""),
        rx.button("Play Immediately", on_click=rx.call_script("playFromStart(button_sfx)")),
        rx.button("Play Later", on_click=SoundEffectState.delayed_play),
    )
```

## External Scripts

External scripts can be loaded either from the `assets` directory, or from CDN URL, and then controlled
via `rx.call_script`.

```python demo
rx.vstack(
    rx.script(
        src="https://cdn.jsdelivr.net/gh/scottschiller/snowstorm@snowstorm_20131208/snowstorm-min.js",
        on_ready=rx.call_script("snowStorm.autoStart = false; snowStorm.snowColor = '#111'"),
    ),
    rx.button("Start Duststorm", on_click=rx.call_script("snowStorm.start()")),
    rx.button("Toggle Duststorm", on_click=rx.call_script("snowStorm.toggleSnow()")),
)
```

## Accessing Client Side Values

The `rx.call_script` function accepts a `callback` parameter that expects an
Event Handler with one argument which will receive the result of evaluating the
Javascript code. This can be used to access client-side values such as the
`window.location` or current scroll location, or any previously defined value.

```python demo exec
class WindowState(rx.State):
    location: dict[str, str] = {}
    scroll_position: dict[str, int] = {}

    def update_location(self, location):
        self.location = location

    def update_scroll_position(self, scroll_position):
        self.scroll_position = {
            "x": scroll_position[0],
            "y": scroll_position[1],
        }

    @rx.event
    def get_client_values(self):
        return [
            rx.call_script(
                "window.location",
                callback=WindowState.update_location
            ),
            rx.call_script(
                "[window.scrollX, window.scrollY]",
                callback=WindowState.update_scroll_position,
            ),
        ]


def window_state_demo():
    return rx.vstack(
        rx.button("Update Values", on_click=WindowState.get_client_values),
        rx.text(f"Scroll Position: {WindowState.scroll_position.to_string()}"),
        rx.text("window.location:"),
        rx.text_area(value=WindowState.location.to_string(), is_read_only=True),
        on_mount=WindowState.get_client_values,
    )
```

```md alert
# Allowed Callback Values

The `callback` parameter may be an `EventHandler` with one argument, or a lambda with one argument that returns an `EventHandler`.
If the callback is None, then no event is triggered.
```

## Using React Hooks

To use React Hooks directly in a Reflex app, you must subclass `rx.Component`,
typically `rx.Fragment` is used when the hook functionality has no visual
element. The hook code is returned by the `add_hooks` method, which is expected
to return a `list[str]` containing Javascript code which will be inserted into the
page component (i.e the render function itself).

For supporting code that must be defined outside of the component render
function, use `_get_custom_code`.

The following example uses `useEffect` to register global hotkeys on the
`document` object, and then triggers an event when a specific key is pressed.

```python demo exec
import dataclasses

from reflex.utils import imports

@dataclasses.dataclass
class KeyEvent:
    """Interface of Javascript KeyboardEvent"""
    key: str = ""

def key_event_spec(ev: rx.Var[KeyEvent]) -> tuple[rx.Var[str]]:
    # Takes the event object and returns the key pressed to send to the state
    return (ev.key,)

class GlobalHotkeyState(rx.State):
    key: str = ""

    @rx.event
    def update_key(self, key):
        self.key = key


class GlobalHotkeyWatcher(rx.Fragment):
    """A component that listens for key events globally."""

    # The event handler that will be called
    on_key_down: rx.EventHandler[key_event_spec]

    def add_imports(self) -> imports.ImportDict:
        """Add the imports for the component."""
        return {
            "react": [imports.ImportVar(tag="useEffect")],
        }

    def add_hooks(self) -> list[str | rx.Var]:
        """Add the hooks for the component."""
        return [
            """
            useEffect(() => {
                const handle_key = %s;
                document.addEventListener("keydown", handle_key, false);
                return () => {
                    document.removeEventListener("keydown", handle_key, false);
                }
            })
            """
            % str(rx.Var.create(self.event_triggers["on_key_down"]))
        ]

def global_key_demo():
    return rx.vstack(
        GlobalHotkeyWatcher.create(
            keys=["a", "s", "d", "w"],
            on_key_down=lambda key: rx.cond(
                rx.Var.create(["a", "s", "d", "w"]).contains(key),
                GlobalHotkeyState.update_key(key),
                rx.console_log(key)
            )
        ),
        rx.text("Press a, s, d or w to trigger an event"),
        rx.heading(f"Last watched key pressed: {GlobalHotkeyState.key}"),
    )
```

This snippet can also be imported through pip: [reflex-global-hotkey](https://pypi.org/project/reflex-global-hotkey/).

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/api-reference/browser_storage.md`:

```md
# Browser Storage

## rx.Cookie

Represents a state Var that is stored as a cookie in the browser. Currently only supports string values.

Parameters

- `name` : The name of the cookie on the client side.
- `path`: The cookie path. Use `/` to make the cookie accessible on all pages.
- `max_age` : Relative max age of the cookie in seconds from when the client receives it.
- `domain`: Domain for the cookie (e.g., `sub.domain.com` or `.allsubdomains.com`).
- `secure`: If the cookie is only accessible through HTTPS.
- `same_site`: Whether the cookie is sent with third-party requests. Can be one of (`True`, `False`, `None`, `lax`, `strict`).

```python
class CookieState(rx.State):
    c1: str = rx.Cookie()
    c2: str = rx.Cookie('c2 default')

    # cookies with custom settings
    c3: str = rx.Cookie(max_age=2)  # expires after 2 second
    c4: str = rx.Cookie(same_site='strict')
    c5: str = rx.Cookie(path='/foo/')  # only accessible on `/foo/`
    c6: str = rx.Cookie(name='c6-custom-name')
```

```md alert warning
# **The default value of a Cookie is never set in the browser!**

The Cookie value is only set when the Var is assigned. If you need to set a
default value, you can assign a value to the cookie in an `on_load` event
handler.
```

## Accessing Cookies

Cookies are accessed like any other Var in the state. If another state needs access
to the value of a cookie, the state should be a substate of the state that defines
the cookie. Alternatively the `get_state` API can be used to access the other state.

For rendering cookies in the frontend, import the state that defines the cookie and
reference it directly.

```md alert warning
# **Two separate states should _avoid_ defining `rx.Cookie` with the same name.**

Although it is technically possible, the cookie options may differ, leading to
unexpected results.

Additionally, updating the cookie value in one state will not automatically
update the value in the other state without a page refresh or navigation event.
```

## rx.remove_cookies

Remove a cookie from the client's browser.

Parameters:

- `key`: The name of cookie to remove.

```python
rx.button(
    'Remove cookie', on_click=rx.remove_cookie('key')
)
```

This event can also be returned from an event handler:

```python
class CookieState(rx.State):
    ...
    def logout(self):
        return rx.remove_cookie('auth_token')
```

## rx.LocalStorage

Represents a state Var that is stored in localStorage in the browser. Currently only supports string values.

Parameters

- `name`: The name of the storage key on the client side.
- `sync`: Boolean indicates if the state should be kept in sync across tabs of the same browser.

```python
class LocalStorageState(rx.State):
    # local storage with default settings
    l1: str = rx.LocalStorage()

    # local storage with custom settings
    l2: str = rx.LocalStorage("l2 default")
    l3: str = rx.LocalStorage(name="l3")

    # local storage that automatically updates in other states across tabs
    l4: str = rx.LocalStorage(sync=True)
```

### Syncing Vars

Because LocalStorage applies to the entire browser, all LocalStorage Vars are
automatically shared across tabs.

The `sync` parameter controls whether an update in one tab should be actively
propagated to other tabs without requiring a navigation or page refresh event.

## rx.remove_local_storage

Remove a local storage item from the client's browser.

Parameters

- `key`: The key to remove from local storage.

```python
rx.button(
    'Remove Local Storage',
    on_click=rx.remove_local_storage('key'),
)
```

This event can also be returned from an event handler:

```python
class LocalStorageState(rx.State):
    ...
    def logout(self):
        return rx.remove_local_storage('local_storage_state.l1')
```

## rx.clear_local_storage()

Clear all local storage items from the client's browser. This may affect other
apps running in the same domain or libraries within your app that use local
storage.

```python
rx.button(
    'Clear all Local Storage',
    on_click=rx.clear_local_storage(),
)
```

# Serialization Strategies

If a non-trivial data structure should be stored in a `Cookie` or `LocalStorage` var it needs to be serialized before and after storing it. It is recommended to use a dataclass for the data which provides simple serialization helpers and works recursively in complex object structures.

```python demo exec
import reflex as rx
import dataclasses

@dataclasses.dataclass
class AppSettings:
    theme: str = 'light'
    sidebar_visible: bool = True
    update_frequency: int = 60
    error_messages: list[str] = dataclasses.field(default_factory=list)


class ComplexLocalStorageState(rx.State):
    data_raw: str = rx.LocalStorage("{}")
    data: AppSettings = AppSettings()
    settings_open: bool = False

    @rx.event
    def save_settings(self):
        self.data_raw = self.data.json()
        self.settings_open = False

    @rx.event
    def open_settings(self):
        self.data = AppSettings.parse_raw(self.data_raw)
        self.settings_open = True

    @rx.event
    def set_field(self, field, value):
        setattr(self.data, field, value)


def app_settings():
    return rx.form.root(
        rx.foreach(
            ComplexLocalStorageState.data.error_messages,
            rx.text,
        ),
        rx.form.field(
            rx.flex(
                rx.form.label(
                    "Theme",
                    rx.input(
                        value=ComplexLocalStorageState.data.theme,
                        on_change=lambda v: ComplexLocalStorageState.set_field(
                            "theme", v
                        ),
                    ),
                ),
                rx.form.label(
                    "Sidebar Visible",
                    rx.switch(
                        checked=ComplexLocalStorageState.data.sidebar_visible,
                        on_change=lambda v: ComplexLocalStorageState.set_field(
                            "sidebar_visible",
                            v,
                        ),
                    ),
                ),
                rx.form.label(
                    "Update Frequency (seconds)",
                    rx.input(
                    value=ComplexLocalStorageState.data.update_frequency,
                    on_change=lambda v: ComplexLocalStorageState.set_field(
                        "update_frequency",
                        v,
                    ),
                ),
                ),
                rx.dialog.close(rx.button("Save", type="submit")),
                gap=2,
                direction="column",
            )
        ),
        on_submit=lambda _: ComplexLocalStorageState.save_settings(),
    )

def app_settings_example():
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("App Settings", on_click=ComplexLocalStorageState.open_settings),
        ),
        rx.dialog.content(
            rx.dialog.title("App Settings"),
            rx.dialog.description(app_settings()),
        ),
    )
```

```