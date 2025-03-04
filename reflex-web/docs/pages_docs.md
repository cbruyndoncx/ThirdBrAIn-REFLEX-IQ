Project Path: pages

Source Tree:

```
pages
├── overview.md
└── dynamic_routing.md

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/pages/overview.md`:

```md

# Pages

Pages map components to different URLs in your app. This section covers creating pages, handling URL arguments, accessing query parameters, managing page metadata, and handling page load events.

## Adding a Page

You can create a page by defining a function that returns a component.
By default, the function name will be used as the route, but you can also specify a route.

```python
def index():
    return rx.text('Root Page')

def about():
    return rx.text('About Page')


def custom():
    return rx.text('Custom Route')

app = rx.App()

app.add_page(index)
app.add_page(about)
app.add_page(custom, route="/custom-route")
```

In this example we create three pages:

- `index` - The root route, available at `/`
- `about` - available at `/about`
- `custom` - available at `/custom-route`

```md alert
# Index is a special exception where it is available at both `/` and `/index`. All other pages are only available at their specified route.
```

```md video https://youtube.com/embed/ITOZkzjtjUA?start=3853&end=4083
# Video: Pages and URL Routes
```

## Page Decorator

You can also use the `@rx.page` decorator to add a page.

```python
@rx.page(route='/', title='My Beautiful App')
def index():
    return rx.text('A Beautiful App')
```

This is equivalent to calling `app.add_page` with the same arguments.

```md alert warning
# Remember to import the modules defining your decorated pages.

This is necessary for the pages to be registered with the app.

You can directly import the module or import another module that imports the decorated pages.
```

## Navigating Between Pages

### Links

[Links]({library.typography.link.path}) are accessible elements used primarily for navigation. Use the `href` prop to specify the location for the link to navigate to.

```python demo
rx.link("Reflex Home Page.", href="https://reflex.dev/")
```

You can also provide local links to other pages in your project without writing the full url.

```python demo
rx.link("Example", href="/docs/library")
```

To open the link in a new tab, set the `is_external` prop to `True`.

```python demo
rx.link("Open in new tab", href="https://reflex.dev/", is_external=True)
```

Check out the [link docs]({library.typography.link.path}) to learn more.

```md video https://youtube.com/embed/ITOZkzjtjUA?start=4083&end=4423
# Video: Link-based Navigation
```

### Redirect

Redirect the user to a new path within the application using `rx.redirect()`.

- `path`: The destination path or URL to which the user should be redirected.
- `external`: If set to True, the redirection will open in a new tab. Defaults to `False`.

```python demo
rx.vstack(
    rx.button("open in tab", on_click=rx.redirect("/docs/api-reference/special_events")),
    rx.button("open in new tab", on_click=rx.redirect('https://github.com/reflex-dev/reflex/', is_external=True))
)
```

Redirect can also be run from an event handler in State, meaning logic can be added behind it. It is necessary to `return` the `rx.redirect()`.

```python demo exec
class Redirect2ExampleState(rx.State):
    redirect_to_org: bool = False

    @rx.event
    def change_redirect(self):
        self.redirect_to_org = not self.redirect_to_org

    @rx.var
    def url(self) -> str:
        return 'https://github.com/reflex-dev/' if self.redirect_to_org else 'https://github.com/reflex-dev/reflex/'

    @rx.event
    def change_page(self):
        return rx.redirect(self.url, is_external=True)

def redirect_example():
    return rx.vstack(
        rx.text(f"{Redirect2ExampleState.url}"),
        rx.button("Change redirect location", on_click=Redirect2ExampleState.change_redirect),
        rx.button("Redirect to new page in State", on_click=Redirect2ExampleState.change_page),

    )
```

```md video https://youtube.com/embed/ITOZkzjtjUA?start=4423&end=4903
# Video: Redirecting to a New Page
```

## Nested Routes

Pages can also have nested routes.

```python
def nested_page():
    return rx.text('Nested Page')

app = rx.App()
app.add_page(nested_page, route='/nested/page')
```

This component will be available at `/nested/page`.

## Page Metadata


You can add page metadata such as:

- The title to be shown in the browser tab
- The description as shown in search results
- The preview image to be shown when the page is shared on social media
- Any additional metadata

```python
{meta_data}
```

## Getting the Current Page

You can access the current page from the `router` attribute in any state. See the [router docs]({docs.utility_methods.router_attributes.path}) for all available attributes.

```python
class State(rx.State):
    def some_method(self):
        current_page_route = self.router.page.path
        current_page_url = self.router.page.raw_path
        # ... Your logic here ...
```

The `router.page.path` attribute allows you to obtain the path of the current page from the router data,
for [dynamic pages]({docs.pages.dynamic_routing.path}) this will contain the slug rather than the actual value used to load the page.

To get the actual URL displayed in the browser, use `router.page.raw_path`. This
will contain all query parameters and dynamic path segments.


In the above example, `current_page_route` will contain the route pattern (e.g., `/posts/[id]`), while `current_page_url`
will contain the actual URL (e.g., `/posts/123`).

To get the full URL, access the same attributes with `full_` prefix.

Example:

```python
class State(rx.State):
    @rx.var
    def current_url(self) -> str:
        return self.router.page.full_raw_path

def index():
    return rx.text(State.current_url)

app = rx.App()
app.add_page(index, route='/posts/[id]')
```

In this example, running on `localhost` should display `http://localhost:3000/posts/123/`

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/pages/dynamic_routing.md`:

```md


# Dynamic Routes

Dynamic routes in Reflex allow you to handle varying URL structures, enabling you to create flexible
and adaptable web applications. This section covers regular dynamic routes, catch-all routes,
and optional catch-all routes, each with detailed examples.

## Regular Dynamic Routes

Regular dynamic routes in Reflex allow you to match specific segments in a URL dynamically. A regular dynamic route is defined by square brackets in a route string / url pattern. For example `/users/[id]` or `/products/[category]`. These dynamic route arguments can be accessed through a state var. For the examples above they would be `rx.State.id` and `rx.State.category` respectively. 

```md alert info
# Why is the state var accessed as `rx.State.id`?
The dynamic route arguments are accessible as `rx.State.id` and `rx.State.category` here as the var is added to the root state, so that it is accessible from any state.
```

Example:

```python
   
@rx.page(route='/post/[pid]')
def post():
    '''A page that updates based on the route.'''
    # Displays the dynamic part of the URL, the post ID
    return rx.heading(rx.State.pid)

app = rx.App()
```

The [pid] part in the route is a dynamic segment, meaning it can match any value provided in the URL. For instance, `/post/5`, `/post/10`, or `/post/abc` would all match this route.

If a user navigates to `/post/5`, `State.post_id` will return `5`, and the page will display `5` as the heading. If the URL is `/post/xyz`, it will display `xyz`. If the URL is `/post/` without any additional parameter, it will display `""`.


### Adding Dynamic Routes

Adding dynamic routes uses the `add_page` method like any other page. The only difference is that the route string contains dynamic segments enclosed in square brackets.


If you are using the `app.add_page` method to define pages, it is necessary to add the dynamic routes first, especially if they use the same function as a non dynamic route.

For example the code snippet below will:

```python
app.add_page(index, route="/page/[page_id]", on_load=DynamicState.on_load)
app.add_page(index, route="/static/x", on_load=DynamicState.on_load)
app.add_page(index)
```

But if we switch the order of adding the pages, like in the example below, it will not work:

```python
app.add_page(index, route="/static/x", on_load=DynamicState.on_load) 
app.add_page(index)
app.add_page(index, route="/page/[page_id]", on_load=DynamicState.on_load)
```


## Catch-All Routes

Catch-all routes in Reflex allow you to match any number of segments in a URL dynamically.

Example:

```python
class State(rx.State):
    @rx.var
    def user_post(self) -> str:
        args = self.router.page.params
        usernames = args.get('username', [])
        return f"Posts by \{', '.join(usernames)}"

@rx.page(route='/users/[id]/posts/[...username]')
def post():
    return rx.center(
        rx.text(State.user_post)
    )


app = rx.App()

```

In this case, the `...username` catch-all pattern captures any number of segments after
`/users/`, allowing URLs like `/users/2/posts/john/` and `/users/1/posts/john/doe/` to match the route.

## Optional Catch-All Routes

Optional catch-all routes, enclosed in double square brackets (`[[...]]`). This indicates that the specified segments
are optional, and the route can match URLs with or without those segments.

Example:

```python

class State(rx.State):
    @rx.var
    def user_post(self) -> str:
        args = self.router.page.params
        usernames = args.get('username', [])
        return f'Posts by \{', '.join(usernames)}'

@rx.page(route='/users/[id]/posts/[[...username]]')
def post():
    return rx.center(
        rx.text(State.user_post)
    )


app = rx.App()

```

Optional catch-all routes allow matching URLs with or without specific segments.
Each optional catch-all pattern should be independent and not nested within another catch-all pattern.

```md alert
# Catch-all routes must be placed at the end of the URL pattern to ensure proper route matching.
```

### Routes Validation Table

| Route Pattern                                         | Example URl                                            |    valid |
|:------------------------------------------------------|:-------------------------------------------------------|---------:|
| `/users/posts`                                        | `/users/posts`                                         |    valid |
| `/products/[category]`                                | `/products/electronics`                                |    valid |
| `/users/[username]/posts/[id]`                       | `/users/john/posts/5`                                  |    valid |
| `/users/[...username]/posts`                          | `/users/john/posts`                                    |  invalid |
|                                                       | `/users/john/doe/posts`                                |  invalid |
| `/users/[...username]`                                | `/users/john/`                                         |    valid |
|                                                       | `/users/john/doe`                                      |    valid |
| `/products/[category]/[...subcategories]`             | `/products/electronics/laptops`                        |    valid |
|                                                       | `/products/electronics/laptops/lenovo`                 |    valid |
| `/products/[category]/[[...subcategories]]`           | `/products/electronics`                                |    valid |
|                                                       | `/products/electronics/laptops`                        |    valid |
|                                                       | `/products/electronics/laptops/lenovo`                 |    valid |
|                                                       | `/products/electronics/laptops/lenovo/thinkpad`        |    valid |
| `/products/[category]/[...subcategories]/[...items]`  | `/products/electronics/laptops`                        |  invalid |
|                                                       | `/products/electronics/laptops/lenovo`                 |  invalid |
|                                                       | `/products/electronics/laptops/lenovo/thinkpad`        |  invalid |

```