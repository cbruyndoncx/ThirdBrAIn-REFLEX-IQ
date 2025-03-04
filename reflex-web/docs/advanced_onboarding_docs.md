Project Path: advanced_onboarding

Source Tree:

```
advanced_onboarding
├── configuration.md
├── how-reflex-works.md
└── code_structure.md

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/advanced_onboarding/configuration.md`:

```md

# Configuration

Reflex apps can be configured using a configuration file, environment variables, and command line arguments.

## Configuration File

Running `reflex init` will create an `rxconfig.py` file in your root directory.
You can pass keyword arguments to the `Config` class to configure your app.

For example:

```python
# rxconfig.py
import reflex as rx

config = rx.Config(
    app_name="my_app_name",
    # Connect to your own database.
    db_url="postgresql://user:password@localhost:5432/my_db",
    # Change the frontend port.
    frontend_port=3001,
)
```

See the [config reference]({api_reference.config.path}) for all the parameters available.

## Environment Variables

You can override the configuration file by setting environment variables.
For example, to override the `frontend_port` setting, you can set the `FRONTEND_PORT` environment variable.

```bash
FRONTEND_PORT=3001 reflex run
```

## Command Line Arguments

Finally, you can override the configuration file and environment variables by passing command line arguments to `reflex run`.

```bash
reflex run --frontend-port 3001
```

See the [CLI reference]({api_reference.cli.path}) for all the arguments available.

## Customizable App Data Directory

The `REFLEX_DIR` environment variable can be set, which allows users to set the location where Reflex writes helper tools like Bun and NodeJS.

By default we use Platform specific directories:

On windows, `C:/Users/<username>/AppData/Local/reflex` is used.

On macOS, `~/Library/Application Support/reflex` is used.

On linux, `~/.local/share/reflex` is used.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/advanced_onboarding/how-reflex-works.md`:

```md

# How Reflex Works

We'll use the following basic app that displays Github profile images as an example to explain the different parts of the architecture.

```python demo exec
import requests
import reflex as rx

class GithubState(rx.State):
    url: str = "https://github.com/reflex-dev"
    profile_image: str = "https://avatars.githubusercontent.com/u/104714959"

    @rx.event
    def set_profile(self, username: str):
        if username == "":
            return
        github_data = requests.get(f"https://api.github.com/users/{username}").json()
        self.url = github_data["url"]
        self.profile_image = github_data["avatar_url"]

def index():
    return rx.hstack(
        rx.link(
            rx.avatar(src=GithubState.profile_image),
            href=GithubState.url,
        ),
        rx.input(
            placeholder="Your Github username",
            on_blur=GithubState.set_profile,
        ),
    )
```

## The Reflex Architecture

Full-stack web apps are made up of a frontend and a backend. The frontend is the user interface, and is served as a web page that runs on the user's browser. The backend handles the logic and state management (such as databases and APIs), and is run on a server.

In traditional web development, these are usually two separate apps, and are often written in different frameworks or languages. For example, you may combine a Flask backend with a React frontend. With this approach, you have to maintain two separate apps and end up writing a lot of boilerplate code to connect the frontend and backend.

We wanted to simplify this process in Reflex by defining both the frontend and backend in a single codebase, while using Python for everything. Developers should only worry about their app's logic and not about the low-level implementation details.

### TLDR

Under the hood, Reflex apps compile down to a [React](https://react.dev) frontend app and a [FastAPI](https://github.com/tiangolo/fastapi) backend app. Only the UI is compiled to Javascript; all the app logic and state management stays in Python and is run on the server. Reflex uses [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) to send events from the frontend to the backend, and to send state updates from the backend to the frontend.

The diagram below provides a detailed overview of how a Reflex app works. We'll go through each part in more detail in the following sections.


```python eval
image_zoom(rx.image(src="/architecture.png"))
```

```python eval
rx.box(height="1em")
```

## Frontend

We wanted Reflex apps to look and feel like a traditional web app to the end user, while still being easy to build and maintain for the developer. To do this, we built on top of mature and popular web technologies.

When you `reflex run` your app, Reflex compiles the frontend down to a single-page [Next.js](https://nextjs.org) app and serves it on a port (by default `3000`) that you can access in your browser.

The frontend's job is to reflect the app's state, and send events to the backend when the user interacts with the UI. No actual logic is run on the frontend.

### Components

Reflex frontends are built using components that can be composed together to create complex UIs. Instead of using a templating language that mixes HTML and Python, we just use Python functions to define the UI.

```python
def index():
    return rx.hstack(
        rx.link(
            rx.avatar(src=GithubState.profile_image),
            href=GithubState.url,
        ),
        rx.input(
            placeholder="Your Github username",
            on_blur=GithubState.set_profile,
        ),
    )
```

In our example app, we have components such as `rx.hstack`, `rx.avatar`, and `rx.input`. These components can have different **props** that affect their appearance and functionality - for example the `rx.input` component has a `placeholder` prop to display the default text.

We can make our components respond to user interactions with events such as `on_blur`, which we will discuss more below.

Under the hood, these components compile down to React components. For example, the above code compiles down to the following React code:

```jsx
<HStack>
    <Link href=\{GithubState.url}>
        <Avatar src=\{GithubState.profile_image}/>
    </Link>
    <Input
        placeholder="Your Github username"
        // This would actually be a websocket call to the backend.
        onBlur=\{GithubState.set_profile}
    >
</HStack>
```

Many of our core components are based on [Radix](https://radix-ui.com/), a popular React component library. We also have many other components for graphing, datatables, and more.

We chose React because it is a popular library with a huge ecosystem. Our goal isn't to recreate the web ecosystem, but to make it accessible to Python developers.

This also lets our users bring their own components if we don't have a component they need. Users can [wrap their own React components]({wrapping_react.overview.path}) and then [publish them]({custom_components.overview.path}) for others to use. Over time we will build out our [third party component ecosystem]({cc.path}) so that users can easily find and use components that others have built.

### Styling

We wanted to make sure Reflex apps look good out of the box, while still giving developers full control over the appearance of their app.

We have a core [theming system]({styling.theming.path}) that lets you set high level styling options such as dark mode and accent color throughout your app to give it a unified look and feel.

Beyond this, Reflex components can be styled using the full power of CSS. We leverage the [Emotion](https://emotion.sh/docs/introduction) library to allow "CSS-in-Python" styling, so you can pass any CSS prop as a keyword argument to a component. This includes [responsive props]({styling.responsive.path}) by passing a list of values.

## Backend

Now let's look at how we added interactivity to our apps.

In Reflex only the frontend compiles to Javascript and runs on the user's browser, while all the state and logic stays in Python and is run on the server. When you `reflex run`, we start a FastAPI server (by default on port `8000`) that the frontend connects to through a websocket.

All the state and logic are defined within a `State` class.

```python
class GithubState(rx.State):
    url: str = "https://github.com/reflex-dev"
    profile_image: str = "https://avatars.githubusercontent.com/u/104714959"

    def set_profile(self, username: str):
        if username == "":
            return
        github_data = requests.get(f"https://api.github.com/users/\{username}").json()
        self.url = github_data["url"]
        self.profile_image = github_data["avatar_url"]
```

The state is made up of **vars** and **event handlers**.

Vars are any values in your app that can change over time. They are defined as class attributes on your `State` class, and may be any Python type that can be serialized to JSON. In our example, `url` and `profile_image` are vars.

Event handlers are methods in your `State` class that are called when the user interacts with the UI. They are the only way that we can modify the vars in Reflex, and can be called in response to user actions, such as clicking a button or typing in a text box. In our example, `set_profile` is an event handler that updates the `url` and `profile_image` vars.

Since event handlers are run on the backend, you can use any Python library within them. In our example, we use the `requests` library to make an API call to Github to get the user's profile image.

## Event Processing

Now we get into the interesting part - how we handle events and state updates.

Normally when writing web apps, you have to write a lot of boilerplate code to connect the frontend and backend. With Reflex, you don't have to worry about that - we handle the communication between the frontend and backend for you. Developers just have to write their event handler logic, and when the vars are updated the UI is automatically updated.

You can refer to the diagram above for a visual representation of the process. Let's walk through it with our Github profile image example.

### Event Triggers

The user can interact with the UI in many ways, such as clicking a button, typing in a text box, or hovering over an element. In Reflex, we call these **event triggers**.

```python
rx.input(
    placeholder="Your Github username",
    on_blur=GithubState.set_profile,
)
```

In our example we bind the `on_blur` event trigger to the `set_profile` event handler. This means that when the user types in the input field and then clicks away, the `set_profile` event handler is called.

### Event Queue

On the frontend, we maintain an event queue of all pending events. An event consists of three major pieces of data:

- **client token**: Each client (browser tab) has a unique token to identify it. This let's the backend know which state to update.
- **event handler**: The event handler to run on the state.
- **arguments**: The arguments to pass to the event handler.

Let's assume I type my username "picklelo" into the input. In this example, our event would look something like this:

```json
{
  "client_token": "abc123",
  "event_handler": "GithubState.set_profile",
  "arguments": ["picklelo"]
}
```

On the frontend, we maintain an event queue of all pending events.

When an event is triggered, it is added to the queue. We have a `processing` flag to make sure only one event is processed at a time. This ensures that the state is always consistent and there aren't any race conditions with two event handlers modifying the state at the same time.

```md alert info
# There are exceptions to this, such as [background events]({events.background_events.path}) which allow you to run events in the background without blocking the UI.
```

Once the event is ready to be processed, it is sent to the backend through a WebSocket connection.

### State Manager

Once the event is received, it is processed on the backend.

Reflex uses a **state manager** which maintains a mapping between client tokens and their state. By default, the state manager is just an in-memory dictionary, but it can be extended to use a database or cache. In production we use Redis as our state manager.

### Event Handling

Once we have the user's state, the next step is to run the event handler with the arguments.

```python
 def set_profile(self, username: str):
    if username == "":
        return
    github_data = requests.get(f"https://api.github.com/users/\{username}").json()
    self.url = github_data["url"]
    self.profile_image = github_data["avatar_url"]
```

In our example, the `set_profile` event handler is run on the user's state. This makes an API call to Github to get the user's profile image, and then updates the state's `url` and `profile_image` vars.

### State Updates

Every time an event handler returns (or [yields]({events.yield_events.path})), we save the state in the state manager and send the **state updates** to the frontend to update the UI.

To maintain performance as your state grows, internally Reflex keeps track of vars that were updated during the event handler (**dirty vars**). When the event handler is done processing, we find all the dirty vars and create a state update to send to the frontend.

In our case, the state update may look something like this:

```json
{
  "url": "https://github.com/picklelo",
  "profile_image": "https://avatars.githubusercontent.com/u/104714959"
}
```

We store the new state in our state manager, and then send the state update to the frontend. The frontend then updates the UI to reflect the new state. In our example, the new Github profile image is displayed.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/advanced_onboarding/code_structure.md`:

```md

# Project Structure (Advanced)

## App Module

Reflex imports the main app module based on the `app_name` from the config, which **must define a module-level global named `app` as an instance of `rx.App`**.

The main app module is responsible for importing all other modules that make up the app and defining `app = rx.App()`.

**All other modules containing pages, state, and models MUST be imported by the main app module or package** for Reflex to include them in the compiled output.

# Breaking the App into Smaller Pieces

As applications scale, effective organization is crucial. This is achieved by breaking the application down into smaller, manageable modules and organizing them into logical packages that avoid circular dependencies.

In the following documentation there will be an app with an `app_name` of `example_big_app`. The main module would be `example_big_app/example_big_app.py`.

In the [Putting it all together](#putting-it-all-together) section there is a visual of the project folder structure to help follow along with the examples below.

### Pages Package: `example_big_app/pages`

All complex apps will have multiple pages, so it is recommended to create `example_big_app/pages` as a package.

1. This package should contain one module per page in the app.
2. If a particular page depends on the state, the substate should be defined in the same module as the page.
3. The page-returning function should be decorated with `rx.page()` to have it added as a route in the app.

```python
import reflex as rx

from ..state import AuthState


class LoginState(AuthState):
    @rx.event
    def handle_submit(self, form_data):
        self.logged_in = authenticate(form_data["username"], form_data["password"])


def login_field(name: str, **input_props):
    return rx.hstack(
        rx.text(name.capitalize()),
        rx.input(name=name, **input_props),
        width="100%",
        justify="between",
    )


@rx.page(route="/login")
def login():
    return rx.card(
        rx.form(
            rx.vstack(
                login_field("username"),
                login_field("password", type="password"),
                rx.button("Login"),
                width="100%",
                justify="center",
            ),
            on_submit=LoginState.handle_submit,
        ),
    )
```

### Templating: `example_big_app/template.py`

Most applications maintain a consistent layout and structure across pages. Defining this common structure in a separate module facilitates easy sharing and reuse when constructing individual pages.

**Best Practices**

1. Factor out common frontend UI elements into a function that returns a component.
2. If a function accepts a function that returns a component, it can be used as a decorator as seen below.

```python
from typing import Callable

import reflex as rx

from .components.menu import menu
from .components.navbar import navbar


def template(page: Callable[[], rx.Component]) -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.hstack(
            menu(),
            rx.container(page()),
        ),
        width="100%",
    )
```

The `@template` decorator should appear below the `@rx.page` decorator and above the page-returning function. See the [Posts Page](#a-post-page-example_big_apppagespostspy) code for an example.

## State Management

Most pages will use State in some capacity. You should avoid adding vars to a
shared state that will only be used in a single page. Instead, define a new
subclass of `rx.State` and keep it in the same module as the page.

### Accessing other States

As of Reflex 0.4.3, any event handler can get access to an instance of any other
substate via the `get_state` API. From a practical perspective, this means that
state can be split up into smaller pieces without requiring a complex
inheritance hierarchy to share access to other states.

In previous releases, if an app wanted to store settings in `SettingsState` with
a page or component for modifying them, any other state with an event handler
that needed to access those settings would have to inherit from `SettingsState`,
even if the other state was mostly orthogonal. The other state would also now
always have to load the settings, even for event handlers that didn't need to
access them.

A better strategy is to load the desired state on demand from only the event
handler which needs access to the substate.

### A Settings Component: `example_big_app/components/settings.py`

```python
import reflex as rx


class SettingsState(rx.State):
    refresh_interval: int = 15
    auto_update: bool = True
    prefer_plain_text: bool = True
    posts_per_page: int = 20


def settings_dialog():
    return rx.dialog(...)
```

### A Post Page: `example_big_app/pages/posts.py`

This page loads the `SettingsState` to determine how many posts to display per page
and how often to refresh.

```python
import reflex as rx

from ..models import Post
from ..template import template
from ..components.settings import SettingsState


class PostsState(rx.State):
    refresh_tick: int
    page: int
    posts: list[Post]

    @rx.event
    async def on_load(self):
        settings = await self.get_state(SettingsState)
        if settings.auto_update:
            self.refresh_tick = settings.refresh_interval * 1000
        else:
            self.refresh_tick = 0

    @rx.event
    async def tick(self, _):
        settings = await self.get_state(SettingsState)
        with rx.session() as session:
            q = Post.select().offset(self.page * settings.posts_per_page).limit(settings.posts_per_page)
            self.posts = q.all()

    @rx.event
    def go_to_previous(self):
        if self.page > 0:
            self.page = self.page - 1

    @rx.event
    def go_to_next(self):
        if self.posts:
            self.page = self.page + 1


@rx.page(route="/posts", on_load=PostsState.on_load)
@template
def posts():
    return rx.vstack(
        rx.foreach(PostsState.posts, post_view),
        rx.hstack(
            rx.button("< Prev", on_click=PostsState.go_to_previous),
            rx.button("Next >", on_click=PostsState.go_to_next),
            justify="between",
        ),
        rx.moment(interval=PostsState.refresh_tick, on_change=PostsState.tick, display="none"),
        width="100%",
    )
```

### Common State: `example_big_app/state.py`

_Common_ states and substates that are shared by multiple pages or components
should be implemented in a separate module to avoid circular imports. This
module should not import other modules in the app.

## Component Reusability

The primary mechanism for reusing components in Reflex is to define a function that returns
the component, then simply call it where that functionality is needed.

Component functions typically should not take any State classes as arguments, but prefer
to import the needed state and access the vars on the class directly.

### Memoize Functions for Improved Performance

In a large app, if a component has many subcomponents or is used in a large number of places, it can improve compile and runtime performance to memoize the function with the `@lru_cache` decorator.

To memoize the `foo` component to avoid re-creating it many times simply add `@lru_cache` to the function definition, and the component will only be created once per unique set of arguments.

```python
from functools import lru_cache

import reflex as rx

class State(rx.State):
    v: str = "foo"


@lru_cache
def foo():
    return rx.text(State.v)


def index():
    return rx.flex(
        rx.button("Change", on_click=State.set_v(rx.cond(State.v != "bar", "bar", "foo"))),
        *[
            foo()
            for _ in range(100)
        ],
        direction="row",
        wrap="wrap",
    )
```

### example_big_app/components

This package contains reusable parts of the app, for example headers, footers,
and menus. If a particular component requires state, the substate may be defined
in the same module for locality. Any substate defined in a component module
should only contain fields and event handlers pertaining to that individual
component.

### External Components

Reflex 0.4.3 introduced support for the [`reflex component` CLI commands]({custom_components.overview.path}), which makes it easy
to bundle up common functionality to publish on PyPI as a standalone Python package
that can be installed and used in any Reflex app.

When wrapping npm components or other self-contained bits of functionality, it can be helpful
to move this complexity outside the app itself for easier maintenance and reuse in other apps.

## Database Models: `example_big_app/models.py`

It is recommended to implement all database models in a single file to make it easier to define relationships and understand the entire schema.

However, if the schema is very large, it might make sense to have a `models` package with individual models defined in their own modules.

At any rate, defining the models separately allows any page or component to import and use them without circular imports.

## Top-level Package: `example_big_app/__init__.py`

This is a great place to import all state, models, and pages that should be part of the app.
Typically, components and helpers do not need to imported, because they will be imported by
pages that use them (or they would be unused).

```python
from . import state, models
from .pages import index, login, post, product, profile, schedule

__all__ = [
    "state",
    "models",
    "index",
    "login",
    "post",
    "product",
    "profile",
    "schedule",
]
```

If any pages are not imported here, they will not be compiled as part of the app.

## example_big_app/example_big_app.py

This is the main app module. Since everything else is defined in other modules, this file becomes very simple.

```python
import reflex as rx

app = rx.App()
```

## File Management

There are two categories of non-code assets (media, fonts, stylesheets,
documents) typically used in a Reflex app.

### assets

The `assets` directory is used for **static** files that should be accessible
relative to the root of the frontend (default port 3000). When an app is deployed in
production mode, changes to the assets directory will NOT be available at runtime!

When referencing an asset, always use a leading forward slash, so the
asset can be resolved regardless of the page route where it may appear.

### uploaded_files

If an app needs to make files available dynamically at runtime, it is
recommended to set the target directory via `REFLEX_UPLOADED_FILES_DIR`
environment variable (default `./uploaded_files`), write files relative to the
path returned by `rx.get_upload_dir()`, and create working links via
`rx.get_upload_url(relative_path)`.

Uploaded files are served from the backend (default port 8000) via
`/_upload/<relative_path>`

## Putting it all together

Based on the previous discussion, the recommended project layout look like this.

```text
example-big-app/
├─ assets/
├─ example_big_app/
│  ├─ components/
│  │  ├─ __init__.py
│  │  ├─ auth.py
│  │  ├─ footer.py
│  │  ├─ menu.py
│  │  ├─ navbar.py
│  ├─ pages/
│  │  ├─ __init__.py
│  │  ├─ index.py
│  │  ├─ login.py
│  │  ├─ posts.py
│  │  ├─ product.py
│  │  ├─ profile.py
│  │  ├─ schedule.py
│  ├─ __init__.py
│  ├─ example_big_app.py
│  ├─ models.py
│  ├─ state.py
│  ├─ template.py
├─ uploaded_files/
├─ requirements.txt
├─ rxconfig.py
```

## Key Takeaways

- Like any other Python project, **split up the app into modules and packages** to keep the codebase organized and manageable.
- Using smaller modules and packages makes it easier to **reuse components and state** across the app
  without introducing circular dependencies.
- Create **individual functions** to encapsulate units of functionality and **reuse them** where needed.

```