Project Path: utility_methods

Source Tree:

```
utility_methods
├── lifespan_tasks.md
├── exception_handlers.md
├── other_methods.md
└── router_attributes.md

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/utility_methods/lifespan_tasks.md`:

```md
# Lifespan Tasks

_Added in v0.5.2_

Lifespan tasks are coroutines that run when the backend server is running. They
are useful for setting up the initial global state of the app, running periodic
tasks, and cleaning up resources when the server is shut down.

Lifespan tasks are defined as async coroutines or async contextmanagers. To avoid
blocking the event thread, never use `time.sleep` or perform non-async I/O within
a lifespan task.

In dev mode, lifespan tasks will stop and restart when a hot-reload occurs.

## Tasks

Any async coroutine can be used as a lifespan task. It will be started when the
backend comes up and will run until it returns or is cancelled due to server
shutdown. Long-running tasks should catch `asyncio.CancelledError` to perform
any necessary clean up.

```python
async def long_running_task(foo, bar):
    print(f"Starting \{foo} \{bar} task")
    some_api = SomeApi(foo)
    try:
        while True:
            updates = some_api.poll_for_updates()
            other_api.push_changes(updates, bar)
            await asyncio.sleep(5)  # add some polling delay to avoid running too often
    except asyncio.CancelledError:
        some_api.close()  # clean up the API if needed
        print("Task was stopped")
```

### Register the Task

To register a lifespan task, use `app.register_lifespan_task(coro_func, **kwargs)`.
Any keyword arguments specified during registration will be passed to the task.

If the task accepts the special argument, `app`, it will be an instance of the `FastAPI` object
associated with the app.

```python
app = rx.App()
app.register_lifespan_task(long_running_task, foo=42, bar=os.environ["BAR_PARAM"])
```

## Context Managers

Lifespan tasks can also be defined as async contextmanagers. This is useful for
setting up and tearing down resources and behaves similarly to the ASGI lifespan
protocol.

Code up to the first `yield` will run when the backend comes up. As the backend
is shutting down, the code after the `yield` will run to clean up.

Here is an example borrowed from the FastAPI docs and modified to work with this
interface.

```python
from contextlib import asynccontextmanager


def fake_answer_to_everything_ml_model(x: float):
    return x * 42


ml_models = \{}


@asynccontextmanager
async def setup_model(app: FastAPI):
    # Load the ML model
    ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()

...

app = rx.App()
app.register_lifespan_task(setup_model)
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/utility_methods/exception_handlers.md`:

```md
# Exception handlers

_Added in v0.5.7_

Exceptions handlers are functions that can be assigned to your app to handle exceptions that occur during the application runtime.
They are useful for customizing the response when an error occurs, logging errors, and performing cleanup tasks.

## Types

Reflex support two type of exception handlers `frontend_exception_handler` and `backend_exception_handler`.

They are used to handle exceptions that occur in the `frontend` and `backend` respectively.

The `frontend` errors are coming from the JavaScript side of the application, while `backend` errors are coming from the the event handlers on the Python side.

## Register an Exception Handler

To register an exception handler, assign it to `app.frontend_exception_handler` or `app.backend_exception_handler` to assign a function that will handle the exception.

The expected signature for an error handler is `def handler(exception: Exception)`.

```md alert warning
# Only named functions are supported as exception handler.
```

## Examples

```python
import reflex as rx

def custom_frontend_handler(exception: Exception) -> None:
    # My custom logic for frontend errors
    print("Frontend Error: " + str(exception))

def custom_backend_handler(exception: Exception) -> Optional[rx.event.EventSpec]:
    # My custom logic for backend errors
    print("Backend Error: " + str(exception))

app = rx.App(
    frontend_exception_handler = custom_frontend_handler,
    backend_exception_handler = custom_backend_handler
    )
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/utility_methods/other_methods.md`:

```md
# Other Methods

* `reset`: set all Vars to their default value for the given state (including substates).
* `get_value`: returns the value of a Var **without tracking changes to it**. This is useful
   for serialization where the tracking wrapper is considered unserializable.
* `dict`: returns all state Vars (and substates) as a dictionary. This is
  used internally when a page is first loaded and needs to be "hydrated" and
  sent to the client.

## Special Attributes

* `dirty_vars`: a set of all Var names that have been modified since the last
  time the state was sent to the client. This is used internally to determine
  which Vars need to be sent to the client after processing an event.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/utility_methods/router_attributes.md`:

```md

# State Utility Methods

The state object has several methods and attributes that return information
about the current page, session, or state.

## Router Attributes

The `self.router` attribute has several sub-attributes that provide various information:

* `router.page`: data about the current page and route
  * `host`: The hostname and port serving the current page (frontend).
  * `path`: The path of the current page (for dynamic pages, this will contain the slug)
  * `raw_path`: The path of the page displayed in the browser (including params and dynamic values)
  * `full_path`: `path` with `host` prefixed
  * `full_raw_path`: `raw_path` with `host` prefixed
  * `params`: Dictionary of query params associated with the request

* `router.session`: data about the current session
  * `client_token`: UUID associated with the current tab's token. Each tab has a unique token.
  * `session_id`: The ID associated with the client's websocket connection. Each tab has a unique session ID.
  * `client_ip`: The IP address of the client. Many users may share the same IP address.

* `router.headers`: a selection of common headers associated with the websocket
  connection. These values can only change when the websocket is re-established
  (for example, during page refresh). All other headers are available in the
  dictionary `self.router_data.headers`.
  * `host`: The hostname and port serving the websocket (backend).

### Example Values on this Page

```python eval
rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Value"),
            ),
        ),
        rx.table.body(
            *[
                rx.table.row(
                    rx.table.cell(item["name"], style=cell_style),
                    rx.table.cell(rx.code(item["value"], style=get_code_style("violet"))),
                )
                for item in router_data
            ]
        ),
        variant="surface",
        margin_y="1em",
    )
```

```