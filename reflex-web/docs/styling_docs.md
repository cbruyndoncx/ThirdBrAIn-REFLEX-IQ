Project Path: styling

Source Tree:

```
styling
├── responsive.md
├── overview.md
├── theming.md
├── layout.md
├── custom-stylesheets.md
└── common-props.md

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/styling/responsive.md`:

```md

# Responsive

Reflex apps can be made responsive to look good on mobile, tablet, and desktop.

You can pass a list of values to any style property to specify its value on different screen sizes.

```python demo
rx.text(
    "Hello World",
    color=["orange", "red", "purple", "blue", "green"],
)
```

The text will change color based on your screen size. If you are on desktop, try changing the size of your browser window to see the color change.

_New in 0.5.6_

Responsive values can also be specified using `rx.breakpoints`. Each size maps to a corresponding key, the value of which will be applied when the screen size is greater than or equal to the named breakpoint.

```python demo
rx.text(
    "Hello World",
    color=rx.breakpoints(
        initial="orange",
        sm="purple",
        lg="green",
    ),
)
```

Custom breakpoints in CSS units can be mapped to values per component using a dictionary instead of named parameters.

```python
rx.text(
    "Hello World",
    color=rx.breakpoints({
        "0px": "orange",
        "48em": "purple",
        "80em": "green",
    }),
)
```

For the Radix UI components' fields that supports responsive value, you can also use `rx.breakpoints` (note that custom breakpoints and list syntax aren't supported).

```python demo
rx.grid(
    rx.foreach(
        list(range(6)),
        lambda _: rx.box(bg_color="#a7db76", height="100px", width="100px")
    ),
    columns=rx.breakpoints(
        initial="2",
        sm="4",
        lg="6"
    ),
    spacing="4"
)
```

## Setting Defaults

The default breakpoints are shown below.

```python eval
rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Size"),
            rx.table.column_header_cell("Width"),
        ),
    ),
    rx.table.body(
        rx.table.row(
            rx.table.cell(rx.code("initial", style=get_code_style("violet"))),
            rx.table.cell("0px", style=cell_style),
        ),
        rx.table.row(
            rx.table.cell(rx.code("xs", style=get_code_style("violet"))),
            rx.table.cell("30em", style=cell_style),
        ),
        rx.table.row(
            rx.table.cell(rx.code("sm", style=get_code_style("violet"))),
            rx.table.cell("48em", style=cell_style),
        ),
        rx.table.row(
            rx.table.cell(rx.code("md", style=get_code_style("violet"))),
            rx.table.cell("62em", style=cell_style),
        ),
        rx.table.row(
            rx.table.cell(rx.code("lg", style=get_code_style("violet"))),
            rx.table.cell("80em", style=cell_style),
        ),
        rx.table.row(
            rx.table.cell(rx.code("xl", style=get_code_style("violet"))),
            rx.table.cell("96em", style=cell_style),
        ),
    ),
    margin_bottom="1em",
)
```

You can customize them using the style property.

```python
app = rx.App(style=\{"breakpoints": ["520px", "768px", "1024px", "1280px", "1640px"]\})
```

## Showing Components Based on Display

A common use case for responsive is to show different components based on the screen size.

Reflex provides useful helper components for this.

```python demo
rx.vstack(
    rx.desktop_only(
        rx.text("Desktop View"),
    ),
    rx.tablet_only(
        rx.text("Tablet View"),
    ),
    rx.mobile_only(
        rx.text("Mobile View"),
    ),
    rx.mobile_and_tablet(
        rx.text("Visible on Mobile and Tablet"),
    ),
    rx.tablet_and_desktop(
        rx.text("Visible on Desktop and Tablet"),
    ),
)
```

## Specifying Display Breakpoints

You can specify the breakpoints to use for the responsive components by using the `display` style property.

```python demo
rx.vstack(
    rx.text(
        "Hello World",
        color="green",
        display=["none", "none", "none", "none", "flex"],
    ),
    rx.text(
        "Hello World",
        color="blue",
        display=["none", "none", "none", "flex", "flex"],
    ),
    rx.text(
        "Hello World",
        color="red",
        display=["none", "none", "flex", "flex", "flex"],
    ),
    rx.text(
        "Hello World",
        color="orange",
        display=["none", "flex", "flex", "flex", "flex"],
    ),
    rx.text(
        "Hello World",
        color="yellow",
        display=["flex", "flex", "flex", "flex", "flex"],
    ),
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/styling/overview.md`:

```md

# Styling

Reflex components can be styled using the full power of [CSS]({"https://www.w3schools.com/css/"}).

There are three main ways to add style to your app and they take precedence in the following order:

1. **Inline:** Styles applied to a single component instance.
2. **Component:** Styles applied to components of a specific type.
3. **Global:** Styles applied to all components.

```md alert success
# Style keys can be any valid CSS property name.
To be consistent with Python standards, you can specify keys in `snake_case`.
```

## Global Styles

You can pass a style dictionary to your app to apply base styles to all components.

For example, you can set the default font family and font size for your app here just once rather than having to set it on every component.

```python
style = {
    "font_family": "Comic Sans MS",
    "font_size": "16px",
}

app = rx.App(style=style)
```

## Component Styles

In your style dictionary, you can also specify default styles for specific component types or arbitrary CSS classes and IDs.

```python
style = {
    # Set the selection highlight color globally.
    "::selection": {
        "background_color": accent_color,
    },
    # Apply global css class styles.
    ".some-css-class": {
        "text_decoration": "underline",
    },
    # Apply global css id styles.
    "#special-input": \{"width": "20vw"},
    # Apply styles to specific components.
    rx.text: {
        "font_family": "Comic Sans MS",
    },
    rx.divider: {
        "margin_bottom": "1em",
        "margin_top": "0.5em",
    },
    rx.heading: {
        "font_weight": "500",
    },
    rx.code: {
        "color": "green",
    },
}

app = rx.App(style=style)
```

Using style dictionaries like this, you can easily create a consistent theme for your app.


```md alert warning
# Watch out for underscores in class names and IDs
Reflex automatically converts `snake_case` identifiers into `camelCase` format when applying styles. To ensure consistency, it is recommended to use the dash character or camelCase identifiers in your own class names and IDs. To style third-party libraries relying on underscore class names, an external stylesheet should be used. See [custom stylesheets]({styling.custom_stylesheets.path}) for how to reference external CSS files.
```

## Inline Styles

Inline styles apply to a single component instance. They are passed in as regular props to the component.

```python demo
rx.text(
    "Hello World",
    background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
    background_clip="text",
    font_weight="bold",
    font_size="2em",
)
```

Children components inherit inline styles unless they are overridden by their own inline styles.

```python demo
rx.box(
    rx.hstack(
        rx.button("Default Button"),
        rx.button("Red Button", color="red"),
    ),
    color="blue",
)
```

### Style Prop

Inline styles can also be set with a `style` prop. This is useful for reusing styles between multiple components.


```python
text_style={text_style}
```

```python demo
rx.vstack(
    rx.text("Hello", style=text_style),
    rx.text("World", style=text_style),
)
```


```python
style1={style1}
style2={style2}
```

```python demo
rx.box(
    "Multiple Styles",
    style=[style1, style2],
)
```

The style dictionaries are applied in the order they are passed in. This means that styles defined later will override styles defined earlier.


## Theming

As of Reflex 'v0.4.0', you can now theme your Reflex web apps. To learn more checkout the [Theme docs]({styling.theming.path}).

The `Theme` component is used to change the theme of the application. The `Theme` can be set directly in your rx.App.

```python
app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="teal"
    )
)
```

Additionally you can modify the theme of your app through using the `Theme Panel` component which can be found in the [Theme Panel docs]({library.other.theme.path}).




## Tailwind

Reflex supports [Tailwind CSS]({"https://tailwindcss.com/"}) out of the box. To enable it, pass in a dictionary for the `tailwind` argument of your `rxconfig.py`:

```python
import reflex as rx


class AppConfig(rx.Config):
    pass


config = AppConfig(
    app_name="app",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    tailwind=\{},
)
```

All Tailwind configuration options are supported. Plugins and presets are automatically wrapped in `require()`:

```python
config = AppConfig(
    app_name="app",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    tailwind={
        "theme": {
            "extend": \{},
        },
        "plugins": ["@tailwindcss/typography"],
    },
)
```

You can use any of the [utility classes]({"https://tailwindcss.com/docs/utility-first"}) under the `class_name` prop:

```python demo
rx.box(
    "Hello World",
    class_name="text-4xl text-center text-blue-500",
)
```

### Disabling Tailwind

If you want to disable Tailwind in your configuration, you can do so by setting the `tailwind` config to `None`. This can be useful if you need to temporarily turn off Tailwind for your project:

```python
config = rx.Config(app_name="app", tailwind=None)
```

With this configuration, Tailwind will be disabled, and no Tailwind styles will be applied to your application.

## Special Styles

We support all of Chakra UI's [pseudo styles]({"https://v2.chakra-ui.com/docs/styled-system/style-props#pseudo"}).

Below is an example of text that changes color when you hover over it.

```python demo
rx.box(
    rx.text("Hover Me", _hover={"color": "red"}),
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/styling/theming.md`:

```md

# Theming

As of Reflex `v0.4.0`, you can now theme your Reflex applications. The core of our theming system is directly based on the [Radix Themes](https://www.radix-ui.com) library. This allows you to easily change the theme of your application along with providing a default light and dark theme. Themes cause all the components to have a unified color appearance.

## Overview

The `Theme` component is used to change the theme of the application. The `Theme` can be set directly in your rx.App.

```python
app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="teal"
    )
)
```

Here are the props that can be passed to the `rx.theme` component:

```python eval
rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Name", class_name="table-header"),
            rx.table.column_header_cell("Type", class_name="table-header"),
            rx.table.column_header_cell("Description", class_name="table-header"),
        ),
    ),
    rx.table.body(
        rx.table.row(
            rx.table.row_header_cell(rx.code("has_background", style=get_code_style_rdx("violet"), class_name="code-style")),
            rx.table.cell(rx.code("Bool", style=get_code_style_rdx("gray"), class_name="code-style")),
            rx.table.cell("Whether to apply the themes background color to the theme node. Defaults to True.", style=cell_style),
        ),
        rx.table.row(
            rx.table.row_header_cell(rx.code("appearance", style=get_code_style_rdx("violet"), class_name="code-style")),
            rx.table.cell(rx.code('"inherit" | "light" | "dark"', style=get_code_style_rdx("gray"), class_name="code-style")),
            rx.table.cell("The appearance of the theme. Can be 'light' or 'dark'. Defaults to 'light'.", style=cell_style),
        ),
        rx.table.row(
            rx.table.row_header_cell(rx.code("accent_color", style=get_code_style_rdx("violet"), class_name="code-style")),
            rx.table.cell(rx.code("Str", style=get_code_style_rdx("gray"), class_name="code-style")),
            rx.table.cell("The primary color used for default buttons, typography, backgrounds, etc.", style=cell_style),
        ),
        rx.table.row(
            rx.table.row_header_cell(rx.code("gray_color", style=get_code_style_rdx("violet"), class_name="code-style")),
            rx.table.cell(rx.code("Str", style=get_code_style_rdx("gray"), class_name="code-style")),
            rx.table.cell("The secondary color used for default buttons, typography, backgrounds, etc.", style=cell_style),
        ),
        rx.table.row(
            rx.table.row_header_cell(rx.code("panel_background", style=get_code_style_rdx("violet"), class_name="code-style")),
            rx.table.cell(rx.code('"solid" | "translucent"', style=get_code_style_rdx("gray"), class_name="code-style")),
            rx.table.cell('Whether panel backgrounds are translucent: "solid" | "translucent" (default).', style=cell_style),
        ),
        rx.table.row(
            rx.table.row_header_cell(rx.code("radius", style=get_code_style_rdx("violet"), class_name="code-style")),
            rx.table.cell(rx.code('"none" | "small" | "medium" | "large" | "full"', style=get_code_style_rdx("gray"))),
            rx.table.cell("The radius of the theme. Can be 'small', 'medium', or 'large'. Defaults to 'medium'.", style=cell_style),
        ),
        rx.table.row(
            rx.table.row_header_cell(rx.code("scaling", style=get_code_style_rdx("violet"), class_name="code-style")),
            rx.table.cell(rx.code('"90%" | "95%" | "100%" | "105%" | "110%"', style=get_code_style_rdx("gray"), class_name="code-style")),
            rx.table.cell("Scale of all theme items.", style=cell_style),
        ),
    ),
    variant="surface",
    margin_y="1em",
)

```

Additionally you can modify the theme of your app through using the `Theme Panel` component which can be found in the [Theme Panel docs]({library.other.theme.path}).


## Colors

### Color Scheme

On a high-level, component `color_scheme` inherits from the color specified in the theme. This means that if you change the theme, the color of the component will also change. Available colors can be found [here](https://www.radix-ui.com/colors).

You can also specify the `color_scheme` prop.

```python demo
rx.flex(
    rx.button(
        "Hello World",
        color_scheme="tomato",
    ),
    rx.button(
        "Hello World",
        color_scheme="teal",
    ),
    spacing="2"
)
```

### Shades

Sometime you may want to use a specific shade of a color from the theme. This is recommended vs using a hex color directly as it will automatically change when the theme changes appearance change from light/dark.


To access a specific shade of color from the theme, you can use the `rx.color`. When switching to light and dark themes, the color will automatically change. Shades can be accessed by using the color name and the shade number. The shade number ranges from 1 to 12. Additionally, they can have their alpha value set by using the `True` parameter it defaults to `False`. A full list of colors can be found [here](https://www.radix-ui.com/colors).

```python demo
rx.flex(
    rx.button(
        "Hello World",
        color=rx.color("grass", 1),
        background_color=rx.color("grass", 7),
        border_color=f"1px solid {rx.color('grass', 1)}",
    ),
    spacing="2"
)
```

```python eval
rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Name"),
            rx.table.column_header_cell("Type"),
            rx.table.column_header_cell("Description"),
        ),
    ),
    rx.table.body(
        rx.table.row(
            rx.table.row_header_cell(rx.code("color", style=get_code_style_rdx("violet"), class_name="code-style")),
            rx.table.cell(rx.code("Str", style=get_code_style_rdx("gray"), class_name="code-style")),
            rx.table.cell("The color to use. Can be any valid accent color or 'accent' to reference the current theme color.", style=cell_style),
        ),
        rx.table.row(
            rx.table.row_header_cell(rx.code("shade", style=get_code_style_rdx("violet"), class_name="code-style")),
            rx.table.cell(rx.link(rx.code('1 - 12', style=get_code_style_rdx("gray"), class_name="code-style"), href="https://www.radix-ui.com/colors")),
            rx.table.cell("The shade of the color to use. Defaults to 7.", style=cell_style),
        ),
        rx.table.row(
            rx.table.row_header_cell(rx.code("alpha", style=get_code_style_rdx("violet"), class_name="code-style")),
            rx.table.cell(rx.code("Bool", style=get_code_style_rdx("gray"), class_name="code-style")),
            rx.table.cell("Whether to use the alpha value of the color. Defaults to False.", style=cell_style),
        )
    ),
    variant="surface",
    margin_y="1em",
)

```

### Regular Colors

You can also use standard hex, rgb, and rgba colors.

```python demo
rx.flex(
    rx.button(
        "Hello World",
        color="white",
        background_color="#87CEFA",
        border="1px solid rgb(176,196,222)",
    ),
    spacing="2"
)
```

## Toggle Appearance

To toggle between the light and dark mode manually, you can use the `toggle_color_mode` with the desired event trigger of your choice.

```python

from reflex.style import toggle_color_mode



def index():
    return rx.button(
        "Toggle Color Mode",
        on_click=toggle_color_mode,
    )
```

## Appearance Conditional Rendering

To render a different component depending on whether the app is in `light` mode or `dark` mode, you can use the `rx.color_mode_cond` component. The first component will be rendered if the app is in `light` mode and the second component will be rendered if the app is in `dark` mode.

```python demo
rx.color_mode_cond(
    light=rx.image(src="/logos/light/reflex.svg", alt="Reflex Logo light", height="4em"),
    dark=rx.image(src="/logos/dark/reflex.svg", alt="Reflex Logo dark", height="4em"),
)
```

This can also be applied to props.

```python demo
rx.button(
    "Hello World",
    color=rx.color_mode_cond(light="black", dark="white"),
    background_color=rx.color_mode_cond(light="white", dark="black"),
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/styling/layout.md`:

```md

# Layout Components

Layout components such as `rx.flex`, `rx.container`, `rx.box`, etc. are used to organize and structure the visual presentation of your application. This page gives a breakdown of when and how each of these components might be used.

```md video https://youtube.com/embed/ITOZkzjtjUA?start=3311&end=3853
# Video: Example of Laying Out the Main Content of a Page
```

## Box

`rx.box` is a generic component that can apply any CSS style to its children. It's a building block that can be used to apply a specific layout or style property.

**When to use:** Use `rx.box` when you need to apply specific styles or constraints to a part of your interface.


```python demo
rx.box(
    rx.box(
        "CSS color",
        background_color="red",
        border_radius="2px",
        width="50%",
        margin="4px",
        padding="4px",
    ),
    rx.box(
        "Radix Color",
        background_color=rx.color("tomato", 3),
        border_radius="5px",
        width="80%",
        margin="12px",
        padding="12px",
    ),
    text_align="center",
    width="100%",
)
```

## Stack

`rx.stack` is a layout component that arranges its children in a single column or row, depending on the direction. It’s useful for consistent spacing between elements.

**When to use:** Use `rx.stack` when you need to lay out a series of components either vertically or horizontally with equal spacing.

```python demo
rx.flex(
    rx.stack(
        rx.box(
            "Example",
            bg="orange",
            border_radius="3px",
            width="20%",
        ),
        rx.box(
            "Example",
            bg="lightblue",
            border_radius="3px",
            width="30%",
        ),
        flex_direction="row",
        width="100%",
    ),
    rx.stack(
        rx.box(
            "Example",
            bg="orange",
            border_radius="3px",
            width="20%",
        ),
        rx.box(
            "Example",
            bg="lightblue",
            border_radius="3px",
            width="30%",
        ),
        flex_direction="column",
        width="100%",
    ),
    width="100%",
)
```

## Flex

The `rx.flex` component is used to create a flexible box layout, inspired by [CSS Flexbox](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox). It's ideal for designing a layout where the size of the items can grow and shrink dynamically based on the available space.

**When to use:** Use `rx.flex` when you need a responsive layout that adjusts the size and position of child components dynamically.


```python demo
rx.flex(
    rx.card("Card 1"),
    rx.card("Card 2"),
    rx.card("Card 3"),
    spacing="2",
    width="100%",
)
```


## Grid

`rx.grid` components are used to create complex responsive layouts based on a grid system, similar to [CSS Grid Layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout).

**When to use:** Use `rx.grid` when dealing with complex layouts that require rows and columns, especially when alignment and spacing among multiple axes are needed.

```python demo
rx.grid(
    rx.foreach(
        rx.Var.range(12),
        lambda i: rx.card(f"Card {i + 1}", height="10vh"),
    ),
    columns="3",
    spacing="4",
    width="100%",
)
```

## Container

The `rx.container` component typically provides padding and fixes the maximum width of the content inside it, often used to center content on large screens.

**When to use:** Use `rx.container` for wrapping your application’s content in a centered block with some padding.

```python demo
rx.box(
    rx.container(
        rx.card(
            "This content is constrained to a max width of 448px.",
            width="100%",
        ),
        size="1",
    ),
    rx.container(
        rx.card(
            "This content is constrained to a max width of 688px.",
            width="100%",
        ),
        size="2",
    ),
    rx.container(
        rx.card(
            "This content is constrained to a max width of 880px.",
            width="100%",
        ),
        size="3",
    ),
    background_color="var(--gray-3)",
    width="100%",
)
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/styling/custom-stylesheets.md`:

```md

# Custom Stylesheets

Reflex allows you to add custom stylesheets. Simply pass the URLs of the stylesheets to `rx.App`:

```python
app = rx.App(
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    ],
)
```

## Local Stylesheets

You can also add local stylesheets. Just put the stylesheet under [`assets/`]({assets.upload_and_download_files.path}) and pass the path to the stylesheet to `rx.App`:

```python
app = rx.App(
    stylesheets=[
        "/styles.css",  # This path is relative to assets/
    ],
)
```

```md alert warning
# Always use a leading slash (/) when referencing files in the assets directory.
Without a leading slash the path is considered relative to the current page route and may
not work for routes containing more than one path component, like `/blog/my-cool-post`.
```

## Fonts

You can take advantage of Reflex's support for custom stylesheets to add custom fonts to your app.

In this example, we will use the [IBM Plex Mono]({"https://fonts.google.com/specimen/IBM+Plex+Mono"}) font from Google Fonts. First, add the stylesheet with the font to your app. You can get this link from the "Get embed code" section of the Google font page.

```python
app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap",
    ],
)
```

Then you can use the font in your component by setting the `font_family` prop.

```python demo
rx.text(
    "Check out my font",
    font_family="IBM Plex Mono",
    font_size="1.5em",
)
```

## Local Fonts

By making use of the two previous points, we can also make a stylesheet that allow you to use a font hosted on your server.

If your font is called `MyFont.otf`, copy it in `assets/fonts`.

Now we have the font ready, let's create the stylesheet `myfont.css`.

```css
@font-face {
    font-family: MyFont;
    src: url("/fonts/MyFont.otf") format("opentype");
}

@font-face {
    font-family: MyFont;
    font-weight: bold;
    src: url("/fonts/MyFont.otf") format("opentype");
}
```

Add the reference to your new Stylesheet in your App.

```python
app = rx.App(
    stylesheets=[
        "/fonts/myfont.css",  # This path is relative to assets/
    ],
)
```

And that's it! You can now use `MyFont` like any other FontFamily to style your components.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/styling/common-props.md`:

```md
# Style and Layout Props


Any [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) prop can be used in a component in Reflex. This is a short list of the most commonly used props. To see all CSS props that can be used check out this [documentation](https://developer.mozilla.org/en-US/docs/Web/CSS). 

Hyphens in CSS property names may be replaced by underscores to use as valid python identifiers, i.e. the CSS prop `z-index` would be used as `z_index` in Reflex.

```python eval
rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell(
                "Prop", justify="center"
            ),
            rx.table.column_header_cell(
                "Description",
                justify="center",
                
            ),
            rx.table.column_header_cell(
                "Potential Values",
                justify="center",
            ),
        )
    ),
    rx.table.body(
        *[show_props(key, props) for key in props]
    ),
    width="100%",
    padding_x="0",
    size="1",
)
```
```