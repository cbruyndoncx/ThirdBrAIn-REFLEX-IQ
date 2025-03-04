Project Path: wrapping-react

Source Tree:

```
wrapping-react
├── guide.md
├── overview.md
├── example.md
└── more-wrapping-examples.md

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/wrapping-react/guide.md`:

```md


# Full Guide

Let's walk step by step through how to wrap a React component in Reflex, using the color picker as our primary example. You can also see the full [API reference]({api_reference.component.path}).

```python eval
rx.box(
    ColorPickerState,
    rx.vstack(
        rx.heading(ColorPickerState.value, color="white"),
        color_picker(
            on_change=ColorPickerState.set_value
        ),
    ),
    background_color=ColorPickerState.value,
    padding="5em",
    border_radius="12px",
    margin_bottom="1em",
)
```

## Find The Component

There are two ways to find a component to wrap:
1. Write the component yourself locally.
2. Find a well-maintained React library on [npm](https://www.npmjs.com/) that contains the component you need.

In both cases, the process of wrapping the component is the same except for the `library` field.

In this guide we are wrapping the `HexColorPicker` component from the [react-colorful](https://www.npmjs.com/package/react-colorful) library.

## Define the Component

The first step to wrapping any React component is to subclass `rx.Component`.

```python
class ColorPicker(rx.Component):
    """A color picker component."""
```

## Set the Library and Tag

The library is just the name of the `npm` package, and the tag is the name of the React component from the package that you want to wrap. Some packages have multiple components, and you can wrap each one as a separate Reflex component.

You can generally find the library and tag by looking at the import statement in the React code.

```javascript
import \{ HexColorPicker } from "react-colorful"
```

In this case, the library is `react-colorful` and the tag is `HexColorPicker`.


```python
class ColorPicker(rx.Component):
    """Color picker component."""

    library = "react-colorful"
    tag = "HexColorPicker"
```

When you create your component, Reflex will automatically install the library for you.

### Local Components

You can also wrap components that you have written yourself. Local components should be stored in your `assets` directory. For example, you could define a basic `Hello` component like this:

```javascript
// assets/hello.js
import React from 'react';

export function Hello() {
  return (
    <div>
      <h1>Hello!</h1>
    </div>
  )
}
```

Then specify the library as following (note: we use the `public` directory here instead of `assets` as this is the directory that is served by the web server):

```python
import reflex as rx

class Hello(rx.Component):
    # Use an absolute path starting with /public
    library = "/public/hello"

    # Define everything else as normal.
    tag = "Hello"
```

### Local Packages

If the component is part of a local package, available on Github, or
downloadable via a web URL, it can also be wrapped in Reflex. Specify the path
or URL after an `@` following the package name.

Any local paths are relative to the `.web` folder, so you can use `../` prefix
to reference the Reflex project root.

Some examples of valid specifiers for a package called 
[`@masenf/hello-react`](https://github.com/masenf/hello-react) are:

* GitHub: `@masenf/hello-react@github:masenf/hello-react`
* URL: `@masenf/hello-react@https://github.com/masenf/hello-react/archive/refs/heads/main.tar.gz`
* Local Archive: `@masenf/hello-react@../hello-react.tgz`
* Local Directory: `@masenf/hello-react@../hello-react`

It is important that the package name matches the name in `package.json` so
Reflex can generate the correct import statement in the generated javascript
code.

These package specifiers can be used for `library` or `lib_dependencies`.

```python demo exec
class GithubComponent(rx.Component):
    library = "@masenf/hello-react@github:masenf/hello-react"
    tag = "Counter"

    def add_imports(self):
        return {
            "": ["@masenf/hello-react/dist/style.css"]
        }

def github_component_example():
    return GithubComponent.create()
```

Although more complicated, this approach is useful when the local components
have additional dependencies or build steps required to prepare the component
for use.

Some important notes regarding this approach:

* The repo or archive must contain a `package.json` file.
* `prepare` or `build` scripts will NOT be executed. The distribution archive,
  directory, or repo must already contain the built javascript files (this is common).

```md alert
# Ensure CSS files are exported in `package.json`

In addition to exporting the module containing the component, any CSS files
intended to be imported by the wrapped component must also be listed in the
`exports` key of `package.json`.

```json
{
  // ...,
  "exports": {
    ".": {
      "import": "./dist/index.js",
      "require": "./dist/index.umd.cjs"
    },
    "./dist/style.css": {
      "import": "./dist/style.css",
      "require": "./dist/style.css"
    }
  },
  // ...
}
```

### Import Types

Sometimes the component is a default export from the module (meaning it doesn't require curly braces in the import statement).

```javascript
import Spline from '@splinetool/react-spline';
```

In these cases you must set `is_default = True` in your component class, as we did in the Spline example in the overview section:

```python
class Spline(rx.Component):
    """Spline component."""
 
    library = "@splinetool/react-spline"
    tag = "Spline"
    is_default = True  # Needed for default imports
```

### Library Dependencies

By default Reflex will install the library you have specified in the library property. However, sometimes you may need to install other libraries to use a component. In this case you can use the `lib_dependencies` property to specify other libraries to install.

As seen in the Spline example in the overview section, we need to import the `@splinetool/runtime` library to use the `Spline` component. We can specify this in our component class like this:

```python
class Spline(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline"  # This is installed by default
    lib_dependencies: list[str] = ["@splinetool/runtime@1.5.5"]  # Specify extra npm packages to install.
```

In this example we are adding this dependency to pin its version. It would be automatically installed alongside the `react-spline` library when the component is created.

A useful time to add `lib_dependencies` is when we are wrapping a component and we want plugins or extensions for the library. A good example is the React component `react-markdown` with its [extensions](https://www.npmjs.com/package/react-markdown#plugins). 

### Versions

You can specify the version of the library you want to install by appending `@` and the version number to the library name.

```python
class Spline(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline@1.0.0"
```

This is recommended to ensure that your app works consistently across different environments.

### Dynamic Imports

Some libraries you may want to wrap may require dynamic imports. This is because they they may not be compatible with Server-Side Rendering (SSR).

To handle this in Reflex, subclass `NoSSRComponent` when defining your component.

Often times when you see an import something like this:

```javascript
import dynamic from 'next/dynamic';

const MyLibraryComponent = dynamic(() => import('./MyLibraryComponent'), {
  ssr: false
});
```

You can wrap it in Reflex like this, here we are wrapping the `react-plotly.js` library which requires dynamic imports:

```python
from reflex.components.component import NoSSRComponent

class PlotlyLib(NoSSRComponent):
    """A component that wraps a plotly lib."""

    library = "react-plotly.js@2.6.0"

    lib_dependencies: List[str] = ["plotly.js@2.22.0"]
```

It may not always be clear when a library requires dynamic imports. A few things to keep in mind are if the component is very client side heavy i.e. the view and structure depends on things that are fetched at run time, or if it uses `window` or `document` objects directly it will need to be wrapped as a `NoSSRComponent`. 

Some examples are:

1. Video and Audio Players
2. Maps
3. Drawing Canvas
4. 3D Graphics
5. QR Scanners
6. Reactflow

The reason for this is that it does not make sense for your server to render these components as the server does not have access to your camera, it cannot draw on your canvas or render a video from a file. 

In addition, if in the component documentation it mentions nextJS compatibility or server side rendering compatibility, it is a good sign that it requires dynamic imports.


### Additional Imports

Sometimes you may need to import additional files or stylesheets to use a component. You can do this by overriding the `add_imports` method in your component class. The method returns a dictionary where the key is the library and the values are a list of imports.

```python
class ReactFlowLib(rx.Component):
    """A component that wraps a react flow lib."""

    library = "reactflow"

    def add_imports(self):
        return {
            "": ['reactflow/dist/style.css']
        }
```

You can use the empty string as the key to import files that are not part of a library.

### Aliases

If you are wrapping another component with the same tag as a component in your project you can use aliases to differentiate between them and avoid naming conflicts.

Lets check out the code below, in this case if we needed to wrap another color picker library with the same tag we use an alias to avoid a conflict.

```python
class AnotherColorPicker(rx.Component):
    library = "some-other-colorpicker"
    tag = "HexColorPicker"
    alias = "OtherHexColorPicker" # This can now coexist with the original HexColorPicker
```

## Custom Code

Sometimes you may need to add custom code to your component, such as defining constants and functions used. Custom code will be inserted _outside_ of the react component function.

```javascript
import React from "react";
// Other imports...
...

// Custom code
const customCode = "const customCode = 'customCode';";
```

To add custom code to your component you can use the `add_custom_code` method in your component class.

```python
from reflex.components.component import NoSSRComponent

class PlotlyLib(NoSSRComponent):
    """A component that wraps a plotly lib."""

    library = "react-plotly.js@2.6.0"

    lib_dependencies: List[str] = ["plotly.js@2.22.0"]

    def add_custom_code(self) -> str:
        return "const customCode = 'customCode';"
```

## Props

Props are the variables that you can pass to the component. In the case of our color picker, we have a single prop `color`. Props are defined using `rx.Var` with the type of the prop. Specifying the type helps the compiler catch errors and provides better intellisense.

```python
class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"

    # Define all props using rx.Var
    color: rx.Var[str]

color_picker = ColorPicker.create
```

Then when you create the component, you can pass in the props as keyword arguments.

```python demo
color_picker(color="#db114b")
```

### Default Value

You can set a default value for the prop by assigning it in the class definition.

```python
class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"

    # Set a default value for the color prop
    color: rx.Var[str] = "#db114b" 
```

## Serializers

Vars can be any type that can be serialized to JSON. This includes primitive types like strings, numbers, and booleans, as well as more complex types like lists, dictionaries, and dataframes.

In case you need to serialize a more complex type, you can use the `serializer` decorator to convert the type to a primitive type that can be stored in the state. Just define a method that takes the complex type as an argument and returns a primitive type. We use type annotations to determine the type that you want to serialize.

For example, the Plotly component serializes a plotly figure into a JSON string that can be stored in the state.

```python
import json
import reflex as rx
from plotly.graph_objects import Figure
from plotly.io import to_json

# Use the serializer decorator to convert the figure to a JSON string.
# Specify the type of the argument as an annotation.
@rx.serializer
def serialize_figure(figure: Figure) -> list:
    # Use Plotly's to_json method to convert the figure to a JSON string.
    return json.loads(str(to_json(figure)))["data"]
```

We can then define a var of this type as a prop in our component.

```python
import reflex as rx
from plotly.graph_objects import Figure

class Plotly(rx.Component):
    """Display a plotly graph."""
    library = "react-plotly.js@2.6.0"
    lib_dependencies: List[str] = ["plotly.js@2.22.0"]

    tag = "Plot"

    is_default = True

    # Since a serialize is defined now, we can use the Figure type directly.
    data: rx.Var[Figure]
```

## Event Handlers

Recall that [event handlers]({events.events_overview.path}) are ways that components can handle user interactions. In the case of the color picker, we have a single event trigger `on_change` that triggers when the color changes. The event trigger takes a single argument `color` which is the new color.

```python
class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: rx.Var[str]
    on_change: rx.EventHandler[lambda color: [color]]
```

We can then bind this event trigger to an event handler in our state that takes the color as an argument.

```python
class ColorPickerState(rx.State):
    color: str = "#db114b"

    def set_color(self, color: str):
        self.color = color

def index():
    return color_picker(
        color=ColorPickerState.color,
        # Set the event handler.
        on_change=ColorPickerState.set_color
    )
```

## Assets

_Experimental feature added in v0.5.3_.

If a wrapped component depends on assets such as images, scripts, or
stylesheets, these can kept adjacent to the component code and
included in the final build using the `rx._x.asset` function.

`rx._x.asset` returns a relative path that references the asset in the compiled
output. The target files are copied into a subdirectory of `assets/external`
based on the module where they are initially used. This allows third-party
components to have external assets with the same name without conflicting
with each other.

For example, if there is an SVG file named `wave.svg` in the same directory as
this component, it can be rendered using `rx.image` and `rx._x.asset`.

```python
class Hello(rx.Component):
    @classmethod
    def create(cls, *children, **props) -> rx.Component:
        props.setdefault("align", "center")
        return rx.hstack(
            rx.image(src=rx._x.asset("wave.svg"), width="50px", height="50px"),
            rx.heading("Hello ", *children),
            **props
        )
```


## Debugging

If you encounter an error while wrapping a component it is recommended to check the Console in the browser developer tools. You can access this by going to inspect element and then clicking on the Console tab on Mac. This is because the Console is where most Javascript errors are logged.
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/wrapping-react/overview.md`:

```md

# Wrapping React

One of Reflex's most powerful features is the ability to wrap React components and take advantage of the vast ecosystem of React libraries.

If you want a specific component for your app but Reflex doesn't provide it, there's a good chance it's available as a React component. Search for it on [npm]({constants.NPMJS_URL}), and if it's there, you can use it in your Reflex app. You can also create your own local React components and wrap them in Reflex.

Once you wrap your component, you [publish it]({custom_components.overview.path}) to the Reflex library so that others can use it.

## Simple Example

Simple components that don't have any interaction can be wrapped with just a few lines of code. 

Below we show how to wrap the [Spline]({constants.SPLINE_URL}) library can be used to create 3D scenes and animations.

```python demo exec
import reflex as rx

class Spline(rx.Component):
    """Spline component."""

    # The name of the npm package.
    library = "@splinetool/react-spline"

    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = ["@splinetool/runtime@1.5.5"]

    # The name of the component to use from the package.
    tag = "Spline"

    # Spline is a default export from the module.
    is_default = True

    # Any props that the component takes.
    scene: rx.Var[str]

# Convenience function to create the Spline component.
spline = Spline.create

# Use the Spline component in your app.
def index():
    return spline(scene="https://prod.spline.design/joLpOOYbGL-10EJ4/scene.splinecode")
```


## ColorPicker Example

Similar to the Spline example we start with defining the library and tag. In this case the library is `react-colorful` and the tag is `HexColorPicker`.

We also have a var `color` which is the current color of the color picker.

Since this component has interaction we must specify any event triggers that the component takes. The color picker has a single trigger `on_change` to specify when the color changes. This trigger takes in a single argument `color` which is the new color.


```python eval
rx.box(
    ColorPickerState,
    rx.vstack(
        rx.heading(ColorPickerState.value, color="white"),
        color_picker(
            on_change=ColorPickerState.set_value
        ),
    ),
    background_color=ColorPickerState.value,
    padding="5em",
    border_radius="12px",
    margin_bottom="1em",
)
```

```python
class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: rx.Var[str]
    on_change: rx.EventHandler[lambda color: [color]]

color_picker = ColorPicker.create

class ColorPickerState(rx.State):
    color: str = "#db114b"

def index():
    return rx.box(
        rx.vstack(
            rx.heading(ColorPickerState.color, color="white"),
            color_picker(
                on_change=ColorPickerState.set_color
            ),
        ),
        background_color=ColorPickerState.color,
        padding="5em",
        border_radius="1em",
    )
```

## What Not To Wrap

There are some libraries on npm that are not do not expose React components and therefore are very hard to wrap with Reflex. 

A library like [spline](https://www.npmjs.com/package/@splinetool/runtime) below is going to be difficult to wrap with Reflex because it does not expose a React component.

```javascript
import \{ Application } from '@splinetool/runtime';

// make sure you have a canvas in the body
const canvas = document.getElementById('canvas3d');

// start the application and load the scene
const spline = new Application(canvas);
spline.load('https://prod.spline.design/6Wq1Q7YGyM-iab9i/scene.splinecode');
```

You should look out for JSX, a syntax extension to JavaScript, which has angle brackets `(<h1>Hello, world!</h1>)`. If you see JSX, it's likely that the library is a React component and can be wrapped with Reflex. 

If the library does not expose a react component you need to try and find a JS React wrapper for the library, such as [react-spline](https://www.npmjs.com/package/@splinetool/react-spline).

```javascript
import Spline from '@splinetool/react-spline';

export default function App() {
  return (
    <div>
      <Spline scene="https://prod.spline.design/6Wq1Q7YGyM-iab9i/scene.splinecode" />
    </div>
  );
}
```



In the next page, we will go step by step through a more complex example of wrapping a React component.
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/wrapping-react/example.md`:

```md

# Complex Example

In this more complex example we will be wrapping `reactflow` a library for building node based applications like flow charts, diagrams, graphs, etc.

## Import

Lets start by importing the library [reactflow](https://www.npmjs.com/package/reactflow). Lets make a separate file called `reactflow.py` and add the following code:

```python
import refex as rx
from typing import Any, Dict, List, Union

class ReactFlowLib(rx.Component):
    """A component that wraps a react flow lib."""

    library = "reactflow"

    def _get_custom_code(self) -> str:
        return """import 'reactflow/dist/style.css';
        """
```

Notice we also use the `_get_custom_code` method to import the css file that is needed for the styling of the library.

## Components

For this tutorial we will wrap three components from Reactflow: `ReactFlow`, `Background`, and `Controls`. Lets start with the `ReactFlow` component.

Here we will define the `tag` and the `vars` that we will need to use the component.

For this tutorial we will define `EventHandler` props `on_nodes_change` and `on_connect`, but you can find all the events that the component triggers in the [reactflow docs](https://reactflow.dev/docs/api/react-flow-props/#onnodeschange).

```python
import reflex as rx
from typing import Any, Dict, List, Union

class ReactFlowLib(rx.Component):
    ...

class ReactFlow(ReactFlowLib):

    tag = "ReactFlow"

    nodes: rx.Var[List[Dict[str, Any]]]

    edges: rx.Var[List[Dict[str, Any]]]

    fit_view: rx.Var[bool]

    nodes_draggable: rx.Var[bool]

    nodes_connectable: rx.Var[bool]

    nodes_focusable: rx.Var[bool]

    on_nodes_change: rx.EventHandler[lambda e0: [e0]]

    on_connect: rx.EventHandler[lambda e0: [e0]]
```

Now lets add the `Background` and `Controls` components. We will also create the components using the `create` method so that we can use them in our app.

```python
import reflex as rx
from typing import Any, Dict, List, Union

class ReactFlowLib(rx.Component):
    ...

class ReactFlow(ReactFlowLib):
    ...

class Background(ReactFlowLib):

    tag = "Background"

    color: rx.Var[str]

    gap: rx.Var[int]

    size: rx.Var[int]

    variant: rx.Var[str]

class Controls(ReactFlowLib):

    tag = "Controls"

react_flow = ReactFlow.create
background = Background.create
controls = Controls.create
```

## Building the App

Now that we have our components lets build the app.

Lets start by defining the initial nodes and edges that we will use in our app.

```python
import reflex as rx
from .react_flow import react_flow, background, controls
import random
from collections import defaultdict
from typing import Any, Dict, List


initial_nodes = [
    \{
        'id': '1',
        'type': 'input',
        'data': \{'label': '150'},
        'position': \{'x': 250, 'y': 25},
    },
    \{
        'id': '2',
        'data': \{'label': '25'},
        'position': \{'x': 100, 'y': 125},
    },
    \{
        'id': '3',
        'type': 'output',
        'data': \{'label': '5'},
        'position': \{'x': 250, 'y': 250},
    },
]

initial_edges = [
    \{'id': 'e1-2', 'source': '1', 'target': '2', 'label': '*', 'animated': True},
    \{'id': 'e2-3', 'source': '2', 'target': '3', 'label': '+', 'animated': True},
]
```

Next we will define the state of our app. We have four event handlers: `add_random_node`, `clear_graph`, `on_connect` and `on_nodes_change`.

The `on_nodes_change` event handler is triggered when a node is selected and dragged. This function is used to update the position of a node during dragging. It takes a single argument `node_changes`, which is a list of dictionaries containing various types of metadata. For updating positions, the function specifically processes changes of type `position`.

```python
class State(rx.State):
    """The app state."""
    nodes: List[Dict[str, Any]] = initial_nodes
    edges: List[Dict[str, Any]] = initial_edges

    @rx.event
    def add_random_node(self):
        new_node_id = f'\{len(self.nodes) + 1\}'
        node_type = random.choice(['default'])
        # Label is random number
        label = new_node_id
        x = random.randint(0, 500)
        y = random.randint(0, 500)

        new_node = {
            'id': new_node_id,
            'type': node_type,
            'data': \{'label': label},
            'position': \{'x': x, 'y': y},
            'draggable': True,
        }
        self.nodes.append(new_node)

    @rx.event
    def clear_graph(self):
        self.nodes = []  # Clear the nodes list
        self.edges = []  # Clear the edges list

    @rx.event
    def on_connect(self, new_edge):
        # Iterate over the existing edges
        for i, edge in enumerate(self.edges):
            # If we find an edge with the same ID as the new edge
            if edge["id"] == f"e\{new_edge['source']}-\{new_edge['target']}":
                # Delete the existing edge
                del self.edges[i]
                break

        # Add the new edge
        self.edges.append({
            "id": f"e\{new_edge['source']}-\{new_edge['target']}",
            "source": new_edge["source"],
            "target": new_edge["target"],
            "label": random.choice(["+", "-", "*", "/"]),
            "animated": True,
        })

    @rx.event
    def on_nodes_change(self, node_changes: List[Dict[str, Any]]):
        # Receives a list of Nodes in case of events like dragging
        map_id_to_new_position = defaultdict(dict)

        # Loop over the changes and store the new position
        for change in node_changes:
            if change["type"] == "position" and change.get("dragging") == True:
                map_id_to_new_position[change["id"]] = change["position"]

        # Loop over the nodes and update the position
        for i, node in enumerate(self.nodes):
            if node["id"] in map_id_to_new_position:
                new_position = map_id_to_new_position[node["id"]]
                self.nodes[i]["position"] = new_position
```

Now lets define the UI of our app. We will use the `react_flow` component and pass in the `nodes` and `edges` from our state. We will also add the `on_connect` event handler to the `react_flow` component to handle when an edge is connected.

```python
def index() -> rx.Component:
    return rx.vstack(
        react_flow(
            background(),
            controls(),
            nodes_draggable=True,
            nodes_connectable=True,
            on_connect=lambda e0: State.on_connect(e0),
            on_nodes_change=lambda e0: State.on_nodes_change(e0),
            nodes=State.nodes,
            edges=State.edges,
            fit_view=True,
        ),
        rx.hstack(
            rx.button("Clear graph", on_click=State.clear_graph, width="100%"),
            rx.button("Add node", on_click=State.add_random_node, width="100%"),
            width="100%",
        ),
        height="30em",
        width="100%",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
```


Here is an example of the app running:

```python eval
rx.vstack(
        react_flow(
            background(),
            controls(),
            nodes_draggable=True,
            nodes_connectable=True,
            on_connect=lambda e0: ReactFlowState.on_connect(e0),
            on_nodes_change=lambda e0: ReactFlowState.on_nodes_change(e0),
            nodes=ReactFlowState.nodes,
            edges=ReactFlowState.edges,
            fit_view=True,
        ),
        rx.hstack(
            rx.button("Clear graph", on_click=ReactFlowState.clear_graph, width="50%"),
            rx.button("Add node", on_click=ReactFlowState.add_random_node, width="50%"),
            width="100%",
        ),
        height="30em",
        width="100%",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/wrapping-react/more-wrapping-examples.md`:

```md
# More React Libraries 


## AG Charts

Here we wrap the AG Charts library from the NPM package [ag-charts-react](https://www.npmjs.com/package/ag-charts-react). 

In the react code below we can see the first `2` lines are importing React and ReactDOM, and this can be ignored when wrapping your component.

We import the `AgCharts` component from the `ag-charts-react` library on line 5. In Reflex this is wrapped by `library = "ag-charts-react"` and `tag = "AgCharts"`.

Line `7` defines a functional React component, which on line `26` returns `AgCharts` which is similar in the Reflex code to using the `chart` component.

Line `9` uses the `useState` hook to create a state variable `chartOptions` and its setter function `setChartOptions` (equivalent to the event handler `set_chart_options` in reflex). The initial state variable is of type dict and has two key value pairs `data` and `series`. 

When we see `useState` in React code, it correlates to state variables in your State. As you can see in our Reflex code we have a state variable `chart_options` which is a dictionary, like in our React code.

Moving to line `26` we see that the `AgCharts` has a prop `options`. In order to use this in Reflex we must wrap this prop. We do this with `options: rx.Var[dict]` in the `AgCharts` component. 

Lines `31` and `32` are rendering the component inside the root element. This can be ignored when we are wrapping a component as it is done in Reflex by creating an `index` function and adding it to the app.


---md tabs

--tab React Code    

```javascript
1 | import React, \{ useState } from 'react';
2 | import ReactDOM from 'react-dom/client';
3 | 
4 | // React Chart Component
5 | import \{ AgCharts } from 'ag-charts-react';
6 | 
7 | const ChartExample = () => {
8 |     // Chart Options: Control & configure the chart
9 |     const [chartOptions, setChartOptions] = useState({
10|         // Data: Data to be displayed in the chart
11|         data: [
12|             \{ month: 'Jan', avgTemp: 2.3, iceCreamSales: 162000 },
13|             \{ month: 'Mar', avgTemp: 6.3, iceCreamSales: 302000 },
14|             \{ month: 'May', avgTemp: 16.2, iceCreamSales: 800000 },
15|             \{ month: 'Jul', avgTemp: 22.8, iceCreamSales: 1254000 },
16|             \{ month: 'Sep', avgTemp: 14.5, iceCreamSales: 950000 },
17|             \{ month: 'Nov', avgTemp: 8.9, iceCreamSales: 200000 },
18|         ],
19|         // Series: Defines which chart type and data to use
20|         series: [\{ type: 'bar', xKey: 'month', yKey: 'iceCreamSales' }],
21|     });
22| 
23|     // React Chart Component
24|     return (
25|         // AgCharts component with options passed as prop
26|         <AgCharts options=\{chartOptions} />
27|     );
28| }
29| 
30| // Render component inside root element
31| const root = ReactDOM.createRoot(document.getElementById('root'));
32| root.render(<ChartExample />);
```

--
--tab Reflex Code

```python
import reflex as rx

class AgCharts(rx.Component):
    """ A simple line chart component using AG Charts """

    library = "ag-charts-react"
    
    tag = "AgCharts"

    options: rx.Var[dict]


chart = AgCharts.create


class State(rx.State):
    """The app state."""
    chart_options: dict = {
           "data": [
                \{"month":"Jan", "avgTemp":2.3, "iceCreamSales":162000},
                \{"month":"Mar", "avgTemp":6.3, "iceCreamSales":302000},
                \{"month":"May", "avgTemp":16.2, "iceCreamSales":800000},
                \{"month":"Jul", "avgTemp":22.8, "iceCreamSales":1254000},
                \{"month":"Sep", "avgTemp":14.5, "iceCreamSales":950000},
                \{"month":"Nov", "avgTemp":8.9, "iceCreamSales":200000}
            ],
            "series": [\{"type":"bar", "xKey":"month", "yKey":"iceCreamSales"}]
        }

def index() -> rx.Component:
    return chart(
        options=State.chart_options,
    )

app = rx.App()
app.add_page(index)
```
--

---


## React Leaflet


In this example we are wrapping the React Leaflet library from the NPM package [react-leaflet](https://www.npmjs.com/package/react-leaflet).

On line `1` we import the `dynamic` function from Next.js and on line `21` we set `ssr: false`. Lines `4` and `6` use the `dynamic` function to import the `MapContainer` and `TileLayer` components from the `react-leaflet` library. This is used to dynamically import the `MapContainer` and `TileLayer` components from the `react-leaflet` library. This is done in Reflex by using the `NoSSRComponent` class when defining the component. There is more information of when this is needed on the `Dynamic Imports` section of this [page]({docs.wrapping_react.guide.path}).

It mentions in the documentation that it is necessary to include the Leaflet CSS file, which is added on line `2` in the React code below. This can be done in Reflex by using the `add_imports` method in the `MapContainer` component. We can add a relative path from within the React library or a full URL to the CSS file.

Line `4` defines a functional React component, which on line `8` returns the `MapContainer` which is done in the Reflex code using the `map_container` component.

The `MapContainer` component has props `center`, `zoom`, `scrollWheelZoom`, which we wrap in the `MapContainer` component in the Reflex code. We ignore the `style` prop as it is a reserved name in Reflex. We can use the `rename_props` method to change the name of the prop, as we will see in the React PDF Renderer example, but in this case we just ignore it and add the `width` and `height` props as css in Reflex.

The `TileLayer` component has a prop `url` which we wrap in the `TileLayer` component in the Reflex code.

Lines `24` and `25` defines and exports a React functional component named `Home` which returns the `MapComponent` component. This can be ignored in the Reflex code when wrapping the component as we return the `map_container` component in the `index` function.

---md tabs

--tab React Code 

```javascript
1 | import dynamic from "next/dynamic";
2 | import "leaflet/dist/leaflet.css";
3 | 
4 | const MapComponent = dynamic(
5 |   () => {
6 |     return import("react-leaflet").then((\{ MapContainer, TileLayer }) => {
7 |       return () => (
8 |         <MapContainer
9 |           center=\{[51.505, -0.09]}
10|           zoom=\{13}
11|           scrollWheelZoom=\{true}
12|           style=\{\{ height: "50vh", width: "100%" }}
13|        >
14|          <TileLayer
15|            url="https://\{s}.tile.openstreetmap.org/\{z}/\{x}/\{y}.png"
16|          />
17|        </MapContainer>
18|      );
19|    });
20|  },
21|  \{ ssr: false }
22| );
23|
24| export default function Home() {
25|   return <MapComponent />;
26| }
```

--
--tab Reflex Code

```python 
import reflex as rx

class MapContainer(rx.NoSSRComponent):

    library = "react-leaflet"

    tag = "MapContainer"

    center: rx.Var[list]

    zoom: rx.Var[int]

    scroll_wheel_zoom: rx.Var[bool]

    # Can also pass a url like: https://unpkg.com/leaflet/dist/leaflet.css 
    def add_imports(self):
        return \{"": ["leaflet/dist/leaflet.css"]}



class TileLayer(rx.NoSSRComponent):

    library = "react-leaflet"

    tag = "TileLayer"

    url: rx.Var[str]


map_container = MapContainer.create
tile_layer = TileLayer.create

def index() -> rx.Component:
    return map_container(
                tile_layer(url="https://\{s}.tile.openstreetmap.org/\{z}/\{x}/\{y}.png"),
                center=[51.505, -0.09], 
                zoom=13,
                #scroll_wheel_zoom=True
                width="100%",
                height="50vh",
            )


app = rx.App()
app.add_page(index)

```
--

---


## React PDF Renderer

In this example we are wrapping the React renderer for creating PDF files on the browser and server from the NPM package [@react-pdf/renderer](https://www.npmjs.com/package/@react-pdf/renderer).

This example is similar to the previous examples, and again Dynamic Imports are required for this library. This is done in Reflex by using the `NoSSRComponent` class when defining the component. There is more information on why this is needed on the `Dynamic Imports` section of this [page]({docs.wrapping_react.guide.path}).

The main difference with this example is that the `style` prop, used on lines `20`, `21` and `24` in React code, is a reserved name in Reflex so can not be wrapped. A different name must be used when wrapping this prop and then this name must be changed back to the original with the `rename_props` method. In this example we name the prop `theme` in our Reflex code and then change it back to `style` with the `rename_props` method in both the `Page` and `View` components.


```md alert info
# List of reserved names in Reflex

_The style of the component._

`style: Style = Style()`

_A mapping from event triggers to event chains._

`event_triggers: Dict[str, Union[EventChain, Var]] = \{}`

_The alias for the tag._

`alias: Optional[str] = None`

_Whether the import is default or named._

`is_default: Optional[bool] = False`

_A unique key for the component._

`key: Any = None`

_The id for the component._

`id: Any = None`

_The class name for the component._

`class_name: Any = None`

_Special component props._

`special_props: List[Var] = []`

_Whether the component should take the focus once the page is loaded_

`autofocus: bool = False`

_components that cannot be children_

`_invalid_children: List[str] = []`

_only components that are allowed as children_

`_valid_children: List[str] = []`

_only components that are allowed as parent_

`_valid_parents: List[str] = []`

_props to change the name of_

`_rename_props: Dict[str, str] = \{}`

_custom attribute_

`custom_attrs: Dict[str, Union[Var, str]] = \{}`

_When to memoize this component and its children._

`_memoization_mode: MemoizationMode = MemoizationMode()`

_State class associated with this component instance_

`State: Optional[Type[reflex.state.State]] = None`
```

---md tabs

--tab React Code    

```javascript
1 | import ReactDOM from 'react-dom';
2 | import \{ Document, Page, Text, View, StyleSheet, PDFViewer } from '@react-pdf/renderer';
3 |
4 | // Create styles
5 | const styles = StyleSheet.create({
6 |   page: {
7 |     flexDirection: 'row',
8 |     backgroundColor: '#E4E4E4',
9 |   },
10|   section: {
11|     margin: 10,
12|    padding: 10,
13|     flexGrow: 1,
14|   },
15| });
16|
17| // Create Document Component
18| const MyDocument = () => (
19|   <Document>
20|     <Page size="A4" style=\{styles.page}>
21|       <View style=\{styles.section}>
22|         <Text>Section #1</Text>
23|       </View>
24|       <View style=\{styles.section}>
25|         <Text>Section #2</Text>
26|       </View>
27|     </Page>
28|   </Document>
29| );
30| 
31| const App = () => (
32|   <PDFViewer>
33|     <MyDocument />
34|   </PDFViewer>
35| );
36| 
37| ReactDOM.render(<App />, document.getElementById('root'));
```

--
--tab Reflex Code

```python
import reflex as rx

class Document(rx.Component):
    
    library = "@react-pdf/renderer"

    tag = "Document"
    

class Page(rx.Component):
    
    library = "@react-pdf/renderer"

    tag = "Page"

    size: rx.Var[str]
    # here we are wrapping style prop but as style is a reserved name in Reflex we must name it something else and then change this name with rename props method
    theme: rx.Var[dict]

    _rename_props: dict[str, str] = {
        "theme": "style",
    }


class Text(rx.Component):
    
    library = "@react-pdf/renderer"

    tag = "Text"


class View(rx.Component):
    
    library = "@react-pdf/renderer"

    tag = "View"

    # here we are wrapping style prop but as style is a reserved name in Reflex we must name it something else and then change this name with rename props method
    theme: rx.Var[dict]

    _rename_props: dict[str, str] = {
        "theme": "style",
    }


class StyleSheet(rx.Component):
    
    library = "@react-pdf/renderer"

    tag = "StyleSheet"

    page: rx.Var[dict]

    section: rx.Var[dict]


class PDFViewer(rx.NoSSRComponent):
    
    library = "@react-pdf/renderer"

    tag = "PDFViewer"


document = Document.create
page = Page.create
text = Text.create
view = View.create
style_sheet = StyleSheet.create
pdf_viewer = PDFViewer.create


styles = style_sheet({
  "page": {
    "flexDirection": 'row',
    "backgroundColor": '#E4E4E4',
  },
  "section": {
    "margin": 10,
    "padding": 10,
    "flexGrow": 1,
  },
})


def index() -> rx.Component:
    return pdf_viewer( 
        document(
            page(
                view(
                    text("Hello, World!"),
                    theme=styles.section,
                ),
                view(
                    text("Hello, 2!"),
                    theme=styles.section,
                ),
                size="A4", theme=styles.page),
        ),
        width="100%",
        height="80vh",
    )

app = rx.App()
app.add_page(index)
```
--

---
```