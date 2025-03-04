Project Path: library

Source Tree:

```
library
├── layout
│   ├── section.md
│   ├── stack.md
│   ├── box.md
│   ├── card.md
│   ├── aspect_ratio.md
│   ├── container.md
│   ├── spacer.md
│   ├── separator.md
│   ├── center.md
│   ├── flex.md
│   ├── grid.md
│   ├── inset.md
│   └── fragment.md
├── forms
│   ├── button.md
│   ├── upload.md
│   ├── radio_group.md
│   ├── text_area.md
│   ├── form-ll.md
│   ├── input-ll.md
│   ├── switch.md
│   ├── input.md
│   ├── select-ll.md
│   ├── select.md
│   ├── editor.md
│   ├── form.md
│   ├── slider.md
│   └── checkbox.md
├── tables-and-data-grids
│   ├── data_table.md
│   ├── data_editor.md
│   ├── ag_grid.md
│   └── table.md
├── typography
│   ├── blockquote.md
│   ├── heading.md
│   ├── markdown.md
│   ├── link.md
│   ├── kbd.md
│   ├── quote.md
│   ├── strong.md
│   ├── code.md
│   ├── em.md
│   └── text.md
├── other
│   ├── html_embed.md
│   ├── clipboard.md
│   ├── script.md
│   ├── html.md
│   ├── theme.md
│   └── skeleton.md
├── graphing
│   ├── general
│   │   ├── reference.md
│   │   ├── cartesiangrid.md
│   │   ├── tooltip.md
│   │   ├── brush.md
│   │   ├── label.md
│   │   ├── legend.md
│   │   └── axis.md
│   ├── other-charts
│   │   ├── plotly.md
│   │   └── pyplot.md
│   └── charts
│       ├── radialbarchart.md
│       ├── linechart.md
│       ├── barchart.md
│       ├── scatterchart.md
│       ├── funnelchart.md
│       ├── piechart.md
│       ├── errorbar.md
│       ├── composedchart.md
│       ├── areachart.md
│       └── radarchart.md
├── overlay
│   ├── drawer.md
│   ├── alert_dialog.md
│   ├── toast.md
│   ├── popover.md
│   ├── dropdown_menu.md
│   ├── hover_card.md
│   ├── context_menu.md
│   ├── tooltip.md
│   └── dialog.md
├── media
│   ├── audio.md
│   ├── video.md
│   └── image.md
├── disclosure
│   ├── accordion.md
│   ├── segmented_control.md
│   └── tabs.md
├── dynamic-rendering
│   ├── foreach.md
│   ├── cond.md
│   └── match.md
└── data-display
    ├── list.md
    ├── moment.md
    ├── progress.md
    ├── callout.md
    ├── scroll_area.md
    ├── data_list.md
    ├── spinner.md
    ├── code_block.md
    ├── callout-ll.md
    ├── icon.md
    ├── badge.md
    └── avatar.md

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/layout/section.md`:

```md
---
components:
  - rx.section
---


# Section

Denotes a section of page content, providing vertical padding by default.

Primarily this is a semantic component that is used to group related textual content.

## Basic Example

```python demo
rx.box(
    rx.section(
        rx.heading("First"),
        rx.text("This is the first content section"),
        padding_left="12px",
        padding_right="12px",
        background_color="var(--gray-2)",
    ),
    rx.section(
        rx.heading("Second"),
        rx.text("This is the second content section"),
        padding_left="12px",
        padding_right="12px",
        background_color="var(--gray-2)",
    ),
    width="100%",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/layout/stack.md`:

```md
---
components:
    - rx.stack
    - rx.hstack
    - rx.vstack
Stack: |
    lambda **props: rx.stack(
        rx.card("Card 1", size="2"), rx.card("Card 2", size="2"), rx.card("Card 3", size="2"),
        width="100%",
        height="20vh",
        **props,
    )
---


# Stack

`Stack` is a layout component used to group elements together and apply a space between them.

`vstack` is used to stack elements in the vertical direction.

`hstack` is used to stack elements in the horizontal direction.

`stack` is used to stack elements in the vertical or horizontal direction.

These components are based on the `flex` component and therefore inherit all of its props.

The `stack` component can be used with the `flex_direction` prop to set to either `row` or `column` to set the direction.

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
        rx.box(
            "Example",
            bg="lightgreen",
            border_radius="3px",
            width="50%",
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
        rx.box(
            "Example",
            bg="lightgreen",
            border_radius="3px",
            width="50%",
        ),
        flex_direction="column",
        width="100%",
    ),
    width="100%",
)
```

## Hstack

```python demo
rx.hstack(
    rx.box(
        "Example", bg="red", border_radius="3px", width="10%"
    ),
    rx.box(
        "Example",
        bg="orange",
        border_radius="3px",
        width="10%",
    ),
    rx.box(
        "Example",
        bg="yellow",
        border_radius="3px",
        width="10%",
    ),
    rx.box(
        "Example",
        bg="lightblue",
        border_radius="3px",
        width="10%",
    ),
    rx.box(
        "Example",
        bg="lightgreen",
        border_radius="3px",
        width="60%",
    ),
    width="100%",
)
```

## Vstack

```python demo
rx.vstack(
    rx.box(
        "Example", bg="red", border_radius="3px", width="20%"
    ),
    rx.box(
        "Example",
        bg="orange",
        border_radius="3px",
        width="40%",
    ),
    rx.box(
        "Example",
        bg="yellow",
        border_radius="3px",
        width="60%",
    ),
    rx.box(
        "Example",
        bg="lightblue",
        border_radius="3px",
        width="80%",
    ),
    rx.box(
        "Example",
        bg="lightgreen",
        border_radius="3px",
        width="100%",
    ),
    width="100%",
)
```

## Real World Example

```python demo
rx.hstack(
    rx.box(
        rx.heading("Saving Money"),
        rx.text("Saving money is an art that combines discipline, strategic planning, and the wisdom to foresee future needs and emergencies. It begins with the simple act of setting aside a portion of one's income, creating a buffer that can grow over time through interest or investments.", margin_top="0.5em"),
        padding="1em",
        border_width="1px",
    ),
    rx.box(
        rx.heading("Spending Money"),
        rx.text("Spending money is a balancing act between fulfilling immediate desires and maintaining long-term financial health. It's about making choices, sometimes indulging in the pleasures of the moment, and at other times, prioritizing essential expenses.", margin_top="0.5em"),
        padding="1em",
        border_width="1px",
    ),
    gap="2em",
)

```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/layout/box.md`:

```md
---
components:
  - rx.box
---


# Box

Box is a generic container component that can be used to group other components.

By default, the Box component is based on the `div` and rendered as a block element. It's primary use is for applying styles.

## Basic Example

```python demo
rx.box(
    rx.box("CSS color", background_color="yellow", border_radius="2px", width="20%", margin="4px", padding="4px"),
    rx.box("CSS color", background_color="orange", border_radius="5px", width="40%", margin="8px", padding="8px"),
    rx.box("Radix Color", background_color="var(--tomato-3)", border_radius="5px", width="60%", margin="12px", padding="12px"),
    rx.box("Radix Color", background_color="var(--plum-3)", border_radius="10px", width="80%", margin="16px", padding="16px"),
    rx.box("Radix Theme Color", background_color="var(--accent-2)", radius="full", width="100%", margin="24px", padding="25px"),
    flex_grow="1",
    text_align="center",
)
```

## Background

To set a background [image](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_images) or
[gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_images/Using_CSS_gradients),
use the [`background` CSS prop](https://developer.mozilla.org/en-US/docs/Web/CSS/background).

```python demo
rx.flex(
    rx.box(background="linear-gradient(45deg, var(--tomato-9), var(--plum-9))", width="20%", height="100%"),
    rx.box(background="linear-gradient(red, yellow, blue, orange)", width="20%", height="100%"),
    rx.box(background="radial-gradient(at 0% 30%, red 10px, yellow 30%, #1e90ff 50%)", width="20%", height="100%"),
    rx.box(background="center/cover url('/reflex_banner.png')", width="20%", height="100%"),
    spacing="2",
    width="100%",
    height="10vh",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/layout/card.md`:

```md
---
components:
  - rx.card

Card: |
    lambda **props: rx.card("Basic Card ", **props)
---


# Card

A Card component is used for grouping related components. It is similar to the Box, except it has a
border, uses the theme colors and border radius, and provides a `size` prop to control spacing
and margin according to the Radix `"1"` - `"5"` scale.

The Card requires less styling than a Box to achieve consistent visual results when used with
themes.

## Basic Example

```python demo
rx.flex(
    rx.card("Card 1", size="1"),
    rx.card("Card 2", size="2"),
    rx.card("Card 3", size="3"),
    rx.card("Card 4", size="4"),
    rx.card("Card 5", size="5"),
    spacing="2",
    align_items="flex-start",
    flex_wrap="wrap",
)
```

## Rendering as a Different Element

The `as_child` prop may be used to render the Card as a different element. Link and Button are
commonly used to make a Card clickable.

```python demo
rx.card(
    rx.link(
        rx.flex(
            rx.avatar(src="/reflex_banner.png"),
            rx.box(
                rx.heading("Quick Start"),
                rx.text("Get started with Reflex in 5 minutes."),
            ),
            spacing="2",
        ),
    ),
    as_child=True,
)
```

## Using Inset Content

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/layout/aspect_ratio.md`:

```md
---
components:
  - rx.aspect_ratio
---


# Aspect Ratio

Displays content with a desired ratio.

## Basic Example

Setting the `ratio` prop will adjust the width or height
of the content such that the `width` divided by the `height` equals the `ratio`.
For responsive scaling, set the `width` or `height` of the content to `"100%"`.

```python demo
rx.grid(
    rx.aspect_ratio(
        rx.box(
            "Widescreen 16:9",
            background_color="papayawhip",
            width="100%",
            height="100%",
        ),
        ratio=16 / 9,
    ),
    rx.aspect_ratio(
        rx.box(
            "Letterbox 4:3",
            background_color="orange",
            width="100%",
            height="100%",
        ),
        ratio=4 / 3,
    ),
    rx.aspect_ratio(
        rx.box(
            "Square 1:1",
            background_color="green",
            width="100%",
            height="100%",
        ),
        ratio=1,
    ),
    rx.aspect_ratio(
        rx.box(
            "Portrait 5:7",
            background_color="lime",
            width="100%",
            height="100%",
        ),
        ratio=5 / 7,
    ),
    spacing="2",
    width="25%",
)
```

```md alert warning
# Never set `height` or `width` directly on an `aspect_ratio` component or its contents.

Instead, wrap the `aspect_ratio` in a `box` that constrains either the width or the height, then set the content width and height to `"100%"`.
```

```python demo
rx.flex(
    *[
        rx.box(
            rx.aspect_ratio(
                rx.image(src="/logo.jpg", width="100%", height="100%"),
                ratio=ratio,
            ),
            width="20%",
        )
        for ratio in [16 / 9, 3 / 2, 2 / 3, 1]
    ],
    justify="between",
    width="100%",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/layout/container.md`:

```md
---
components:
  - rx.container
---


# Container

Constrains the maximum width of page content, while keeping flexible margins
for responsive layouts.

A Container is generally used to wrap the main content for a page.

## Basic Example

```python demo
rx.box(
    rx.container(
        rx.card("This content is constrained to a max width of 448px.", width="100%"),
        size="1",
    ),
    rx.container(
        rx.card("This content is constrained to a max width of 688px.", width="100%"),
        size="2",
    ),
    rx.container(
        rx.card("This content is constrained to a max width of 880px.", width="100%"),
        size="3",
    ),
    rx.container(
        rx.card("This content is constrained to a max width of 1136px.", width="100%"),
        size="4",
    ),
    background_color="var(--gray-3)",
    width="100%",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/layout/spacer.md`:

```md
---
components:
    - rx.spacer
---


# Spacer

Creates an adjustable, empty space that can be used to tune the spacing between child elements within `flex`.

```python demo
rx.flex(
    rx.center(rx.text("Example"), bg="lightblue"),
    rx.spacer(),
    rx.center(rx.text("Example"), bg="lightgreen"),
    rx.spacer(),
    rx.center(rx.text("Example"), bg="salmon"),
    width="100%",
)
```

As `stack`, `vstack` and `hstack` are all built from `flex`, it is possible to also use `spacer` inside of these components.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/layout/separator.md`:

```md
---
components:
    - rx.separator
Separator: |
    lambda **props: rx.separator(**props)

---


# Separator

Visually or semantically separates content.

## Basic Example

```python demo
rx.flex(
    rx.card("Section 1"),
    rx.divider(),
    rx.card("Section 2"),
    spacing="4",
    direction="column",
    align="center",
)
```

## Size

The `size` prop controls how long the separator is. Using `size="4"` will make
the separator fill the parent container. Setting CSS `width` or `height` prop to `"100%"`
can also achieve this effect, but `size` works the same regardless of the orientation.

```python demo
rx.flex(
    rx.card("Section 1"),
    rx.divider(size="4"),
    rx.card("Section 2"),
    spacing="4",
    direction="column",
)
```

## Orientation

Setting the orientation prop to `vertical` will make the separator appear vertically.

```python demo
rx.flex(
    rx.card("Section 1"),
    rx.divider(orientation="vertical", size="4"),
    rx.card("Section 2"),
    spacing="4",
    width="100%",
    height="10vh",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/layout/center.md`:

```md
---
components:
    - rx.center
---


# Center

`Center` is a component that centers its children within itself. It is based on the `flex` component and therefore inherits all of its props.

```python demo
rx.center(
    rx.text("Hello World!"),
    border_radius="15px",
    border_width="thick",
    width="50%",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/layout/flex.md`:

```md
---
components:
  - rx.flex
---


# Flex

The Flex component is used to make [flexbox layouts](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox).
It makes it simple to arrange  child components in horizontal or vertical directions, apply wrapping,
justify and align  content, and automatically size components based on available space, making it
ideal for building responsive layouts.

By default, children are arranged horizontally (`direction="row"`) without wrapping.

## Basic Example

```python demo
rx.flex(
    rx.card("Card 1"),
    rx.card("Card 2"),
    rx.card("Card 3"),
    rx.card("Card 4"),
    rx.card("Card 5"),
    spacing="2",
    width="100%",
)
```

## Wrapping

With `flex_wrap="wrap"`, the children will wrap to the next line instead of being resized.

```python demo
rx.flex(
    rx.foreach(
        rx.Var.range(10),
        lambda i: rx.card(f"Card {i + 1}", width="16%"),
    ),
    spacing="2",
    flex_wrap="wrap",
    width="100%",
)
```

## Direction

With `direction="column"`, the children will be arranged vertically.

```python demo
rx.flex(
    rx.card("Card 1"),
    rx.card("Card 2"),
    rx.card("Card 3"),
    rx.card("Card 4"),
    spacing="2",
    direction="column",
)
```

## Alignment

Two props control how children are aligned within the Flex component:

* `align` controls how children are aligned along the cross axis (vertical for `row` and horizontal for `column`).
* `justify` controls how children are aligned along the main axis (horizontal for `row` and vertical for `column`).

The following example visually demonstrates the effect of these props with different `wrap` and `direction` values.

```python demo exec
class FlexPlaygroundState(rx.State):
    align: str = "stretch"
    justify: str = "start"
    direction: str = "row"
    wrap: str = "nowrap"
    
    
def select(label, items, value, on_change):
    return rx.flex(
        rx.text(label),
        rx.select.root(
            rx.select.trigger(),
            rx.select.content(
                *[
                    rx.select.item(item, value=item)
                    for item in items
                ]
            ),
            value=value,
            on_change=on_change,
        ),
        align="center",
        justify="center",
        direction="column",
    )


def selectors():
    return rx.flex(
        select("Wrap", ["nowrap", "wrap", "wrap-reverse"], FlexPlaygroundState.wrap, FlexPlaygroundState.set_wrap),
        select("Direction", ["row", "column", "row-reverse", "column-reverse"], FlexPlaygroundState.direction, FlexPlaygroundState.set_direction),
        select("Align", ["start", "center", "end", "baseline", "stretch"], FlexPlaygroundState.align, FlexPlaygroundState.set_align),
        select("Justify", ["start", "center", "end", "between"], FlexPlaygroundState.justify, FlexPlaygroundState.set_justify),
        width="100%",
        spacing="2",
        justify="between",
    )


def example1():
    return rx.box(
        selectors(),
        rx.flex(
            rx.foreach(
                rx.Var.range(10),
                lambda i: rx.card(f"Card {i + 1}", width="16%"),
            ),
            spacing="2",
            direction=FlexPlaygroundState.direction,
            align=FlexPlaygroundState.align,
            justify=FlexPlaygroundState.justify,
            wrap=FlexPlaygroundState.wrap,
            width="100%",
            height="20vh",
            margin_top="16px",
        ),
        width="100%",
    )
```

## Size Hinting

When a child component is included in a flex container,
the `flex_grow` (default `"0"`) and `flex_shrink` (default `"1"`) props control
how the box is sized relative to other components in the same container.

The resizing always applies to the main axis of the flex container. If the direction is
`row`, then the sizing applies to the `width`. If the direction is `column`, then the sizing
applies to the `height`. To set the optimal size along the main axis, the `flex_basis` prop
is used and may be either a percentage or CSS size units. When unspecified, the
corresponding `width` or `height` value is used if set, otherwise the content size is used.

When `flex_grow="0"`, the box will not grow beyond the `flex_basis`.

When `flex_shrink="0"`, the box will not shrink to less than the `flex_basis`.

These props are used when creating flexible responsive layouts.

Move the slider below and see how adjusting the width of the flex container
affects the computed  sizes of the flex items based on the props that are set.

```python demo exec
class FlexGrowShrinkState(rx.State):
    width_pct: list[int] = [100]
    
    
def border_box(*children, **props):
    return rx.box(
        *children,
        border="1px solid var(--gray-10)",
        border_radius="2px",
        **props,
    )

    
def example2():
    return rx.box(
        rx.flex(
            border_box("flex_shrink=0", flex_shrink="0", width="100px"),
            border_box("flex_shrink=1", flex_shrink="1", width="200px"),
            border_box("flex_grow=0", flex_grow="0"),
            border_box("flex_grow=1", flex_grow="1"),
            width=f"{FlexGrowShrinkState.width_pct}%",
            margin_bottom="16px",
            spacing="2",
        ),
        rx.slider(
            min=0,
            max=100,
            value=FlexGrowShrinkState.width_pct,
            on_change=FlexGrowShrinkState.set_width_pct,
        ),
        width="100%",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/layout/grid.md`:

```md
---
components:
  - rx.grid
---


# Grid

Component for creating grid layouts. Either `rows` or `columns` may be specified.

## Basic Example

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

```python demo
rx.grid(
    rx.foreach(
        rx.Var.range(12),
        lambda i: rx.card(f"Card {i + 1}", height="10vh"),
    ),
    rows="3",
    flow="column",
    justify="between",
    spacing="4",
    width="100%",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/layout/inset.md`:

```md
---
components:
    - rx.inset

Inset: |
    lambda **props: rx.card(
        rx.inset(
            rx.image(src="/reflex_banner.png", height="auto"),
            **props,
        ),
        width="500px",
    )
    
---


# Inset

Applies a negative margin to allow content to bleed into the surrounding container.

## Basic Example

Nesting an Inset component inside a Card will render the content from edge to edge of the card.

```python demo
rx.card(
    rx.inset(
        rx.image(src="/reflex_banner.png", width="100%", height="auto"),
        side="top",
        pb="current",
    ),
    rx.text("Reflex is a web framework that allows developers to build their app in pure Python."),
    width="25vw",
)
```

## Other Directions

The `side` prop controls which side the negative margin is applied to. When using a specific side,
it is helpful to set the padding for the opposite side to `current` to retain the same padding the
content would have had if it went to the edge of the parent component.

```python demo
rx.card(
    rx.text("The inset below uses a bottom side."),
    rx.inset(
        rx.image(src="/reflex_banner.png", width="100%", height="auto"),
        side="bottom",
        pt="current",
    ),
    width="25vw",
)
```

```python demo
rx.card(
    rx.flex(
        rx.text("This inset uses a right side, which requires a flex with direction row."),
        rx.inset(
            rx.box(background="center/cover url('/reflex_banner.png')", height="100%"),
            width="100%",
            side="right",
            pl="current",
        ),
        direction="row",
        width="100%",
    ),
    width="25vw",
)
```

```python demo
rx.card(
    rx.flex(
        rx.inset(
            rx.box(background="center/cover url('/reflex_banner.png')", height="100%"),
            width="100%",
            side="left",
            pr="current",
        ),
        rx.text("This inset uses a left side, which also requires a flex with direction row."),
        direction="row",
        width="100%",
    ),
    width="25vw",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/layout/fragment.md`:

```md
---
components:
    - rx.fragment
---

# Fragment


A Fragment is a Component that allow you to group multiple Components without a wrapper node.

Refer to the React docs at [React/Fragment]({constants.FRAGMENT_COMPONENT_INFO_URL}) for more information on its use-case.

```python demo
rx.fragment(
    rx.text("Component1"), 
    rx.text("Component2")
)
```


```md video https://youtube.com/embed/ITOZkzjtjUA?start=3196&end=3340
# Video: Fragment
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/forms/button.md`:

```md
---
components:
  - rx.button

Button: |
  lambda **props: rx.button("Basic Button", **props)
---


# Button

Buttons are essential elements in your application's user interface that users can click to trigger events.

## Basic Example

The `on_click` trigger is called when the button is clicked.

```python demo exec
class CountState(rx.State):
    count: int = 0

    @rx.event
    def increment(self):
        self.count += 1

    @rx.event
    def decrement(self):
        self.count -= 1

def counter():
    return rx.flex(
        rx.button(
            "Decrement",
            color_scheme="red",
            on_click=CountState.decrement,
        ),
        rx.heading(CountState.count),
        rx.button(
            "Increment",
            color_scheme="grass",
            on_click=CountState.increment,
        ),
        spacing="3",
    )
```

### Loading and Disabled

The `loading` prop is used to indicate that the action triggered by the button is currently in progress. When set to `True`, the button displays a loading spinner, providing visual feedback to the user that the action is being processed. This also prevents multiple clicks while the button is in the loading state. By default, `loading` is set to `False`.

The `disabled` prop also prevents the button from being but does not provide a spinner.

```python demo
rx.flex(
    rx.button("Regular"),
    rx.button("Loading", loading=True),
    rx.button("Disabled", disabled=True),
    spacing="2",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/forms/upload.md`:

```md
---
components:
  - rx.upload

Upload: |
  lambda **props: rx.center(rx.upload(id="my_upload", **props), height="4em", width="100%")
---


# Upload

The Upload component can be used to upload files to the server.

You can pass components as children to customize its appearance.
You can upload files by clicking on the component or by dragging and dropping files onto it.

```python demo
rx.upload(
    id="my_upload",
)
```

Selecting a file will add it to the browser's file list, which can be rendered
on the frontend using the `rx.selected_files(id)` special Var. To clear the
selected files, you can use another special Var `rx.clear_selected_files(id)` as
an event handler.

To upload the file(s), you need to bind an event handler and pass the special
`rx.upload_files(upload_id=id)` event arg to it.


### Multiple File Upload

Below is an example of how to allow multiple file uploads (in this case images).

```python demo box
rx.image(src="/upload.gif")
```

```python
class State(rx.State):
    """The app state."""

    # The images to show.
    img: list[str]

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)


color = "rgb(107,99,246)"


def index():
    """The main view."""
    return rx.vstack(
        rx.upload(
            rx.vstack(
                rx.button("Select File", color=color, bg="white", border=f"1px solid \{color}"),
                rx.text("Drag and drop files here or click to select files"),
            ),
            id="upload1",
            border=f"1px dotted \{color}",
            padding="5em",
        ),
        rx.hstack(rx.foreach(rx.selected_files("upload1"), rx.text)),
        rx.button(
            "Upload",
            on_click=State.handle_upload(rx.upload_files(upload_id="upload1")),
        ),
        rx.button(
            "Clear",
            on_click=rx.clear_selected_files("upload1"),
        ),
        rx.foreach(State.img, lambda img: rx.image(src=rx.get_upload_url(img))),
        padding="5em",
    )
```

### Uploading a Single File (Video)

Below is an example of how to allow only a single file upload and render (in this case a video).

```python demo box
rx.el.video(src="/upload_single_video.webm", auto_play=True, controls=True, loop=True)
```

```python
class State(rx.State):
    """The app state."""

    # The video to show.
    video: str

    @rx.event
    async def handle_upload(
        self, files: list[rx.UploadFile]
    ):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        current_file = files[0]
        upload_data = await current_file.read()
        outfile = rx.get_upload_dir() / current_file.filename

        # Save the file.
        with outfile.open("wb") as file_object:
            file_object.write(upload_data)

        # Update the video var.
        self.video = current_file.filename


color = "rgb(107,99,246)"


def index():
    """The main view."""
    return rx.vstack(
        rx.upload(
            rx.vstack(
                rx.button(
                    "Select File",
                    color=color,
                    bg="white",
                    border=f"1px solid \{color}",
                ),
                rx.text(
                    "Drag and drop files here or click to select files"
                ),
            ),
            id="upload1",
            max_files=1,
            border=f"1px dotted \{color}",
            padding="5em",
        ),
        rx.text(rx.selected_files("upload1")),
        rx.button(
            "Upload",
            on_click=State.handle_upload(
                rx.upload_files(upload_id="upload1")
            ),
        ),
        rx.button(
            "Clear",
            on_click=rx.clear_selected_files("upload1"),
        ),
        rx.cond(
            State.video,
            rx.video(url=rx.get_upload_url(State.video)),
        ),
        padding="5em",
    )
```


### Customizing the Upload

In the example below, the upload component accepts a maximum number of 5 files of specific types.
It also disables the use of the space or enter key in uploading files.

To use a one-step upload, bind the event handler to the `rx.upload` component's
`on_drop` trigger.

```python
class State(rx.State):
    """The app state."""

    # The images to show.
    img: list[str]

    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)


color = "rgb(107,99,246)"


def index():
    """The main view."""
    return rx.vstack(
        rx.upload(
            rx.vstack(
                rx.button("Select File", color=color, bg="white", border=f"1px solid \{color}"),
                rx.text("Drag and drop files here or click to select files"),
            ),
            id="upload2",
            multiple=True,
            accept = {
                "application/pdf": [".pdf"],
                "image/png": [".png"],
                "image/jpeg": [".jpg", ".jpeg"],
                "image/gif": [".gif"],
                "image/webp": [".webp"],
                "text/html": [".html", ".htm"],
            },
            max_files=5,
            disabled=False,
            no_keyboard=True,
            on_drop=State.handle_upload(rx.upload_files(upload_id="upload2")),
            border=f"1px dotted \{color}",
            padding="5em",
        ),
        rx.grid(
            rx.foreach(
                State.img,
                lambda img: rx.vstack(
                    rx.image(src=rx.get_upload_url(img)),
                    rx.text(img),
                ),
            ),
            columns="2",
            spacing="1",
        ),
        padding="5em",
    )
```


## Handling the Upload

Your event handler should be an async function that accepts a single argument,
`files: list[UploadFile]`, which will contain [FastAPI UploadFile](https://fastapi.tiangolo.com/tutorial/request-files) instances.
You can read the files and save them anywhere as shown in the example.

In your UI, you can bind the event handler to a trigger, such as a button
`on_click` event or upload `on_drop` event, and pass in the files using
`rx.upload_files()`.

### Saving the File

By convention, Reflex provides the function `rx.get_upload_dir()` to get the directory where uploaded files may be saved. The upload dir comes from the environment variable `REFLEX_UPLOADED_FILES_DIR`, or `./uploaded_files` if not specified.

The backend of your app will mount this uploaded files directory on `/_upload` without restriction. Any files uploaded via this mechanism will automatically be publicly accessible. To get the URL for a file inside the upload dir, use the `rx.get_upload_url(filename)` function in a frontend component.

```md alert info
# When using the Reflex hosting service, the uploaded files directory is not persistent and will be cleared on every deployment. For persistent storage of uploaded files, it is recommended to use an external service, such as S3.
```

## Cancellation

The `id` provided to the `rx.upload` component can be passed to the special event handler `rx.cancel_upload(id)` to stop uploading on demand. Cancellation can be triggered directly by a frontend event trigger, or it can be returned from a backend event handler.

## Progress

The `rx.upload_files` special event arg also accepts an `on_upload_progress` event trigger which will be fired about every second during the upload operation to report the progress of the upload. This can be used to update a progress bar or other UI elements to show the user the progress of the upload.

```python
class UploadExample(rx.State):
    uploading: bool = False
    progress: int = 0
    total_bytes: int = 0

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        for file in files:
            self.total_bytes += len(await file.read())

    @rx.event
    def handle_upload_progress(self, progress: dict):
        self.uploading = True
        self.progress = round(progress["progress"] * 100)
        if self.progress >= 100:
            self.uploading = False

    @rx.event
    def cancel_upload(self):
        self.uploading = False
        return rx.cancel_upload("upload3")


def upload_form():
    return rx.vstack(
        rx.upload(
            rx.text("Drag and drop files here or click to select files"),
            id="upload3",
            border="1px dotted rgb(107,99,246)",
            padding="5em",
        ),
        rx.vstack(rx.foreach(rx.selected_files("upload3"), rx.text)),
        rx.progress(value=UploadExample.progress, max=100),
        rx.cond(
            ~UploadExample.uploading,
            rx.button(
                "Upload",
                on_click=UploadExample.handle_upload(
                    rx.upload_files(
                        upload_id="upload3",
                        on_upload_progress=UploadExample.handle_upload_progress,
                    ),
                ),
            ),
            rx.button("Cancel", on_click=UploadExample.cancel_upload),
        ),
        rx.text("Total bytes uploaded: ", UploadExample.total_bytes),
        align="center",
    )
```

The `progress` dictionary contains the following keys:

```javascript
\{
    'loaded': 36044800,
    'total': 54361908,
    'progress': 0.6630525183185255,
    'bytes': 20447232,
    'rate': None,
    'estimated': None,
    'event': \{'isTrusted': True},
    'upload': True
}
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/forms/radio_group.md`:

```md
---
components:
  - rx.radio_group
  - rx.radio_group.root
  - rx.radio_group.item

HighLevelRadioGroup: |
  lambda **props: rx.radio_group(["1", "2", "3", "4", "5"], **props)

RadioGroupRoot: |
  lambda **props: rx.radio_group.root(
      rx.radio_group.item(value="1"),
      rx.radio_group.item(value="2"),
      rx.radio_group.item(value="3"),
      rx.radio_group.item(value="4"),
      rx.radio_group.item(value="5"),
      **props
  )

RadioGroupItem: |
  lambda **props: rx.radio_group.root(
      rx.radio_group.item(value="1", **props),
      rx.radio_group.item(value="2", **props),
      rx.radio_group.item(value="3",),
      rx.radio_group.item(value="4",),
      rx.radio_group.item(value="5",),
  )
---


# Radio Group

A set of interactive radio buttons where only one can be selected at a time.

## Basic example

```python demo exec
class RadioGroupState(rx.State):
    item: str = "No Selection"

    @rx.event
    def set_item(self, item: str):
        self.item = item

def radio_group_state_example():
    return rx.vstack(
        rx.badge(RadioGroupState.item, color_scheme="green"),
        rx.radio(["1", "2", "3"], on_change=RadioGroupState.set_item, direction="row"),
    )
```

## Submitting a form using Radio Group

The `name` prop is used to name the group. It is submitted with its owning form as part of a name/value pair.

When the `required` prop is `True`, it indicates that the user must check a radio item before the owning form can be submitted.

```python demo exec
class FormRadioState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def radio_form_example():
    return rx.card(
        rx.vstack(
            rx.heading("Example Form"),
            rx.form.root(
                rx.vstack(
                    rx.radio_group(
                        ["Option 1", "Option 2", "Option 3"],
                        name="radio_choice",
                        direction="row",
                    ),
                    rx.button("Submit", type="submit"),
                    width="100%",
                    spacing="4",
                ),
                on_submit=FormRadioState.handle_submit,
                reset_on_submit=True,
            ),
            rx.divider(),
            rx.hstack(
                rx.heading("Results:"),
                rx.badge(FormRadioState.form_data.to_string()),
            ),
            align_items="left",
            width="100%",
            spacing="4",
        ),
        width="50%",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/forms/text_area.md`:

```md
---
components:
  - rx.text_area

TextArea: |
  lambda **props: rx.text_area(**props)
---


# Text Area

A text area is a multi-line text input field.

## Basic Example

The text area component can be controlled by a single value. The `on_blur` prop can be used to update the value when the text area loses focus.

```python demo exec
class TextAreaBlur(rx.State):
    text: str = "Hello World!"


def blur_example():
    return rx.vstack(
        rx.heading(TextAreaBlur.text),
        rx.text_area(
            placeholder="Type here...",
            on_blur=TextAreaBlur.set_text,
        ),
    )
```

## Text Area in forms

Here we show how to use a text area in a form. We use the `name` prop to identify the text area in the form data. The form data is then passed to the `submit_feedback` method to be processed.

```python demo exec
class TextAreaFeedbackState(rx.State):
    feedback: str = ""
    submitted: bool = False

    @rx.event
    def submit_feedback(self, form_data: dict):
        self.submitted = True

    @rx.event
    def reset_form(self):
        self.feedback = ""
        self.submitted = False

def feedback_form():
    return rx.cond(
        TextAreaFeedbackState.submitted,
        rx.card(
            rx.vstack(
                rx.text("Thank you for your feedback!"),
                rx.button("Submit another response", on_click=TextAreaFeedbackState.reset_form),
            ),
        ),
        rx.card(
            rx.form(
                rx.flex(
                    rx.text("Are you enjoying Reflex?"),
                    rx.text_area(
                        placeholder="Write your feedback…",
                        value=TextAreaFeedbackState.feedback,
                        on_change=TextAreaFeedbackState.set_feedback,
                        resize="vertical",
                    ),
                    rx.button("Send", type="submit"),
                    direction="column",
                    spacing="3",
                ),
                on_submit=TextAreaFeedbackState.submit_feedback,
            ),
        ),
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/forms/form-ll.md`:

```md
---
components:
  - rx.form.root
  - rx.form.field
  - rx.form.control
  - rx.form.label
  - rx.form.message
  - rx.form.submit

FormRoot: |
  lambda **props: rx.form.root(
      rx.form.field(
          rx.flex(
              rx.form.label("Email"),
              rx.form.control(
                  rx.input(
                      placeholder="Email Address",
                      # type attribute is required for "typeMismatch" validation
                      type="email",
                  ),
                  as_child=True,
              ),
              rx.form.message("Please enter a valid email"),
              rx.form.submit(
                  rx.button("Submit"),
                  as_child=True,
              ),
              direction="column",
              spacing="2",
              align="stretch",
          ),
          name="email",
      ),
      **props,
  )

FormField: |
  lambda **props: rx.form.root(
      rx.form.field(
          rx.flex(
              rx.form.label("Email"),
              rx.form.control(
                  rx.input(
                      placeholder="Email Address",
                      # type attribute is required for "typeMismatch" validation
                      type="email",
                  ),
                  as_child=True,
              ),
              rx.form.message("Please enter a valid email", match="typeMismatch"),
              rx.form.submit(
                  rx.button("Submit"),
                  as_child=True,
              ),
              direction="column",
              spacing="2",
              align="stretch",
          ),
          **props,
      ),
      reset_on_submit=True,
  )

FormMessage: |
  lambda **props: rx.form.root(
              rx.form.field(
                  rx.flex(
                      rx.form.label("Email"),
                      rx.form.control(
                          rx.input(
                              placeholder="Email Address",
                              # type attribute is required for "typeMismatch" validation
                              type="email",
                          ),
                          as_child=True,
                      ),
                      rx.form.message("Please enter a valid email", **props,),
                      rx.form.submit(
                          rx.button("Submit"),
                          as_child=True,
                      ),
                      direction="column",
                      spacing="2",
                      align="stretch",
                  ),
                  name="email",
              ),
              on_submit=lambda form_data: rx.window_alert(form_data.to_string()),
              reset_on_submit=True,
          )
---

# Form


```md warning info
# Low Level Form is Experimental

Please use the High Level Form for now for production.
```

Forms are used to collect information from your users. Forms group the inputs and submit them together.

## Basic Example

Here is an example of a form collecting an email address, with built-in validation on the email. If email entered is invalid, the form cannot be submitted. Note that the `form.submit` button is not automatically disabled. It is still clickable, but does not submit the form data. After successful submission, an alert window shows up and the form is cleared. There are a few `flex` containers used in the example to control the layout of the form components.

```python demo
rx.form.root(
    rx.form.field(
        rx.flex(
            rx.form.label("Email"),
            rx.form.control(
                rx.input(
                    placeholder="Email Address",
                    # type attribute is required for "typeMismatch" validation
                    type="email",
                ),
                as_child=True,
            ),
            rx.form.message("Please enter a valid email", match="typeMismatch"),
            rx.form.submit(
                  rx.button("Submit"),
                  as_child=True,
            ),
            direction="column",
            spacing="2",
            align="stretch",
        ),
        name="email",
    ),
    on_submit=lambda form_data: rx.window_alert(form_data.to_string()),
    reset_on_submit=True,
)
```

In this example, the `rx.input` has an attribute `type="email"` and the `form.message` has the attribute `match="typeMismatch"`. Those are required for the form to validate the input by its type. The prop `as_child="True"` is required when using other components to construct a Form component. This example has used `rx.input` to construct the Form Control and `button` the Form Submit.

## Form Anatomy

```python eval
rx._x.code_block(
    """form.root(
    form.field(
        form.label(...),
        form.control(...),
        form.message(...),
    ),
    form.submit(...),
)""",
    language="python",
)
```

A Form Root (`form.root`) contains all the parts of a form. The Form Field (`form.field`), Form Submit (`form.submit`), etc should all be inside a Form Root. A Form Field can contain a Form Label (`form.label`), a Form Control (`form.control`), and a Form Message (`form.message`). A Form Label is a label element. A Form Control is where the user enters the input or makes selections. By default, the Form Control is a input. Using other form components to construct the Form Control is supported. To do that, set the prop `as_child=True` on the Form Control.

```md alert info
The current version of Radix Forms does not support composing **Form Control** with other Radix form primitives such as **Checkbox**, **Select**, etc.
```

The Form Message is a validation message which is automatically wired (functionality and accessibility). When the Form Control determines the input is invalid, the Form Message is shown. The `match` prop is to enable [client side validation](#client-side-validation). To perform [server side validation](#server-side-validation), **both** the `force_match` prop of the Form Control and the `server_invalid` prop of the Form Field are set together.

The Form Submit is by default a button that submits the form. To use another button component as a Form Submit, include that button as a child inside `form.submit` and set the prop `as_child=True`.

The `on_submit` prop of the Form Root accepts an event handler. It is called with the submitted form data dictionary. To clear the form after submission, set the `reset_on_submit=True` prop.

## Data Submission

As previously mentioned, the various pieces of data in the form are submitted together as a dictionary. The form control or the input components must have the `name` attribute. This `name` is the key to get the value from the form data dictionary. If no validation is needed, the form type components such as Checkbox, Radio Groups, TextArea can be included directly under the Form Root instead of inside a Form Control.

```python demo exec
import reflex as rx
import reflex.components.radix.primitives as rdxp

class RadixFormSubmissionState(rx.State):
    form_data: dict

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

    @rx.var
    def form_data_keys(self) -> list:
        return list(self.form_data.keys())

    @rx.var
    def form_data_values(self) -> list:
        return list(self.form_data.values())


def radix_form_submission_example():
    return rx.flex(
        rx.form.root(
            rx.flex(
                rx.flex(
                    rx.checkbox(
                        default_checked=True,
                        name="box1",
                    ),
                    rx.text("box1 checkbox"),
                    direction="row",
                    spacing="2",
                    align="center",
                ),
                rx.radio.root(
                    rx.flex(
                        rx.radio.item(value="1"),
                        "1",
                        direction="row",
                        align="center",
                        spacing="2",
                    ),
                    rx.flex(
                        rx.radio.item(value="2"),
                        "2",
                        direction="row",
                        align="center",
                        spacing="2",
                    ),
                    rx.flex(
                        rx.radio.item(value="3"),
                        "3",
                        direction="row",
                        align="center",
                        spacing="2",
                    ),
                    default_value="1",
                    name="box2",
                ),
                rx.input(
                    placeholder="box3 textfield input",
                    name="box3",
                ),
                rx.select.root(
                    rx.select.trigger(
                        placeholder="box4 select",
                    ),
                    rx.select.content(
                        rx.select.group(
                            rx.select.item(
                                "Orange",
                                value="orange"
                            ),
                            rx.select.item(
                                "Apple",
                                value="apple"
                            ),
                        ),
                    ),
                    name="box4",
                ),
                rx.flex(
                    rx.switch(
                        default_checked=True,
                        name="box5",
                    ),
                    "box5 switch",
                    spacing="2",
                    align="center",
                    direction="row",
                ),
                rx.flex(
                    rx.slider(
                        default_value=[40],
                        width="100%",
                        name="box6",
                    ),
                    "box6 slider",
                    direction="row",
                    spacing="2",
                    align="center",
                ),
                rx.text_area(
                    placeholder="Enter for box7 textarea",
                    name="box7",
                ),
                rx.form.submit(
                    rx.button("Submit"),
                    as_child=True,
                ),
                direction="column",
                spacing="4",
            ),
            on_submit=RadixFormSubmissionState.handle_submit,
        ),
        rx.divider(size="4"),
        rx.text(
            "Results",
            weight="bold",
        ),
        rx.foreach(RadixFormSubmissionState.form_data_keys,
            lambda key, idx: rx.text(key, " : ", RadixFormSubmissionState.form_data_values[idx])
        ),
        direction="column",
        spacing="4",
    )
```

## Validation

Server side validation is done through **Computed Vars** on the State. The **Var** should return a boolean flag indicating when input is invalid. Set that **Var** on both the `server_invalid` prop of `form.field` and the `force_match` prop of `form.message`. There is an example how to do that in the [Final Example](#final-example).

## Final Example

The final example shows a form that collects username and email during sign-up and validates them using server side validation. When server side validation fails, messages are displayed in red to show what is not accepted in the form, and the submit button is disabled. After submission, the collected form data is displayed in texts below the form and the form is cleared.

```python demo exec
import re
import reflex as rx
import reflex.components.radix.primitives as rdxp

class RadixFormState(rx.State):
    # These track the user input real time for validation
    user_entered_username: str
    user_entered_email: str

    # These are the submitted data
    username: str
    email: str

    mock_username_db: list[str] = ["reflex", "admin"]

    @rx.var
    def invalid_email(self) -> bool:
        return not re.match(r"[^@]+@[^@]+\.[^@]+", self.user_entered_email)

    @rx.var
    def username_empty(self) -> bool:
        return not self.user_entered_username.strip()

    @rx.var
    def username_is_taken(self) -> bool:
        return self.user_entered_username in self.mock_username_db

    @rx.var
    def input_invalid(self) -> bool:
        return self.invalid_email or self.username_is_taken or self.username_empty

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.username = form_data.get("username")
        self.email = form_data.get("email")

def radix_form_example():
    return rx.flex(
        rx.form.root(
            rx.flex(
                rx.form.field(
                    rx.flex(
                        rx.form.label("Username"),
                        rx.form.control(
                            rx.input(
                                placeholder="Username",
                                # workaround: `name` seems to be required when on_change is set
                                on_change=RadixFormState.set_user_entered_username,
                                name="username",
                            ),
                            as_child=True,
                        ),
                        # server side validation message can be displayed inside a rx.cond
                        rx.cond(
                            RadixFormState.username_empty,
                            rx.form.message(
                                "Username cannot be empty",
                                color="var(--red-11)",
                            ),
                        ),
                        # server side validation message can be displayed by `force_match` prop
                        rx.form.message(
                            "Username already taken",
                            # this is a workaround:
                            # `force_match` does not work without `match`
                            # This case does not want client side validation
                            # and intentionally not set `required` on the input
                            # so "valueMissing" is always false
                            match="valueMissing",
                            force_match=RadixFormState.username_is_taken,
                            color="var(--red-11)",
                        ),
                        direction="column",
                        spacing="2",
                        align="stretch",
                    ),
                    name="username",
                    server_invalid=RadixFormState.username_is_taken,
                ),
                rx.form.field(
                    rx.flex(
                        rx.form.label("Email"),
                        rx.form.control(
                            rx.input(
                                placeholder="Email Address",
                                on_change=RadixFormState.set_user_entered_email,
                                name="email",
                            ),
                            as_child=True,
                        ),
                        rx.form.message(
                            "A valid Email is required",
                            match="valueMissing",
                            force_match=RadixFormState.invalid_email,
                            color="var(--red-11)",
                        ),
                        direction="column",
                        spacing="2",
                        align="stretch",
                    ),
                    name="email",
                    server_invalid=RadixFormState.invalid_email,
                ),
                rx.form.submit(
                    rx.button(
                        "Submit",
                        disabled=RadixFormState.input_invalid,
                    ),
                    as_child=True,
                ),
                direction="column",
                spacing="4",
                width="25em",
            ),
            on_submit=RadixFormState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(size="4"),
        rx.text(
            "Username submitted: ",
            rx.text(
                RadixFormState.username,
                weight="bold",
                color="var(--accent-11)",
            ),
        ),
        rx.text(
            "Email submitted: ",
            rx.text(
                RadixFormState.email,
                weight="bold",
                color="var(--accent-11)",
            ),
        ),
        direction="column",
        spacing="4",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/forms/input-ll.md`:

```md
---
components:
    - rx.input
    - rx.input.slot
---


# Input

A text field is an input field that users can type into. This component uses Radix's [text field](https://www.radix-ui.com/themes/docs/components/text-field) component.


## Overview

The TextField component is used to capture user input and can include an optional slot for buttons and icons. It is based on the <div> element and supports common margin props.

## Basic Example

```python demo
rx.input(
    rx.input.slot(
        rx.icon(tag="search"),

    ),
    placeholder="Search here...",
)
```

## Stateful Example with Blur Event

```python demo exec
class TextfieldBlur1(rx.State):
    text: str = "Hello World!"


def blur_example1():
    return rx.vstack(
        rx.heading(TextfieldBlur1.text),
        rx.input(
            rx.input.slot(
                rx.icon(tag="search"),
            ),
            placeholder="Search here...",
            on_blur=TextfieldBlur1.set_text,
        )
    )
```

## Controlled Example

```python demo exec
class TextfieldControlled1(rx.State):
    text: str = "Hello World!"


def controlled_example1():
    return rx.vstack(
        rx.heading(TextfieldControlled1.text),
        rx.input(
            rx.input.slot(
                rx.icon(tag="search"),
            ),
            placeholder="Search here...",
            value=TextfieldControlled1.text,
            on_change=TextfieldControlled1.set_text,
        ),
    )
```

# Real World Example

```python demo exec

def song(title, initials: str, genre: str):
    return rx.card(rx.flex(
        rx.flex(
            rx.avatar(fallback=initials),
            rx.flex(
                rx.text(title, size="2", weight="bold"),
                rx.text(genre, size="1", color_scheme="gray"),
                direction="column",
                spacing="1",
            ),
            direction="row",
            align_items="left",
            spacing="1",
        ),
        rx.flex(
            rx.icon(tag="chevron_right"),
            align_items="center",
        ),
        justify="between",
    ))

def search():
    return rx.card(
    rx.flex(
        rx.input(
            rx.input.slot(
                rx.icon(tag="search"),
            ),
            placeholder="Search songs...",
        ),
        rx.flex(
            song("The Less I Know", "T", "Rock"),
            song("Breathe Deeper", "ZB", "Rock"),
            song("Let It Happen", "TF", "Rock"),
            song("Borderline", "ZB", "Pop"),
            song("Lost In Yesterday", "TO", "Rock"),
            song("Is It True", "TO", "Rock"),
            direction="column",
            spacing="1",
        ),
        direction="column",
        spacing="3",
    ),
    style={"maxWidth": 500},
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/forms/switch.md`:

```md
---
components:
  - rx.switch

Switch: |
  lambda **props: rx.switch(**props)
---


# Switch

A toggle switch alternative to the checkbox.

## Basic Example

Here is a basic example of a switch. We use the `on_change` trigger to toggle the value in the state.

```python demo exec
class SwitchState(rx.State):
    value: bool = False

    @rx.event
    def set_end(self, value: bool):
        self.value = value

def switch_intro():
    return rx.center(
        rx.switch(on_change=SwitchState.set_end),
        rx.badge(SwitchState.value),
    )
```

## Control the value

The `checked` prop is used to control the state of the switch. The event `on_change` is called when the state of the switch changes, when the `change_checked` event handler is called.

The `disabled` prop when `True`, prevents the user from interacting with the switch. In our example below, even though the second switch is `disabled` we are still able to change whether it is checked or not using the `checked` prop.

```python demo exec
class ControlSwitchState(rx.State):

    checked = True

    @rx.event
    def change_checked(self, checked: bool):
        """Change the switch checked var."""
        self.checked = checked


def control_switch_example():
    return rx.hstack(
        rx.switch(
            checked=ControlSwitchState.checked,
            on_change=ControlSwitchState.change_checked,
        ),
        rx.switch(
            checked=ControlSwitchState.checked,
            on_change=ControlSwitchState.change_checked,
            disabled=True,
        ),
    )
```

## Switch in forms

The `name` of the switch is needed to submit with its owning form as part of a name/value pair. When the `required` prop is `True`, it indicates that the user must check the switch before the owning form can be submitted.

The `value` prop is only used for form submission, use the `checked` prop to control state of the `switch`.

```python demo exec
class FormSwitchState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def switch_form_example():
    return rx.card(
            rx.vstack(
                rx.heading("Example Form"),
                rx.form.root(
                    rx.hstack(
                        rx.switch(name="switch"),
                        rx.button("Submit", type="submit"),
                        width="100%",
                    ),
                    on_submit=FormSwitchState.handle_submit,
                    reset_on_submit=True,
                ),
                rx.divider(),
                rx.hstack(
                    rx.heading("Results:"),
                    rx.badge(FormSwitchState.form_data.to_string()),
                ),
                align_items="left",
                width="100%",
            ),
        width="50%",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/forms/input.md`:

```md
---
components:
  - rx.input
  - rx.input.slot

Input: |
  lambda **props: rx.input(placeholder="Search the docs", **props)

TextFieldSlot: |
  lambda **props: rx.input(
      rx.input.slot(
          rx.icon(tag="search", height="16", width="16"),
          **props,
      ),
      placeholder="Search the docs",
  )
---


# Input

The `input` component is an input field that users can type into.

```md video https://youtube.com/embed/ITOZkzjtjUA?start=1517&end=1869
# Video: Input
```

## Basic Example

The `on_blur` event handler is called when focus has left the `input` for example, it’s called when the user clicks outside of a focused text input.

```python demo exec
class TextfieldBlur(rx.State):
    text: str = "Hello World!"


def blur_example():
    return rx.vstack(
        rx.heading(TextfieldBlur.text),
        rx.input(
            placeholder="Search here...",
            on_blur=TextfieldBlur.set_text,
        ),
    )
```

The `on_change` event handler is called when the `value` of `input` has changed.

```python demo exec
class TextfieldControlled(rx.State):
    text: str = "Hello World!"


def controlled_example():
    return rx.vstack(
        rx.heading(TextfieldControlled.text),
        rx.input(
            placeholder="Search here...",
            value=TextfieldControlled.text,
            on_change=TextfieldControlled.set_text,
        ),
    )
```

Behind the scenes, the input component is implemented as a debounced input to avoid sending individual state updates per character to the backend while the user is still typing. This allows a state variable to directly control the `value` prop from the backend without the user experiencing input lag.

### Submitting a form using input

The `name` prop is needed to submit with its owning form as part of a name/value pair.

When the `required` prop is `True`, it indicates that the user must input text before the owning form can be submitted.

The `type` is set here to `password`. The element is presented as a one-line plain text editor control in which the text is obscured so that it cannot be read. The `type` prop can take any value of `email`, `file`, `password`, `text` and several others. Learn more [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).

```python demo exec
class FormInputState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_input1():
    return rx.card(
        rx.vstack(
            rx.heading("Example Form"),
            rx.form.root(
                rx.hstack(
                    rx.input(
                        name="input",
                        placeholder="Enter text...",
                        type="text",
                        required=True,
                    ),
                    rx.button("Submit", type="submit"),
                    width="100%",
                ),
                on_submit=FormInputState.handle_submit,
                reset_on_submit=True,
            ),
            rx.divider(),
            rx.hstack(
                rx.heading("Results:"),
                rx.badge(FormInputState.form_data.to_string()),
            ),
            align_items="left",
            width="100%",
        ),
        width="50%",
    )
```

To learn more about how to use forms in the [Form]({library.forms.form.path}) docs.

### Setting a value without using a State var

Set the value of the specified reference element, without needing to link it up to a State var. This is an alternate way to modify the value of the `input`.

```python demo
rx.hstack(
    rx.input(id="input1"),
    rx.button("Erase", on_click=rx.set_value("input1", "")),
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/forms/select-ll.md`:

```md
---
components:
  - rx.select
  - rx.select.root
  - rx.select.trigger
  - rx.select.content
  - rx.select.group
  - rx.select.item
  - rx.select.label
  - rx.select.separator
---


# Select

Displays a list of options for the user to pick from, triggered by a button.

## Basic Example

```python demo
rx.select.root(
    rx.select.trigger(),
    rx.select.content(
        rx.select.group(
            rx.select.label("Fruits"),
            rx.select.item("Orange", value="orange"),
            rx.select.item("Apple", value="apple"),
            rx.select.item("Grape", value="grape", disabled=True),
        ),
        rx.select.separator(),
        rx.select.group(
            rx.select.label("Vegetables"),
            rx.select.item("Carrot", value="carrot"),
            rx.select.item("Potato", value="potato"),
        ),
    ),
    default_value="apple",
)
```

## Usage

## Disabling

It is possible to disable individual items in a `select` using the `disabled` prop associated with the `rx.select.item`.

```python demo
rx.select.root(
    rx.select.trigger(placeholder="Select a Fruit"),
    rx.select.content(
        rx.select.group(
            rx.select.item("Apple", value="apple"),
            rx.select.item("Grape", value="grape", disabled=True),
            rx.select.item("Pineapple", value="pineapple"),
        ),
    ),
)
```

To prevent the user from interacting with select entirely, set the `disabled` prop to `True` on the `rx.select.root` component.

```python demo
rx.select.root(
    rx.select.trigger(placeholder="This is Disabled"),
    rx.select.content(
        rx.select.group(
            rx.select.item("Apple", value="apple"),
            rx.select.item("Grape", value="grape"),
        ),
    ),
    disabled=True,
)
```

## Setting Defaults

It is possible to set several default values when constructing a `select`.

The `placeholder` prop in the `rx.select.trigger` specifies the content that will be rendered when `value` or `default_value` is empty or not set.

```python demo
rx.select.root(
    rx.select.trigger(placeholder="pick a fruit"),
    rx.select.content(
        rx.select.group(
            rx.select.item("Apple", value="apple"),
            rx.select.item("Grape", value="grape"),
        ),
    ),
)
```

The `default_value` in the `rx.select.root` specifies the value of the `select` when initially rendered.
The `default_value` should correspond to the `value` of a child `rx.select.item`.

```python demo
rx.select.root(
    rx.select.trigger(),
    rx.select.content(
        rx.select.group(
            rx.select.item("Apple", value="apple"),
            rx.select.item("Grape", value="grape"),
        ),
    ),
    default_value="apple",
)
```

## Fully controlled

The `on_change` event trigger is fired when the value of the select changes.
In this example the `rx.select_root` `value` prop specifies which item is selected, and this
can also be controlled using state and a button without direct interaction with the select component.

```python demo exec
class SelectState2(rx.State):

    values: list[str] = ["apple", "grape", "pear"]

    value: str = ""

    @rx.event
    def choose_randomly(self):
        """Change the select value var."""
        original_value = self.value
        while self.value == original_value:
            self.value = random.choice(self.values)


def select_example2():
    return rx.vstack(
        rx.select.root(
            rx.select.trigger(placeholder="No Selection"),
            rx.select.content(
                rx.select.group(
                    rx.foreach(SelectState2.values, lambda x: rx.select.item(x, value=x))
                ),
            ),
            value=SelectState2.value,
            on_change=SelectState2.set_value,

        ),
        rx.button("Choose Randomly", on_click=SelectState2.choose_randomly),
        rx.button("Reset", on_click=SelectState2.set_value("")),
    )
```

The `open` prop and `on_open_change` event trigger work similarly to `value` and `on_change` to control the open state of the select.
If `on_open_change` handler does not alter the `open` prop, the select will not be able to be opened or closed by clicking on the
`select_trigger`.

```python demo exec
class SelectState8(rx.State):
   is_open: bool = False

def select_example8():
   return rx.flex(
       rx.select.root(
           rx.select.trigger(placeholder="No Selection"),
           rx.select.content(
               rx.select.group(
                   rx.select.item("Apple", value="apple"),
                   rx.select.item("Grape", value="grape"),
               ),
           ),
           open=SelectState8.is_open,
           on_open_change=SelectState8.set_is_open,
       ),
       rx.button("Toggle", on_click=SelectState8.set_is_open(~SelectState8.is_open)),
       spacing="2",
   )
```

### Submitting a Form with Select

When a select is part of a form, the `name` prop of the `rx.select.root` sets the key that will be submitted with the form data.

The `value` prop of `rx.select.item` provides the value to be associated with the `name` key when the form is submitted with that item selected.

When the `required` prop of the `rx.select.root` is `True`, it indicates that the user must select a value before the form may be submitted.

```python demo exec
class FormSelectState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_select():
    return rx.flex(
        rx.form.root(
            rx.flex(
                rx.select.root(
                    rx.select.trigger(),
                    rx.select.content(
                        rx.select.group(
                            rx.select.label("Fruits"),
                            rx.select.item("Orange", value="orange"),
                            rx.select.item("Apple", value="apple"),
                            rx.select.item("Grape", value="grape"),
                        ),
                        rx.select.separator(),
                        rx.select.group(
                            rx.select.label("Vegetables"),
                            rx.select.item("Carrot", value="carrot"),
                            rx.select.item("Potato", value="potato"),
                        ),
                    ),
                    default_value="apple",
                    name="select",
                ),
                rx.button("Submit"),
                width="100%",
                direction="column",
                spacing="2",
            ),
            on_submit=FormSelectState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(size="4"),
        rx.heading("Results"),
        rx.text(FormSelectState.form_data.to_string()),
        width="100%",
        direction="column",
        spacing="2",
    )
```

## Real World Example

```python demo
rx.card(
    rx.flex(
        rx.image(src="/reflex_banner.png", width="100%", height="auto"),
        rx.flex(
            rx.heading("Reflex Swag", size="4", margin_bottom="4px"),
            rx.heading("$99", size="6", margin_bottom="4px"),
            direction="row", justify="between",
            width="100%",
        ),
        rx.text("Reflex swag with a sense of nostalgia, as if they carry whispered tales of past adventures", size="2", margin_bottom="4px"),
        rx.divider(size="4"),
        rx.flex(
            rx.flex(
                rx.text("Color", size="2", margin_bottom="4px", color_scheme="gray"),
                rx.select.root(
                    rx.select.trigger(),
                    rx.select.content(
                        rx.select.group(
                            rx.select.item("Light", value="light"),
                            rx.select.item("Dark", value="dark"),
                        ),
                    ),
                    default_value="light",
                ),
                direction="column",
            ),
            rx.flex(
                rx.text("Size", size="2", margin_bottom="4px", color_scheme="gray"),
                rx.select.root(
                    rx.select.trigger(),
                    rx.select.content(
                        rx.select.group(
                            rx.select.item("24", value="24"),
                            rx.select.item("26", value="26"),
                            rx.select.item("28", value="28", disabled=True),
                            rx.select.item("30", value="30"),
                            rx.select.item("32", value="32"),
                            rx.select.item("34", value="34"),
                            rx.select.item("36", value="36"),
                        ),
                    ),
                    default_value="30",
                ),
                direction="column",
            ),
            rx.button(rx.icon(tag="plus"), "Add"),
            align="end",
            justify="between",
            spacing="2",
            width="100%",
        ),
        width="15em",
        direction="column",
        spacing="2",
    ),
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/forms/select.md`:

```md
---
components:
  - rx.select
  - rx.select.root
  - rx.select.trigger
  - rx.select.content
  - rx.select.group
  - rx.select.item
  - rx.select.label
  - rx.select.separator

HighLevelSelect: |
  lambda **props: rx.select(["apple", "grape", "pear"], default_value="pear", **props)

SelectRoot: |
  lambda **props: rx.select.root(
      rx.select.trigger(),
      rx.select.content(
          rx.select.group(
              rx.select.item("apple", value="apple"),
              rx.select.item("grape", value="grape"),
              rx.select.item("pear", value="pear"),
          ),
      ),
      default_value="pear",
      **props
  )

SelectTrigger: |
  lambda **props: rx.select.root(
      rx.select.trigger(**props),
      rx.select.content(
          rx.select.group(
              rx.select.item("apple", value="apple"),
              rx.select.item("grape", value="grape"),
              rx.select.item("pear", value="pear"),
          ),
      ),
      default_value="pear",
  )

SelectContent: |
  lambda **props: rx.select.root(
      rx.select.trigger(),
      rx.select.content(
          rx.select.group(
              rx.select.item("apple", value="apple"),
              rx.select.item("grape", value="grape"),
              rx.select.item("pear", value="pear"),
          ),
          **props,
      ),
      default_value="pear",
  )

SelectItem: |
  lambda **props: rx.select.root(
      rx.select.trigger(),
      rx.select.content(
          rx.select.group(
              rx.select.item("apple", value="apple", **props),
              rx.select.item("grape", value="grape"),
              rx.select.item("pear", value="pear"),
          ),
      ),
      default_value="pear",
  )
---


# Select

Displays a list of options for the user to pick from—triggered by a button.

```python demo exec
class SelectState(rx.State):
    value: str = "apple"

    @rx.event
    def change_value(self, value: str):
        """Change the select value var."""
        self.value = value


def select_intro():
    return rx.center(
        rx.select(
            ["apple", "grape", "pear"],
            value=SelectState.value,
            on_change=SelectState.change_value,
        ),
        rx.badge(SelectState.value),
    )
```

```python demo exec
class SelectState3(rx.State):

    values: list[str] = ["apple", "grape", "pear"]

    value: str = "apple"

    @rx.event
    def change_value(self):
        """Change the select value var."""
        self.value = random.choice(self.values)


def select_example3():
    return rx.vstack(
        rx.select(
            SelectState3.values,
            value=SelectState3.value,
            on_change=SelectState3.set_value,
        ),
        rx.button("Change Value", on_click=SelectState3.change_value),

    )
```

The `on_open_change` event handler acts in a similar way to the `on_change` and is called when the open state of the select changes.

```python demo
rx.select(
    ["apple", "grape", "pear"],
    on_change=rx.window_alert("on_change event handler called"),
)

```

### Submitting a form using select

The `name` prop is needed to submit with its owning form as part of a name/value pair.

When the `required` prop is `True`, it indicates that the user must select a value before the owning form can be submitted.

```python demo exec
class FormSelectState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def select_form_example():
    return rx.card(
        rx.vstack(
            rx.heading("Example Form"),
            rx.form.root(
                rx.flex(
                    rx.select(["apple", "grape", "pear"], default_value="apple", name="select", required=True),
                    rx.button("Submit", flex="1", type="submit"),
                    width="100%",
                    spacing="3",
                ),
                on_submit=FormSelectState.handle_submit,
                reset_on_submit=True,
            ),
            rx.divider(),
            rx.hstack(
                rx.heading("Results:"),
                rx.badge(FormSelectState.form_data.to_string()),
            ),
            align_items="left",
            width="100%",
        ),
        width="50%",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/forms/editor.md`:

```md
---
components:
  - rx.editor
---

# Editor

An HTML editor component based on [Suneditor](http://suneditor.com/sample/index.html).

```python demo exec
import reflex as rx


class EditorState(rx.State):
    content: str = "<p>Editor content</p>"

    @rx.event
    def handle_change(self, content: str):
        """Handle the editor value change."""
        self.content = content


def editor_example():
    return rx.vstack(
        rx.editor(
            set_contents=EditorState.content,
            on_change=EditorState.handle_change,
        ),
        rx.box(
            rx.html(EditorState.content),
            border="1px dashed #ccc",
            border_radius="4px",
            width="100%",
        ),
    )
```

# EditorOptions

The extended options and toolbar buttons can be customized by passing an instance
of `rx.EditorOptions` for the `set_options` prop.


```python eval
rx.fragment(
    h2_comp(text="Fields"),
    rx.box(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Field"),
                    rx.table.column_header_cell("Description"),
                )
            ),
            rx.table.body(
                *[
                    rx.table.row(
                        rx.table.cell(rx.code(field["prop"].name, font_weight=styles.BOLD_WEIGHT)),
                        rx.table.cell(field["description"]),
                    )
                    for field in editor_options_source.get_fields()
                ],
            ),
        ),
        style={"overflow": "auto"},
    ),
)
```

```python eval
rx.box(height="2em")
```

The `button_list` prop expects a list of lists, where each sublist contains the
names of buttons forming a group on the toolbar. The character "/" can be used
in place of a sublist to denote a line break in the toolbar.

Some valid `button_list` options are enumerated in `rx.EditorButtonList`, seen below.

```python
class EditorButtonList(list, enum.Enum):

    BASIC = [
        ["font", "fontSize"],
        ["fontColor"],
        ["horizontalRule"],
        ["link", "image"],
    ]
    FORMATTING = [
        ["undo", "redo"],
        ["bold", "underline", "italic", "strike", "subscript", "superscript"],
        ["removeFormat"],
        ["outdent", "indent"],
        ["fullScreen", "showBlocks", "codeView"],
        ["preview", "print"],
    ]
    COMPLEX = [
        ["undo", "redo"],
        ["font", "fontSize", "formatBlock"],
        ["bold", "underline", "italic", "strike", "subscript", "superscript"],
        ["removeFormat"],
        "/",
        ["fontColor", "hiliteColor"],
        ["outdent", "indent"],
        ["align", "horizontalRule", "list", "table"],
        ["link", "image", "video"],
        ["fullScreen", "showBlocks", "codeView"],
        ["preview", "print"],
        ["save", "template"],
    ]
```

A custom list of toolbar buttons may also be specified using these names as seen
in the following example.

Since this example uses the same state as above, the two editors contents are
shared and can be modified by either one.

```python demo
rx.editor(
    set_contents=EditorState.content,
    set_options=rx.EditorOptions(
        button_list=[
            ["font", "fontSize", "formatBlock"],
            ["fontColor", "hiliteColor"],
            ["bold", "underline", "italic", "strike", "subscript", "superscript"],
            ["removeFormat"],
            "/",
            ["outdent", "indent"],
            ["align", "horizontalRule", "list", "table"],
            ["link"],
            ["fullScreen", "showBlocks", "codeView"],
            ["preview", "print"],
        ]
    ),
    on_change=EditorState.handle_change,
)
```

See the [Suneditor README.md](https://github.com/JiHong88/suneditor/blob/master/README.md) for more
details on buttons and options.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/forms/form.md`:

```md
---
components:
  - rx.form
  - rx.form.root
  - rx.form.field
  - rx.form.control
  - rx.form.label
  - rx.form.message
  - rx.form.submit

FormRoot: |
  lambda **props: rx.form.root(
      rx.form.field(
          rx.flex(
              rx.form.label("Email"),
              rx.form.control(
                  rx.input(
                      placeholder="Email Address",
                      # type attribute is required for "typeMismatch" validation
                      type="email",
                  ),
                  as_child=True,
              ),
              rx.form.message("Please enter a valid email"),
              rx.form.submit(
                  rx.button("Submit"),
                  as_child=True,
              ),
              direction="column",
              spacing="2",
              align="stretch",
          ),
          name="email",
      ),
      **props,
  )

FormField: |
  lambda **props: rx.form.root(
      rx.form.field(
          rx.flex(
              rx.form.label("Email"),
              rx.form.control(
                  rx.input(
                      placeholder="Email Address",
                      # type attribute is required for "typeMismatch" validation
                      type="email",
                  ),
                  as_child=True,
              ),
              rx.form.message("Please enter a valid email", match="typeMismatch"),
              rx.form.submit(
                  rx.button("Submit"),
                  as_child=True,
              ),
              direction="column",
              spacing="2",
              align="stretch",
          ),
          **props,
      ),
      reset_on_submit=True,
  )

FormLabel: |
  lambda **props: rx.form.root(
      rx.form.field(
          rx.flex(
              rx.form.label("Email", **props,),
              rx.form.control(
                  rx.input(
                      placeholder="Email Address",
                      # type attribute is required for "typeMismatch" validation
                      type="email",
                  ),
                  as_child=True,
              ),
              rx.form.message("Please enter a valid email", match="typeMismatch"),
              rx.form.submit(
                  rx.button("Submit"),
                  as_child=True,
              ),
              direction="column",
              spacing="2",
              align="stretch",
          ),
      ),
      reset_on_submit=True,
  )

FormMessage: |
  lambda **props: rx.form.root(
              rx.form.field(
                  rx.flex(
                      rx.form.label("Email"),
                      rx.form.control(
                          rx.input(
                              placeholder="Email Address",
                              # type attribute is required for "typeMismatch" validation
                              type="email",
                          ),
                          as_child=True,
                      ),
                      rx.form.message("Please enter a valid email", **props,),
                      rx.form.submit(
                          rx.button("Submit"),
                          as_child=True,
                      ),
                      direction="column",
                      spacing="2",
                      align="stretch",
                  ),
                  name="email",
              ),
              on_submit=lambda form_data: rx.window_alert(form_data.to_string()),
              reset_on_submit=True,
          )
---


# Form

Forms are used to collect user input. The `rx.form` component is used to group inputs and submit them together.

The form component's children can be form controls such as `rx.input`, `rx.checkbox`, `rx.slider`, `rx.textarea`, `rx.radio_group`, `rx.select` or `rx.switch`. The controls should have a `name` attribute that is used to identify the control in the form data. The `on_submit` event trigger submits the form data as a dictionary to the `handle_submit` event handler.

The form is submitted when the user clicks the submit button or presses enter on the form controls.

```python demo exec
class FormState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_example():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(placeholder="First Name", name="first_name"),
                rx.input(placeholder="Last Name", name="last_name"),
                rx.hstack(
                    rx.checkbox("Checked", name="check"),
                    rx.switch("Switched", name="switch"),
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(FormState.form_data.to_string()),
    )
```

```md alert warning
# When using the form you must include a button or input with `type='submit'`.
```

```md alert info
# Using `name` vs `id`.

When using the `name` attribute in form controls like `rx.switch`, `rx.radio_group`, and `rx.checkbox`, these controls will only be included in the form data if their values are set (e.g., if the checkbox is checked, the switch is toggled, or a radio option is selected).

If you need these controls to be passed in the form data even when their values are not set, you can use the `id` attribute instead of name. The id attribute ensures that the control is always included in the submitted form data, regardless of whether its value is set or not.
```

```md video https://youtube.com/embed/ITOZkzjtjUA?start=5287&end=6040
# Video: Forms
```

## Dynamic Forms

Forms can be dynamically created by iterating through state vars using `rx.foreach`.

This example allows the user to add new fields to the form prior to submit, and all
fields will be included in the form data passed to the `handle_submit` function.

```python demo exec
class DynamicFormState(rx.State):
    form_data: dict = {}
    form_fields: list[str] = ["first_name", "last_name", "email"]

    @rx.var(cache=True)
    def form_field_placeholders(self) -> list[str]:
        return [
            " ".join(w.capitalize() for w in field.split("_"))
            for field in self.form_fields
        ]

    @rx.event
    def add_field(self, form_data: dict):
        new_field = form_data.get("new_field")
        if not new_field:
            return
        field_name = new_field.strip().lower().replace(" ", "_")
        self.form_fields.append(field_name)

    @rx.event
    def handle_submit(self, form_data: dict):
        self.form_data = form_data


def dynamic_form():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.foreach(
                    DynamicFormState.form_fields,
                    lambda field, idx: rx.input(
                        placeholder=DynamicFormState.form_field_placeholders[idx],
                        name=field,
                    ),
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=DynamicFormState.handle_submit,
            reset_on_submit=True,
        ),
        rx.form(
            rx.hstack(
                rx.input(placeholder="New Field", name="new_field"),
                rx.button("+", type="submit"),
            ),
            on_submit=DynamicFormState.add_field,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(DynamicFormState.form_data.to_string()),
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/forms/slider.md`:

```md
---
components:
  - rx.slider

Slider: |
  lambda **props: rx.center(rx.slider(default_value=40, height="100%", **props), height="4em", width="100%")
---


# Slider

Provides user selection from a range of values. The

## Basic Example

The slider can be controlled by a single value or a range of values. Slider can be hooked to state to control its value. Passing a list of two values creates a range slider.

```python demo exec
class SliderState(rx.State):
    value: int = 50

    @rx.event
    def set_end(self, value: list[int]):
        self.value = value[0]

def slider_intro():
    return rx.vstack(
        rx.heading(SliderState.value),
        rx.slider(on_value_commit=SliderState.set_end),
        width="100%",
    )
```

## Range Slider

Range slider is created by passing a list of two values to the `default_value` prop. The list should contain two values that are in the range of the slider.

```python demo exec
class RangeSliderState(rx.State):
    value_start: int = 25
    value_end: int = 75

    @rx.event
    def set_end(self, value: list[int]):
        self.value_start = value[0]
        self.value_end = value[1]

def range_slider_intro():
    return rx.vstack(
        rx.hstack(
            rx.heading(RangeSliderState.value_start),
            rx.heading(RangeSliderState.value_end),
        ),
        rx.slider(
            default_value=[25, 75],
            min_=0,
            max=100,
            size="1",
            on_value_commit=RangeSliderState.set_end,
        ),
        width="100%",
    )
```

## Live Updating Slider

You can use the `on_change` prop to update the slider value as you interact with it. The `on_change` prop takes a function that will be called with the new value of the slider.

Here we use the `throttle` method to limit the rate at which the function is called, which is useful to prevent excessive updates. In this example, the slider value is updated every 100ms.

```python demo exec
class LiveSliderState(rx.State):
    value: int = 50

    @rx.event
    def set_end(self, value: list[int]):
        self.value = value[0]

def live_slider_intro():
    return rx.vstack(
        rx.heading(LiveSliderState.value),
        rx.slider(
            default_value=50,
            min_=0,
            max=100,
            on_change=LiveSliderState.set_end.throttle(100),
        ),
        width="100%",
    )
```

## Slider in forms

Here we show how to use a slider in a form. We use the `name` prop to identify the slider in the form data. The form data is then passed to the `handle_submit` method to be processed.

```python demo exec
class FormSliderState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def slider_form_example():
    return rx.card(
            rx.vstack(
                rx.heading("Example Form"),
                rx.form.root(
                    rx.hstack(
                        rx.slider(default_value=40, name="slider"),
                        rx.button("Submit", type="submit"),
                        width="100%",
                    ),
                    on_submit=FormSliderState.handle_submit,
                    reset_on_submit=True,
                ),
                rx.divider(),
                rx.hstack(
                    rx.heading("Results:"),
                    rx.badge(FormSliderState.form_data.to_string()),
                ),
                align_items="left",
                width="100%",
            ),
        width="50%",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/forms/checkbox.md`:

```md
---
components:
  - rx.checkbox

HighLevelCheckbox: |
  lambda **props: rx.checkbox("Basic Checkbox", **props)
---


# Checkbox

## Basic Example

The `on_change` trigger is called when the `checkbox` is clicked.

```python demo exec
class CheckboxState(rx.State):
    checked: bool = False

def checkbox_example():
    return rx.vstack(
        rx.heading(CheckboxState.checked),
        rx.checkbox(on_change=CheckboxState.set_checked),
    )
```

The `input` prop is used to set the `checkbox` as a controlled component.

```python demo exec
class FormCheckboxState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)
        self.form_data = form_data


def form_checkbox_example():
    return rx.card(
        rx.vstack(
            rx.heading("Example Form"),
            rx.form.root(
                rx.hstack(
                    rx.checkbox(
                        name="checkbox",
                        label="Accept terms and conditions",
                    ),
                    rx.button("Submit", type="submit"),
                    width="100%",
                ),
                on_submit=FormCheckboxState.handle_submit,
                reset_on_submit=True,
            ),
            rx.divider(),
            rx.hstack(
                rx.heading("Results:"),
                rx.badge(FormCheckboxState.form_data.to_string()),
            ),
            align_items="left",
            width="100%",
        ),
        width="50%",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/tables-and-data-grids/data_table.md`:

```md
---
components:
    - rx.data_table
---


# Data Table

The data table component is a great way to display static data in a table format.
You can pass in a pandas dataframe to the data prop to create the table.

In this example we will read data from a csv file, convert it to a pandas dataframe and display it in a data_table.

We will also add a search, pagination, sorting to the data_table to make it more accessible.

If you want to [add, edit or remove data]({library.tables_and_data_grids.table.path}) in your app or deal with anything but static data then the [`rx.table`]({library.tables_and_data_grids.table.path}) might be a better fit for your use case.


```python demo box
rx.data_table(
    data=[
        ["Avery Bradley", "6-2", 25.0],
        ["Jae Crowder", "6-6", 25.0],
        ["John Holland", "6-5", 27.0],
        ["R.J. Hunter", "6-5", 22.0],
        ["Jonas Jerebko", "6-10", 29.0],
        ["Amir Johnson", "6-9", 29.0],
        ["Jordan Mickey", "6-8", 21.0],
        ["Kelly Olynyk", "7-0", 25.0],
        ["Terry Rozier", "6-2", 22.0],
        ["Marcus Smart", "6-4", 22.0],
    ],
    columns=["Name", "Height", "Age"],
    pagination=True,
    search=True,
    sort=True,
)
```

```python
import pandas as pd
nba_data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
...
rx.data_table(
    data = nba_data[["Name", "Height", "Age"]],
    pagination= True,
    search= True,
    sort= True,
)  
```

The example below shows how to create a data table from from a list.

```python
class State(rx.State):
    data: List = [
        ["Lionel", "Messi", "PSG"],
        ["Christiano", "Ronaldo", "Al-Nasir"]
     ]
    columns: List[str] = ["First Name", "Last Name"]
    
def index():  
    return rx.data_table(
        data=State.data,
        columns=State.columns,
    )   
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/tables-and-data-grids/data_editor.md`:

```md
---
components:
    - rx.data_editor
---

# Data Editor

A datagrid editor based on [Glide Data Grid](https://grid.glideapps.com/)


This component is introduced as an alternative to the [datatable]({library.tables_and_data_grids.data_table.path}) to support editing the displayed data.

## Columns

The columns definition should be a `list` of `dict`, each `dict` describing the associated columns.
Property of a column dict:

- `title`: The text to display in the header of the column.
- `id`: An id for the column, if not defined, will default to a lower case of `title`
- `width`: The width of the column.
- `type`: The type of the columns, default to `"str"`.

## Data

The `data` props of `rx.data_editor` accept a `list` of `list`, where each `list` represent a row of data to display in the table.

## Simple Example

Here is a basic example of using the data_editor representing data with no interaction and no styling. Below we define the `columns` and the `data` which are taken in by the `rx.data_editor` component. When we define the `columns` we must define a `title` and a `type` for each column we create. The columns in the `data` must then match the defined `type` or errors will be thrown.

```python demo box
rx.data_editor(
    columns=columns,
    data=data,
)
```

```python
columns: list[dict[str, str]] = [
    {
        "title":"Code",
        "type": "str",
    },
    {
        "title":"Value",
        "type": "int",
    }, 
    {
        "title":"Activated",
        "type": "bool",
    },
]
data: list[list[Any]] = [
    ["A", 1, True],
    ["B", 2, False],
    ["C", 3, False],
    ["D", 4, True],
    ["E", 5, True],
    ["F", 6, False],
]
```

```python
rx.data_editor(
    columns=columns,
    data=data,
)
```

## Interactive Example


Here we define a State, as shown below, that allows us to print the location of the cell as a heading when we click on it, using the `on_cell_clicked` `event trigger`. Check out all the other `event triggers` that you can use with datatable at the bottom of this page. We also define a `group` with a label `Data`. This groups all the columns with this `group` label under a larger group `Data` as seen in the table below.

```python demo box
rx.heading(DataEditorState_HP.clicked_data)
```

```python demo box
rx.data_editor(
    columns=DataEditorState_HP.cols,
    data=DataEditorState_HP.data,
    on_cell_clicked=DataEditorState_HP.click_cell,
)
```

```python
class DataEditorState_HP(rx.State):
    
    clicked_data: str = "Cell clicked: "

    cols: list[Any] = [
        {
            "title": "Title", 
            "type": "str"
        },
        {
            "title": "Name",
            "type": "str",
            "group": "Data",
            "width": 300,
        },
        {
            "title": "Birth",
            "type": "str",
            "group": "Data",
            "width": 150,
        },
        {
            "title": "Human",
            "type": "bool",
            "group": "Data",
            "width": 80,
        },
        {
            "title": "House",
            "type": "str",
            "group": "Data",
        },
        {
            "title": "Wand",
            "type": "str",
            "group": "Data",
            "width": 250,
        },
        {
            "title": "Patronus",
            "type": "str",
            "group": "Data",
        },
        {
            "title": "Blood status",
            "type": "str",
            "group": "Data",
            "width": 200,
        }
    ]

    data = [
        ["1", "Harry James Potter", "31 July 1980", True, "Gryffindor", "11'  Holly  phoenix feather", "Stag", "Half-blood"],
        ["2", "Ronald Bilius Weasley", "1 March 1980", True,"Gryffindor", "12' Ash unicorn tail hair", "Jack Russell terrier", "Pure-blood"],
        ["3", "Hermione Jean Granger", "19 September, 1979", True, "Gryffindor", "10¾'  vine wood dragon heartstring", "Otter", "Muggle-born"], 
        ["4", "Albus Percival Wulfric Brian Dumbledore", "Late August 1881", True, "Gryffindor", "15' Elder Thestral tail hair core", "Phoenix", "Half-blood"], 
        ["5", "Rubeus Hagrid", "6 December 1928", False, "Gryffindor", "16'  Oak unknown core", "None", "Part-Human (Half-giant)"], 
        ["6", "Fred Weasley", "1 April, 1978", True, "Gryffindor", "Unknown", "Unknown", "Pure-blood"], 
    ]


    def click_cell(self, pos):
        col, row = pos
        yield self.get_clicked_data(pos)
        

    def get_clicked_data(self, pos) -> str:
        self.clicked_data = f"Cell clicked: \{pos}"
```

```python
rx.data_editor(
    columns=DataEditorState_HP.cols,
    data=DataEditorState_HP.data,
    on_cell_clicked=DataEditorState_HP.click_cell,
)
```

## Styling Example

Now let's style our datatable to make it look more aesthetic and easier to use. We must first import `DataEditorTheme` and then we can start setting our style props as seen below in `dark_theme`.

We then set these themes using `theme=DataEditorTheme(**dark_theme)`. On top of the styling we can also set some `props` to make some other aesthetic changes to our datatable. We have set the `row_height` to equal `50` so that the content is easier to read. We have also made the `smooth_scroll_x` and `smooth_scroll_y` equal `True` so that we can smoothly scroll along the columns and rows. Finally, we added `column_select=single`, where column select can take any of the following values `none`, `single` or `multiple`.


```python demo box
rx.data_editor(
    columns=DataEditorState_HP.cols,
    data=DataEditorState_HP.data,
    row_height=80,
    smooth_scroll_x=True,
    smooth_scroll_y=True,
    column_select="single",
    theme=DataEditorTheme(**dark_theme),
    height="30vh",
)
```

```python
from reflex.components.datadisplay.dataeditor import DataEditorTheme
dark_theme_snake_case = {
    "accent_color": "#8c96ff",
    "accent_light": "rgba(202, 206, 255, 0.253)",
    "text_dark": "#ffffff",
    "text_medium": "#b8b8b8",
    "text_light": "#a0a0a0",
    "text_bubble": "#ffffff",
    "bg_icon_header": "#b8b8b8",
    "fg_icon_header": "#000000",
    "text_header": "#a1a1a1",
    "text_header_selected": "#000000",
    "bg_cell": "#16161b",
    "bg_cell_medium": "#202027",
    "bg_header": "#212121",
    "bg_header_has_focus": "#474747",
    "bg_header_hovered": "#404040",
    "bg_bubble": "#212121",
    "bg_bubble_selected": "#000000",
    "bg_search_result": "#423c24",
    "border_color": "rgba(225,225,225,0.2)",
    "drilldown_border": "rgba(225,225,225,0.4)",
    "link_color": "#4F5DFF",
    "header_font_style": "bold 14px",
    "base_font_style": "13px",
    "font_family": "Inter, Roboto, -apple-system, BlinkMacSystemFont, avenir next, avenir, segoe ui, helvetica neue, helvetica, Ubuntu, noto, arial, sans-serif",
}
```

```python
rx.data_editor(
    columns=DataEditorState_HP.cols,
    data=DataEditorState_HP.data,
    row_height=80,
    smooth_scroll_x=True,
    smooth_scroll_y=True,
    column_select="single",
    theme=DataEditorTheme(**dark_theme),
    height="30vh",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/tables-and-data-grids/ag_grid.md`:

```md
---
components:
  - ag_grid
---


# AG Grid

Reflex AG Grid is a high-performance and highly customizable grid that wraps AG Grid.

```bash
pip install reflex-ag-grid
```

## Your First Reflex AG Grid

A basic Reflex AG Grid contains column definitions `column_defs`, which define the columns to be displayed in the grid, and `row_data`, which contains the data to be displayed in the grid.

Each grid also requires a unique `id`, which is needed to uniquely identify the Ag-Grid instance on the page. If you have multiple grids on the same page, each grid must have a unique `id` so that it can be correctly rendered and managed.

```md alert info
# Grid for Layout

If you are looking for a grid for layout purposes, i.e. to layout Reflex components, consider using the [Grid component]({library.layout.grid.path}).
```

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/wind_dataset.csv")

column_defs = [
    ag_grid.column_def(field="direction"),
    ag_grid.column_def(field="strength"),
    ag_grid.column_def(field="frequency"),

]

def ag_grid_simple():
    return ag_grid(
        id="ag_grid_basic_1",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        width="100%",
    )
```

The format of the data passed to the `row_data` prop is a list of dictionaries. Each dictionary represents a row in the grid as seen below.

```python
[
   \{direction: "N", strength: "0-1", frequency: 0.5},
   \{direction: "NNE", strength: "0-1", frequency: 0.6},
   \{direction: "NE", strength: "0-1", frequency: 0.5},
]
```

The previous example showed the `column_defs` written out in full. You can also extract the required information from the dataframe's column names:

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/wind_dataset.csv")


def ag_grid_simple_2():
    return ag_grid(
        id="ag_grid_basic_2",
        row_data=df.to_dict("records"),
        column_defs=[{"field": i} for i in df.columns],
        width="100%",
        height="40vh",
    )
```

## Headers

In the above example, the first letter of the field names provided are capitalized when displaying the header name. You can customize the header names by providing a `header_name` key in the column definition. In this example, the `header_name` is customized for the second and third columns.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="lifeExp", header_name="Life Expectancy"),
]

def ag_grid_simple_headers():
    return ag_grid(
            id="ag_grid_basic_headers",
            row_data=df.to_dict("records"),
            column_defs=column_defs,
            width="100%",
            height="40vh",
        )
```

## Column Filtering

Allow a user to filter a column by setting the `filter` key to `True` in the column definition. In this example we enable filtering for the first and last columns.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs =  [
    ag_grid.column_def(field="country", header_name="Country", filter=True),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="lifeExp", header_name="Life Expectancy", filter=True),
]

def ag_grid_simple_column_filtering():
    return ag_grid(
        id="ag_grid_basic_column_filtering",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        width="100%",
        height="40vh",
    )
```

### Filter Types

You can set `filter=True` to enable the default filter for a column.

You can also set the filter type using the `filter` key. The following filter types are available: `ag_grid.filters.date`, `ag_grid.filters.number` and `ag_grid.filters.text`. These ensure that the input you enter to the filter is of the correct type.

(`ag_grid.filters.set` and `ag_grid.filters.multi` are available with AG Grid Enterprise)

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/GanttChart-updated.csv")

column_defs =  [
    ag_grid.column_def(field="Task", filter=True),
    ag_grid.column_def(field="Start", filter=ag_grid.filters.date),
    ag_grid.column_def(field="Duration", filter=ag_grid.filters.number),
    ag_grid.column_def(field="Resource", filter=ag_grid.filters.text),
]

def ag_grid_simple_column_filtering():
    return ag_grid(
        id="ag_grid_basic_column_filtering",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        width="100%",
        height="40vh",
    )
```

## Row Sorting

By default, the rows can be sorted by any column by clicking on the column header. You can disable sorting of the rows for a column by setting the `sortable` key to `False` in the column definition.

In this example, we disable sorting for the first column.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs =  [
    ag_grid.column_def(field="country", sortable=False),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="lifeExp", header_name="Life Expectancy"),
]

def ag_grid_simple_row_sorting():
    return ag_grid(
        id="ag_grid_basic_row_sorting",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        width="100%",
        height="40vh",
    )
```

## Row Selection

Row Selection is enabled using the `row_selection` attribute. Setting it to `multiple` allows users to select multiple rows at a time. You can use the `checkbox_selection` column definition attribute to render checkboxes for selection.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs = [
    ag_grid.column_def(field="country", checkbox_selection=True),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="continent"),
]

def ag_grid_simple_row_selection():
    return ag_grid(
        id="ag_grid_basic_row_selection",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        row_selection="multiple",
        width="100%",
        height="40vh",
    )
```

## Editing

Enable Editing by setting the `editable` attribute to `True`. The cell editor is inferred from the cell data type. Set the cell editor type using the `cell_editor` attribute.

There are 7 provided cell editors in AG Grid:

1. `ag_grid.editors.text`
2. `ag_grid.editors.large_text`
3. `ag_grid.editors.select`
4. `ag_grid.editors.rich_select`
5. `ag_grid.editors.number`
6. `ag_grid.editors.date`
7. `ag_grid.editors.checkbox`

In this example, we enable editing for the second and third columns. The second column uses the `number` cell editor, and the third column uses the `select` cell editor.

The `on_cell_value_changed` event trigger is linked to the `cell_value_changed` event handler in the state. This event handler is called whenever a cell value is changed and changes the value of the backend var `_data_df` and the state var `data`.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

class AGGridEditingState(rx.State):
    data: list[dict] = []

    @rx.event
    def load_data(self):
        _df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")
        self.data = _df.to_dict("records")

    @rx.event
    def cell_value_changed(self, row, col_field, new_value):
        self._data_df.at[row, col_field] = new_value
        self.data = self._data_df.to_dict("records")
        yield rx.toast(f"Cell value changed, Row: {row}, Column: {col_field}, New Value: {new_value}")


column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(field="pop", header_name="Population", editable=True, cell_editor=ag_grid.editors.number),
    ag_grid.column_def(field="continent", editable=True, cell_editor=ag_grid.editors.select, cell_editor_params={
        "values": ['Asia', 'Europe', 'Africa', 'Americas', 'Oceania']
        }
    ),
]

def ag_grid_simple_editing():
    return ag_grid(
        id="ag_grid_basic_editing",
        row_data=AGGridEditingState.data,
        column_defs=column_defs,
        on_cell_value_changed=AGGridEditingState.cell_value_changed,
        on_mount=AGGridEditingState.load_data,
        width="100%",
        height="40vh",
    )
```

## Pagination

By default, the grid uses a vertical scroll. You can reduce the amount of scrolling required by adding pagination. To add pagination, set `pagination=True`. You can set the `pagination_page_size` to the number of rows per page and `pagination_page_size_selector` to a list of options for the user to select from.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="lifeExp", header_name="Life Expectancy"),
]

def ag_grid_simple_pagination():
    return ag_grid(
        id="ag_grid_basic_pagination",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        pagination=True,
        pagination_page_size=10,
        pagination_page_size_selector=[10, 40, 100],
        width="100%",
        height="40vh",
    )
```

## Themes

You can style your grid with a theme. AG Grid includes the following themes:

1. `quartz`
2. `alpine`
3. `balham`
4. `material`

The grid uses `quartz` by default. To use any other theme, set it using the `theme` prop, i.e. `theme="alpine"`.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

class AGGridThemeState(rx.State):
    """The app state."""

    theme: str = "quartz"
    themes: list[str] = ["quartz", "balham", "alpine", "material"]

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="lifeExp", header_name="Life Expectancy"),
]

def ag_grid_simple_themes():
    return rx.vstack(
        rx.hstack(
            rx.text("Theme:"),
            rx.select(AGGridThemeState.themes, value=AGGridThemeState.theme, on_change=AGGridThemeState.set_theme),
        ),
        ag_grid(
            id="ag_grid_basic_themes",
            row_data=df.to_dict("records"),
            column_defs=column_defs,
            theme=AGGridThemeState.theme,
            width="100%",
            height="40vh",
        ),
        width="100%",
    )
```

## AG Grid with State

### Putting Data in State

Assuming you want to make any edit to your data, you can put the data in State. This allows you to update the grid based on user input. Whenever the `data` var is updated, the grid will be re-rendered with the new data.

```python demo exec
from typing import Any
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

class AGGridState2(rx.State):
    data: list[dict] = []

    @rx.event
    def load_data(self):
        _df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")
        self.data = _df.to_dict("records")

column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="continent"),
]

def ag_grid_state_2():
    return ag_grid(
        id="ag_grid_state_2",
        row_data=AGGridState2.data,
        column_defs=column_defs,
        on_mount=AGGridState2.load_data,
        width="100%",
        height="40vh",
    )
```

### Updating the Grid with State

You can use State to update the grid based on a users input. In this example, we update the `column_defs` of the grid when a user clicks a button.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

class AgGridState(rx.State):
    """The app state."""
    all_columns: list = []

    two_columns: list = []
    column_defs: list = all_columns
    n_clicks = 0

    @rx.event
    def init_columns(self):
        self.all_columns = [
            ag_grid.column_def(field="country"),
            ag_grid.column_def(field="pop"),
            ag_grid.column_def(field="continent"),
            ag_grid.column_def(field="lifeExp"),
            ag_grid.column_def(field="gdpPercap"),
        ]
        self.two_columns = [
            ag_grid.column_def(field="country"),
            ag_grid.column_def(field="pop"),
        ]
        self.column_defs = self.all_columns

    @rx.event
    def update_columns(self):
        self.n_clicks += 1
        if self.n_clicks % 2 != 0:
            self.column_defs = self.two_columns
        else:
            self.column_defs = self.all_columns


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")


def ag_grid_simple_with_state():
    return rx.box(
        rx.button("Toggle Columns", on_click=AgGridState.update_columns),
        ag_grid(
            id="ag_grid_basic_with_state",
            row_data=df.to_dict("records"),
            column_defs=AgGridState.column_defs,
            on_mount=AgGridState.init_columns,
            width="100%",
            height="40vh",
        ),
        width="100%",
    )
```

## AG Grid with Data from a Database

In this example, we will use a database to store the data. The data is loaded from a csv file and inserted into the database when the page is loaded using the `insert_dataframe_to_db` event handler.

The data is then fetched from the database and displayed in the grid using the `data` [computed var]({vars.computed_vars.path}).

When a cell value is changed, the data is updated in the database using the `cell_value_changed` event handler.

```python
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd
from sqlmodel import select

class Country(rx.Model, table=True):
    country: str
    population: int
    continent: str


class AGGridDatabaseState(rx.State):

    countries: list[Country]

    # Insert data from a csv loaded dataframe to the database (Do this on the page load)
    @rx.event
    def insert_dataframe_to_db(self):
        data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")
        with rx.session() as session:
            for _, row in data.iterrows():
                db_record = Country(
                    country=row['country'],
                    population=row['pop'],
                    continent=row['continent'],
                )
                session.add(db_record)
            session.commit()

    # Fetch data from the database using a computed variable
    @rx.var
    def data(self) -> list[dict]:
        with rx.session() as session:
            results = session.exec(select(Country)).all()
            self.countries = [result.dict() for result in results]
        return self.countries

    # Update the database when a cell value is changed
    @rx.event
    def cell_value_changed(self, row, col_field, new_value):
        self.countries[row][col_field] = new_value
        with rx.session() as session:
            country = Country(**self.countries[row])
            session.merge(country)
            session.commit()
        yield rx.toast(f"Cell value changed, Row: \{row}, Column: \{col_field}, New Value: \{new_value}")


column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(field="population", header_name="Population", editable=True, cell_editor=ag_grid.editors.number),
    ag_grid.column_def(field="continent", editable=True, cell_editor=ag_grid.editors.select, cell_editor_params={
        "values": ['Asia', 'Europe', 'Africa', 'Americas', 'Oceania']
        }
    ),
]

def index():
    return ag_grid(
        id="ag_grid_basic_editing",
        row_data=AGGridDatabaseState.data,
        column_defs=column_defs,
        on_cell_value_changed=AGGridDatabaseState.cell_value_changed,
        width="100%",
        height="40vh",
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index, on_load=AGGridDatabaseState.insert_dataframe_to_db)
```

## Using AG Grid Enterprise

AG Grid offers both community and enterprise versions. See the [AG Grid docs](https://www.ag-grid.com/archive/31.2.0/react-data-grid/licensing/) for details on purchasing a license key.

To use an AG Grid Enterprise license key with Reflex AG Grid set the environment variable `AG_GRID_LICENSE_KEY`:

```bash
export AG_GRID_LICENSE_KEY="your_license_key"
```

## column_def props

The following props are available for `column_defs` as well as many others that can be found here: [AG Grid Column Def Docs](https://www.ag-grid.com/react-data-grid/column-properties/). (it is necessary to use snake_case for the keys in Reflex, unlike in the AG Grid docs where camelCase is used)

- `field`: `str`: The field of the row object to get the cell's data from.
- `col_id`: `str | None`: The unique ID to give the column. This is optional. If missing, the ID will default to the field.
- `type`: `str | None`: The type of the column.
- `cell_data_type`: `bool | str | None`: The data type of the cell values for this column. Can either infer the data type from the row data (true - the default behaviour), define a specific data type (string), or have no data type (false).
- `hide`: `bool`: Set to true for this column to be hidden.
- `editable`: `bool | None`: Set to true if this column is editable, otherwise false.
- `filter`: `AGFilters | str | None`: Filter component to use for this column. Set to true to use the default filter. Set to the name of a provided filter to use that filter. (Check out the Filter Types section of this page for more information)
- `floating_filter`: `bool`: Whether to display a floating filter for this column.
- `header_name`: `str | None`: The name to render in the column header. If not specified and field is specified, the field name will be used as the header name.
- `header_tooltip`: `str | None`: Tooltip for the column header.
- `checkbox_selection`: `bool | None`: Set to true to render a checkbox for row selection.
- `cell_editor`: `AGEditors | str | None`: Provide your own cell editor component for this column's cells. (Check out the Editing section of this page for more information)
- `cell_editor_params`: `dict[str, list[Any]] | None`: Params to be passed to the cellEditor component.



## Functionality you need is not available in Reflex

Since Reflex AG Grid is wrapping the underlying AG Grid library, there is much more functionality available that is currently not exposed in Reflex. Check out this [documentation](https://www.ag-grid.com/react-data-grid/reference/) for more information on what is available in AG Grid.

As Reflex does not expose all the functionality of AG Grid, you can use `ag_grid.api()`, which is hanging off the `ag_grid` namespace, to access the underlying AG Grid API. This allows you to access the full functionality of AG Grid.

Best practice is to create a single instance of `ag_grid.api()` with the same `id` as the `id` of the `ag_grid` component that is to be referenced, `"ag_grid_basic_row_selection"` in this first example.

The example below uses the `select_all()` and `deselect_all()` methods of the AG Grid API to select and deselect all rows in the grid. This method is not available in Reflex directly. Check out this [documentation](https://www.ag-grid.com/react-data-grid/grid-api/#reference-selection-selectAll) to see what the methods look like in the AG Grid docs.

```md alert info
# Ensure that the docs are set to React tab in AG Grid
```

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

column_defs = [
    ag_grid.column_def(field="country", checkbox_selection=True),
    ag_grid.column_def(field="pop"),
    ag_grid.column_def(field="continent"),
]

def ag_grid_api_simple():
    my_api = ag_grid.api(id="ag_grid_basic_row_selection")
    return rx.vstack(
            ag_grid(
            id="ag_grid_basic_row_selection",
            row_data=df.to_dict("records"),
            column_defs=column_defs,
            width="100%",
            height="40vh",
        ),
        rx.button("Select All", on_click=my_api.select_all()),
        rx.button("Deselect All", on_click=my_api.deselect_all()),
        spacing="4",
        width="100%",
    )
```


The react code for the `select_all()` event handler is `selectAll = (source?: SelectionEventSourceType) => void;`. 

To use this in Reflex as you can see, it should be called in snake case rather than camel case. The `void` means it doesn't return anything. The `source?` indicates that it takes an optional `source` argument.



```md alert info
# Another way to use the AG Grid API
It is also possible to use the AG Grid API directly with the event trigger (`on_click`) of the component. This removes the need to create a variable `my_api`. This is shown in the example below. It is necessary to use the `id` of the `ag_grid` component that is to be referenced.
```python
rx.button("Select all", on_click=ag_grid.api(id="ag_grid_basic_row_selection").select_all()),
```


### More examples

The following example lets a user [export the data as a csv](https://www.ag-grid.com/javascript-data-grid/grid-api/#reference-export-exportDataAsCsv) and [adjust the size of columns to fit the available horizontal space](https://www.ag-grid.com/javascript-data-grid/grid-api/#reference-columnSizing-sizeColumnsToFit). (Try resizing the screen and then clicking the resize columns button)


```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

column_defs = [
    ag_grid.column_def(field="country", checkbox_selection=True),
    ag_grid.column_def(field="pop"),
    ag_grid.column_def(field="continent"),
]

def ag_grid_api_simple2():
    my_api = ag_grid.api(id="ag_grid_export_and_resize")
    return rx.vstack(
            ag_grid(
            id="ag_grid_export_and_resize",
            row_data=df.to_dict("records"),
            column_defs=column_defs,
            width="100%",
            height="40vh",
        ),
        rx.button("Export", on_click=my_api.export_data_as_csv()),
        rx.button("Resize Columns", on_click=my_api.size_columns_to_fit()),
        spacing="4",
        width="100%",
    )
```

The react code for both of these is shown below. The key point to see is that both of these functions return `void` and therefore does not return anything.

`exportDataAsCsv = (params?: CsvExportParams) => void;`

`sizeColumnsToFit = (paramsOrGridWidth?: ISizeColumnsToFitParams  |  number) => void;`


### Example with a Return Value

This example shows how to get the data from `ag_grid` as a [csv on the backend](https://www.ag-grid.com/javascript-data-grid/grid-api/#reference-export-getDataAsCsv). The data that was passed to the backend is then displayed as a toast with the data.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

class AGGridStateAPI(rx.State):
    def handle_get_data(self, data: str):
        yield rx.toast(f"Got CSV data: {data}")

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

column_defs = [
    ag_grid.column_def(field="country", checkbox_selection=True),
    ag_grid.column_def(field="pop"),
    ag_grid.column_def(field="continent"),
]

def ag_grid_api_argument():
    my_api = ag_grid.api(id="ag_grid_get_data_as_csv")
    return rx.vstack(
            ag_grid(
            id="ag_grid_get_data_as_csv",
            row_data=df.to_dict("records"),
            column_defs=column_defs,
            width="100%",
            height="40vh",
        ),
        rx.button("Get CSV data on backend", on_click=my_api.get_data_as_csv(callback=AGGridStateAPI.handle_get_data)),
        spacing="4",
        width="100%",
    )
```

The react code for the `get_data_as_csv` method of the AG Grid API is `getDataAsCsv = (params?: CsvExportParams) => string  |  undefined;`. Here the function returns a `string` (or undefined). 

In Reflex to handle this returned value it is necessary to pass a `callback` as an argument to the `get_data_as_csv` method that will get the returned value. In this example the `handle_get_data` event handler is passed as the callback. This event handler will be called with the returned value from the `get_data_as_csv` method. 

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/tables-and-data-grids/table.md`:

```md
---
components:
  - rx.table.root
  - rx.table.header
  - rx.table.row
  - rx.table.column_header_cell
  - rx.table.body
  - rx.table.cell
  - rx.table.row_header_cell

only_low_level:
  - True

TableRoot: |
  lambda **props: rx.table.root(
          rx.table.header(
              rx.table.row(
                  rx.table.column_header_cell("Full Name"),
                  rx.table.column_header_cell("Email"),
                  rx.table.column_header_cell("Group"),
              ),
          ),
          rx.table.body(
              rx.table.row(
                  rx.table.row_header_cell("Danilo Rosa"),
                  rx.table.cell("danilo@example.com"),
                  rx.table.cell("Developer"),
              ),
              rx.table.row(
                  rx.table.row_header_cell("Zahra Ambessa"),
                  rx.table.cell("zahra@example.com"),
                  rx.table.cell("Admin"),
              ),
          ),
          width="80%",
          **props,
      )

TableRow: |
  lambda **props: rx.table.root(
          rx.table.header(
              rx.table.row(
                  rx.table.column_header_cell("Full Name"),
                  rx.table.column_header_cell("Email"),
                  rx.table.column_header_cell("Group"),
                  **props,
              ),
          ),
          rx.table.body(
              rx.table.row(
                  rx.table.row_header_cell("Danilo Rosa"),
                  rx.table.cell(rx.text("danilo@example.com", as_="p"), rx.text("danilo@yahoo.com", as_="p"), rx.text("danilo@gmail.com", as_="p"),),
                  rx.table.cell("Developer"),
                  **props,
              ),
              rx.table.row(
                  rx.table.row_header_cell("Zahra Ambessa"),
                  rx.table.cell("zahra@example.com"),
                  rx.table.cell("Admin"),
                  **props,
              ),
          ),
          width="80%",
      )

TableColumnHeaderCell: |
  lambda **props: rx.table.root(
          rx.table.header(
              rx.table.row(
                  rx.table.column_header_cell("Full Name", **props,),
                  rx.table.column_header_cell("Email", **props,),
                  rx.table.column_header_cell("Group", **props,),
              ),
          ),
          rx.table.body(
              rx.table.row(
                  rx.table.row_header_cell("Danilo Rosa"),
                  rx.table.cell("danilo@example.com"),
                  rx.table.cell("Developer"),
              ),
              rx.table.row(
                  rx.table.row_header_cell("Zahra Ambessa"),
                  rx.table.cell("zahra@example.com"),
                  rx.table.cell("Admin"),
              ),
          ),
          width="80%",
      )

TableCell: |
  lambda **props: rx.table.root(
          rx.table.header(
              rx.table.row(
                  rx.table.column_header_cell("Full Name"),
                  rx.table.column_header_cell("Email"),
                  rx.table.column_header_cell("Group"),
              ),
          ),
          rx.table.body(
              rx.table.row(
                  rx.table.row_header_cell("Danilo Rosa"),
                  rx.table.cell("danilo@example.com", **props,),
                  rx.table.cell("Developer", **props,),
              ),
              rx.table.row(
                  rx.table.row_header_cell("Zahra Ambessa"),
                  rx.table.cell("zahra@example.com", **props,),
                  rx.table.cell("Admin", **props,),
              ),
          ),
          width="80%",
      )

TableRowHeaderCell: |
  lambda **props: rx.table.root(
          rx.table.header(
              rx.table.row(
                  rx.table.column_header_cell("Full Name"),
                  rx.table.column_header_cell("Email"),
                  rx.table.column_header_cell("Group"),
              ),
          ),
          rx.table.body(
              rx.table.row(
                  rx.table.row_header_cell("Danilo Rosa", **props,),
                  rx.table.cell("danilo@example.com"),
                  rx.table.cell("Developer"),
              ),
              rx.table.row(
                  rx.table.row_header_cell("Zahra Ambessa", **props,),
                  rx.table.cell("zahra@example.com"),
                  rx.table.cell("Admin"),
              ),
          ),
          width="80%",
      )
---


# Table

A semantic table for presenting tabular data.

If you just want to [represent static data]({library.tables_and_data_grids.data_table.path}) then the [`rx.data_table`]({library.tables_and_data_grids.data_table.path}) might be a better fit for your use case as it comes with in-built pagination, search and sorting.

## Basic Example

```python demo
rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Full name"),
            rx.table.column_header_cell("Email"),
            rx.table.column_header_cell("Group"),
        ),
    ),
    rx.table.body(
        rx.table.row(
            rx.table.row_header_cell("Danilo Sousa"),
            rx.table.cell("danilo@example.com"),
            rx.table.cell("Developer"),
        ),
        rx.table.row(
            rx.table.row_header_cell("Zahra Ambessa"),
            rx.table.cell("zahra@example.com"),
            rx.table.cell("Admin"),
        ),rx.table.row(
            rx.table.row_header_cell("Jasper Eriks"),
            rx.table.cell("jasper@example.com"),
            rx.table.cell("Developer"),
        ),
    ),
    width="100%",
)
```

```md alert info
# Set the table `width` to fit within its container and prevent it from overflowing.
```

## Showing State data (using foreach)

Many times there is a need for the data we represent in our table to be dynamic. Dynamic data must be in `State`. Later we will show an example of how to access data from a database and how to load data from a source file.

In this example there is a `people` data structure in `State` that is [iterated through using `rx.foreach`]({components.rendering_iterables.path}).

```python demo exec
class TableForEachState(rx.State):
    people: list[list] = [
        ["Danilo Sousa", "danilo@example.com", "Developer"],
        ["Zahra Ambessa", "zahra@example.com", "Admin"],
        ["Jasper Eriks", "jasper@example.com", "Developer"],
    ]

def show_person(person: list):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(person[0]),
        rx.table.cell(person[1]),
        rx.table.cell(person[2]),
    )

def foreach_table_example():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Full name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Group"),
            ),
        ),
        rx.table.body(rx.foreach(TableForEachState.people, show_person)),
        width="100%",
    )
```

It is also possible to define a `class` such as `Person` below and then iterate through this data structure, as a `list[Person]`.

```python
import dataclasses

@dataclasses.dataclass
class Person:
    full_name: str
    email: str
    group: str
```

## Sorting and Filtering (Searching)

In this example we sort and filter the data.

The state variable `_people` is set to be a [backend-only variable]({vars.base_vars.path}). This is done in case the variable is very large in order to reduce network traffic and improve performance.

For sorting the `rx.select` component is used. The data is sorted based on the attributes of the `Person` class. When a `select` item is selected, as the `on_change` event trigger is hooked up to the `set_sort_value` event handler, the data is sorted based on the state variable `sort_value` attribute selected. (Every base var has a [built-in event handler to set]({events.setters.path}) it's value for convenience, called `set_VARNAME`.)

For filtering the `rx.input` component is used. The data is filtered based on the search query entered into the `rx.input` component. When a search query is entered, as the `on_change` event trigger is hooked up to the `set_search_value` event handler, the data is filtered based on if the state variable `search_value` is present in any of the data in that specific `Person`.

`current_people` is an [`rx.var(cache=True)`]({vars.computed_vars.path}). It is a var that is only recomputed when the other state vars it depends on change. This is to ensure that the `People` shown in the table are always up to date whenever they are searched or sorted.

```python demo exec
import dataclasses

@dataclasses.dataclass
class Person:
    full_name: str
    email: str
    group: str


class TableSortingState(rx.State):

    _people: list[Person] = [
        Person(full_name="Danilo Sousa", email="danilo@example.com", group="Developer"),
        Person(full_name="Zahra Ambessa", email="zahra@example.com", group="Admin"),
        Person(full_name="Jasper Eriks", email="zjasper@example.com", group="B-Developer"),
    ]

    sort_value = ""
    search_value = ""

    @rx.var(cache=True)
    def current_people(self) -> list[Person]:
        people = self._people

        if self.sort_value != "":
            people = sorted(
                people, key=lambda user: getattr(user, self.sort_value).lower()
            )

        if self.search_value != "":
            people = [
                person for person in people
                if any(
                    self.search_value in getattr(person, attr).lower()
                    for attr in ['full_name', 'email', 'group']
                )
            ]
        return people


def show_person(person: list):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(person.full_name),
        rx.table.cell(person.email),
        rx.table.cell(person.group),
    )

def sorting_table_example():
    return rx.vstack(
        rx.select(
            ["full_name", "email", "group"],
            placeholder="Sort By: full_name",
            on_change=TableSortingState.set_sort_value,
        ),
        rx.input(
            placeholder="Search here...",
            on_change=TableSortingState.set_search_value,
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Full name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Group"),
                ),
            ),
            rx.table.body(rx.foreach(TableSortingState.current_people, show_person)),
            width="100%",
        ),
        width="100%",
    )
```

# Database

The more common use case for building an `rx.table` is to use data from a database.

The code below shows how to load data from a database and place it in an `rx.table`.

## Loading data into table

A `Customer` [model]({database.tables.path}) is defined that inherits from `rx.Model`.

The `load_entries` event handler executes a [query]({database.queries.path}) that is used to request information from a database table. This `load_entries` event handler is called on the `on_mount` event trigger of the `rx.table.root`.

If you want to load the data when the page in the app loads you can set `on_load` in `app.add_page()` to equal this event handler, like `app.add_page(page_name, on_load=State.load_entries)`.

```python
class Customer(rx.Model, table=True):
    """The customer model."""

    name: str
    email: str
    phone: str
    address: str
```

```python demo exec
from sqlmodel import select

class DatabaseTableState(rx.State):

    users: list[Customer] = []

    @rx.event
    def load_entries(self) -> list[Customer]:
        """Get all users from the database."""
        with rx.session() as session:
            self.users = session.exec(select(Customer)).all()


def show_customer(user: Customer):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.phone),
        rx.table.cell(user.address),
    )

def loading_data_table_example():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Phone"),
                rx.table.column_header_cell("Address"),
            ),
        ),
        rx.table.body(rx.foreach(DatabaseTableState.users, show_customer)),
        on_mount=DatabaseTableState.load_entries,
        width="100%",
    )

```

## Filtering (Searching) and Sorting

In this example we sort and filter the data.

For sorting the `rx.select` component is used. The data is sorted based on the attributes of the `Customer` class. When a select item is selected, as the `on_change` event trigger is hooked up to the `sort_values` event handler, the data is sorted based on the state variable `sort_value` attribute selected.

The sorting query gets the `sort_column` based on the state variable `sort_value`, it gets the order using the `asc` function from sql and finally uses the `order_by` function.

For filtering the `rx.input` component is used. The data is filtered based on the search query entered into the `rx.input` component. When a search query is entered, as the `on_change` event trigger is hooked up to the `filter_values` event handler, the data is filtered based on if the state variable `search_value` is present in any of the data in that specific `Customer`.

The `%` character before and after `search_value` makes it a wildcard pattern that matches any sequence of characters before or after the `search_value`. `query.where(...)` modifies the existing query to include a filtering condition. The `or_` operator is a logical OR operator that combines multiple conditions. The query will return results that match any of these conditions. `Customer.name.ilike(search_value)` checks if the `name` column of the `Customer` table matches the `search_value` pattern in a case-insensitive manner (`ilike` stands for "case-insensitive like").

```python
class Customer(rx.Model, table=True):
    """The customer model."""

    name: str
    email: str
    phone: str
    address: str
```

```python demo exec
from sqlmodel import select, asc, or_


class DatabaseTableState2(rx.State):

    users: list[Customer] = []

    sort_value = ""
    search_value = ""

    @rx.event
    def load_entries(self) -> list[Customer]:
        """Get all users from the database."""
        with rx.session() as session:
            query = select(Customer)

            if self.search_value != "":
                search_value = f"%{self.search_value.lower()}%"
                query = query.where(
                    or_(
                        Customer.name.ilike(search_value),
                        Customer.email.ilike(search_value),
                        Customer.phone.ilike(search_value),
                        Customer.address.ilike(search_value),
                    )
                )

            if self.sort_value != "":
                sort_column = getattr(Customer, self.sort_value)
                order = asc(sort_column)
                query = query.order_by(order)

            self.users = session.exec(query).all()

    @rx.event
    def sort_values(self, sort_value):
        self.sort_value = sort_value
        self.load_entries()

    @rx.event
    def filter_values(self, search_value):
        self.search_value = search_value
        self.load_entries()


def show_customer(user: Customer):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.phone),
        rx.table.cell(user.address),
    )


def loading_data_table_example2():
    return rx.vstack(
        rx.select(
            ["name", "email", "phone", "address"],
            placeholder="Sort By: Name",
            on_change= lambda value: DatabaseTableState2.sort_values(value),
        ),
        rx.input(
            placeholder="Search here...",
            on_change= lambda value: DatabaseTableState2.filter_values(value),
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Phone"),
                    rx.table.column_header_cell("Address"),
                ),
            ),
            rx.table.body(rx.foreach(DatabaseTableState2.users, show_customer)),
            on_mount=DatabaseTableState2.load_entries,
            width="100%",
        ),
        width="100%",
    )

```

## Pagination

Pagination is an important part of database management, especially when working with large datasets. It helps in enabling efficient data retrieval by breaking down results into manageable loads.

The purpose of this code is to retrieve a specific subset of rows from the `Customer` table based on the specified pagination parameters `offset` and `limit`.

`query.offset(self.offset)` modifies the query to skip a certain number of rows before returning the results. The number of rows to skip is specified by `self.offset`.

`query.limit(self.limit)` modifies the query to limit the number of rows returned. The maximum number of rows to return is specified by `self.limit`.

```python demo exec
from sqlmodel import select, func


class DatabaseTableState3(rx.State):

    users: list[Customer] = []

    total_items: int
    offset: int = 0
    limit: int = 3

    @rx.var(cache=True)
    def page_number(self) -> int:
        return (
            (self.offset // self.limit)
            + 1
            + (1 if self.offset % self.limit else 0)
        )

    @rx.var(cache=True)
    def total_pages(self) -> int:
        return self.total_items // self.limit + (
            1 if self.total_items % self.limit else 0
        )

    @rx.event
    def prev_page(self):
        self.offset = max(self.offset - self.limit, 0)
        self.load_entries()

    @rx.event
    def next_page(self):
        if self.offset + self.limit < self.total_items:
            self.offset += self.limit
        self.load_entries()

    def _get_total_items(self, session):
        """Return the total number of items in the Customer table."""
        self.total_items = session.exec(select(func.count(Customer.id))).one()

    @rx.event
    def load_entries(self) -> list[Customer]:
        """Get all users from the database."""
        with rx.session() as session:
            query = select(Customer)

            # Apply pagination
            query = query.offset(self.offset).limit(self.limit)

            self.users = session.exec(query).all()
            self._get_total_items(session)


def show_customer(user: Customer):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.phone),
        rx.table.cell(user.address),
    )


def loading_data_table_example3():
    return rx.vstack(
        rx.hstack(
            rx.button(
                "Prev",
                on_click=DatabaseTableState3.prev_page,
            ),
            rx.text(
                f"Page {DatabaseTableState3.page_number} / {DatabaseTableState3.total_pages}"
            ),
            rx.button(
                "Next",
                on_click=DatabaseTableState3.next_page,
            ),
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Phone"),
                    rx.table.column_header_cell("Address"),
                ),
            ),
            rx.table.body(rx.foreach(DatabaseTableState3.users, show_customer)),
            on_mount=DatabaseTableState3.load_entries,
            width="100%",
        ),
        width="100%",
    )

```

## More advanced examples

The real power of the `rx.table` comes where you are able to visualise, add and edit data live in your app. Check out these apps and code to see how this is done: app: https://customer-data-app.reflex.run code: https://github.com/reflex-dev/reflex-examples/tree/main/customer_data_app and code: https://github.com/reflex-dev/data-viewer.

# Download

Most users will want to download their data after they have got the subset that they would like in their table.

In this example there are buttons to download the data as a `json` and as a `csv`.

For the `json` download the `rx.download` is in the frontend code attached to the `on_click` event trigger for the button. This works because if the `Var` is not already a string, it will be converted to a string using `JSON.stringify`.

For the `csv` download the `rx.download` is in the backend code as an event_handler `download_csv_data`. There is also a helper function `_convert_to_csv` that converts the data in `self.users` to `csv` format.

```python demo exec
import io
import csv
from sqlmodel import select

class TableDownloadState(rx.State):

    users: list[Customer] = []

    @rx.event
    def load_entries(self) -> list[Customer]:
        """Get all users from the database."""
        with rx.session() as session:
            self.users = session.exec(select(Customer)).all()


    def _convert_to_csv(self) -> str:
        """Convert the users data to CSV format."""

        # Make sure to load the entries first
        if not self.users:
            self.load_entries()

        # Define the CSV file header based on the Customer model's attributes
        fieldnames = list(Customer.__fields__)

        # Create a string buffer to hold the CSV data
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        for user in self.users:
            writer.writerow(user.dict())

        # Get the CSV data as a string
        csv_data = output.getvalue()
        output.close()
        return csv_data

    @rx.event
    def download_csv_data(self):
        csv_data = self._convert_to_csv()
        return rx.download(
            data=csv_data,
            filename="data.csv",
        )


def show_customer(user: Customer):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.phone),
        rx.table.cell(user.address),
    )

def download_data_table_example():
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Phone"),
                    rx.table.column_header_cell("Address"),
                ),
            ),
            rx.table.body(rx.foreach(TableDownloadState.users, show_customer)),
            width="100%",
            on_mount=TableDownloadState.load_entries,
        ),
        rx.hstack(
            rx.button(
                "Download as JSON",
                on_click=rx.download(
                    data=TableDownloadState.users,
                    filename="data.json",
                ),
            ),
            rx.button(
                "Download as CSV",
                on_click=TableDownloadState.download_csv_data,
            ),
            spacing="7",
        ),
        width="100%",
        spacing="5",
    )

```

# Real World Example UI

```python demo
rx.flex(
    rx.heading("Your Team"),
    rx.text("Invite and manage your team members"),
    rx.flex(
        rx.input(placeholder="Email Address"),
        rx.button("Invite"),
        justify="center",
        spacing="2",
    ),
    rx.table.root(
        rx.table.body(
            rx.table.row(
                rx.table.cell(rx.avatar(fallback="DS")),
                rx.table.row_header_cell(rx.link("Danilo Sousa")),
                rx.table.cell("danilo@example.com"),
                rx.table.cell("Developer"),
                align="center",
            ),
            rx.table.row(
                rx.table.cell(rx.avatar(fallback="ZA")),
                rx.table.row_header_cell(rx.link("Zahra Ambessa")),
                rx.table.cell("zahra@example.com"),
                rx.table.cell("Admin"),
                align="center",
            ),
            rx.table.row(
                rx.table.cell(rx.avatar(fallback="JE")),
                rx.table.row_header_cell(rx.link("Jasper Eriksson")),
                rx.table.cell("jasper@example.com"),
                rx.table.cell("Developer"),
                align="center",
            ),
        ),
        width="100%",
    ),
    width="100%",
    direction="column",
    spacing="2",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/typography/blockquote.md`:

```md
---
components:
    - rx.blockquote
---


# Blockquote

```python demo
rx.blockquote("Perfect typography is certainly the most elusive of all arts.")
```

## Size

Use the `size` prop to control the size of the blockquote. The prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.

```python demo
rx.flex(
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="1"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="2"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="3"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="4"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="5"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="6"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="7"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="8"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="9"),
    direction="column",
    spacing="3",
)
```

## Weight

Use the `weight` prop to set the blockquote weight.

```python demo
rx.flex(
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", weight="light"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", weight="regular"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", weight="medium"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", weight="bold"),
    direction="column",
    spacing="3",
)
```

## Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.

```python demo
rx.flex(
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", color_scheme="indigo"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", color_scheme="cyan"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", color_scheme="crimson"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", color_scheme="orange"),
    direction="column",
    spacing="3",
)
```

## High Contrast

Use the `high_contrast` prop to increase color contrast with the background.

```python demo
rx.flex(
    rx.blockquote("Perfect typography is certainly the most elusive of all arts."),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", high_contrast=True),
    direction="column",
    spacing="3",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/typography/heading.md`:

```md
---
components:
    - rx.heading
---


# Heading

```python demo
rx.heading("The quick brown fox jumps over the lazy dog.")
```

## As another element

Use the `as_` prop to change the heading level. This prop is purely semantic and does not change the visual appearance.

```python demo
rx.flex(
    rx.heading("Level 1", as_="h1"),
    rx.heading("Level 2", as_="h2"),
    rx.heading("Level 3", as_="h3"),
    direction="column",
    spacing="3",
)             
```

## Size

Use the `size` prop to control the size of the heading. The prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease

```python demo
rx.flex(
    rx.heading("The quick brown fox jumps over the lazy dog.", size="1"),
    rx.heading("The quick brown fox jumps over the lazy dog.", size="2"),
    rx.heading("The quick brown fox jumps over the lazy dog.", size="3"),
    rx.heading("The quick brown fox jumps over the lazy dog.", size="4"),
    rx.heading("The quick brown fox jumps over the lazy dog.", size="5"),
    rx.heading("The quick brown fox jumps over the lazy dog.", size="6"),
    rx.heading("The quick brown fox jumps over the lazy dog.", size="7"),
    rx.heading("The quick brown fox jumps over the lazy dog.", size="8"),
    rx.heading("The quick brown fox jumps over the lazy dog.", size="9"),
    direction="column",
    spacing="3",
)
```

## Weight

Use the `weight` prop to set the text weight.

```python demo
rx.flex(
    rx.heading("The quick brown fox jumps over the lazy dog.", weight="light"),
    rx.heading("The quick brown fox jumps over the lazy dog.", weight="regular"),
    rx.heading("The quick brown fox jumps over the lazy dog.", weight="medium"),
    rx.heading("The quick brown fox jumps over the lazy dog.", weight="bold"),
    direction="column",
    spacing="3",
)
```

## Align

Use the `align` prop to set text alignment.

```python demo
rx.flex(
    rx.heading("Left-aligned", align="left"),
    rx.heading("Center-aligned", align="center"),
    rx.heading("Right-aligned", align="right"),
    direction="column",
    spacing="3",
    width="100%",
)
```

## Trim

Use the `trim` prop to trim the leading space at the start, end, or both sides of the text.

```python demo
rx.flex(
    rx.heading("Without Trim",
        trim="normal",
        style={"background": "var(--gray-a2)",
                "border_top": "1px dashed var(--gray-a7)",
                "border_bottom": "1px dashed var(--gray-a7)",}
    ),
    rx.heading("With Trim",
        trim="both",
        style={"background": "var(--gray-a2)",
                "border_top": "1px dashed var(--gray-a7)",
                "border_bottom": "1px dashed var(--gray-a7)",}
    ),
    direction="column",
    spacing="3",
)
```

Trimming the leading is useful when dialing in vertical spacing in cards or other “boxy” components. Otherwise, padding looks larger on top and bottom than on the sides.

```python demo
rx.flex(
    rx.box(
        rx.heading("Without trim", margin_bottom="4px", size="3",),
        rx.text("The goal of typography is to relate font size, line height, and line width in a proportional way that maximizes beauty and makes reading easier and more pleasant."),
        style={"background": "var(--gray-a2)", 
                "border": "1px dashed var(--gray-a7)",},
        padding="16px",
    ),
    rx.box(
        rx.heading("With trim", margin_bottom="4px", size="3", trim="start"),
        rx.text("The goal of typography is to relate font size, line height, and line width in a proportional way that maximizes beauty and makes reading easier and more pleasant."),
        style={"background": "var(--gray-a2)", 
                "border": "1px dashed var(--gray-a7)",},
        padding="16px",
    ),
    direction="column",
    spacing="3",
)
```

## Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.

```python demo
rx.flex(
    rx.heading("The quick brown fox jumps over the lazy dog.", color_scheme="indigo"),
    rx.heading("The quick brown fox jumps over the lazy dog.", color_scheme="cyan"),
    rx.heading("The quick brown fox jumps over the lazy dog.", color_scheme="crimson"),
    rx.heading("The quick brown fox jumps over the lazy dog.", color_scheme="orange"),
    direction="column",
)
```

## High Contrast

Use the `high_contrast` prop to increase color contrast with the background.

```python demo
rx.flex(
    rx.heading("The quick brown fox jumps over the lazy dog.", color_scheme="indigo", high_contrast=True),
    rx.heading("The quick brown fox jumps over the lazy dog.", color_scheme="cyan", high_contrast=True),
    rx.heading("The quick brown fox jumps over the lazy dog.", color_scheme="crimson", high_contrast=True),
    rx.heading("The quick brown fox jumps over the lazy dog.", color_scheme="orange", high_contrast=True),
    direction="column",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/typography/markdown.md`:

```md
---
components:
    - rx.markdown
---


# Markdown

The `rx.markdown` component can be used to render markdown text.
It is based on [Github Flavored Markdown](https://github.github.com/gfm/).

```python demo
rx.vstack(
    rx.markdown("# Hello World!"),
    rx.markdown("## Hello World!"),
    rx.markdown("### Hello World!"),
    rx.markdown("Support us on [Github](https://github.com/reflex-dev/reflex)."),
    rx.markdown("Use `reflex deploy` to deploy your app with **a single command**."),
)
```

## Math Equations

You can render math equations using LaTeX.
For inline equations, surround the equation with `$`:

```python demo
rx.markdown("Pythagorean theorem: $a^2 + b^2 = c^2$.")
```

## Syntax Highlighting

You can render code blocks with syntax highlighting using the \`\`\`\{language} syntax:

```python demo  
rx.markdown(
r"""
\```python
import reflex as rx
from .pages import index

app = rx.App()
app.add_page(index)
\```
"""
)
```

## Tables

You can render tables using the `|` syntax:

```python demo
rx.markdown(
    """
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
"""
)
```

## Component Map

You can specify which components to use for rendering markdown elements using the
`component_map` prop.

Each key in the `component_map` prop is a markdown element, and the value is
a function that takes the text of the element as input and returns a Reflex component.

```md alert
The `codeblock` and `a` tags are special cases. In addition to the `text`, they also receive a `props` argument containing additional props for the component.
```

```python demo exec
component_map = {
    "h1": lambda text: rx.heading(text, size="5", margin_y="1em"),
    "h2": lambda text: rx.heading(text, size="3", margin_y="1em"),
    "h3": lambda text: rx.heading(text, size="1", margin_y="1em"),
    "p": lambda text: rx.text(text, color="green", margin_y="1em"),
    "code": lambda text: rx.code(text, color="purple"),
    "codeblock": lambda text, **props: rx.code_block(text, **props, theme=rx.code_block.themes.dark, margin_y="1em"),
    "a": lambda text, **props: rx.link(text, **props, color="blue", _hover={"color": "red"}),
}

def index():
    return rx.box(
        rx.markdown(
r"""
# Hello World!

## This is a Subheader

### And Another Subheader

Here is some `code`:

\```python
import reflex as rx

component = rx.text("Hello World!")
\```

And then some more text here, followed by a link to [Reflex](https://reflex.dev/).
""",
    component_map=component_map,
)
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/typography/link.md`:

```md
---
components:
    - rx.link
---


# Link

Links are accessible elements used primarily for navigation. Use the `href` prop to specify the location for the link to navigate to.

```python demo
rx.link("Reflex Home Page.", href="https://reflex.dev/")
```

You can also provide local links to other pages in your project without writing the full url.

```python demo
rx.link("Example", href="/docs/library",)
```


The `link` component can be used to wrap other components to make them link to other pages.

```python demo
rx.link(rx.button("Example"), href="https://reflex.dev/")
```

You can also create anchors to link to specific parts of a page using the `id` prop.

```python demo
rx.box("Example", id="example")
```

To reference an anchor, you can use the `href` prop of the `link` component. The `href` should be in the format of the page you want to link to followed by a # and the id of the anchor.

```python demo
rx.link("Example", href="/docs/library/typography/link#example")
```

```md alert info
# Redirecting the user using State 
It is also possible to redirect the user to a new path within the application, using `rx.redirect()`. Check out the docs [here]({api_reference.special_events.path}).
```

# Style

## Size

Use the `size` prop to control the size of the link. The prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.

```python demo
rx.flex(
    rx.link("The quick brown fox jumps over the lazy dog.", size="1"),
    rx.link("The quick brown fox jumps over the lazy dog.", size="2"),
    rx.link("The quick brown fox jumps over the lazy dog.", size="3"),
    rx.link("The quick brown fox jumps over the lazy dog.", size="4"),
    rx.link("The quick brown fox jumps over the lazy dog.", size="5"),
    rx.link("The quick brown fox jumps over the lazy dog.", size="6"),
    rx.link("The quick brown fox jumps over the lazy dog.", size="7"),
    rx.link("The quick brown fox jumps over the lazy dog.", size="8"),
    rx.link("The quick brown fox jumps over the lazy dog.", size="9"),
    direction="column",
    spacing="3",
)
```

## Weight

Use the `weight` prop to set the text weight.

```python demo
rx.flex(
    rx.link("The quick brown fox jumps over the lazy dog.", weight="light"),
    rx.link("The quick brown fox jumps over the lazy dog.", weight="regular"),
    rx.link("The quick brown fox jumps over the lazy dog.", weight="medium"),
    rx.link("The quick brown fox jumps over the lazy dog.", weight="bold"),
    direction="column",
    spacing="3",
)
```

## Trim

Use the `trim` prop to trim the leading space at the start, end, or both sides of the rendered text.

```python demo
rx.flex(
    rx.link("Without Trim",
        trim="normal",
        style={"background": "var(--gray-a2)",
                "border_top": "1px dashed var(--gray-a7)",
                "border_bottom": "1px dashed var(--gray-a7)",}
    ),
    rx.link("With Trim",
        trim="both",
        style={"background": "var(--gray-a2)",
                "border_top": "1px dashed var(--gray-a7)",
                "border_bottom": "1px dashed var(--gray-a7)",}
    ),
    direction="column",
    spacing="3",
)
```

## Underline

Use the `underline` prop to manage the visibility of the underline affordance. It defaults to `auto`.

```python demo
rx.flex(
    rx.link("The quick brown fox jumps over the lazy dog.", underline="auto"),
    rx.link("The quick brown fox jumps over the lazy dog.", underline="hover"),
    rx.link("The quick brown fox jumps over the lazy dog.", underline="always"),
    direction="column",
    spacing="3",
)
```

## Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.

```python demo
rx.flex(
    rx.link("The quick brown fox jumps over the lazy dog.", color_scheme="indigo"),
    rx.link("The quick brown fox jumps over the lazy dog.", color_scheme="cyan"),
    rx.link("The quick brown fox jumps over the lazy dog.", color_scheme="crimson"),
    rx.link("The quick brown fox jumps over the lazy dog.", color_scheme="orange"),
    direction="column",
)
```

## High Contrast

Use the `high_contrast` prop to increase color contrast with the background.

```python demo
rx.flex(
    rx.link("The quick brown fox jumps over the lazy dog."),
    rx.link("The quick brown fox jumps over the lazy dog.", high_contrast=True),
    direction="column",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/typography/kbd.md`:

```md
---
components:
    - rx.text.kbd
---


# rx.text.kbd (Keyboard)

Represents keyboard input or a hotkey.

```python demo
rx.text.kbd("Shift + Tab")
```

## Size

Use the `size` prop to control text size. This prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.

```python demo
rx.flex(
    rx.text.kbd("Shift + Tab", size="1"),
    rx.text.kbd("Shift + Tab", size="2"),
    rx.text.kbd("Shift + Tab", size="3"),
    rx.text.kbd("Shift + Tab", size="4"),
    rx.text.kbd("Shift + Tab", size="5"),
    rx.text.kbd("Shift + Tab", size="6"),
    rx.text.kbd("Shift + Tab", size="7"),
    rx.text.kbd("Shift + Tab", size="8"),
    rx.text.kbd("Shift + Tab", size="9"),
    direction="column",
    spacing="3",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/typography/quote.md`:

```md
---
components:
    - rx.text.quote
---


# Quote

A short inline quotation.

```python demo
rx.text("His famous quote, ",
  rx.text.quote("Styles come and go. Good design is a language, not a style"),
  ", elegantly sums up Massimo’s philosophy of design."
  )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/typography/strong.md`:

```md
---
components:
    - rx.text.strong
---


# Strong

Marks text to signify strong importance.

```python demo
rx.text("The most important thing to remember is, ", rx.text.strong("stay positive"), ".")
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/typography/code.md`:

```md
---
components:
    - rx.code
---


# Code

```python demo
rx.code("console.log()")
```

## Size

Use the `size` prop to control text size. This prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.

```python demo
rx.flex(
    rx.code("console.log()", size="1"),
    rx.code("console.log()", size="2"),
    rx.code("console.log()", size="3"),
    rx.code("console.log()", size="4"),
    rx.code("console.log()", size="5"),
    rx.code("console.log()", size="6"),
    rx.code("console.log()", size="7"),
    rx.code("console.log()", size="8"),
    rx.code("console.log()", size="9"),
    direction="column",
    spacing="3",
    align="start",
)
```

## Weight

Use the `weight` prop to set the text weight.

```python demo
rx.flex(
    rx.code("console.log()", weight="light"),
    rx.code("console.log()", weight="regular"),
    rx.code("console.log()", weight="medium"),
    rx.code("console.log()", weight="bold"),
    direction="column",
    spacing="3",
)
```

## Variant

Use the `variant` prop to control the visual style.

```python demo
rx.flex(
    rx.code("console.log()", variant="solid"),
    rx.code("console.log()", variant="soft"),
    rx.code("console.log()", variant="outline"),
    rx.code("console.log()", variant="ghost"),
    direction="column",
    spacing="2",
    align="start",
)
```

## Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.

```python demo
rx.flex(
    rx.code("console.log()", color_scheme="indigo"),
    rx.code("console.log()", color_scheme="crimson"),
    rx.code("console.log()", color_scheme="orange"),
    rx.code("console.log()", color_scheme="cyan"),
    direction="column",
    spacing="2",
    align="start",
)
```

## High Contrast

Use the `high_contrast` prop to increase color contrast with the background.

```python demo
rx.flex(
    rx.flex(
        rx.code("console.log()", variant="solid"),
        rx.code("console.log()", variant="soft"),
        rx.code("console.log()", variant="outline"),
        rx.code("console.log()", variant="ghost"),
        direction="column",
        align="start",
        spacing="2",
    ),
    rx.flex(
        rx.code("console.log()", variant="solid", high_contrast=True),
        rx.code("console.log()", variant="soft", high_contrast=True),
        rx.code("console.log()", variant="outline", high_contrast=True),
        rx.code("console.log()", variant="ghost", high_contrast=True),
        direction="column",
        align="start",
        spacing="2",
    ),
    spacing="3",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/typography/em.md`:

```md
---
components:
    - rx.text.em
---


# Em (Emphasis)

Marks text to stress emphasis.

```python demo
rx.text("We ", rx.text.em("had"), " to do something about it.")
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/typography/text.md`:

```md
---
components:
    - rx.text
    - rx.text.em

---


# Text

```python demo
rx.text("The quick brown fox jumps over the lazy dog.")
```

## As another element

Use the `as_` prop to render text as a `p`, `label`, `div` or `span`. This prop is purely semantic and does not alter visual appearance.

```python demo
rx.flex(
    rx.text("This is a ", rx.text.strong("paragraph"), " element.", as_="p"),
    rx.text("This is a ", rx.text.strong("label"), " element.", as_="label"),
    rx.text("This is a ", rx.text.strong("div"), " element.", as_="div"),
    rx.text("This is a ", rx.text.strong("span"), " element.", as_="span"),
    direction="column",
    spacing="3",
)             
```

## Size

Use the `size` prop to control text size. This prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.

```python demo
rx.flex(
    rx.text("The quick brown fox jumps over the lazy dog.", size="1"),
    rx.text("The quick brown fox jumps over the lazy dog.", size="2"),
    rx.text("The quick brown fox jumps over the lazy dog.", size="3"),
    rx.text("The quick brown fox jumps over the lazy dog.", size="4"),
    rx.text("The quick brown fox jumps over the lazy dog.", size="5"),
    rx.text("The quick brown fox jumps over the lazy dog.", size="6"),
    rx.text("The quick brown fox jumps over the lazy dog.", size="7"),
    rx.text("The quick brown fox jumps over the lazy dog.", size="8"),
    rx.text("The quick brown fox jumps over the lazy dog.", size="9"),
    direction="column",
    spacing="3",
)
```

Sizes 2–4 are designed to work well for long-form content. Sizes 1–3 are designed to work well for UI labels.

## Weight

Use the `weight` prop to set the text weight.

```python demo
rx.flex(
    rx.text("The quick brown fox jumps over the lazy dog.", weight="light", as_="div"),
    rx.text("The quick brown fox jumps over the lazy dog.", weight="regular", as_="div"),
    rx.text("The quick brown fox jumps over the lazy dog.", weight="medium", as_="div"),
    rx.text("The quick brown fox jumps over the lazy dog.", weight="bold", as_="div"),
    direction="column",
    spacing="3",
)
```

## Align

Use the `align` prop to set text alignment.

```python demo
rx.flex(
    rx.text("Left-aligned", align="left", as_="div"),
    rx.text("Center-aligned", align="center", as_="div"),
    rx.text("Right-aligned", align="right", as_="div"),
    direction="column",
    spacing="3",
    width="100%",
)
```

## Trim

Use the `trim` prop to trim the leading space at the start, end, or both sides of the text box.

```python demo
rx.flex(
    rx.text("Without Trim",
        trim="normal",
        style={"background": "var(--gray-a2)",
                "border_top": "1px dashed var(--gray-a7)",
                "border_bottom": "1px dashed var(--gray-a7)",}
    ),
    rx.text("With Trim",
        trim="both",
        style={"background": "var(--gray-a2)",
                "border_top": "1px dashed var(--gray-a7)",
                "border_bottom": "1px dashed var(--gray-a7)",}
    ),
    direction="column",
    spacing="3",
)
```

Trimming the leading is useful when dialing in vertical spacing in cards or other “boxy” components. Otherwise, padding looks larger on top and bottom than on the sides.

```python demo
rx.flex(
    rx.box(
        rx.heading("Without trim", margin_bottom="4px", size="3",),
        rx.text("The goal of typography is to relate font size, line height, and line width in a proportional way that maximizes beauty and makes reading easier and more pleasant."),
        style={"background": "var(--gray-a2)", 
                "border": "1px dashed var(--gray-a7)",},
        padding="16px",
    ),
    rx.box(
        rx.heading("With trim", margin_bottom="4px", size="3", trim="start"),
        rx.text("The goal of typography is to relate font size, line height, and line width in a proportional way that maximizes beauty and makes reading easier and more pleasant."),
        style={"background": "var(--gray-a2)", 
                "border": "1px dashed var(--gray-a7)",},
        padding="16px",
    ),
    direction="column",
    spacing="3",
)
```

## Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.

```python demo
rx.flex(
    rx.text("The quick brown fox jumps over the lazy dog.", color_scheme="indigo"),
    rx.text("The quick brown fox jumps over the lazy dog.", color_scheme="cyan"),
    rx.text("The quick brown fox jumps over the lazy dog.", color_scheme="crimson"),
    rx.text("The quick brown fox jumps over the lazy dog.", color_scheme="orange"),
    direction="column",
)
```

## High Contrast

Use the `high_contrast` prop to increase color contrast with the background.

```python demo
rx.flex(
    rx.text("The quick brown fox jumps over the lazy dog.", color_scheme="indigo", high_contrast=True),
    rx.text("The quick brown fox jumps over the lazy dog.", color_scheme="cyan", high_contrast=True),
    rx.text("The quick brown fox jumps over the lazy dog.", color_scheme="crimson", high_contrast=True),
    rx.text("The quick brown fox jumps over the lazy dog.", color_scheme="orange", high_contrast=True),
    direction="column",
)
```

## With formatting

Compose `Text` with formatting components to add emphasis and structure to content.

```python demo
rx.text(
    "Look, such a helpful ",
    rx.link("link", href="#"),
    ", an ",
    rx.text.em("italic emphasis"),
    " a piece of computer ",
    rx.code("code"),
    ", and even a hotkey combination ",
    rx.text.kbd("⇧⌘A"),
    " within the text.",
    size="5",
)
```

## Preformmatting
By Default, the browser renders multiple white spaces into one. To preserve whitespace, use the `white_space = "pre"` css prop.

```python demo
rx.hstack(
    rx.text("This is not pre     formatted"),
    rx.text("This is pre     formatted", white_space="pre"),
)
```

## With form controls

Composing `text` with a form control like `checkbox`, `radiogroup`, or `switch` automatically centers the control with the first line of text, even when the text is multi-line.

```python demo
rx.box(
    rx.text(
        rx.flex(
            rx.checkbox(default_checked=True),
            "I understand that these documents are confidential and cannot be shared with a third party.",
        ),
        as_="label",
        size="3",
    ),
    style={"max_width": 300},
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/other/html_embed.md`:

```md
---
components:
    - rx.html
---


# HTML Embed

The HTML component can be used to render raw HTML code.

Before you reach for this component, consider using Reflex's raw HTML element support instead.

```python demo
rx.vstack(
    rx.html("<h1>Hello World</h1>"),
    rx.html("<h2>Hello World</h2>"),
    rx.html("<h3>Hello World</h3>"),
    rx.html("<h4>Hello World</h4>"),
    rx.html("<h5>Hello World</h5>"),
    rx.html("<h6>Hello World</h6>"),
)
```

```md alert
# Missing Styles?
Reflex uses Radix-UI and tailwind for styling, both of which reset default styles for headings. 
If you are using the html component and want pretty default styles, consider setting `class_name='prose'`, adding `@tailwindcss/typography` package to `frontend_packages` and enabling it via `tailwind` config in `rxconfig.py`. See the [Tailwind docs]({styling.overview.path}) for an example of adding this plugin.
```

In this example, we render an image.

```python demo
rx.html("<img src='https://reflex.dev/reflex_banner.png' />")
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/other/clipboard.md`:

```md
---
components:
  - rx.clipboard
---


# Clipboard

_New in 0.5.6_

The Clipboard component can be used to respond to paste events with complex data.

If the Clipboard component is included in a page without children,
`rx.clipboard()`, then it will attach to the document's `paste` event handler
and will be triggered when data is pasted anywhere into the page.

```python demo exec
class ClipboardPasteState(rx.State):
    @rx.event
    def on_paste(self, data: list[tuple[str, str]]):
        for mime_type, item in data:
            yield rx.toast(f"Pasted {mime_type} data: {item}")


def clipboard_example():
    return rx.fragment(
        rx.clipboard(on_paste=ClipboardPasteState.on_paste),
        "Paste Content Here",
    )
```

The `data` argument passed to the `on_paste` method is a list of tuples, where
each tuple contains the MIME type of the pasted data and the data itself. Binary
data will be base64 encoded as a data URI, and can be decoded using python's
`urlopen` or used directly as the `src` prop of an image.

## Scoped Paste Events

If you want to limit the scope of the paste event to a specific element, wrap
the `rx.clipboard` component around the elements that should trigger the paste
event.

To avoid having outer paste handlers also trigger the event, you can use the
event action `.stop_propagation` to prevent the paste from bubbling up through
the DOM.

If you need to also prevent the default action of pasting the data into a text
box, you can also attach the `.prevent_default` action.

```python demo exec
class ClipboardPasteImageState(rx.State):
    last_image_uri: str = ""

    def on_paste(self, data: list[tuple[str, str]]):
        for mime_type, item in data:
            if mime_type.startswith("image/"):
                self.last_image_uri = item
                break
        else:
            return rx.toast("Did not find an image in the pasted data")


def clipboard_image_example():
    return rx.vstack(
        rx.clipboard(
            rx.input(placeholder="Paste Image (stop propagation)"),
            on_paste=ClipboardPasteImageState.on_paste.stop_propagation
        ),
        rx.clipboard(
            rx.input(placeholder="Paste Image (prevent default)"),
            on_paste=ClipboardPasteImageState.on_paste.prevent_default
        ),
        rx.image(src=ClipboardPasteImageState.last_image_uri),
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/other/script.md`:

```md
---
components:
    - rx.script
---


# Script

The Script component can be used to include inline javascript or javascript files by URL.

It uses the [`next/script` component](https://nextjs.org/docs/app/api-reference/components/script) to inject the script and can be safely used with conditional rendering to allow script side effects to be controlled by the state.

```python
rx.script("console.log('inline javascript')")
```

Complex inline scripting should be avoided.
If the code to be included is more than a couple lines, it is more maintainable to implement it in a separate javascript file in the `assets` directory and include it via the `src` prop.

```python
rx.script(src="/my-custom.js")
```

This component is particularly helpful for including tracking and social scripts.
Any additional attrs needed for the script tag can be supplied via `custom_attrs` prop.

```python
rx.script(src="//gc.zgo.at/count.js", custom_attrs=\{"data-goatcounter": "https://reflextoys.goatcounter.com/count"})
```

This code renders to something like the following to enable stat counting with a third party service.

```jsx
<script src="//gc.zgo.at/count.js" data-goatcounter="https://reflextoys.goatcounter.com/count" data-nscript="afterInteractive"></script>
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/other/html.md`:

```md
---
components:
    - rx.el.A
    - rx.el.Abbr
    - rx.el.Address
    - rx.el.Area
    - rx.el.Article
    - rx.el.Aside
    - rx.el.Audio
    - rx.el.B
    - rx.el.Bdi
    - rx.el.Bdo
    - rx.el.Blockquote
    - rx.el.Body
    - rx.el.Br
    - rx.el.Button
    - rx.el.Canvas
    - rx.el.Caption
    - rx.el.Cite
    - rx.el.Code
    - rx.el.Col
    - rx.el.Colgroup
    - rx.el.Data
    - rx.el.Dd
    - rx.el.Del
    - rx.el.Details
    - rx.el.Dfn
    - rx.el.Dialog
    - rx.el.Div
    - rx.el.Dl
    - rx.el.Dt
    - rx.el.Em
    - rx.el.Embed
    - rx.el.Fieldset
    - rx.el.Figcaption
    - rx.el.Footer
    - rx.el.Form
    - rx.el.H1
    - rx.el.H2
    - rx.el.H3
    - rx.el.H4
    - rx.el.H5
    - rx.el.H6
    - rx.el.Head
    - rx.el.Header
    - rx.el.Hr
    - rx.el.Html
    - rx.el.I
    - rx.el.Iframe
    - rx.el.Img
    - rx.el.Input
    - rx.el.Ins
    - rx.el.Kbd
    - rx.el.Label
    - rx.el.Legend
    - rx.el.Li
    - rx.el.Link
    - rx.el.Main
    - rx.el.Mark
    - rx.el.Math
    - rx.el.Meta
    - rx.el.Meter
    - rx.el.Nav
    - rx.el.Noscript
    - rx.el.Object
    - rx.el.Ol
    - rx.el.Optgroup
    - rx.el.Option
    - rx.el.Output
    - rx.el.P
    - rx.el.Picture
    - rx.el.Portal
    - rx.el.Pre
    - rx.el.Progress
    - rx.el.Q
    - rx.el.Rp
    - rx.el.Rt
    - rx.el.Ruby
    - rx.el.S
    - rx.el.Samp
    - rx.el.Script
    - rx.el.Section
    - rx.el.Select
    - rx.el.Small
    - rx.el.Source
    - rx.el.Span
    - rx.el.Strong
    - rx.el.Sub
    - rx.el.Sup
    - rx.el.svg.circle
    - rx.el.svg.defs
    - rx.el.svg.linear_gradient
    - rx.el.svg.polygon
    - rx.el.svg.path
    - rx.el.svg.rect
    - rx.el.svg.stop
    - rx.el.Table
    - rx.el.Tbody
    - rx.el.Td
    - rx.el.Template
    - rx.el.Textarea
    - rx.el.Tfoot
    - rx.el.Th
    - rx.el.Thead
    - rx.el.Time
    - rx.el.Title
    - rx.el.Tr
    - rx.el.Track
    - rx.el.U
    - rx.el.Ul
    - rx.el.Video
    - rx.el.Wbr
---

# HTML

Reflex also provides a set of HTML elements that can be used to create web pages. These elements are the same as the HTML elements that are used in web development. These elements come unstyled bhy default. You can style them using style props or tailwindcss classes.

The following is a list of the HTML elements that are available in Reflex:
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/other/theme.md`:

```md
---
 components:
     - rx.theme
     - rx.theme_panel
---

# Theme

 The `Theme` component is used to change the theme of the application. The `Theme` can be set directly in the rx.App.

 ```python
 app = rx.App(
     theme=rx.theme(
         appearance="light", has_background=True, radius="large", accent_color="teal"
     )
 )
 ```

 # Theme Panel

 The `ThemePanel` component is a container for the `Theme` component. It provides a way to change the theme of the application.

 ```python
 rx.theme_panel()
 ```

 The theme panel is closed by default. You can set it open `default_open=True`.

 ```python
 rx.theme_panel(default_open=True)
 ```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/other/skeleton.md`:

```md
---
description: Skeleton, a loading placeholder component for content that is not yet available.
components:
    - rx.skeleton
---


# Skeleton (loading placeholder)

`Skeleton` is a loading placeholder component that serves as a visual placeholder while content is loading.
It is useful for maintaining the layout's structure and providing users with a sense of progression while awaiting the final content.

```python demo
rx.vstack(
    rx.skeleton(rx.button("button-small"), height="10px"),
    rx.skeleton(rx.button("button-big"), height="20px"),
    rx.skeleton(rx.text("Text is loaded."), loading=True,),
    rx.skeleton(rx.text("Text is already loaded."), loading=False,),
),
```

When using `Skeleton` with text, wrap the text itself instead of the parent element to have a placeholder of the same size.

Use the loading prop to control whether the skeleton or its children are displayed. Skeleton preserves the dimensions of children when they are hidden and disables interactive elements.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/general/reference.md`:

```md
---
components:
    - rx.recharts.ReferenceLine
    - rx.recharts.ReferenceDot
    - rx.recharts.ReferenceArea
---

# Reference


The Reference components in Recharts, including ReferenceLine, ReferenceArea, and ReferenceDot, are used to add visual aids and annotations to the chart, helping to highlight specific data points, ranges, or thresholds for better data interpretation and analysis.

## Reference Area

The `rx.recharts.reference_area` component in Recharts is used to highlight a specific area or range on the chart by drawing a rectangular region. It is defined by specifying the coordinates (x1, x2, y1, y2) and can be used to emphasize important data ranges or intervals on the chart.

```python demo graphing
data = [
  {
    "x": 45,
    "y": 100,
    "z": 150,
    "errorY": [
      30,
      20
    ],
    "errorX": 5
  },
  {
    "x": 100,
    "y": 200,
    "z": 200,
    "errorY": [
      20,
      30
    ],
    "errorX": 3
  },
  {
    "x": 120,
    "y": 100,
    "z": 260,
    "errorY": 20,
    "errorX": [
      10,
      3
    ]
  },
  {
    "x": 170,
    "y": 300,
    "z": 400,
    "errorY": [
      15,
      18
    ],
    "errorX": 4
  },
  {
    "x": 140,
    "y": 250,
    "z": 280,
    "errorY": 23,
    "errorX": [
      6,
      7
    ]
  },
  {
    "x": 150,
    "y": 400,
    "z": 500,
    "errorY": [
      21,
      10
    ],
    "errorX": 4
  },
  {
    "x": 110,
    "y": 280,
    "z": 200,
    "errorY": 21,
    "errorX": [
      1,
      8
    ]
  }
]

def reference():
  return rx.recharts.scatter_chart(
    rx.recharts.scatter(
        data=data,
        fill="#8884d8",
        name="A"),
    rx.recharts.reference_area(x1= 150, x2=180, y1=150, y2=300, fill="#8884d8", fill_opacity=0.3),
    rx.recharts.x_axis(data_key="x", name="x", type_="number"), 
    rx.recharts.y_axis(data_key="y", name="y", type_="number"),
    rx.recharts.graphing_tooltip(),
    width = "100%", 
    height = 300,
  )
```

## Reference Line

The `rx.recharts.reference_line` component in rx.recharts is used to draw a horizontal or vertical line on the chart at a specified position. It helps to highlight important values, thresholds, or ranges on the axis, providing visual reference points for better data interpretation.

```python demo graphing
data_2 = [
    {"name": "Page A", "uv": 4000, "pv": 2400, "amt": 2400},
    {"name": "Page B", "uv": 3000, "pv": 1398, "amt": 2210},
    {"name": "Page C", "uv": 2000, "pv": 9800, "amt": 2290},
    {"name": "Page D", "uv": 2780, "pv": 3908, "amt": 2000},
    {"name": "Page E", "uv": 1890, "pv": 4800, "amt": 2181},
    {"name": "Page F", "uv": 2390, "pv": 3800, "amt": 2500},
    {"name": "Page G", "uv": 3490, "pv": 4300, "amt": 2100},
]

def reference_line():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="pv", stroke=rx.color("accent", 8), fill=rx.color("accent", 7),
        ),
        rx.recharts.reference_line(
            x = "Page C",
            stroke = rx.color("accent", 10),
            label="Max PV PAGE",
        ),
        rx.recharts.reference_line(
            y = 9800,
            stroke = rx.color("green", 10),
            label="Max"
        ),
        rx.recharts.reference_line(
            y = 4343,
            stroke = rx.color("green", 10),
            label="Average"
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data_2,
        height = 300,
        width = "100%",
    )

```

## Reference Dot

The `rx.recharts.reference_dot` component in Recharts is used to mark a specific data point on the chart with a customizable dot. It allows you to highlight important values, outliers, or thresholds by providing a visual reference marker at the specified coordinates (x, y) on the chart.

```python demo graphing

data_3 = [
    {
        "x": 45,
        "y": 100,
        "z": 150,
    },
    {
        "x": 100,
        "y": 200,
        "z": 200,
    },
    {
        "x": 120,
        "y": 100,
        "z": 260,
    },
    {
        "x": 170,
        "y": 300,
        "z": 400,
    },
    {
        "x": 140,
        "y": 250,
        "z": 280,
    },
    {
        "x": 150,
        "y": 400,
        "z": 500,
    },
    {
        "x": 110,
        "y": 280,
        "z": 200,
    },
    {
        "x": 80,
        "y": 150,
        "z": 180,
    },
    {
        "x": 200,
        "y": 350,
        "z": 450,
    },
    {
        "x": 90,
        "y": 220,
        "z": 240,
    },
    {
        "x": 130,
        "y": 320,
        "z": 380,
    },
    {
        "x": 180,
        "y": 120,
        "z": 300,
    },
]

def reference_dot():
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(
            data=data_3, 
            fill=rx.color("accent", 9), 
            name="A",
        ),
        rx.recharts.x_axis(
            data_key="x", name="x", type_="number"
        ),
        rx.recharts.y_axis(
            data_key="y", name="y", type_="number"
        ),
        rx.recharts.reference_dot(
            x = 160,
            y = 350,
            r = 15,
            fill = rx.color("accent", 5),
            stroke = rx.color("accent", 10),
        ),
        rx.recharts.reference_dot(
            x = 170,
            y = 300,
            r = 20,
            fill = rx.color("accent", 7),
        ),
        rx.recharts.reference_dot(
            x = 90,
            y = 220,
            r = 18,
            fill = rx.color("green", 7),
        ),
        height = 200,
        width = "100%",
    )

```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/general/cartesiangrid.md`:

```md
---
components:
    - rx.recharts.CartesianGrid
    # - rx.recharts.CartesianAxis
---


# Cartesian Grid

The Cartesian Grid is a component in Recharts that provides a visual reference for data points in charts. It helps users to better interpret the data by adding horizontal and vertical lines across the chart area.

## Simple Example

The `stroke_dasharray` prop in Recharts is used to create dashed or dotted lines for various chart elements like lines, axes, or grids. It's based on the SVG stroke-dasharray attribute. The `stroke_dasharray` prop accepts a comma-separated string of numbers that define a repeating pattern of dashes and gaps along the length of the stroke.

- `stroke_dasharray="5,5"`:  creates a line with 5-pixel dashes and 5-pixel gaps
- `stroke_dasharray="10,5,5,5"`:  creates a more complex pattern with 10-pixel dashes, 5-pixel gaps, 5-pixel dashes, and 5-pixel gaps

Here's a simple example using it on a Line component:

```python demo graphing
data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def cgrid_simple():
  return rx.recharts.line_chart(
    rx.recharts.line(
        data_key="pv",
    ),
    rx.recharts.x_axis(data_key="name"),
    rx.recharts.y_axis(),
    rx.recharts.cartesian_grid(stroke_dasharray="4 4"),
    data=data,
    width = "100%",
    height = 300,
  )
```

## Hidden Axes

A `cartesian_grid` component can be used to hide the horizontal and vertical grid lines in a chart by setting the `horizontal` and `vertical` props to `False`. This can be useful when you want to show the grid lines only on one axis or when you want to create a cleaner look for the chart.

```python demo graphing
data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def cgrid_hidden():
  return rx.recharts.area_chart(
    rx.recharts.area(
        data_key="uv",
        stroke="#8884d8",
        fill="#8884d8"
    ),
    rx.recharts.x_axis(data_key="name"),
    rx.recharts.y_axis(),
    rx.recharts.cartesian_grid(
      stroke_dasharray="2 4",
      vertical=False,
      horizontal=True,
    ),
    data=data,
    width = "100%",
    height = 300,
  )
```

## Custom Grid Lines

The `horizontal_points` and `vertical_points` props allow you to specify custom grid lines on the chart, offering fine-grained control over the grid's appearance.

These props accept arrays of numbers, where each number represents a pixel offset:
- For `horizontal_points`, the offset is measured from the top edge of the chart
- For `vertical_points`, the offset is measured from the left edge of the chart

```md alert info
# **Important**: The values provided to these props are not directly related to the axis values. They represent pixel offsets within the chart's rendering area.
```

Here's an example demonstrating custom grid lines in a scatter chart:

```python demo graphing

data2 = [
    {"x": 100, "y": 200, "z": 200},
    {"x": 120, "y": 100, "z": 260},
    {"x": 170, "y": 300, "z": 400},
    {"x": 170, "y": 250, "z": 280},
    {"x": 150, "y": 400, "z": 500},
    {"x": 110, "y": 280, "z": 200},
    {"x": 200, "y": 150, "z": 300},
    {"x": 130, "y": 350, "z": 450},
    {"x": 90, "y": 220, "z": 180},
    {"x": 180, "y": 320, "z": 350},
    {"x": 140, "y": 230, "z": 320},
    {"x": 160, "y": 180, "z": 240},
]

def cgrid_custom():
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(
            data=data2,
            fill="#8884d8",
        ),
        rx.recharts.x_axis(data_key="x", type_="number"),
        rx.recharts.y_axis(data_key="y"),
        rx.recharts.cartesian_grid(
            stroke_dasharray="3 3",
            horizontal_points=[0, 25, 50],
            vertical_points=[65, 90, 115],
        ),
        width = "100%",
        height = 200,
    )
```

Use these props judiciously to enhance data visualization without cluttering the chart. They're particularly useful for highlighting specific data ranges or creating visual reference points.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/general/tooltip.md`:

```md
---
components:
    - rx.recharts.GraphingTooltip
---

# Tooltip


Tooltips are the little boxes that pop up when you hover over something. Tooltips are always attached to something, like a dot on a scatter chart, or a bar on a bar chart.

```python demo graphing
data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def tooltip_simple():
  return rx.recharts.composed_chart(
    rx.recharts.area(
        data_key="uv",
        stroke="#8884d8",
        fill="#8884d8"
    ), 
    rx.recharts.bar(
        data_key="amt",
        bar_size=20,
        fill="#413ea0"
    ),
    rx.recharts.line(
        data_key="pv",
        type_="monotone",
        stroke="#ff7300"
    ), 
    rx.recharts.x_axis(data_key="name"), 
    rx.recharts.y_axis(),
    rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
    rx.recharts.graphing_tooltip(),
    data=data,
    width = "100%",
    height = 300,
  )
```

## Custom Styling

The `rx.recharts.graphing_tooltip` component allows for customization of the tooltip's style, position, and layout. `separator` sets the separator between the data key and value. `view_box` prop defines the dimensions of the chart's viewbox while `allow_escape_view_box` determines whether the tooltip can extend beyond the viewBox horizontally (x) or vertically (y). `wrapper_style` prop allows you to style the outer container or wrapper of the tooltip. `content_style` prop allows you to style the inner content area of the tooltip. `is_animation_active` prop determines if the tooltip animation is active or not.

```python demo graphing

data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def tooltip_custom_styling():
  return rx.recharts.composed_chart(
    rx.recharts.area(
      data_key="uv", stroke="#8884d8", fill="#8884d8"
    ),
    rx.recharts.bar(
      data_key="amt", bar_size=20, fill="#413ea0"
    ),
    rx.recharts.line(
      data_key="pv", type_="monotone", stroke="#ff7300"
    ),
    rx.recharts.x_axis(data_key="name"),
    rx.recharts.y_axis(),
    rx.recharts.graphing_tooltip(
      separator = " - ",
      view_box = {"width" : 675, " height" : 300 },
      allow_escape_view_box={"x": True, "y": False},
      wrapper_style={
        "backgroundColor": rx.color("accent", 3), 
        "borderRadius": "8px",
        "padding": "10px",
      },
      content_style={
        "backgroundColor": rx.color("accent", 4), 
        "borderRadius": "4px", 
        "padding": "8px",
      },
      position = {"x" : 600, "y" : 0},
      is_animation_active = False,
    ),
    data=data,
    height = 300,
    width = "100%",
  )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/general/brush.md`:

```md
---
components:
    - rx.recharts.Brush
---

# Brush

## Simple Example

The brush component allows us to view charts that have a large number of data points. To view and analyze them efficiently, the brush provides a slider with two handles that helps the viewer to select some range of data points to be displayed.

```python demo graphing
data = [
  { "name": '1', "uv": 300, "pv": 456 },
  { "name": '2', "uv": -145, "pv": 230 },
  { "name": '3', "uv": -100, "pv": 345 },
  { "name": '4', "uv": -8, "pv": 450 },
  { "name": '5', "uv": 100, "pv": 321 },
  { "name": '6', "uv": 9, "pv": 235 },
  { "name": '7', "uv": 53, "pv": 267 },
  { "name": '8', "uv": 252, "pv": -378 },
  { "name": '9', "uv": 79, "pv": -210 },
  { "name": '10', "uv": 294, "pv": -23 },
  { "name": '12', "uv": 43, "pv": 45 },
  { "name": '13', "uv": -74, "pv": 90 },
  { "name": '14', "uv": -71, "pv": 130 },
  { "name": '15', "uv": -117, "pv": 11 },
  { "name": '16', "uv": -186, "pv": 107 },
  { "name": '17', "uv": -16, "pv": 926 },
  { "name": '18', "uv": -125, "pv": 653 },
  { "name": '19', "uv": 222, "pv": 366 },
  { "name": '20', "uv": 372, "pv": 486 },
  { "name": '21', "uv": 182, "pv": 512 },
  { "name": '22', "uv": 164, "pv": 302 },
  { "name": '23', "uv": 316, "pv": 425 },
  { "name": '24', "uv": 131, "pv": 467 },
  { "name": '25', "uv": 291, "pv": -190 },
  { "name": '26', "uv": -47, "pv": 194 },
  { "name": '27', "uv": -415, "pv": 371 },
  { "name": '28', "uv": -182, "pv": 376 },
  { "name": '29', "uv": -93, "pv": 295 },
  { "name": '30', "uv": -99, "pv": 322 },
  { "name": '31', "uv": -52, "pv": 246 },
  { "name": '32', "uv": 154, "pv": 33 },
  { "name": '33', "uv": 205, "pv": 354 },
  { "name": '34', "uv": 70, "pv": 258 },
  { "name": '35', "uv": -25, "pv": 359 },
  { "name": '36', "uv": -59, "pv": 192 },
  { "name": '37', "uv": -63, "pv": 464 },
  { "name": '38', "uv": -91, "pv": -2 },
  { "name": '39', "uv": -66, "pv": 154 },
  { "name": '40', "uv": -50, "pv": 186 },
]

def brush_simple():
  return rx.recharts.bar_chart(
    rx.recharts.bar(
        data_key="uv",
        stroke="#8884d8",
        fill="#8884d8"
    ),
    rx.recharts.bar(
        data_key="pv",
        stroke="#82ca9d",
        fill="#82ca9d"
    ),
    rx.recharts.brush(data_key="name", height=30, stroke="#8884d8"),
    rx.recharts.x_axis(data_key="name"),
    rx.recharts.y_axis(),
    data=data,
    width="100%",
    height=300,
  )
```

## Position, Size, and Range

This example showcases ways to set the Position, Size, and Range. The `gap` prop provides the spacing between stops on the brush when the graph will refresh. The `start_index` and `end_index` props defines the default range of the brush. `traveller_width` prop specifies the width of each handle ("traveller" in recharts lingo).

```python demo graphing
data = [
  { "name": '1', "uv": 300, "pv": 456 },
  { "name": '2', "uv": -145, "pv": 230 },
  { "name": '3', "uv": -100, "pv": 345 },
  { "name": '4', "uv": -8, "pv": 450 },
  { "name": '5', "uv": 100, "pv": 321 },
  { "name": '6', "uv": 9, "pv": 235 },
  { "name": '7', "uv": 53, "pv": 267 },
  { "name": '8', "uv": 252, "pv": -378 },
  { "name": '9', "uv": 79, "pv": -210 },
  { "name": '10', "uv": 294, "pv": -23 },
  { "name": '12', "uv": 43, "pv": 45 },
  { "name": '13', "uv": -74, "pv": 90 },
  { "name": '14', "uv": -71, "pv": 130 },
  { "name": '15', "uv": -117, "pv": 11 },
  { "name": '16', "uv": -186, "pv": 107 },
  { "name": '17', "uv": -16, "pv": 926 },
  { "name": '18', "uv": -125, "pv": 653 },
  { "name": '19', "uv": 222, "pv": 366 },
  { "name": '20', "uv": 372, "pv": 486 },
  { "name": '21', "uv": 182, "pv": 512 },
  { "name": '22', "uv": 164, "pv": 302 },
  { "name": '23', "uv": 316, "pv": 425 },
  { "name": '24', "uv": 131, "pv": 467 },
  { "name": '25', "uv": 291, "pv": -190 },
  { "name": '26', "uv": -47, "pv": 194 },
  { "name": '27', "uv": -415, "pv": 371 },
  { "name": '28', "uv": -182, "pv": 376 },
  { "name": '29', "uv": -93, "pv": 295 },
  { "name": '30', "uv": -99, "pv": 322 },
  { "name": '31', "uv": -52, "pv": 246 },
  { "name": '32', "uv": 154, "pv": 33 },
  { "name": '33', "uv": 205, "pv": 354 },
  { "name": '34', "uv": 70, "pv": 258 },
  { "name": '35', "uv": -25, "pv": 359 },
  { "name": '36', "uv": -59, "pv": 192 },
  { "name": '37', "uv": -63, "pv": 464 },
  { "name": '38', "uv": -91, "pv": -2 },
  { "name": '39', "uv": -66, "pv": 154 },
  { "name": '40', "uv": -50, "pv": 186 },
]

def brush_pos_size_range():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv",
            stroke="#8884d8",
            fill="#8884d8",
        ),
        rx.recharts.area(
            data_key="pv",
            stroke="#82ca9d",
            fill="#82ca9d",
        ),
        rx.recharts.brush(
            data_key="name",
            traveller_width=15,
            start_index=3,
            end_index=10,
            stroke=rx.color("mauve", 10),
            fill=rx.color("mauve", 3),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        width="100%",
        height=200,
    )

```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/general/label.md`:

```md
---
components:
    - rx.recharts.Label
    - rx.recharts.LabelList
---

# Label


Label is a component used to display a single label at a specific position within a chart or axis, while LabelList is a component that automatically renders a list of labels for each data point in a chart series, providing a convenient way to display multiple labels without manually positioning each one.

## Simple Example

Here's a simple example that demonstrates how you can customize the label of your axis using `rx.recharts.label`. The `value` prop represents the actual text of the label, the `position` prop specifies where the label is positioned within the axis component, and the `offset` prop is used to fine-tune the label's position.

```python demo graphing
data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 5800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def label_simple():
    return rx.recharts.bar_chart(
        rx.recharts.cartesian_grid(
            stroke_dasharray="3 3"
        ),
        rx.recharts.bar(
            rx.recharts.label_list(
                data_key="uv", position="top"
            ),
            data_key="uv",
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(
            rx.recharts.label(
                value="center",
                position="center",
                offset=30,
            ),
            rx.recharts.label(
                value="inside left",
                position="insideLeft",
                offset=10,
            ),
            rx.recharts.label(
                value="inside right",
                position="insideRight",
                offset=10,
            ),
            height=50,
        ),
        data=data,
        margin={
            "left": 20,
            "right": 20,
            "top": 20,
            "bottom": 20,
        },
        width="100%",
        height=250,
    )
```

## Label List Example

`rx.recharts.label_list` takes in a `data_key` where we define the data column to plot.

```python demo graphing
data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 5800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def label_list():
  return rx.recharts.bar_chart(
    rx.recharts.bar(
        rx.recharts.label_list(data_key="uv", position="top"),
        data_key="uv",
        stroke="#8884d8",
        fill="#8884d8"
    ), 
    rx.recharts.bar(
        rx.recharts.label_list(data_key="pv", position="top"),
        data_key="pv",
        stroke="#82ca9d",
        fill="#82ca9d" 
    ), 
    rx.recharts.x_axis(
        data_key="name"
    ),
    rx.recharts.y_axis(),
    margin={"left": 10, "right": 0, "top": 20, "bottom": 10},
    data=data,
    width="100%",
    height = 300,
  )
```



```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/general/legend.md`:

```md
---
components:
    - rx.recharts.Legend
---

# Legend


A legend tells what each plot represents. Just like on a map, the legend helps the reader understand what they are looking at. For a line graph for example it tells us what each line represents.

## Simple Example

```python demo graphing
data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def legend_simple():
  return rx.recharts.composed_chart(
    rx.recharts.area(
        data_key="uv",
        stroke="#8884d8",
        fill="#8884d8"
    ), 
    rx.recharts.bar(
        data_key="amt",
        bar_size=20,
        fill="#413ea0"
    ),
    rx.recharts.line(
        data_key="pv",
        type_="monotone",
        stroke="#ff7300"
    ), 
    rx.recharts.x_axis(data_key="name"), 
    rx.recharts.y_axis(),
    rx.recharts.legend(),
    data=data,
    width = "100%",
    height = 300,
  )
```

## Example with Props

The style and layout of the legend can be customized using a set of props. `width` and `height` set the dimensions of the container that wraps the legend, and `layout` can set the legend to display vertically or horizontally. `align` and `vertical_align` set the position relative to the chart container. The type and size of icons can be set using `icon_size` and `icon_type`.

```python demo graphing
data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def legend_props():
  return rx.recharts.composed_chart(
    rx.recharts.line(
      data_key="pv",
      type_="monotone",
      stroke=rx.color("accent", 7),
    ), 
    rx.recharts.line(
      data_key="amt",
      type_="monotone",
      stroke=rx.color("green", 7),
    ), 
    rx.recharts.line(
      data_key="uv",
      type_="monotone",
      stroke=rx.color("red", 7),
    ), 
    rx.recharts.x_axis(data_key="name"), 
    rx.recharts.y_axis(),
    rx.recharts.legend(
      width=60,
      height=100,
      layout="vertical",
      align="right",
      vertical_align="top",
      icon_size=15,
      icon_type="square",
    ),
    data=data,
    width="100%",
    height=300,
  )

```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/general/axis.md`:

```md
---
components:
  - rx.recharts.XAxis
  - rx.recharts.YAxis
  - rx.recharts.ZAxis
---


# Axis

The Axis component in Recharts is a powerful tool for customizing and configuring the axes of your charts. It provides a wide range of props that allow you to control the appearance, behavior, and formatting of the axis. Whether you're working with an AreaChart, LineChart, or any other chart type, the Axis component enables you to create precise and informative visualizations.

## Basic Example

```python demo graphing

data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def axis_simple():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(
            data_key="name",
            label={"value": 'Pages', "position": "bottom"},
        ),
        rx.recharts.y_axis(
            data_key="uv",
            label={"value": 'Views', "angle": -90, "position": "left"},
        ),
        data=data,
        width="100%",
        height=300,
        margin={
            "bottom": 40,
            "left": 40,
            "right": 40,
        },
    )
```

## Multiple Axes

Multiple axes can be used for displaying different data series with varying scales or units on the same chart. This allows for a more comprehensive comparison and analysis of the data.

```python demo graphing

data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def multi_axis():
  return rx.recharts.area_chart(
    rx.recharts.area(
        data_key="uv", stroke="#8884d8", fill="#8884d8", y_axis_id="left",
    ),
    rx.recharts.area(
        data_key="pv", y_axis_id="right", type_="monotone", stroke="#82ca9d", fill="#82ca9d"
    ),
    rx.recharts.x_axis(data_key="name"),
    rx.recharts.y_axis(data_key="uv", y_axis_id="left"),
    rx.recharts.y_axis(data_key="pv", y_axis_id="right", orientation="right"),
    rx.recharts.graphing_tooltip(),
    rx.recharts.legend(),
    data=data,
    width = "100%",
    height = 300,
  )
```

## Choosing Location of Labels for Axes

The axes `label` can take several positions. The example below allows you to try out different locations for the x and y axis labels.

```python demo graphing

class AxisState(rx.State):

    label_positions: list[str] = ["center", "insideTopLeft", "insideTopRight", "insideBottomRight", "insideBottomLeft", "insideTop", "insideBottom", "insideLeft", "insideRight", "outside", "top", "bottom", "left", "right"]

    label_offsets: list[str] = ["-30", "-20", "-10", "0", "10", "20", "30"]

    x_axis_postion: str = "bottom"

    x_axis_offset: int

    y_axis_postion: str = "left"

    y_axis_offset: int

    @rx.event
    def set_x_axis_offset(self, offset: str):
        self.x_axis_offset = int(offset)

    @rx.event
    def set_y_axis_offset(self, offset: str):
        self.y_axis_offset = int(offset)

data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def axis_labels():
    return rx.vstack(
        rx.recharts.area_chart(
            rx.recharts.area(
                data_key="uv",
                stroke=rx.color("accent", 9),
                fill=rx.color("accent", 8),
            ),
            rx.recharts.x_axis(
                data_key="name",
                label={"value": 'Pages', "position": AxisState.x_axis_postion, "offset": AxisState.x_axis_offset},
            ),
            rx.recharts.y_axis(
                data_key="uv",
                label={"value": 'Views', "angle": -90, "position": AxisState.y_axis_postion, "offset": AxisState.y_axis_offset},
            ),
            data=data,
            width="100%",
            height=300,
            margin={
                "bottom": 40,
                "left": 40,
                "right": 40,
              }
        ),
        rx.hstack(
            rx.text("X Label Position: "),
            rx.select(
                AxisState.label_positions,
                value=AxisState.x_axis_postion,
                on_change=AxisState.set_x_axis_postion,
            ),
            rx.text("X Label Offset: "),
            rx.select(
              AxisState.label_offsets,
              value=AxisState.x_axis_offset.to_string(),
              on_change=AxisState.set_x_axis_offset,
            ),
            rx.text("Y Label Position: "),
            rx.select(
                AxisState.label_positions,
                value=AxisState.y_axis_postion,
                on_change=AxisState.set_y_axis_postion,
            ),
            rx.text("Y Label Offset: "),
            rx.select(
              AxisState.label_offsets,
              value=AxisState.y_axis_offset.to_string(),
              on_change=AxisState.set_y_axis_offset,
            ),
        ),
        width="100%",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/other-charts/plotly.md`:

```md
---
components:
  - rx.plotly
---

# Plotly


Plotly is a graphing library that can be used to create interactive graphs. Use the rx.plotly component to wrap Plotly as a component for use in your web page. Checkout [Plotly](https://plotly.com/graphing-libraries/) for more information.

```md alert info
# When integrating Plotly graphs into your UI code, note that the method for displaying the graph differs from a regular Python script. Instead of using `fig.show()`, use `rx.plotly(data=fig)` within your UI code to ensure the graph is properly rendered and displayed within the user interface
```

## Basic Example

Let's create a line graph of life expectancy in Canada.

```python demo exec
import plotly.express as px

df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')

def line_chart():
    return rx.center(
        rx.plotly(data=fig),
    )
```

## 3D graphing example

Let's create a 3D surface plot of Mount Bruno. This is a slightly more complicated example, but it wraps in Reflex using the same method. In fact, you can wrap any figure using the same approach.

```python demo exec
import plotly.graph_objects as go
import pandas as pd

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=[go.Surface(z=z_data.values)])
fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))
fig.update_layout(
    scene_camera_eye=dict(x=1.87, y=0.88, z=-0.64),
    margin=dict(l=65, r=50, b=65, t=90)
)

def mountain_surface():
    return rx.center(
        rx.plotly(data=fig),
    )
```

## Plot as State Var

If the figure is set as a state var, it can be updated during run time.

```python demo exec
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

class PlotlyState(rx.State):
    df: pd.DataFrame
    figure: go.Figure = px.line()

    @rx.event
    def create_figure(self):
        self.df = px.data.gapminder().query("country=='Canada'")
        self.figure = px.line(
            self.df,
            x="year",
            y="lifeExp",
            title="Life expectancy in Canada",
        )

    @rx.event
    def set_selected_country(self, country):
        self.df = px.data.gapminder().query(f"country=='{country}'")
        self.figure = px.line(
            self.df,
            x="year",
            y="lifeExp",
            title=f"Life expectancy in {country}",
        )



def line_chart_with_state():
    return rx.vstack(
        rx.select(
            ['China', 'France', 'United Kingdom', 'United States', 'Canada'],
            default_value="Canada",
            on_change=PlotlyState.set_selected_country,
        ),
        rx.plotly(
            data=PlotlyState.figure,
            on_mount=PlotlyState.create_figure,
        ),
    )
```

## Adding Styles and Layouts

Use `update_layout()` method to update the layout of your chart. Checkout [Plotly Layouts](https://plotly.com/python/reference/layout/) for all layouts props.

```md alert info
Note that the width and height props are not recommended to ensure the plot remains size responsive to its container. The size of plot will be determined by it's outer container.
```

```python demo exec
df = px.data.gapminder().query("country=='Canada'")
fig_1 = px.line(
    df,
    x="year",
    y="lifeExp",
    title="Life expectancy in Canada",
)
fig_1.update_layout(
    title_x=0.5,
    plot_bgcolor="#c3d7f7",
    paper_bgcolor="rgba(128, 128, 128, 0.1)",
    showlegend=True,
    title_font_family="Open Sans",
    title_font_size=25,
)

def add_styles():
    return rx.center(
        rx.plotly(data=fig_1),
        width="100%",
        height="100%",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/other-charts/pyplot.md`:

```md
---
components:
  - pyplot
---


# Pyplot

Pyplot (`reflex-pyplot`) is a graphing library that wraps Matplotlib. Use the `pyplot` component to display any Matplotlib plot in your app. Check out [Matplotlib](https://matplotlib.org/) for more information.

## Installation

Install the `reflex-pyplot` package using pip.

```bash
pip install reflex-pyplot
```

## Basic Example

To display a Matplotlib plot in your app, you can use the `pyplot` component. Pass in the figure you created with Matplotlib to the `pyplot` component as a child.

```python demo exec
import matplotlib.pyplot as plt
import reflex as rx
from reflex_pyplot import pyplot
import numpy as np

def create_contour_plot():
    X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-3, 3, 256))
    Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)
    levels = np.linspace(Z.min(), Z.max(), 7)

    fig, ax = plt.subplots()
    ax.contourf(X, Y, Z, levels=levels)
    plt.close(fig)
    return fig

def pyplot_simple_example():
    return rx.card(
            pyplot(create_contour_plot(), width="100%", height="400px"),
            bg_color='#ffffff',
            width="100%",
        )
```

```md alert info
# You must close the figure after creating

Not closing the figure could cause memory issues.
```

## Stateful Example

Lets create a scatter plot of random data. We'll also allow the user to randomize the data and change the number of points.

In this example, we'll use a `color_mode_cond` to display the plot in both light and dark mode. We need to do this manually here because the colors are determined by the matplotlib chart and not the theme.

```python demo exec
import random
from typing import Literal
import matplotlib.pyplot as plt
import reflex as rx
from reflex_pyplot import pyplot
import numpy as np


def create_plot(theme: str, plot_data: tuple, scale: list):
    bg_color, text_color = ('#1e1e1e', 'white') if theme == 'dark' else ('white', 'black')
    grid_color = '#555555' if theme == 'dark' else '#cccccc'

    fig, ax = plt.subplots(facecolor=bg_color)
    ax.set_facecolor(bg_color)

    for (x, y), color in zip(plot_data, ["#4e79a7", "#f28e2b", "#59a14f"]):
        ax.scatter(x, y, c=color, s=scale, label=color, alpha=0.6, edgecolors="none")

    ax.legend(facecolor=bg_color, edgecolor='none', labelcolor=text_color)
    ax.grid(True, color=grid_color)
    ax.tick_params(colors=text_color)
    for spine in ax.spines.values():
        spine.set_edgecolor(text_color)

    for item in [ax.xaxis.label, ax.yaxis.label, ax.title]:
        item.set_color(text_color)
    plt.close(fig)

    return fig

class PyplotState(rx.State):
    num_points: int = 100
    plot_data: tuple
    scale: list
    fig: plt.Figure = plt.Figure()

    @rx.event
    def randomize(self):
        self.plot_data = tuple(np.random.rand(2, self.num_points) for _ in range(3))
        self.scale = [random.uniform(0, 100) for _ in range(self.num_points)]

    @rx.event
    def set_num_points(self, num_points: list[int]):
        self.num_points = num_points[0]
        self.randomize()
    
    @rx.event
    def create_fig(self, theme: Literal["light", "dark"]):
        self.plot_data = tuple(np.random.rand(2, 100) for _ in range(3))
        self.scale = [random.uniform(0, 100) for _ in range(100)]
        self.fig = create_plot(
            theme, self.plot_data, self.scale
        )

def pyplot_example():
    return rx.vstack(
        rx.card(
            pyplot(
                PyplotState.fig,
                width="100%",
                height="100%",
                on_mount=rx.color_mode_cond(PyplotState.create_fig("light"), PyplotState.create_fig("dark")),
            ),
            rx.vstack(
                rx.hstack(
                    rx.button(
                        "Randomize",
                        on_click=PyplotState.randomize,
                    ),
                    rx.text("Number of Points:"),
                    rx.slider(
                        default_value=100,
                        min_=10,
                        max=1000,
                        on_value_commit=PyplotState.set_num_points,
                    ),
                    width="100%",
                ),
                width="100%",
            ),
            width="100%",
        ),
        justify_content="center",
        align_items="center",
        height="100%",
        width="100%",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/charts/radialbarchart.md`:

```md
---
components:
    - rx.recharts.RadialBarChart
---

# Radial Bar Chart

## Simple Example

This example demonstrates how to use a `radial_bar_chart` with a `radial_bar`. The `radial_bar_chart` takes in `data` and then the `radial_bar` takes in a `data_key`. A radial bar chart is a circular visualization where data categories are represented by bars extending outward from a central point, with the length of each bar proportional to its value.

```md alert info
# Fill color supports `rx.color()`, which automatically adapts to dark/light mode changes.
```

```python demo graphing
data = [
    {"name": "C", "x": 3, "fill": rx.color("cyan", 9)},
    {"name": "D", "x": 4, "fill": rx.color("blue", 9)},
    {"name": "E", "x": 5, "fill": rx.color("orange", 9)},
    {"name": "F", "x": 6, "fill": rx.color("red", 9)},
    {"name": "G", "x": 7, "fill": rx.color("gray", 9)},
    {"name": "H", "x": 8, "fill": rx.color("green", 9)},
    {"name": "I", "x": 9, "fill": rx.color("accent", 6)},
]

def radial_bar_simple():
    return rx.recharts.radial_bar_chart(
        rx.recharts.radial_bar(
            data_key="x",
            min_angle=15,
        ),
        data=data,
        width = "100%",
        height = 500,
    )
```

## Advanced Example

The `start_angle` and `end_angle` define the circular arc over which the bars are distributed, while `inner_radius` and `outer_radius` determine the radial extent of the bars from the center. 

```python demo graphing

data_radial_bar = [
    {
        "name": "18-24",
        "uv": 31.47,
        "pv": 2400,
        "fill": "#8884d8"
    },
    {
        "name": "25-29",
        "uv": 26.69,
        "pv": 4567,
        "fill": "#83a6ed"
    },
    {
        "name": "30-34",
        "uv": -15.69,
        "pv": 1398,
        "fill": "#8dd1e1"
    },
    {
        "name": "35-39",
        "uv": 8.22,
        "pv": 9800,
        "fill": "#82ca9d"
    },
    {
        "name": "40-49",
        "uv": -8.63,
        "pv": 3908,
        "fill": "#a4de6c"
    },
    {
        "name": "50+",
        "uv": -2.63,
        "pv": 4800,
        "fill": "#d0ed57"
    },
    {
        "name": "unknown",
        "uv": 6.67,
        "pv": 4800,
        "fill": "#ffc658"
    }
]

def radial_bar_advanced():
    return rx.recharts.radial_bar_chart(
        rx.recharts.radial_bar(
            data_key="uv",
            min_angle=90,
            background=True,
            label={"fill": '#666', "position": 'insideStart'},
        ),
        data=data_radial_bar,
        inner_radius="10%",
        outer_radius="80%",
        start_angle=180,
        end_angle=0,
        width="100%",
        height=300,
    )
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/charts/linechart.md`:

```md
---
components:
  - rx.recharts.LineChart
  - rx.recharts.Line
---

# Line Chart


A line chart is a type of chart used to show information that changes over time. Line charts are created by plotting a series of several points and connecting them with a straight line.

## Simple Example

For a line chart we must define an `rx.recharts.line()` component for each set of values we wish to plot. Each `rx.recharts.line()` component has a `data_key` which clearly states which variable in our data we are tracking. In this simple example we plot `pv` and `uv` as separate lines against the `name` column which we set as the `data_key` in `rx.recharts.x_axis`.

```python demo graphing
data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def line_simple():
  return rx.recharts.line_chart(
    rx.recharts.line(
        data_key="pv",
    ),
    rx.recharts.line(
        data_key="uv",
    ),
    rx.recharts.x_axis(data_key="name"),
    rx.recharts.y_axis(),
    data=data,
    width = "100%",
    height = 300,
  )
```

## Example with Props

Our second example uses exactly the same data as our first example, except now we add some extra features to our line graphs. We add a `type_` prop to `rx.recharts.line` to style the lines differently. In addition, we add an `rx.recharts.cartesian_grid` to get a grid in the background, an `rx.recharts.legend` to give us a legend for our graphs and an `rx.recharts.graphing_tooltip` to add a box with text that appears when you pause the mouse pointer on an element in the graph.

```python demo graphing

data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def line_features():
  return rx.recharts.line_chart(
    rx.recharts.line(
        data_key="pv",
        type_="monotone",
        stroke="#8884d8",),
    rx.recharts.line(
        data_key="uv",
        type_="monotone",
        stroke="#82ca9d",),
    rx.recharts.x_axis(data_key="name"),
    rx.recharts.y_axis(),
    rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
    rx.recharts.graphing_tooltip(),
    rx.recharts.legend(),
    data=data,
    width = "100%",
    height = 300,
  )
```

## Layout

The `layout` prop allows you to set the orientation of the graph to be vertical or horizontal. The `margin` prop defines the spacing around the graph,

```md alert info
# Include margins around your graph to ensure proper spacing and enhance readability. By default, provide margins on all sides of the chart to create a visually appealing and functional representation of your data.
```

```python demo graphing

data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def line_vertical():
    return rx.recharts.line_chart(
        rx.recharts.line(
            data_key="pv",
            stroke=rx.color("accent", 9),
        ),
        rx.recharts.line(
            data_key="uv",
            stroke=rx.color("green", 9),
        ),
        rx.recharts.x_axis(type_="number"),
        rx.recharts.y_axis(data_key="name", type_="category"),
        layout="vertical",
        margin={
            "top": 20,
            "right": 20,
            "left": 20,
            "bottom": 20
        },
        data = data,
        height = 300,
        width = "100%",
    )
```

## Dynamic Data

Chart data can be modified by tying the `data` prop to a State var. Most other
props, such as `type_`, can be controlled dynamically as well. In the following
example the "Munge Data" button can be used to randomly modify the data, and the
two `select` elements change the line `type_`. Since the data and style is saved
in the per-browser-tab State, the changes will not be visible to other visitors.

```python demo exec

initial_data = data

class LineChartState(rx.State):
    data: list[dict[str, Any]] = initial_data
    pv_type: str = "monotone"
    uv_type: str = "monotone"

    @rx.event
    def munge_data(self):
        for row in self.data:
            row["uv"] += random.randint(-500, 500)
            row["pv"] += random.randint(-1000, 1000)

def line_dynamic():
  return rx.vstack(
    rx.recharts.line_chart(
      rx.recharts.line(
        data_key="pv",
        type_=LineChartState.pv_type,
        stroke="#8884d8",
      ),
      rx.recharts.line(
        data_key="uv",
        type_=LineChartState.uv_type,
        stroke="#82ca9d",
      ),
      rx.recharts.x_axis(data_key="name"),
      rx.recharts.y_axis(),
      data=LineChartState.data,
      margin={
        "top": 20,
        "right": 20,
        "left": 20,
        "bottom": 20
      },
      width = "100%",
      height = 300,
    ),
    rx.hstack(
      rx.button("Munge Data", on_click=LineChartState.munge_data),
      rx.select(
        ["monotone", "linear", "step", "stepBefore", "stepAfter"],
        value=LineChartState.pv_type,
        on_change=LineChartState.set_pv_type
      ),
      rx.select(
          ["monotone", "linear", "step", "stepBefore", "stepAfter"],
          value=LineChartState.uv_type,
          on_change=LineChartState.set_uv_type
      ),
    ),
    width="100%",
  )
```

To learn how to use the `sync_id`, `x_axis_id` and `y_axis_id` props check out the of the area chart [documentation]({library.graphing.charts.areachart.path}), where these props are all described with examples.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/charts/barchart.md`:

```md
---
components:
  - rx.recharts.BarChart
  - rx.recharts.Bar
---

# Bar Chart


A bar chart presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent.

For a bar chart we must define an `rx.recharts.bar()` component for each set of values we wish to plot. Each `rx.recharts.bar()` component has a `data_key` which clearly states which variable in our data we are tracking. In this simple example we plot `uv` as a bar against the `name` column which we set as the `data_key` in `rx.recharts.x_axis`.

## Simple Example

```python demo graphing
data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def bar_simple():
  return rx.recharts.bar_chart(
    rx.recharts.bar(
        data_key="uv",
        stroke=rx.color("accent", 9),
        fill=rx.color("accent", 8),
    ),
    rx.recharts.x_axis(data_key="name"),
    rx.recharts.y_axis(),
    data=data,
    width = "100%",
    height = 250,
  )
```

## Multiple Bars

Multiple bars can be placed on the same `bar_chart`, using multiple `rx.recharts.bar()` components.

```python demo graphing
data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def bar_double():
  return rx.recharts.bar_chart(
    rx.recharts.bar(
        data_key="uv",
        stroke=rx.color("accent", 9),
        fill=rx.color("accent", 8),
    ),
    rx.recharts.bar(
        data_key="pv",
        stroke=rx.color("green", 9),
        fill=rx.color("green", 8),
    ),
    rx.recharts.x_axis(data_key="name"),
    rx.recharts.y_axis(),
    data=data,
    width = "100%",
    height = 250,
  )
```

## Ranged Charts

You can also assign a range in the bar by assigning the data_key in the `rx.recharts.bar` to a list with two elements, i.e. here a range of two temperatures for each date.

```python demo graphing
range_data = [
  {
    "day": "05-01",
    "temperature": [
      -1,
      10
    ]
  },
  {
    "day": "05-02",
    "temperature": [
      2,
      15
    ]
  },
  {
    "day": "05-03",
    "temperature": [
      3,
      12
    ]
  },
  {
    "day": "05-04",
    "temperature": [
      4,
      12
    ]
  },
  {
    "day": "05-05",
    "temperature": [
      12,
      16
    ]
  },
  {
    "day": "05-06",
    "temperature": [
      5,
      16
    ]
  },
  {
    "day": "05-07",
    "temperature": [
      3,
      12
    ]
  },
  {
    "day": "05-08",
    "temperature": [
      0,
      8
    ]
  },
  {
    "day": "05-09",
    "temperature": [
      -3,
      5
    ]
  }
]

def bar_range():
  return rx.recharts.bar_chart(
    rx.recharts.bar(
        data_key="temperature",
        stroke=rx.color("accent", 9),
        fill=rx.color("accent", 8),
    ),
    rx.recharts.x_axis(data_key="day"),
    rx.recharts.y_axis(),
    data=range_data,
    width = "100%",
    height = 250,
  )
```

## Stateful Charts

Here is an example of a bar graph with a `State`. Here we have defined a function `randomize_data`, which randomly changes the data for both graphs when the first defined `bar` is clicked on using `on_click=BarState.randomize_data`.

```python demo exec
class BarState(rx.State):
    data = data

    @rx.event
    def randomize_data(self):
        for i in range(len(self.data)):
            self.data[i]["uv"] = random.randint(0, 10000)
            self.data[i]["pv"] = random.randint(0, 10000)
            self.data[i]["amt"] = random.randint(0, 10000)

def bar_with_state():
  return rx.recharts.bar_chart(
    rx.recharts.cartesian_grid(
      stroke_dasharray="3 3",
    ),
    rx.recharts.bar(
      data_key="uv",
      stroke=rx.color("accent", 9),
      fill=rx.color("accent", 8),
    ),
    rx.recharts.bar(
      data_key="pv",
      stroke=rx.color("green", 9),
      fill=rx.color("green", 8),
    ),
    rx.recharts.x_axis(data_key="name"),
    rx.recharts.y_axis(),
    rx.recharts.legend(),
    on_click=BarState.randomize_data,
    data=BarState.data,
    width = "100%",
    height = 300,
  )
```

## Example with Props

Here's an example demonstrates how to customize the appearance and layout of bars using the `bar_category_gap`, `bar_gap`, `bar_size`, and `max_bar_size` props. These props accept values in pixels to control the spacing and size of the bars.

```python demo graphing

data = [
    {'name': 'Page A', 'value': 2400},
    {'name': 'Page B', 'value': 1398},
    {'name': 'Page C', 'value': 9800},
    {'name': 'Page D', 'value': 3908},
    {'name': 'Page E', 'value': 4800},
    {'name': 'Page F', 'value': 3800},
]

def bar_features():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="value",
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        bar_category_gap="15%",
        bar_gap=6,
        bar_size=100,
        max_bar_size=40,
        width="100%",
        height=300,
    )
```

## Vertical Example

The `layout` prop allows you to set the orientation of the graph to be vertical or horizontal, it is set horizontally by default.

```md alert info
# Include margins around your graph to ensure proper spacing and enhance readability. By default, provide margins on all sides of the chart to create a visually appealing and functional representation of your data.
```

```python demo graphing
data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def bar_vertical():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="uv",
            stroke=rx.color("accent", 8),
            fill=rx.color("accent", 3),
        ),
        rx.recharts.x_axis(type_="number"),
        rx.recharts.y_axis(data_key="name", type_="category"),
        data=data,
        layout="vertical",
        margin={
            "top": 20,
            "right": 20,
            "left": 20,
            "bottom": 20
        },
        width = "100%",
        height = 300,

    )
```

To learn how to use the `sync_id`, `stack_id`,`x_axis_id` and `y_axis_id` props check out the of the area chart [documentation]({library.graphing.charts.areachart.path}), where these props are all described with examples.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/charts/scatterchart.md`:

```md
---
components:
  - rx.recharts.ScatterChart
  - rx.recharts.Scatter
---

# Scatter Chart


A scatter chart always has two value axes to show one set of numerical data along a horizontal (value) axis and another set of numerical values along a vertical (value) axis. The chart displays points at the intersection of an x and y numerical value, combining these values into single data points.

## Simple Example

For a scatter chart we must define an `rx.recharts.scatter()` component for each set of values we wish to plot. Each `rx.recharts.scatter()` component has a `data` prop which clearly states which data source we plot. We also must define `rx.recharts.x_axis()` and `rx.recharts.y_axis()` so that the graph knows what data to plot on each axis.

```python demo graphing
data01 = [
  {
    "x": 100,
    "y": 200,
    "z": 200
  },
  {
    "x": 120,
    "y": 100,
    "z": 260
  },
  {
    "x": 170,
    "y": 300,
    "z": 400
  },
  {
    "x": 170,
    "y": 250,
    "z": 280
  },
  {
    "x": 150,
    "y": 400,
    "z": 500
  },
  {
    "x": 110,
    "y": 280,
    "z": 200
  }
]

def scatter_simple():
  return rx.recharts.scatter_chart(
    rx.recharts.scatter(
        data=data01,
        fill="#8884d8",),
    rx.recharts.x_axis(data_key="x", type_="number"),
    rx.recharts.y_axis(data_key="y"),
    width = "100%",
    height = 300,
  )
```

## Multiple Scatters

We can also add two scatters on one chart by using two `rx.recharts.scatter()` components, and we can define an `rx.recharts.z_axis()` which represents a third column of data and is represented by the size of the dots in the scatter plot.

```python demo graphing
data01 = [
  {
    "x": 100,
    "y": 200,
    "z": 200
  },
  {
    "x": 120,
    "y": 100,
    "z": 260
  },
  {
    "x": 170,
    "y": 300,
    "z": 400
  },
  {
    "x": 170,
    "y": 250,
    "z": 280
  },
  {
    "x": 150,
    "y": 350,
    "z": 500
  },
  {
    "x": 110,
    "y": 280,
    "z": 200
  }
]

data02 = [
  {
    "x": 200,
    "y": 260,
    "z": 240
  },
  {
    "x": 240,
    "y": 290,
    "z": 220
  },
  {
    "x": 190,
    "y": 290,
    "z": 250
  },
  {
    "x": 198,
    "y": 250,
    "z": 210
  },
  {
    "x": 180,
    "y": 280,
    "z": 260
  },
  {
    "x": 210,
    "y": 220,
    "z": 230
  }
]

def scatter_double():
  return rx.recharts.scatter_chart(
    rx.recharts.scatter(
        data=data01,
        fill="#8884d8",
        name="A"
      ),
    rx.recharts.scatter(
        data=data02,
        fill="#82ca9d",
        name="B"
      ),
    rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
    rx.recharts.x_axis(data_key="x", type_="number"),
    rx.recharts.y_axis(data_key="y"),
    rx.recharts.z_axis(data_key="z", range=[60, 400], name="score"),
    rx.recharts.legend(),
    rx.recharts.graphing_tooltip(),
    width="100%",
    height=300,
  )
```

To learn how to use the `x_axis_id` and `y_axis_id` props, check out the Multiple Axis section of the area chart [documentation]({library.graphing.charts.areachart.path}).

## Dynamic Data

Chart data tied to a State var causes the chart to automatically update when the
state changes, providing a nice way to visualize data in response to user
interface elements. View the "Data" tab to see the substate driving this
calculation of iterations in the Collatz Conjecture for a given starting number.
Enter a starting number in the box below the chart to recalculate.

```python demo exec
class ScatterChartState(rx.State):
    data: list[dict[str, int]] = []

    @rx.event
    def compute_collatz(self, form_data: dict) -> int:
        n = int(form_data.get("start") or 1)
        yield rx.set_value("start", "")
        self.data = []
        for ix in range(400):
            self.data.append({"x": ix, "y": n})
            if n == 1:
                break
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1


def scatter_dynamic():
    return rx.vstack(
        rx.recharts.scatter_chart(
            rx.recharts.scatter(
                data=ScatterChartState.data,
                fill="#8884d8",
            ),
            rx.recharts.x_axis(data_key="x", type_="number"),
            rx.recharts.y_axis(data_key="y", type_="number"),
        ),
        rx.form.root(
            rx.input(placeholder="Enter a number", id="start"),
            rx.button("Compute", type="submit"),
            on_submit=ScatterChartState.compute_collatz,
        ),
        width="100%",
        height="15em",
        on_mount=ScatterChartState.compute_collatz({"start": "15"}),
    )
```

## Legend Type and Shape

```python demo exec
class ScatterChartState2(rx.State):

    legend_types: list[str] = ["square", "circle", "cross", "diamond", "star", "triangle", "wye"]

    legend_type: str = "circle"

    shapes: list[str] = ["square", "circle", "cross", "diamond", "star", "triangle", "wye"]

    shape: str = "circle"

    data01 = [
    {
      "x": 100,
      "y": 200,
      "z": 200
    },
    {
      "x": 120,
      "y": 100,
      "z": 260
    },
    {
      "x": 170,
      "y": 300,
      "z": 400
    },
    {
      "x": 170,
      "y": 250,
      "z": 280
    },
    {
      "x": 150,
      "y": 400,
      "z": 500
    },
    {
      "x": 110,
      "y": 280,
      "z": 200
    }
  ]


def scatter_shape():
  return rx.vstack(
      rx.recharts.scatter_chart(
          rx.recharts.scatter(
              data=data01,
              fill="#8884d8",
              legend_type=ScatterChartState2.legend_type,
              shape=ScatterChartState2.shape,
          ),
          rx.recharts.x_axis(data_key="x", type_="number"),
          rx.recharts.y_axis(data_key="y"),
          rx.recharts.legend(),
          width = "100%",
          height = 300,
        ),
      rx.hstack(
          rx.text("Legend Type: "),
          rx.select(
              ScatterChartState2.legend_types,
              value=ScatterChartState2.legend_type,
              on_change=ScatterChartState2.set_legend_type,
          ),
          rx.text("Shape: "),
          rx.select(
            ScatterChartState2.shapes,
            value=ScatterChartState2.shape,
            on_change=ScatterChartState2.set_shape,
          ),
      ),
      width="100%",
  )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/charts/funnelchart.md`:

```md
---
components:
  - rx.recharts.FunnelChart
  - rx.recharts.Funnel
---


# Funnel Chart

A funnel chart is a graphical representation used to visualize how data moves through a process. In a funnel chart, the dependent variable’s value diminishes in the subsequent stages of the process. It can be used to demonstrate the flow of users through a business or sales process.

## Simple Example

```python demo graphing
data = [
  {
    "value": 100,
    "name": "Sent",
    "fill": "#8884d8"
  },
  {
    "value": 80,
    "name": "Viewed",
    "fill": "#83a6ed"
  },
  {
    "value": 50,
    "name": "Clicked",
    "fill": "#8dd1e1"
  },
  {
    "value": 40,
    "name": "Add to Cart",
    "fill": "#82ca9d"
  },
  {
    "value": 26,
    "name": "Purchased",
    "fill": "#a4de6c"
  }
]

def funnel_simple():
    return rx.recharts.funnel_chart(
        rx.recharts.funnel(
            rx.recharts.label_list(
                position="right",
                data_key="name",
                fill="#000",
                stroke="none",
            ),
            data_key="value",
            data=data,
        ),
        width="100%",
        height=250,
    )
```

## Event Triggers

Funnel chart supports `on_click`, `on_mouse_enter`, `on_mouse_leave` and `on_mouse_move` event triggers, allows you to interact with the funnel chart and perform specific actions based on user interactions.

```python demo graphing
data = [
  {
    "value": 100,
    "name": "Sent",
    "fill": "#8884d8"
  },
  {
    "value": 80,
    "name": "Viewed",
    "fill": "#83a6ed"
  },
  {
    "value": 50,
    "name": "Clicked",
    "fill": "#8dd1e1"
  },
  {
    "value": 40,
    "name": "Add to Cart",
    "fill": "#82ca9d"
  },
  {
    "value": 26,
    "name": "Purchased",
    "fill": "#a4de6c"
  }
]

def funnel_events():
    return rx.recharts.funnel_chart(
        rx.recharts.funnel(
            rx.recharts.label_list(
                position="right",
                data_key="name",
                fill="#000",
                stroke="none",
            ),
            data_key="value",
            data=data,
        ),
        on_click=rx.toast("Clicked on funnel chart"),
        on_mouse_enter=rx.toast("Mouse entered"),
        on_mouse_leave=rx.toast("Mouse left"),
        width="100%",
        height=250,
    )
```

## Dynamic Data

Here is an example of a funnel chart with a `State`. Here we have defined a function `randomize_data`, which randomly changes the data when the graph is clicked on using `on_click=FunnelState.randomize_data`.


```python demo exec
class FunnelState(rx.State):
    data = data

    @rx.event
    def randomize_data(self):
        self.data[0]["value"] = 100
        for i in range(len(self.data) - 1):
            self.data[i + 1]["value"] = self.data[i][
                "value"
            ] - random.randint(0, 20)


def funnel_state():
  return rx.recharts.funnel_chart(
    rx.recharts.funnel(
      rx.recharts.label_list(
        position="right",
        data_key="name",
        fill="#000",
        stroke="none",
      ),
      data_key="value",
      data=FunnelState.data,
      on_click=FunnelState.randomize_data,
    ),
    rx.recharts.graphing_tooltip(),
    width="100%",
    height=250,
  )
```

## Changing the Chart Animation

The `is_animation_active` prop can be used to turn off the animation, but defaults to `True`. `animation_begin` sets the delay before animation starts, `animation_duration` determines how long the animation lasts, and `animation_easing` defines the speed curve of the animation for smooth transitions.

```python demo graphing
data = [
        {"name": "Visits", "value": 5000, "fill": "#8884d8"},
        {"name": "Cart", "value": 3000, "fill": "#83a6ed"},
        {"name": "Checkout", "value": 2500, "fill": "#8dd1e1"},
        {"name": "Purchase", "value": 1000, "fill": "#82ca9d"},
    ]

def funnel_animation():
    return rx.recharts.funnel_chart(
        rx.recharts.funnel(
            data_key="value",
            data=data,
            animation_begin=300,
            animation_duration=9000,
            animation_easing="ease-in-out",
        ),
        rx.recharts.graphing_tooltip(),
        rx.recharts.legend(),
        width="100%",
        height=300,
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/charts/piechart.md`:

```md
---
components:
  - rx.recharts.PieChart
  - rx.recharts.Pie
---

# Pie Chart


A pie chart is a circular statistical graphic which is divided into slices to illustrate numerical proportion.

For a pie chart we must define an `rx.recharts.pie()` component for each set of values we wish to plot. Each `rx.recharts.pie()` component has a `data`, a `data_key` and a `name_key` which clearly states which data and which variables in our data we are tracking. In this simple example we plot `value` column as our `data_key` against the `name` column which we set as our `name_key`.
We also use the `fill` prop to set the color of the pie slices.

```python demo graphing

data01 = [
  {
    "name": "Group A",
    "value": 400
  },
  {
    "name": "Group B",
    "value": 300,
    "fill":"#AC0E08FF"
  },
  {
    "name": "Group C",
    "value": 300,
    "fill":"rgb(80,40, 190)"
  },
  {
    "name": "Group D",
    "value": 200,
    "fill":rx.color("yellow", 10)
  },
  {
    "name": "Group E",
    "value": 278,
    "fill":"purple"
  },
  {
    "name": "Group F",
    "value": 189,
    "fill":"orange"
  }
]

def pie_simple():
  return rx.recharts.pie_chart(
            rx.recharts.pie(
                data=data01,
                data_key="value",
                name_key="name",
                fill="#8884d8",
                label=True,
            ),
            width="100%",
            height=300,
        )
```

We can also add two pies on one chart by using two `rx.recharts.pie` components.

In this example `inner_radius` and `outer_radius` props are used. They define the doughnut shape of a pie chart: `inner_radius` creates the hollow center (use "0%" for a full pie), while `outer_radius` sets the overall size. The `padding_angle` prop, used on the green pie below, adds space between pie slices, enhancing visibility of individual segments.

```python demo graphing

data01 = [
  {
    "name": "Group A",
    "value": 400
  },
  {
    "name": "Group B",
    "value": 300
  },
  {
    "name": "Group C",
    "value": 300
  },
  {
    "name": "Group D",
    "value": 200
  },
  {
    "name": "Group E",
    "value": 278
  },
  {
    "name": "Group F",
    "value": 189
  }
]
data02 = [
  {
    "name": "Group A",
    "value": 2400
  },
  {
    "name": "Group B",
    "value": 4567
  },
  {
    "name": "Group C",
    "value": 1398
  },
  {
    "name": "Group D",
    "value": 9800
  },
  {
    "name": "Group E",
    "value": 3908
  },
  {
    "name": "Group F",
    "value": 4800
  }
]


def pie_double():
  return rx.recharts.pie_chart(
            rx.recharts.pie(
                data=data01,
                data_key="value",
                name_key="name",
                fill="#82ca9d",
                inner_radius="60%",
                padding_angle=5,
            ),
            rx.recharts.pie(
                data=data02,
                data_key="value",
                name_key="name",
                fill="#8884d8",
                outer_radius="50%",
            ),
            rx.recharts.graphing_tooltip(),
            width="100%",
            height=300,
        )
```

## Dynamic Data

Chart data tied to a State var causes the chart to automatically update when the
state changes, providing a nice way to visualize data in response to user
interface elements. View the "Data" tab to see the substate driving this
half-pie chart.

```python demo exec
from typing import Any


class PieChartState(rx.State):
    resources: list[dict[str, Any]] = [
        dict(type_="🏆", count=1),
        dict(type_="🪵", count=1),
        dict(type_="🥑", count=1),
        dict(type_="🧱", count=1),
    ]

    @rx.var(cache=True)
    def resource_types(self) -> list[str]:
        return [r["type_"] for r in self.resources]

    @rx.event
    def increment(self, type_: str):
        for resource in self.resources:
            if resource["type_"] == type_:
                resource["count"] += 1
                break

    @rx.event
    def decrement(self, type_: str):
        for resource in self.resources:
            if resource["type_"] == type_ and resource["count"] > 0:
                resource["count"] -= 1
                break


def dynamic_pie_example():
    return rx.hstack(
        rx.recharts.pie_chart(
            rx.recharts.pie(
                data=PieChartState.resources,
                data_key="count",
                name_key="type_",
                cx="50%",
                cy="50%",
                start_angle=180,
                end_angle=0,
                fill="#8884d8",
                label=True,
            ),
            rx.recharts.graphing_tooltip(),
        ),
        rx.vstack(
            rx.foreach(
                PieChartState.resource_types,
                lambda type_, i: rx.hstack(
                    rx.button("-", on_click=PieChartState.decrement(type_)),
                    rx.text(type_, PieChartState.resources[i]["count"]),
                    rx.button("+", on_click=PieChartState.increment(type_)),
                ),
            ),
        ),
        width="100%",
        height="15em",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/charts/errorbar.md`:

```md
---
components:
    - rx.recharts.ErrorBar
---


# Error Bar

An error bar is a graphical representation of the uncertainty or variability of a data point in a chart, depicted as a line extending from the data point parallel to one of the axes. The `data_key`, `width`, `stroke_width`, `stroke`, and `direction` props can be used to customize the appearance and behavior of the error bars, specifying the data source, dimensions, color, and orientation of the error bars.

```python demo graphing
data = [
  {
    "x": 45,
    "y": 100,
    "z": 150,
    "errorY": [
      30,
      20
    ],
    "errorX": 5
  },
  {
    "x": 100,
    "y": 200,
    "z": 200,
    "errorY": [
      20,
      30
    ],
    "errorX": 3
  },
  {
    "x": 120,
    "y": 100,
    "z": 260,
    "errorY": 20,
    "errorX": [
      5,
      3
    ]
  },
  {
    "x": 170,
    "y": 300,
    "z": 400,
    "errorY": [
      15,
      18
    ],
    "errorX": 4
  },
  {
    "x": 140,
    "y": 250,
    "z": 280,
    "errorY": 23,
    "errorX": [
      6,
      7
    ]
  },
  {
    "x": 150,
    "y": 400,
    "z": 500,
    "errorY": [
      21,
      10
    ],
    "errorX": 4
  },
  {
    "x": 110,
    "y": 280,
    "z": 200,
    "errorY": 21,
    "errorX": [
      5,
      6
    ]
  }
]

def error():
  return rx.recharts.scatter_chart(
    rx.recharts.scatter(
        rx.recharts.error_bar(data_key="errorY", direction="y", width=4, stroke_width=2, stroke="red"),
        rx.recharts.error_bar(data_key="errorX", direction="x", width=4, stroke_width=2),
        data=data,
        fill="#8884d8",
        name="A"),
    rx.recharts.x_axis(data_key="x", name="x", type_="number"), 
    rx.recharts.y_axis(data_key="y", name="y", type_="number"),
    width = "100%",
    height = 300,
  )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/charts/composedchart.md`:

```md
---
components:
    - rx.recharts.ComposedChart
---

# Composed Chart

A `composed_chart` is a higher-level component chart that is composed of multiple charts, where other charts are the children of the `composed_chart`. The charts are placed on top of each other in the order they are provided in the `composed_chart` function.


```md alert info
# To learn more about individual charts, checkout: **[area_chart]({library.graphing.charts.areachart.path})**, **[line_chart]({library.graphing.charts.linechart.path})**, or **[bar_chart]({library.graphing.charts.barchart.path})**. 
```

```python demo graphing
data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def composed():
  return rx.recharts.composed_chart(
    rx.recharts.area(
        data_key="uv",
        stroke="#8884d8",
        fill="#8884d8"
    ), 
    rx.recharts.bar(
        data_key="amt",
        bar_size=20,
        fill="#413ea0"
    ),
    rx.recharts.line(
        data_key="pv",
        type_="monotone",
        stroke="#ff7300"
    ), 
    rx.recharts.x_axis(data_key="name"), 
    rx.recharts.y_axis(),
    rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
    rx.recharts.graphing_tooltip(),
    data=data,
    height=250,
    width="100%",
  )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/charts/areachart.md`:

```md
---
components:
  - rx.recharts.AreaChart
  - rx.recharts.Area
---

# Area Chart


A Recharts area chart displays quantitative data using filled areas between a line connecting data points and the axis.

## Basic Example

```python demo graphing
data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def area_simple():
  return rx.recharts.area_chart(
    rx.recharts.area(
        data_key="uv",
    ),
    rx.recharts.x_axis(data_key="name"),
    rx.recharts.y_axis(),
    data=data,
    width = "100%",
    height = 250,
  )
```

## Syncing Charts

The `sync_id` prop allows you to sync two graphs. In the example, it is set to "1" for both charts, indicating that they should be synchronized. This means that any interactions (such as brushing) performed on one chart will be reflected in the other chart.

```python demo graphing
data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def area_sync():
  return rx.vstack(
    rx.recharts.bar_chart(
      rx.recharts.graphing_tooltip(),
      rx.recharts.bar(
          data_key="uv", stroke="#8884d8", fill="#8884d8"
      ),
      rx.recharts.bar(
          data_key="pv", stroke="#82ca9d", fill="#82ca9d",
      ),
      rx.recharts.x_axis(data_key="name"),
      rx.recharts.y_axis(),
      data=data,
      sync_id="1",
      width = "100%",
      height = 200,
    ),
    rx.recharts.composed_chart(
      rx.recharts.area(
          data_key="uv", stroke="#8884d8", fill="#8884d8"
      ),
      rx.recharts.line(
          data_key="pv", type_="monotone", stroke="#ff7300",
      ),

      rx.recharts.x_axis(data_key="name"),
      rx.recharts.y_axis(),
      rx.recharts.graphing_tooltip(),
      rx.recharts.brush(
          data_key="name", height=30, stroke="#8884d8"
      ),
      data=data,
      sync_id="1",
      width = "100%",
      height = 250,
    ),
    width="100%",
  )
```

## Stacking Charts

The `stack_id` prop allows you to stack multiple graphs on top of each other. In the example, it is set to "1" for both charts, indicating that they should be stacked together. This means that the bars or areas of the charts will be vertically stacked, with the values of each chart contributing to the total height of the stacked areas or bars.

This is similar to the `sync_id` prop, but instead of synchronizing the interaction between the charts, it just stacks the charts on top of each other.

```python demo graphing

data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def area_stack():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
            stack_id="1",
        ),
        rx.recharts.area(
            data_key="pv",
            stroke=rx.color("green", 9),
            fill=rx.color("green", 8),
            stack_id="1",
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        stack_offset="none",
        margin={"top": 5, "right": 5, "bottom": 5, "left": 5},
        width = "100%",
        height = 300,
    )
```

## Multiple Axis

Multiple axes can be used for displaying different data series with varying scales or units on the same chart. This allows for a more comprehensive comparison and analysis of the data.

```python demo graphing

data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def area_multi_axis():
  return rx.recharts.area_chart(
    rx.recharts.area(
        data_key="uv", stroke="#8884d8", fill="#8884d8", x_axis_id="primary", y_axis_id="left",
    ),
    rx.recharts.area(
        data_key="pv", x_axis_id="secondary", y_axis_id="right", type_="monotone", stroke="#82ca9d", fill="#82ca9d"
    ),
    rx.recharts.x_axis(data_key="name", x_axis_id="primary"),
    rx.recharts.x_axis(data_key="name", x_axis_id="secondary", orientation="top"),
    rx.recharts.y_axis(data_key="uv", y_axis_id="left"),
    rx.recharts.y_axis(data_key="pv", y_axis_id="right", orientation="right"),
    rx.recharts.graphing_tooltip(),
    rx.recharts.legend(),
    data=data,
    width = "100%",
    height = 300,
  )
```

## Layout

Use the `layout` prop to set the orientation to either `"horizontal"` (default) or `"vertical"`.

```md alert info
# Include margins around your graph to ensure proper spacing and enhance readability. By default, provide margins on all sides of the chart to create a visually appealing and functional representation of your data.
```

```python demo graphing

data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def area_vertical():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv",
            stroke=rx.color("accent", 8),
            fill=rx.color("accent", 3),
        ),
        rx.recharts.x_axis(type_="number"),
        rx.recharts.y_axis(data_key="name", type_="category"),
        data=data,
        layout="vertical",
        height = 300,
        width = "100%",
    )
```

## Stateful Example

Here is an example of an area graph with a `State`. Here we have defined a function `randomize_data`, which randomly changes the data for both graphs when the first defined `area` is clicked on using `on_click=AreaState.randomize_data`.

```python demo exec
class AreaState(rx.State):
    data = data
    curve_type = ""

    @rx.event
    def randomize_data(self):
        for i in range(len(self.data)):
            self.data[i]["uv"] = random.randint(0, 10000)
            self.data[i]["pv"] = random.randint(0, 10000)
            self.data[i]["amt"] = random.randint(0, 10000)

    def change_curve_type(self, type_input):
        self.curve_type = type_input

def area_stateful():
    return rx.vstack(
      rx.hstack(
        rx.text("Curve Type:"),
        rx.select(
          [
            'basis',
            'natural',
            'step'
          ],
          on_change = AreaState.change_curve_type,
          default_value = 'basis',
        ),
      ),
      rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv",
            on_click=AreaState.randomize_data,
            type_ = AreaState.curve_type,
        ),
        rx.recharts.area(
            data_key="pv",
            stroke="#82ca9d",
            fill="#82ca9d",
            on_click=AreaState.randomize_data,
            type_ = AreaState.curve_type,
        ),
        rx.recharts.x_axis(
            data_key="name",
        ),
        rx.recharts.y_axis(),
        rx.recharts.legend(),
        rx.recharts.cartesian_grid(),
        data=AreaState.data,
        width = "100%",
        height=400,
      ),
      width="100%",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/graphing/charts/radarchart.md`:

```md
---
components:
  - rx.recharts.RadarChart
  - rx.recharts.Radar
---

# Radar Chart


A radar chart shows multivariate data of three or more quantitative variables mapped onto an axis.

## Simple Example

For a radar chart we must define an `rx.recharts.radar()` component for each set of values we wish to plot. Each `rx.recharts.radar()` component has a `data_key` which clearly states which variable in our data we are plotting. In this simple example we plot the `A` column of our data against the `subject` column which we set as the `data_key` in `rx.recharts.polar_angle_axis`.

```python demo graphing
data = [
  {
    "subject": "Math",
    "A": 120,
    "B": 110,
    "fullMark": 150
  },
  {
    "subject": "Chinese",
    "A": 98,
    "B": 130,
    "fullMark": 150
  },
  {
    "subject": "English",
    "A": 86,
    "B": 130,
    "fullMark": 150
  },
  {
    "subject": "Geography",
    "A": 99,
    "B": 100,
    "fullMark": 150
  },
  {
    "subject": "Physics",
    "A": 85,
    "B": 90,
    "fullMark": 150
  },
  {
    "subject": "History",
    "A": 65,
    "B": 85,
    "fullMark": 150
  }
]

def radar_simple():
    return rx.recharts.radar_chart(
        rx.recharts.radar(
            data_key="A",
            stroke="#8884d8",
            fill="#8884d8",
        ),
        rx.recharts.polar_grid(),
        rx.recharts.polar_angle_axis(data_key="subject"),
        rx.recharts.polar_radius_axis(angle=90, domain=[0, 150]),
        data=data,
        width="100%",
        height=300,
    )
```

## Multiple Radars

We can also add two radars on one chart by using two `rx.recharts.radar` components.

In this plot an `inner_radius` and an `outer_radius` are set which determine the chart's size and shape. The `inner_radius` sets the distance from the center to the innermost part of the chart (creating a hollow center if greater than zero), while the `outer_radius` defines the chart's overall size by setting the distance from the center to the outermost edge of the radar plot.

```python demo graphing

data = [
  {
    "subject": "Math",
    "A": 120,
    "B": 110,
    "fullMark": 150
  },
  {
    "subject": "Chinese",
    "A": 98,
    "B": 130,
    "fullMark": 150
  },
  {
    "subject": "English",
    "A": 86,
    "B": 130,
    "fullMark": 150
  },
  {
    "subject": "Geography",
    "A": 99,
    "B": 100,
    "fullMark": 150
  },
  {
    "subject": "Physics",
    "A": 85,
    "B": 90,
    "fullMark": 150
  },
  {
    "subject": "History",
    "A": 65,
    "B": 85,
    "fullMark": 150
  }
]

def radar_multiple():
    return rx.recharts.radar_chart(
        rx.recharts.radar(
            data_key="A",
            stroke="#8884d8",
            fill="#8884d8",
        ),
        rx.recharts.radar(
            data_key="B",
            stroke="#82ca9d",
            fill="#82ca9d",
            fill_opacity=0.6,
        ),
        rx.recharts.polar_grid(),
        rx.recharts.polar_angle_axis(data_key="subject"),
        rx.recharts.polar_radius_axis(angle=90, domain=[0, 150]),
        rx.recharts.legend(),
        data=data,
        inner_radius="15%",
        outer_radius="80%",
        width="100%",
        height=300,
    )

```

## Using More Props

The `dot` prop shows points at each data vertex when true. `legend_type="line"` displays a line in the chart legend. `animation_begin=0` starts the animation immediately, `animation_duration=8000` sets an 8-second animation, and `animation_easing="ease-in"` makes the animation start slowly and speed up. These props control the chart's appearance and animation behavior.

```python demo graphing

data = [
    {
        "subject": "Math",
        "A": 120,
        "B": 110,
        "fullMark": 150
    },
    {
        "subject": "Chinese",
        "A": 98,
        "B": 130,
        "fullMark": 150
    },
    {
        "subject": "English",
        "A": 86,
        "B": 130,
        "fullMark": 150
    },
    {
        "subject": "Geography",
        "A": 99,
        "B": 100,
        "fullMark": 150
    },
    {
        "subject": "Physics",
        "A": 85,
        "B": 90,
        "fullMark": 150
    },
    {
        "subject": "History",
        "A": 65,
        "B": 85,
        "fullMark": 150
    }
    ]


def radar_start_end():
    return rx.recharts.radar_chart(
            rx.recharts.radar(
                data_key="A",
                dot=True,
                stroke="#8884d8",
                fill="#8884d8",
                fill_opacity=0.6,
                legend_type="line",
                animation_begin=0,
                animation_duration=8000,
                animation_easing="ease-in",
            ),
            rx.recharts.polar_grid(),
            rx.recharts.polar_angle_axis(data_key="subject"),
            rx.recharts.polar_radius_axis(angle=90, domain=[0, 150]),
            rx.recharts.legend(),
            data=data,
            width="100%",
            height=300,
        )

```

# Dynamic Data

Chart data tied to a State var causes the chart to automatically update when the
state changes, providing a nice way to visualize data in response to user
interface elements. View the "Data" tab to see the substate driving this
radar chart of character traits.

```python demo exec
class RadarChartState(rx.State):
    total_points: int = 100
    traits: list[dict[str, Any]] = [
        dict(trait="Strength", value=15),
        dict(trait="Dexterity", value=15),
        dict(trait="Constitution", value=15),
        dict(trait="Intelligence", value=15),
        dict(trait="Wisdom", value=15),
        dict(trait="Charisma", value=15),
    ]

    @rx.var
    def remaining_points(self) -> int:
        return self.total_points - sum(t["value"] for t in self.traits)

    @rx.var(cache=True)
    def trait_names(self) -> list[str]:
        return [t["trait"] for t in self.traits]

    @rx.event
    def set_trait(self, trait: str, value: int):
        for t in self.traits:
            if t["trait"] == trait:
                available_points = self.remaining_points + t["value"]
                value = min(value, available_points)
                t["value"] = value
                break

def radar_dynamic():
    return rx.hstack(
        rx.recharts.radar_chart(
            rx.recharts.radar(
                data_key="value",
                stroke="#8884d8",
                fill="#8884d8",
            ),
            rx.recharts.polar_grid(),
            rx.recharts.polar_angle_axis(data_key="trait"),
            data=RadarChartState.traits,
        ),
        rx.vstack(
            rx.foreach(
                RadarChartState.trait_names,
                lambda trait_name, i: rx.hstack(
                    rx.text(trait_name, width="7em"),
                    rx.slider(
                        default_value=RadarChartState.traits[i]["value"].to(int),
                        on_change=lambda value: RadarChartState.set_trait(trait_name, value),
                        width="25vw",
                    ),
                    rx.text(RadarChartState.traits[i]['value']),
                ),
            ),
            rx.text("Remaining points: ", RadarChartState.remaining_points),
        ),
        width="100%",
        height="15em",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/overlay/drawer.md`:

```md
---
components:
  - rx.drawer.root
  - rx.drawer.trigger
  - rx.drawer.overlay
  - rx.drawer.portal
  - rx.drawer.content
  - rx.drawer.close

only_low_level:
  - True

DrawerRoot: |
  lambda **props: rx.drawer.root(
      rx.drawer.trigger(rx.button("Open Drawer")),
      rx.drawer.overlay(z_index="5"),
      rx.drawer.portal(
          rx.drawer.content(
              rx.flex(
                  rx.drawer.close(rx.button("Close")),
              ),
              height="100%",
              width="20em",
              background_color="#FFF"
          ),
      ),
      **props,
  )
---


# Drawer

```python demo
rx.drawer.root(
        rx.drawer.trigger(
            rx.button("Open Drawer")
        ),
        rx.drawer.overlay(
            z_index="5"
        ),
        rx.drawer.portal(
            rx.drawer.content(
                rx.flex(
                    rx.drawer.close(rx.box(rx.button("Close"))),
                    align_items="start",
                    direction="column",
                ),
                top="auto",
                right="auto",
                height="100%",
                width="20em",
                padding="2em",
                background_color="#FFF"
                #background_color=rx.color("green", 3)
            )
        ),
        direction="left",
)
```

## Sidebar Menu with a Drawer and State

This example shows how to create a sidebar menu with a drawer. The drawer is opened by clicking a button. The drawer contains links to different sections of the page. When a link is clicked the drawer closes and the page scrolls to the section.

The `rx.drawer.root` component has an `open` prop that is set by the state variable `is_open`. Setting the `modal` prop to `False` allows the user to interact with the rest of the page while the drawer is open and allows the page to be scrolled when a user clicks one of the links.

```python demo exec
class DrawerState(rx.State):
    is_open: bool = False

    @rx.event
    def toggle_drawer(self):
        self.is_open = not self.is_open

def drawer_content():
    return rx.drawer.content(
        rx.flex(
            rx.drawer.close(rx.button("Close", on_click=DrawerState.toggle_drawer)),
            rx.link("Link 1", href="#test1", on_click=DrawerState.toggle_drawer),
            rx.link("Link 2", href="#test2", on_click=DrawerState.toggle_drawer),
            align_items="start",
            direction="column",
        ),
        height="100%",
        width="20%",
        padding="2em",
        background_color=rx.color("grass", 7),
    )


def lateral_menu():
    return rx.drawer.root(
        rx.drawer.trigger(rx.button("Open Drawer", on_click=DrawerState.toggle_drawer)),
        rx.drawer.overlay(),
        rx.drawer.portal(drawer_content()),
        open=DrawerState.is_open,
        direction="left",
        modal=False,
    )

def drawer_sidebar():
    return rx.vstack(
        lateral_menu(),
        rx.section(
            rx.heading("Test1", size="8"),
            id='test1',
            height="400px",
        ),
        rx.section(
            rx.heading("Test2", size="8"),
            id='test2',
            height="400px",
        )
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/overlay/alert_dialog.md`:

```md
---
components:
  - rx.alert_dialog.root
  - rx.alert_dialog.content
  - rx.alert_dialog.trigger
  - rx.alert_dialog.title
  - rx.alert_dialog.description
  - rx.alert_dialog.action
  - rx.alert_dialog.cancel

only_low_level:
  - True

AlertDialogRoot: |
  lambda **props: rx.alert_dialog.root(
      rx.alert_dialog.trigger(
          rx.button("Revoke access"),
      ),
      rx.alert_dialog.content(
          rx.alert_dialog.title("Revoke access"),
          rx.alert_dialog.description(
              "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
          ),
          rx.flex(
              rx.alert_dialog.cancel(
                  rx.button("Cancel"),
              ),
              rx.alert_dialog.action(
                  rx.button("Revoke access"),
              ),
              spacing="3",
          ),
      ),
      **props
  )

AlertDialogContent: |
  lambda **props: rx.alert_dialog.root(
      rx.alert_dialog.trigger(
          rx.button("Revoke access"),
      ),
      rx.alert_dialog.content(
          rx.alert_dialog.title("Revoke access"),
          rx.alert_dialog.description(
              "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
          ),
          rx.flex(
              rx.alert_dialog.cancel(
                  rx.button("Cancel"),
              ),
              rx.alert_dialog.action(
                  rx.button("Revoke access"),
              ),
              spacing="3",
          ),
          **props
      ),
  )
---


# Alert Dialog

An alert dialog is a modal confirmation dialog that interrupts the user and expects a response.

The `alert_dialog.root` contains all the parts of the dialog.

The `alert_dialog.trigger` wraps the control that will open the dialog.

The `alert_dialog.content` contains the content of the dialog.

The `alert_dialog.title` is the title that is announced when the dialog is opened.

The `alert_dialog.description` is an optional description that is announced when the dialog is opened.

The `alert_dialog.action` wraps the control that will close the dialog. This should be distinguished visually from the `alert_dialog.cancel` control.

The `alert_dialog.cancel` wraps the control that will close the dialog. This should be distinguished visually from the `alert_dialog.action` control.

## Basic Example

```python demo
rx.alert_dialog.root(
    rx.alert_dialog.trigger(
        rx.button("Revoke access"),
    ),
    rx.alert_dialog.content(
        rx.alert_dialog.title("Revoke access"),
        rx.alert_dialog.description(
            "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
        ),
        rx.flex(
            rx.alert_dialog.cancel(
                rx.button("Cancel"),
            ),
            rx.alert_dialog.action(
                rx.button("Revoke access"),
            ),
            spacing="3",
        ),
    ),
)
```

This example has a different color scheme and the `cancel` and `action` buttons are right aligned.

```python demo
rx.alert_dialog.root(
    rx.alert_dialog.trigger(
        rx.button("Revoke access", color_scheme="red"),
    ),
    rx.alert_dialog.content(
        rx.alert_dialog.title("Revoke access"),
        rx.alert_dialog.description(
            "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
            size="2",
        ),
        rx.flex(
            rx.alert_dialog.cancel(
                rx.button("Cancel", variant="soft", color_scheme="gray"),
            ),
            rx.alert_dialog.action(
                rx.button("Revoke access", color_scheme="red", variant="solid"),
            ),
            spacing="3",
            margin_top="16px",
            justify="end",
        ),
        style={"max_width": 450},
    ),
)
```

Use the `inset` component to align content flush with the sides of the dialog.

```python demo
rx.alert_dialog.root(
    rx.alert_dialog.trigger(
        rx.button("Delete Users", color_scheme="red"),
    ),
    rx.alert_dialog.content(
        rx.alert_dialog.title("Delete Users"),
        rx.alert_dialog.description(
            "Are you sure you want to delete these users? This action is permanent and cannot be undone.",
            size="2",
        ),
        rx.inset(
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Full Name"),
                        rx.table.column_header_cell("Email"),
                        rx.table.column_header_cell("Group"),
                    ),
                ),
                rx.table.body(
                    rx.table.row(
                        rx.table.row_header_cell("Danilo Rosa"),
                        rx.table.cell("danilo@example.com"),
                        rx.table.cell("Developer"),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("Zahra Ambessa"),
                        rx.table.cell("zahra@example.com"),
                        rx.table.cell("Admin"),
                    ),
                ),
            ),
            side="x",
            margin_top="24px",
            margin_bottom="24px",
        ),
        rx.flex(
            rx.alert_dialog.cancel(
                rx.button("Cancel", variant="soft", color_scheme="gray"),
            ),
            rx.alert_dialog.action(
                rx.button("Delete users", color_scheme="red"),
            ),
            spacing="3",
            justify="end",
        ),
        style={"max_width": 500},
    ),
)
```

## Events when the Alert Dialog opens or closes

The `on_open_change` event is called when the `open` state of the dialog changes. It is used in conjunction with the `open` prop.

```python demo exec
class AlertDialogState(rx.State):
    num_opens: int = 0
    opened: bool = False

    @rx.event
    def count_opens(self, value: bool):
        self.opened = value
        self.num_opens += 1


def alert_dialog():
    return rx.flex(
        rx.heading(f"Number of times alert dialog opened or closed: {AlertDialogState.num_opens}"),
        rx.heading(f"Alert Dialog open: {AlertDialogState.opened}"),
        rx.alert_dialog.root(
            rx.alert_dialog.trigger(
                rx.button("Revoke access", color_scheme="red"),
            ),
            rx.alert_dialog.content(
                rx.alert_dialog.title("Revoke access"),
                rx.alert_dialog.description(
                    "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
                    size="2",
                ),
                rx.flex(
                    rx.alert_dialog.cancel(
                        rx.button("Cancel", variant="soft", color_scheme="gray"),
                    ),
                    rx.alert_dialog.action(
                        rx.button("Revoke access", color_scheme="red", variant="solid"),
                    ),
                    spacing="3",
                    margin_top="16px",
                    justify="end",
                ),
                style={"max_width": 450},
            ),
            on_open_change=AlertDialogState.count_opens,
        ),
        direction="column",
        spacing="3",
    )
```

## Controlling Alert Dialog with State

This example shows how to control whether the dialog is open or not with state. This is an easy way to show the dialog without needing to use the `rx.alert_dialog.trigger`.

`rx.alert_dialog.root` has a prop `open` that can be set to a boolean value to control whether the dialog is open or not.

We toggle this `open` prop with a button outside of the dialog and the `rx.alert_dialog.cancel` and `rx.alert_dialog.action` buttons inside the dialog.

```python demo exec
class AlertDialogState2(rx.State):
    opened: bool = False

    @rx.event
    def dialog_open(self):
        self.opened = ~self.opened


def alert_dialog2():
    return rx.box(
            rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.alert_dialog.title("Revoke access"),
            rx.alert_dialog.description(
                "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button("Cancel", on_click=AlertDialogState2.dialog_open),
                ),
                rx.alert_dialog.action(
                    rx.button("Revoke access", on_click=AlertDialogState2.dialog_open),
                ),
                spacing="3",
            ),
        ),
        open=AlertDialogState2.opened,
    ),
    rx.button("Button to Open the Dialog", on_click=AlertDialogState2.dialog_open),
)
```


## Form Submission to a Database from an Alert Dialog

This example adds new users to a database from an alert dialog using a form.

1. It defines a User1 model with name and email fields.
2. The `add_user_to_db` method adds a new user to the database, checking for existing emails.
3. On form submission, it calls the `add_user_to_db` method.
4. The UI component has:
- A button to open an alert dialog
- An alert dialog containing a form to add a new user
- Input fields for name and email
- Submit and Cancel buttons


```python demo exec
class User1(rx.Model, table=True):
    """The user model."""
    name: str
    email: str

class State(rx.State):
   
    current_user: User1 = User1()

    @rx.event
    def add_user_to_db(self, form_data: dict):
        self.current_user = form_data
        ### Uncomment the code below to add your data to a database ###
        # with rx.session() as session:
        #     if session.exec(
        #         select(User1).where(user.email == self.current_user["email"])
        #     ).first():
        #         return rx.window_alert("User with this email already exists")
        #     session.add(User1(**self.current_user))
        #     session.commit()
        
        return rx.toast.info(f"User {self.current_user['name']} has been added.", position="bottom-right")


def index() -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Add User", size="4"),
            ),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(
                "Add New User",
            ),
            rx.alert_dialog.description(
                "Fill the form with the user's info",
            ),
            rx.form(
                rx.flex(
                    rx.input(
                        placeholder="User Name", name="name"
                    ),
                    rx.input(
                        placeholder="user@reflex.dev", name="email"
                    ),
                    rx.flex(
                        rx.alert_dialog.cancel(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.alert_dialog.action(
                            rx.button("Submit", type="submit"),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),                     
                on_submit=State.add_user_to_db,
                reset_on_submit=False,
            ),
            max_width="450px",
        ),
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/overlay/toast.md`:

```md
---
components:
  - rx.toast.provider
---


# Toast

A `rx.toast` is a non-blocking notification that disappears after a certain amount of time. It is often used to show a message to the user without interrupting their workflow.

## Usage

You can use `rx.toast` as an event handler for any component that triggers an action.

```python demo
rx.button("Show Toast", on_click=rx.toast("Hello, World!"))
```

### Usage in State

You can also use `rx.toast` in a state to show a toast when a specific action is triggered, using `yield`.

```python demo exec
import asyncio
class ToastState(rx.State):

    @rx.event
    async def fetch_data(self):
        # Simulate fetching data for a 2-second delay
        await asyncio.sleep(2)
        # Shows a toast when the data is fetched
        yield rx.toast("Data fetched!")


def render():
    return rx.button("Get Data", on_click=ToastState.fetch_data)
```

## Interaction

If you want to interact with a toast, a few props are available to customize the behavior.

By passing a `ToastAction` to the `action` or `cancel` prop, you can trigger an action when the toast is clicked or when it is closed.

```python demo
rx.button("Show Toast", on_click=rx.toast("Hello, World!", duration=5000, close_button=True))
```

### Presets

`rx.toast` has some presets that you can use to show different types of toasts.

```python demo
rx.hstack(
    rx.button("Success", on_click=rx.toast.success("Success!"), color_scheme="green"),
    rx.button("Error", on_click=rx.toast.error("Error!"), color_scheme="red"),
    rx.button("Warning", on_click=rx.toast.warning("Warning!"), color_scheme="orange"),
    rx.button("Info", on_click=rx.toast.info("Info!"), color_scheme="blue"),
)
```

### Customization

If the presets don't fit your needs, you can customize the toasts by passing to `rx.toast` or to `rx.toast.options` some kwargs.

```python demo
rx.button(
    "Custom",
    on_click=rx.toast(
        "Custom Toast!",
        position="top-right",
        style={"background-color": "green", "color": "white", "border": "1px solid green", "border-radius": "0.53m"}
    )
)
```

The following props are available for customization:

- `description`: `str | Var`: Toast's description, renders underneath the title.
- `close_button`: `bool`: Whether to show the close button.
- `invert`: `bool`: Dark toast in light mode and vice versa.
- `important`: `bool`: Control the sensitivity of the toast for screen readers.
- `duration`: `int`: Time in milliseconds that should elapse before automatically closing the toast.
- `position`: `LiteralPosition`: Position of the toast.
- `dismissible`: `bool`: If false, it'll prevent the user from dismissing the toast.
- `action`: `ToastAction`: Renders a primary button, clicking it will close the toast.
- `cancel`: `ToastAction`: Renders a secondary button, clicking it will close the toast.
- `id`: `str | Var`: Custom id for the toast.
- `unstyled`: `bool`: Removes the default styling, which allows for easier customization.
- `style`: `Style`: Custom style for the toast.
- `on_dismiss`: `Any`: The function gets called when either the close button is clicked, or the toast is swiped.
- `on_auto_close`: `Any`: Function that gets called when the toast disappears automatically after it's timeout (`duration` prop).

## Toast Provider

Using the `rx.toast` function require to have a toast provider in your app.

`rx.toast.provider` is a component that provides a context for displaying toasts. It should be placed at the root of your app.

```md alert warning
# In most case you will not need to include this component directly, as it is already included in `rx.app` as the `overlay_component` for displaying connections errors.
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/overlay/popover.md`:

```md
---
components:
  - rx.popover.root
  - rx.popover.content
  - rx.popover.trigger
  - rx.popover.close

only_low_level:
  - True

PopoverRoot: |
  lambda **props: rx.popover.root(
      rx.popover.trigger(
          rx.button("Popover"),
      ),
      rx.popover.content(
          rx.flex(
              rx.text("Simple Example"),
              rx.popover.close(
                  rx.button("Close"),
              ),
              direction="column",
              spacing="3",
          ),
      ),
      **props
  )

PopoverContent: |
  lambda **props: rx.popover.root(
      rx.popover.trigger(
          rx.button("Popover"),
      ),
      rx.popover.content(
          rx.flex(
              rx.text("Simple Example"),
              rx.popover.close(
                  rx.button("Close"),
              ),
              direction="column",
              spacing="3",
          ),
          **props
      ),
  )
---


# Popover

A popover displays content, triggered by a button.

The `popover.root` contains all the parts of a popover.

The `popover.trigger` contains the button that toggles the popover.

The `popover.content` is the component that pops out when the popover is open.

The `popover.close` is the button that closes an open popover.

## Basic Example

```python demo
rx.popover.root(
    rx.popover.trigger(
        rx.button("Popover"),
    ),
    rx.popover.content(
        rx.flex(
            rx.text("Simple Example"),
            rx.popover.close(
                rx.button("Close"),
            ),
            direction="column",
            spacing="3",
        ),
    ),
)
```

## Examples in Context

```python demo

rx.popover.root(
    rx.popover.trigger(
        rx.button("Comment", variant="soft"),
    ),
    rx.popover.content(
        rx.flex(
            rx.avatar(
                "2",
                fallback="RX",
                radius="full"
            ),
            rx.box(
                rx.text_area(placeholder="Write a comment…", style={"height": 80}),
                rx.flex(
                    rx.checkbox("Send to group"),
                    rx.popover.close(
                        rx.button("Comment", size="1")
                    ),
                    spacing="3",
                    margin_top="12px",
                    justify="between",
                ),
                flex_grow="1",
            ),
            spacing="3"
        ),
        style={"width": 360},
    )
)
```

```python demo
rx.popover.root(
    rx.popover.trigger(
        rx.button("Feedback", variant="classic"),
    ),
    rx.popover.content(
        rx.inset(
            side="top",
            background="url('https://images.unsplash.com/5/unsplash-kitsune-4.jpg') center/cover",
            height="100px",
        ),
        rx.box(
            rx.text_area(placeholder="Write a comment…", style={"height": 80}),
            rx.flex(
                rx.checkbox("Send to group"),
                rx.popover.close(
                    rx.button("Comment", size="1")
                ),
                spacing="3",
                margin_top="12px",
                justify="between",
            ),
            padding_top="12px",
        ),
        style={"width": 360},
    )
)
```

## Popover with dynamic title

Code like below will not work as expected and it is necessary to place the dynamic title (`Index2State.language`) inside of an `rx.text` component.

```python
class Index2State(rx.State):
    language: str = "EN"

def index() -> rx.Component:
    return rx.popover.root(
        rx.popover.trigger(
            rx.button(Index2State.language),
        ),
        rx.popover.content(
            rx.text('Success')
        )
    )
```

This code will work:

```python demo exec
class Index2State(rx.State):
    language: str = "EN"

def index() -> rx.Component:
    return rx.popover.root(
        rx.popover.trigger(
            rx.button(
                rx.text(Index2State.language)
            ),
        ),
        rx.popover.content(
            rx.text('Success')
        )
    )
```

## Events when the Popover opens or closes

The `on_open_change` event is called when the `open` state of the popover changes. It is used in conjunction with the `open` prop, which is passed to the event handler.

```python demo exec
class PopoverState(rx.State):
    num_opens: int = 0
    opened: bool = False

    @rx.event
    def count_opens(self, value: bool):
        self.opened = value
        self.num_opens += 1


def popover_example():
    return rx.flex(
        rx.heading(f"Number of times popover opened or closed: {PopoverState.num_opens}"),
        rx.heading(f"Popover open: {PopoverState.opened}"),
        rx.popover.root(
            rx.popover.trigger(
                rx.button("Popover"),
            ),
            rx.popover.content(
                rx.flex(
                    rx.text("Simple Example"),
                    rx.popover.close(
                        rx.button("Close"),
                    ),
                    direction="column",
                    spacing="3",
                ),
            ),
            on_open_change=PopoverState.count_opens,
        ),
        direction="column",
        spacing="3",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/overlay/dropdown_menu.md`:

```md
---
components:
  - rx.dropdown_menu.root
  - rx.dropdown_menu.content
  - rx.dropdown_menu.trigger
  - rx.dropdown_menu.item
  - rx.dropdown_menu.separator
  - rx.dropdown_menu.sub_content

only_low_level:
  - True

DropdownMenuRoot: |
  lambda **props: rx.menu.root(
      rx.menu.trigger(rx.button("drop down menu")),
      rx.menu.content(
          rx.menu.item("Edit", shortcut="⌘ E"),
          rx.menu.item("Share"),
          rx.menu.item("Delete", shortcut="⌘ ⌫", color="red"),
          rx.menu.sub(
              rx.menu.sub_trigger("More"),
              rx.menu.sub_content(
                  rx.menu.item("Eradicate"),
                  rx.menu.item("Duplicate"),
                  rx.menu.item("Archive"),
              ),
          ),
      ),
      **props
  )

DropdownMenuContent: |
  lambda **props: rx.menu.root(
      rx.menu.trigger(rx.button("drop down menu")),
      rx.menu.content(
          rx.menu.item("Edit", shortcut="⌘ E"),
          rx.menu.item("Share"),
          rx.menu.item("Delete", shortcut="⌘ ⌫", color="red"),
          rx.menu.sub(
              rx.menu.sub_trigger("More"),
              rx.menu.sub_content(
                  rx.menu.item("Eradicate"),
                  rx.menu.item("Duplicate"),
                  rx.menu.item("Archive"),
              ),
          ),
          **props,
      ),
  )

DropdownMenuItem: |
  lambda **props: rx.menu.root(
      rx.menu.trigger(rx.button("drop down menu")),
      rx.menu.content(
          rx.menu.item("Edit", shortcut="⌘ E", **props),
          rx.menu.item("Share", **props),
          rx.menu.item("Delete", shortcut="⌘ ⌫", color="red", **props),
          rx.menu.sub(
              rx.menu.sub_trigger("More"),
              rx.menu.sub_content(
                  rx.menu.item("Eradicate", **props),
                  rx.menu.item("Duplicate", **props),
                  rx.menu.item("Archive", **props),
              ),
          ),
      ),
  )

DropdownMenuSub: |
  lambda **props: rx.menu.root(
      rx.menu.trigger(rx.button("drop down menu")),
      rx.menu.content(
          rx.menu.item("Edit", shortcut="⌘ E"),
          rx.menu.item("Share"),
          rx.menu.item("Delete", shortcut="⌘ ⌫", color="red"),
          rx.menu.sub(
              rx.menu.sub_trigger("More"),
              rx.menu.sub_content(
                  rx.menu.item("Eradicate"),
                  rx.menu.item("Duplicate"),
                  rx.menu.item("Archive"),
              ),
              **props,
          ),
      ),
  )

DropdownMenuSubTrigger: |
  lambda **props: rx.menu.root(
      rx.menu.trigger(rx.button("drop down menu")),
      rx.menu.content(
          rx.menu.item("Edit", shortcut="⌘ E"),
          rx.menu.item("Share"),
          rx.menu.item("Delete", shortcut="⌘ ⌫", color="red"),
          rx.menu.sub(
              rx.menu.sub_trigger("More", **props),
              rx.menu.sub_content(
                  rx.menu.item("Eradicate"),
                  rx.menu.item("Duplicate"),
                  rx.menu.item("Archive"),
              ),
          ),
      ),
  )

DropdownMenuSubContent: |
  lambda **props: rx.menu.root(
      rx.menu.trigger(rx.button("drop down menu")),
      rx.menu.content(
          rx.menu.item("Edit", shortcut="⌘ E"),
          rx.menu.item("Share"),
          rx.menu.item("Delete", shortcut="⌘ ⌫", color="red"),
          rx.menu.sub(
              rx.menu.sub_trigger("More"),
              rx.menu.sub_content(
                  rx.menu.item("Eradicate"),
                  rx.menu.item("Duplicate"),
                  rx.menu.item("Archive"),
                  **props,
              ),
          ),
      ),
  )
---


# Dropdown Menu

A Dropdown Menu is a menu that offers a list of options that a user can select from. They are typically positioned near a button that will control their appearance and disappearance.

A Dropdown Menu is composed of a `menu.root`, a `menu.trigger` and a `menu.content`. The `menu.trigger` is the element that the user interacts with to open the menu. It wraps the element that will open the dropdown menu. The `menu.content` is the component that pops out when the dropdown menu is open.

The `menu.item` contains the actual dropdown menu items and sits under the `menu.content`. The `shortcut` prop is an optional shortcut command displayed next to the item text.

The `menu.sub` contains all the parts of a submenu. There is a `menu.sub_trigger`, which is an item that opens a submenu. It must be rendered inside a `menu.sub` component. The `menu.sub_component` is the component that pops out when a submenu is open. It must also be rendered inside a `menu.sub` component.

The `menu.separator` is used to visually separate items in a dropdown menu.

```python demo
rx.menu.root(
    rx.menu.trigger(
        rx.button("Options", variant="soft"),
    ),
    rx.menu.content(
        rx.menu.item("Edit", shortcut="⌘ E"),
        rx.menu.item("Duplicate", shortcut="⌘ D"),
        rx.menu.separator(),
        rx.menu.item("Archive", shortcut="⌘ N"),
        rx.menu.sub(
            rx.menu.sub_trigger("More"),
            rx.menu.sub_content(
                rx.menu.item("Move to project…"),
                rx.menu.item("Move to folder…"),
                rx.menu.separator(),
                rx.menu.item("Advanced options…"),
            ),
        ),
        rx.menu.separator(),
        rx.menu.item("Share"),
        rx.menu.item("Add to favorites"),
        rx.menu.separator(),
        rx.menu.item("Delete", shortcut="⌘ ⌫", color="red"),
    ),
)
```

## Events when the Dropdown Menu opens or closes

The `on_open_change` event, from the `menu.root`, is called when the `open` state of the dropdown menu changes. It is used in conjunction with the `open` prop, which is passed to the event handler.

```python demo exec
class DropdownMenuState(rx.State):
    num_opens: int = 0
    opened: bool = False

    @rx.event
    def count_opens(self, value: bool):
        self.opened = value
        self.num_opens += 1


def dropdown_menu_example():
    return rx.flex(
        rx.heading(f"Number of times Dropdown Menu opened or closed: {DropdownMenuState.num_opens}"),
        rx.heading(f"Dropdown Menu open: {DropdownMenuState.opened}"),
        rx.menu.root(
            rx.menu.trigger(
                rx.button("Options", variant="soft", size="2"),
            ),
            rx.menu.content(
                rx.menu.item("Edit", shortcut="⌘ E"),
                rx.menu.item("Duplicate", shortcut="⌘ D"),
                rx.menu.separator(),
                rx.menu.item("Archive", shortcut="⌘ N"),
                rx.menu.separator(),
                rx.menu.item("Delete", shortcut="⌘ ⌫", color="red"),
            ),
            on_open_change=DropdownMenuState.count_opens,
        ),
        direction="column",
        spacing="3",
    )
```

## Opening a Dialog from Menu using State

Accessing an overlay component from within another overlay component is a common use case but does not always work exactly as expected.

The code below will not work as expected as because the dialog is within the menu and the dialog will only be open when the menu is open, rendering the dialog unusable.

```python
rx.menu.root(
    rx.menu.trigger(rx.icon("ellipsis-vertical")),
    rx.menu.content(
        rx.menu.item(
            rx.dialog.root(
            rx.dialog.trigger(rx.text("Edit")),
            rx.dialog.content(....),
            .....
            ),
        ),
    ),
)
```

In this example, we will show how to open a dialog box from a dropdown menu, where the menu will close and the dialog will open and be functional.

```python demo exec
class DropdownMenuState2(rx.State):
    which_dialog_open: str = ""

    @rx.event
    def delete(self):
        yield rx.toast("Deleted item")

    @rx.event
    def save_settings(self):
        yield rx.toast("Saved settings")


def delete_dialog():
    return rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.alert_dialog.title("Are you Sure?"),
            rx.alert_dialog.description(
                rx.text(
                    "This action cannot be undone. Are you sure you want to delete this item?",
                ),
                margin_bottom="20px",
            ),
            rx.hstack(
                rx.alert_dialog.action(
                    rx.button(
                        "Delete",
                        color_scheme="red",
                        on_click=DropdownMenuState2.delete,
                    ),
                ),
                rx.spacer(),
                rx.alert_dialog.cancel(rx.button("Cancel")),
            ),
        ),
        open=DropdownMenuState2.which_dialog_open == "delete",
        on_open_change=DropdownMenuState2.set_which_dialog_open(""),
    )


def settings_dialog():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Settings"),
            rx.dialog.description(
                rx.text("Set your settings in this settings dialog."),
                margin_bottom="20px",
            ),
            rx.dialog.close(
                rx.button("Close", on_click=DropdownMenuState2.save_settings),
            ),
        ),
        open=DropdownMenuState2.which_dialog_open == "settings",
        on_open_change=DropdownMenuState2.set_which_dialog_open(""),
    )


def menu_call_dialog() -> rx.Component:
    return rx.vstack(
        rx.menu.root(
            rx.menu.trigger(rx.icon("menu")),
            rx.menu.content(
                rx.menu.item(
                    "Delete",
                    on_click=DropdownMenuState2.set_which_dialog_open("delete"),
                ),
                rx.menu.item(
                    "Settings",
                    on_click=DropdownMenuState2.set_which_dialog_open("settings"),
                ),
            ),
        ),
        rx.cond(
            DropdownMenuState2.which_dialog_open,
            rx.heading(f"{DropdownMenuState2.which_dialog_open} dialog is open"),
        ),
        delete_dialog(),
        settings_dialog(),
        align="center",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/overlay/hover_card.md`:

```md
---
components:
  - rx.hover_card.root
  - rx.hover_card.content
  - rx.hover_card.trigger

only_low_level:
  - True

HoverCardRoot: |
  lambda **props: rx.hover_card.root(
      rx.hover_card.trigger(
          rx.link("Hover over me"),
      ),
      rx.hover_card.content(
          rx.text("This is the tooltip content."),
      ),
      **props
  )

HoverCardContent: |
  lambda **props: rx.hover_card.root(
      rx.hover_card.trigger(
          rx.link("Hover over me"),
      ),
      rx.hover_card.content(
          rx.text("This is the tooltip content."),
          **props
      ),
  )
---


# Hovercard

The `hover_card.root` contains all the parts of a hover card.

The `hover_card.trigger` wraps the link that will open the hover card.

The `hover_card.content` contains the content of the open hover card.

```python demo
rx.text(
    "Hover over the text to see the tooltip. ",
    rx.hover_card.root(
        rx.hover_card.trigger(
            rx.link("Hover over me", color_scheme="blue", underline="always"),
        ),
        rx.hover_card.content(
            rx.text("This is the hovercard content."),
        ),
    ),
)
```

```python demo
rx.text(
    "Hover over the text to see the tooltip. ",
    rx.hover_card.root(
        rx.hover_card.trigger(
            rx.link("Hover over me", color_scheme="blue", underline="always"),
        ),
        rx.hover_card.content(
            rx.grid(
                rx.inset(
                    side="left",
                    pr="current",
                    background="url('https://images.unsplash.com/5/unsplash-kitsune-4.jpg') center/cover",
                    height="full",
                ),
                rx.box(
                    rx.text_area(placeholder="Write a comment…", style={"height": 80}),
                    rx.flex(
                        rx.checkbox("Send to group"),
                        spacing="3",
                        margin_top="12px",
                        justify="between",
                    ),
                    padding_left="12px",
                ),
                columns="120px 1fr",
            ),
            style={"width": 360},
        ),
    ),
)
```

## Events when the Hovercard opens or closes

The `on_open_change` event is called when the `open` state of the hovercard changes. It is used in conjunction with the `open` prop, which is passed to the event handler.

```python demo exec
class HovercardState(rx.State):
    num_opens: int = 0
    opened: bool = False

    @rx.event
    def count_opens(self, value: bool):
        self.opened = value
        self.num_opens += 1


def hovercard_example():
    return rx.flex(
        rx.heading(f"Number of times hovercard opened or closed: {HovercardState.num_opens}"),
        rx.heading(f"Hovercard open: {HovercardState.opened}"),
        rx.text(
            "Hover over the text to see the hover card. ",
            rx.hover_card.root(
                rx.hover_card.trigger(
                    rx.link("Hover over me", color_scheme="blue", underline="always"),
                ),
                rx.hover_card.content(
                    rx.text("This is the tooltip content."),
                ),
                on_open_change=HovercardState.count_opens,
            ),
        ),
        direction="column",
        spacing="3",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/overlay/context_menu.md`:

```md
---
components:
  - rx.context_menu.root
  - rx.context_menu.item
  - rx.context_menu.separator
  - rx.context_menu.trigger
  - rx.context_menu.content
  - rx.context_menu.sub
  - rx.context_menu.sub_trigger
  - rx.context_menu.sub_content

only_low_level:
  - True

ContextMenuRoot: |
  lambda **props: rx.context_menu.root(
          rx.context_menu.trigger(
              rx.text("Context Menu (right click)")
          ),
          rx.context_menu.content(
              rx.context_menu.item("Copy", shortcut="⌘ C"),
              rx.context_menu.item("Share"),
              rx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
              rx.context_menu.sub(
                  rx.context_menu.sub_trigger("More"),
                  rx.context_menu.sub_content(
                      rx.context_menu.item("Eradicate"),
                      rx.context_menu.item("Duplicate"),
                      rx.context_menu.item("Archive"),
                  ),
              ),
          ),
          **props
      )

ContextMenuTrigger: |
  lambda **props: rx.context_menu.root(
          rx.context_menu.trigger(
              rx.text("Context Menu (right click)"),
              **props
          ),
          rx.context_menu.content(
              rx.context_menu.item("Copy", shortcut="⌘ C"),
              rx.context_menu.item("Share"),
              rx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
              rx.context_menu.sub(
                  rx.context_menu.sub_trigger("More"),
                  rx.context_menu.sub_content(
                      rx.context_menu.item("Eradicate"),
                      rx.context_menu.item("Duplicate"),
                      rx.context_menu.item("Archive"),
                  ),
              ),
          ),
      )

ContextMenuContent: |
  lambda **props: rx.context_menu.root(
          rx.context_menu.trigger(
              rx.text("Context Menu (right click)")
          ),
          rx.context_menu.content(
              rx.context_menu.item("Copy", shortcut="⌘ C"),
              rx.context_menu.item("Share"),
              rx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
              rx.context_menu.sub(
                  rx.context_menu.sub_trigger("More"),
                  rx.context_menu.sub_content(
                      rx.context_menu.item("Eradicate"),
                      rx.context_menu.item("Duplicate"),
                      rx.context_menu.item("Archive"),
                  ),
              ),
              **props
          ),
      )

ContextMenuSub: |
  lambda **props: rx.context_menu.root(
          rx.context_menu.trigger(
              rx.text("Context Menu (right click)")
          ),
          rx.context_menu.content(
              rx.context_menu.item("Copy", shortcut="⌘ C"),
              rx.context_menu.item("Share"),
              rx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
              rx.context_menu.sub(
                  rx.context_menu.sub_trigger("More"),
                  rx.context_menu.sub_content(
                      rx.context_menu.item("Eradicate"),
                      rx.context_menu.item("Duplicate"),
                      rx.context_menu.item("Archive"),
                  ),
              **props
              ),
          ),
      )

ContextMenuSubTrigger: |
  lambda **props: rx.context_menu.root(
          rx.context_menu.trigger(
              rx.text("Context Menu (right click)")
          ),
          rx.context_menu.content(
              rx.context_menu.item("Copy", shortcut="⌘ C"),
              rx.context_menu.item("Share"),
              rx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
              rx.context_menu.sub(
                  rx.context_menu.sub_trigger("More", **props),
                  rx.context_menu.sub_content(
                      rx.context_menu.item("Eradicate"),
                      rx.context_menu.item("Duplicate"),
                      rx.context_menu.item("Archive"),
                  ),
              ),
          ),
      )

ContextMenuSubContent: |
  lambda **props: rx.context_menu.root(
          rx.context_menu.trigger(
              rx.text("Context Menu (right click)")
          ),
          rx.context_menu.content(
              rx.context_menu.item("Copy", shortcut="⌘ C"),
              rx.context_menu.item("Share"),
              rx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
              rx.context_menu.sub(
                  rx.context_menu.sub_trigger("More"),
                  rx.context_menu.sub_content(
                      rx.context_menu.item("Eradicate"),
                      rx.context_menu.item("Duplicate"),
                      rx.context_menu.item("Archive"),
                      **props
                  ),
              ),
          ),
      )

ContextMenuItem: |
  lambda **props: rx.context_menu.root(
          rx.context_menu.trigger(
              rx.text("Context Menu (right click)")
          ),
          rx.context_menu.content(
              rx.context_menu.item("Copy", shortcut="⌘ C", **props),
              rx.context_menu.item("Share", **props),
              rx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red", **props),
              rx.context_menu.sub(
                  rx.context_menu.sub_trigger("More"),
                  rx.context_menu.sub_content(
                      rx.context_menu.item("Eradicate", **props),
                      rx.context_menu.item("Duplicate", **props),
                      rx.context_menu.item("Archive", **props),
                  ),
              ),
          ),
      )
---


# Context Menu

A Context Menu is a popup menu that appears upon user interaction, such as a right-click or a hover.

## Basic Usage

A Context Menu is composed of a `context_menu.root`, a `context_menu.trigger` and a `context_menu.content`. The `context_menu_root` contains all the parts of a context menu. The `context_menu.trigger` is the element that the user interacts with to open the menu. It wraps the element that will open the context menu. The `context_menu.content` is the component that pops out when the context menu is open.

The `context_menu.item` contains the actual context menu items and sits under the `context_menu.content`.

The `context_menu.sub` contains all the parts of a submenu. There is a `context_menu.sub_trigger`, which is an item that opens a submenu. It must be rendered inside a `context_menu.sub` component. The `context_menu.sub_content` is the component that pops out when a submenu is open. It must also be rendered inside a `context_menu.sub` component.

The `context_menu.separator` is used to visually separate items in a context menu.

```python demo
rx.context_menu.root(
    rx.context_menu.trigger(
       rx.button("Right click me"),
    ),
    rx.context_menu.content(
        rx.context_menu.item("Edit", shortcut="⌘ E"),
        rx.context_menu.item("Duplicate", shortcut="⌘ D"),
        rx.context_menu.separator(),
        rx.context_menu.item("Archive", shortcut="⌘ N"),
        rx.context_menu.sub(
            rx.context_menu.sub_trigger("More"),
            rx.context_menu.sub_content(
                rx.context_menu.item("Move to project…"),
                rx.context_menu.item("Move to folder…"),
                rx.context_menu.separator(),
                rx.context_menu.item("Advanced options…"),
            ),
        ),
        rx.context_menu.separator(),
        rx.context_menu.item("Share"),
        rx.context_menu.item("Add to favorites"),
        rx.context_menu.separator(),
        rx.context_menu.item("Delete", shortcut="⌘ ⌫", color="red"),
    ),
)
```

````md alert warning
# `rx.context_menu.item` must be a DIRECT child of `rx.context_menu.content`

The code below for example is not allowed:

```python
rx.context_menu.root(
    rx.context_menu.trigger(
       rx.button("Right click me"),
    ),
    rx.context_menu.content(
        rx.cond(
            State.count % 2 == 0,
            rx.vstack(
                rx.context_menu.item("Even Option 1", on_click=State.set_selected_option("Even Option 1")),
                rx.context_menu.item("Even Option 2", on_click=State.set_selected_option("Even Option 2")),
                rx.context_menu.item("Even Option 3", on_click=State.set_selected_option("Even Option 3")),
            ),
            rx.vstack(
                rx.context_menu.item("Odd Option A", on_click=State.set_selected_option("Odd Option A")),
                rx.context_menu.item("Odd Option B", on_click=State.set_selected_option("Odd Option B")),
                rx.context_menu.item("Odd Option C", on_click=State.set_selected_option("Odd Option C")),
            )
        )
    ),
)
```
````

## Opening a Dialog from Context Menu using State

Accessing an overlay component from within another overlay component is a common use case but does not always work exactly as expected.

The code below will not work as expected as because the dialog is within the menu and the dialog will only be open when the menu is open, rendering the dialog unusable.

```python
rx.context_menu.root(
    rx.context_menu.trigger(rx.icon("ellipsis-vertical")),
    rx.context_menu.content(
        rx.context_menu.item(
            rx.dialog.root(
            rx.dialog.trigger(rx.text("Edit")),
            rx.dialog.content(....),
            .....
            ),
        ),
    ),
)
```

In this example, we will show how to open a dialog box from a context menu, where the menu will close and the dialog will open and be functional.

```python demo exec
class ContextMenuState(rx.State):
    which_dialog_open: str = ""

    @rx.event
    def delete(self):
        yield rx.toast("Deleted item")

    @rx.event
    def save_settings(self):
        yield rx.toast("Saved settings")


def delete_dialog():
    return rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.alert_dialog.title("Are you Sure?"),
            rx.alert_dialog.description(
                rx.text(
                    "This action cannot be undone. Are you sure you want to delete this item?",
                ),
                margin_bottom="20px",
            ),
            rx.hstack(
                rx.alert_dialog.action(
                    rx.button(
                        "Delete",
                        color_scheme="red",
                        on_click=ContextMenuState.delete,
                    ),
                ),
                rx.spacer(),
                rx.alert_dialog.cancel(rx.button("Cancel")),
            ),
        ),
        open=ContextMenuState.which_dialog_open == "delete",
        on_open_change=ContextMenuState.set_which_dialog_open(""),
    )


def settings_dialog():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Settings"),
            rx.dialog.description(
                rx.text("Set your settings in this settings dialog."),
                margin_bottom="20px",
            ),
            rx.dialog.close(
                rx.button("Close", on_click=ContextMenuState.save_settings),
            ),
        ),
        open=ContextMenuState.which_dialog_open == "settings",
        on_open_change=ContextMenuState.set_which_dialog_open(""),
    )


def context_menu_call_dialog() -> rx.Component:
    return rx.vstack(
        rx.context_menu.root(
            rx.context_menu.trigger(rx.icon("ellipsis-vertical")),
            rx.context_menu.content(
                rx.context_menu.item(
                    "Delete",
                    on_click=ContextMenuState.set_which_dialog_open("delete"),
                ),
                rx.context_menu.item(
                    "Settings",
                    on_click=ContextMenuState.set_which_dialog_open("settings"),
                ),
            ),
        ),
        rx.cond(
            ContextMenuState.which_dialog_open,
            rx.heading(f"{ContextMenuState.which_dialog_open} dialog is open"),
        ),
        delete_dialog(),
        settings_dialog(),
        align="center",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/overlay/tooltip.md`:

```md
---
components:
  - rx.tooltip

Tooltip: |
  lambda **props: rx.tooltip(
      rx.button("Hover over me"),
      content="This is the tooltip content.",
      **props,
  )
---


# Tooltip

A `tooltip` displays informative information when users hover over or focus on an element.

It takes a `content` prop, which is the content associated with the tooltip.

```python demo
rx.tooltip(
    rx.button("Hover over me"),
    content="This is the tooltip content.",
)
```

## Events when the Tooltip opens or closes

The `on_open_change` event is called when the `open` state of the tooltip changes. It is used in conjunction with the `open` prop, which is passed to the event handler.

```python demo exec
class TooltipState(rx.State):
    num_opens: int = 0
    opened: bool = False

    @rx.event
    def count_opens(self, value: bool):
        self.opened = value
        self.num_opens += 1


def index():
    return rx.flex(
        rx.heading(f"Number of times tooltip opened or closed: {TooltipState.num_opens}"),
        rx.heading(f"Tooltip open: {TooltipState.opened}"),
        rx.text(
            "Hover over the button to see the tooltip.",
            rx.tooltip(
                rx.button("Hover over me"),
                content="This is the tooltip content.",
                on_open_change=TooltipState.count_opens,
            ),
        ),
        direction="column",
        spacing="3",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/overlay/dialog.md`:

```md
---
components:
  - rx.dialog.root
  - rx.dialog.trigger
  - rx.dialog.title
  - rx.dialog.content
  - rx.dialog.description
  - rx.dialog.close

only_low_level:
  - True

DialogRoot: |
  lambda **props: rx.dialog.root(
      rx.dialog.trigger(rx.button("Open Dialog")),
      rx.dialog.content(
          rx.dialog.title("Welcome to Reflex!"),
          rx.dialog.description(
              "This is a dialog component. You can render anything you want in here.",
          ),
          rx.dialog.close(
              rx.button("Close Dialog"),
          ),
      ),
      **props,
  )

DialogContent: |
  lambda **props: rx.dialog.root(
      rx.dialog.trigger(rx.button("Open Dialog")),
      rx.dialog.content(
          rx.dialog.title("Welcome to Reflex!"),
          rx.dialog.description(
              "This is a dialog component. You can render anything you want in here.",
          ),
          rx.dialog.close(
              rx.button("Close Dialog"),
          ),
          **props,
      ),
  )
---


# Dialog

The `dialog.root` contains all the parts of a dialog.

The `dialog.trigger` wraps the control that will open the dialog.

The `dialog.content` contains the content of the dialog.

The `dialog.title` is a title that is announced when the dialog is opened.

The `dialog.description` is a description that is announced when the dialog is opened.

The `dialog.close` wraps the control that will close the dialog.

```python demo
rx.dialog.root(
    rx.dialog.trigger(rx.button("Open Dialog")),
    rx.dialog.content(
        rx.dialog.title("Welcome to Reflex!"),
        rx.dialog.description(
            "This is a dialog component. You can render anything you want in here.",
        ),
        rx.dialog.close(
            rx.button("Close Dialog", size="3"),
        ),
    ),
)
```

## In context examples

```python demo
rx.dialog.root(
    rx.dialog.trigger(
        rx.button("Edit Profile", size="4")
    ),
    rx.dialog.content(
        rx.dialog.title("Edit Profile"),
        rx.dialog.description(
            "Change your profile details and preferences.",
            size="2",
            margin_bottom="16px",
        ),
        rx.flex(
            rx.text("Name", as_="div", size="2", margin_bottom="4px", weight="bold"),
            rx.input(default_value="Freja Johnson", placeholder="Enter your name"),
            rx.text("Email", as_="div", size="2", margin_bottom="4px", weight="bold"),
            rx.input(default_value="freja@example.com", placeholder="Enter your email"),
            direction="column",
            spacing="3",
        ),
        rx.flex(
            rx.dialog.close(
                rx.button("Cancel", color_scheme="gray", variant="soft"),
            ),
            rx.dialog.close(
                rx.button("Save"),
            ),
            spacing="3",
            margin_top="16px",
            justify="end",
        ),
    ),
)
```

```python demo
rx.dialog.root(
    rx.dialog.trigger(rx.button("View users", size="4")),
    rx.dialog.content(
        rx.dialog.title("Users"),
        rx.dialog.description("The following users have access to this project."),

        rx.inset(
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Full Name"),
                        rx.table.column_header_cell("Email"),
                        rx.table.column_header_cell("Group"),
                    ),
                ),
                rx.table.body(
                    rx.table.row(
                        rx.table.row_header_cell("Danilo Rosa"),
                        rx.table.cell("danilo@example.com"),
                        rx.table.cell("Developer"),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("Zahra Ambessa"),
                        rx.table.cell("zahra@example.com"),
                        rx.table.cell("Admin"),
                    ),
                ),
            ),
            side="x",
            margin_top="24px",
            margin_bottom="24px",
        ),
        rx.flex(
            rx.dialog.close(
                rx.button("Close", variant="soft", color_scheme="gray"),
            ),
            spacing="3",
            justify="end",
        ),
    ),
)
```

## Events when the Dialog opens or closes

The `on_open_change` event is called when the `open` state of the dialog changes. It is used in conjunction with the `open` prop, which is passed to the event handler.

```python demo exec
class DialogState(rx.State):
    num_opens: int = 0
    opened: bool = False

    @rx.event
    def count_opens(self, value: bool):
        self.opened = value
        self.num_opens += 1


def dialog_example():
    return rx.flex(
        rx.heading(f"Number of times dialog opened or closed: {DialogState.num_opens}"),
        rx.heading(f"Dialog open: {DialogState.opened}"),
        rx.dialog.root(
            rx.dialog.trigger(rx.button("Open Dialog")),
            rx.dialog.content(
                rx.dialog.title("Welcome to Reflex!"),
                rx.dialog.description(
                    "This is a dialog component. You can render anything you want in here.",
                ),
                rx.dialog.close(
                    rx.button("Close Dialog", size="3"),
                ),
            ),
            on_open_change=DialogState.count_opens,
        ),
        direction="column",
        spacing="3",
    )
```

Check out the [menu docs]({library.overlay.dropdown_menu.path}) for an example of opening a dialog from within a dropdown menu.

## Form Submission to a Database from a Dialog

This example adds new users to a database from a dialog using a form.

1. It defines a User model with name and email fields.
2. The `add_user_to_db` method adds a new user to the database, checking for existing emails.
3. On form submission, it calls the `add_user_to_db` method.
4. The UI component has:

- A button to open a dialog
- A dialog containing a form to add a new user
- Input fields for name and email
- Submit and Cancel buttons

```python demo exec
class User(rx.Model, table=True):
    """The user model."""
    name: str
    email: str

class State(rx.State):

    current_user: User = User()

    @rx.event
    def add_user_to_db(self, form_data: dict):
        self.current_user = form_data
        ### Uncomment the code below to add your data to a database ###
        # with rx.session() as session:
        #     if session.exec(
        #         select(User).where(user.email == self.current_user["email"])
        #     ).first():
        #         return rx.window_alert("User with this email already exists")
        #     session.add(User(**self.current_user))
        #     session.commit()

        return rx.toast.info(f"User {self.current_user['name']} has been added.", position="bottom-right")


def index() -> rx.Component:
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
                        placeholder="User Name", name="name"
                    ),
                    rx.input(
                        placeholder="user@reflex.dev", name="email"
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
                            rx.button("Submit", type="submit"),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=State.add_user_to_db,
                reset_on_submit=False,
            ),
            max_width="450px",
        ),
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/media/audio.md`:

```md
---
components:
    - rx.audio
---

# Audio


The audio component can display an audio given an src path as an argument. This could either be a local path from the assets folder or an external link.

```python demo
rx.audio(
    url="https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3",
    width="400px",
    height="32px",
)
```

If we had a local file in the `assets` folder named `test.mp3` we could set `url="/test.mp3"` to view the audio file.

```md alert info
# How to let your user upload an audio file
To let a user upload an audio file to your app check out the [upload docs]({library.forms.upload.path}).
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/media/video.md`:

```md
---
components:
    - rx.video
---

# Video


The video component can display a video given an src path as an argument. This could either be a local path from the assets folder or an external link.

```python demo
rx.video(
    url="https://www.youtube.com/embed/9bZkp7q19f0", 
    width="400px",
    height="auto"
)
```

If we had a local file in the `assets` folder named `test.mp4` we could set `url="/test.mp4"` to view the video.


```md alert info
# How to let your user upload a video
To let a user upload a video to your app check out the [upload docs]({library.forms.upload.path}).
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/media/image.md`:

```md
---
components:
    - rx.image
---


# Image

The Image component can display an image given a `src` path as an argument.
This could either be a local path from the assets folder or an external link.

```python demo
rx.image(src="/logo.jpg", width="100px", height="auto")
```

Image composes a box and can be styled similarly.

```python demo
rx.image(
    src="/logo.jpg",
    width="100px",
    height="auto",
    border_radius="15px 50px",
    border="5px solid #555",
)
```

You can also pass a `PIL` image object as the `src`.

```python demo box
rx.image(src="https://picsum.photos/id/1/200/300", alt="An Unsplash Image")
```

```python
from PIL import Image
import requests


class ImageState(rx.State):
    url = f"https://picsum.photos/id/1/200/300"
    image = Image.open(requests.get(url, stream=True).raw)


def image_pil_example():
    return rx.vstack(
        rx.image(src=ImageState.image)
    )
```

```md alert info
# rx.image only accepts URLs and Pillow Images
A cv2 image must be converted to a PIL image to be passed directly to `rx.image` as a State variable, or saved to the `assets` folder and then passed to the `rx.image` component.
```

```md alert info
# How to let your user upload an image
To let a user upload an image to your app check out the [upload docs]({library.forms.upload.path}).
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/disclosure/accordion.md`:

```md
---
components:
  - rx.accordion.root
  - rx.accordion.item

AccordionRoot: |
  lambda **props: rx.accordion.root(
      rx.accordion.item(header="First Item", content="The first accordion item's content"),
      rx.accordion.item(
          header="Second Item", content="The second accordion item's content",
      ),
      rx.accordion.item(header="Third item", content="The third accordion item's content"),
      width="300px",
      **props,
  )

AccordionItem: |
  lambda **props: rx.accordion.root(
      rx.accordion.item(header="First Item", content="The first accordion item's content", **props),
      rx.accordion.item(
          header="Second Item", content="The second accordion item's content", **props,
      ),
      rx.accordion.item(header="Third item", content="The third accordion item's content", **props),
      width="300px",
  )
---


# Accordion

An accordion is a vertically stacked set of interactive headings that each reveal an associated section of content.
The accordion component is made up of `accordion`, which is the root of the component and takes in an `accordion.item`,
which contains all the contents of the collapsible section.

## Basic Example

```python demo
rx.accordion.root(
    rx.accordion.item(header="First Item", content="The first accordion item's content"),
    rx.accordion.item(
        header="Second Item", content="The second accordion item's content",
    ),
    rx.accordion.item(header="Third item", content="The third accordion item's content"),
    width="300px",
)
```

## Styling

### Type

We use the `type` prop to determine whether multiple items can be opened at once. The allowed values for this prop are
`single` and `multiple` where `single` will only open one item at a time. The default value for this prop is `single`.

```python demo
rx.accordion.root(
    rx.accordion.item(header="First Item", content="The first accordion item's content"),
    rx.accordion.item(
        header="Second Item", content="The second accordion item's content",
    ),
    rx.accordion.item(header="Third item", content="The third accordion item's content"),
    collapsible=True,
    width="300px",
    type="multiple",
)
```

### Default Value

We use the `default_value` prop to specify which item should open by default. The value for this prop should be any of the
unique values set by an `accordion.item`.

```python demo
rx.flex(
    rx.accordion.root(
        rx.accordion.item(
            header="First Item",
            content="The first accordion item's content",
            value="item_1",
        ),
        rx.accordion.item(
            header="Second Item",
            content="The second accordion item's content",
            value="item_2",
        ),
        rx.accordion.item(
            header="Third item",
            content="The third accordion item's content",
            value="item_3",
        ),
        width="300px",
        default_value="item_2",
    ),
    direction="row",
    spacing="2"
)
```

### Collapsible

We use the `collapsible` prop to allow all items to close. If set to `False`, an opened item cannot be closed.

```python demo
rx.flex(
    rx.accordion.root(
        rx.accordion.item(header="First Item", content="The first accordion item's content"),
        rx.accordion.item(header="Second Item", content="The second accordion item's content"),
        rx.accordion.item(header="Third item", content="The third accordion item's content"),
        collapsible=True,
        width="300px",
    ),
    rx.accordion.root(
        rx.accordion.item(header="First Item", content="The first accordion item's content"),
        rx.accordion.item(header="Second Item", content="The second accordion item's content"),
        rx.accordion.item(header="Third item", content="The third accordion item's content"),
        collapsible=False,
        width="300px",
    ),
    direction="row",
    spacing="2"
)
```

### Disable

We use the `disabled` prop to prevent interaction with the accordion and all its items.

```python demo
rx.accordion.root(
    rx.accordion.item(header="First Item", content="The first accordion item's content"),
    rx.accordion.item(header="Second Item", content="The second accordion item's content"),
    rx.accordion.item(header="Third item", content="The third accordion item's content"),
    collapsible=True,
    width="300px",
    disabled=True,
)
```

### Orientation

We use `orientation` prop to set the orientation of the accordion to `vertical` or `horizontal`. By default, the orientation
will be set to `vertical`. Note that, the orientation prop won't change the visual orientation but the
functional orientation of the accordion. This means that for vertical orientation, the up and down arrow keys moves focus between the next or previous item,
while for horizontal orientation, the left or right arrow keys moves focus between items.

```python demo
rx.accordion.root(
    rx.accordion.item(header="First Item", content="The first accordion item's content"),
    rx.accordion.item(
        header="Second Item", content="The second accordion item's content",
    ),
    rx.accordion.item(header="Third item", content="The third accordion item's content"),
    collapsible=True,
    width="300px",
    orientation="vertical",
)
```

```python demo
rx.accordion.root(
    rx.accordion.item(header="First Item", content="The first accordion item's content"),
    rx.accordion.item(
        header="Second Item", content="The second accordion item's content",
    ),
    rx.accordion.item(header="Third item", content="The third accordion item's content"),
    collapsible=True,
    width="300px",
    orientation="horizontal",
)
```

### Variant

```python demo
rx.flex(
    rx.accordion.root(
        rx.accordion.item(header="First Item", content="The first accordion item's content"),
        rx.accordion.item(
            header="Second Item", content="The second accordion item's content",
        ),
        rx.accordion.item(header="Third item", content="The third accordion item's content"),
        collapsible=True,
        variant="classic",
    ),
    rx.accordion.root(
        rx.accordion.item(header="First Item", content="The first accordion item's content"),
        rx.accordion.item(
            header="Second Item", content="The second accordion item's content",
        ),
        rx.accordion.item(header="Third item", content="The third accordion item's content"),
        collapsible=True,
        variant="soft",
    ),
    rx.accordion.root(
        rx.accordion.item(header="First Item", content="The first accordion item's content"),
        rx.accordion.item(
            header="Second Item", content="The second accordion item's content",
        ),
        rx.accordion.item(header="Third item", content="The third accordion item's content"),
        collapsible=True,
        variant="outline",
    ),
    rx.accordion.root(
        rx.accordion.item(header="First Item", content="The first accordion item's content"),
        rx.accordion.item(
            header="Second Item", content="The second accordion item's content",
        ),
        rx.accordion.item(header="Third item", content="The third accordion item's content"),
        collapsible=True,
        variant="surface",
    ),
    rx.accordion.root(
        rx.accordion.item(header="First Item", content="The first accordion item's content"),
        rx.accordion.item(
            header="Second Item", content="The second accordion item's content",
        ),
        rx.accordion.item(header="Third item", content="The third accordion item's content"),
        collapsible=True,
        variant="ghost",
    ),
    direction="row",
    spacing="2"
)
```

### Color Scheme

We use the `color_scheme` prop to assign a specific color to the accordion background, ignoring the global theme.

```python demo
rx.flex(
    rx.accordion.root(
        rx.accordion.item(header="First Item", content="The first accordion item's content"),
        rx.accordion.item(
            header="Second Item", content="The second accordion item's content",
        ),
        rx.accordion.item(header="Third item", content="The third accordion item's content"),
        collapsible=True,
        width="300px",
        color_scheme="grass",
    ),
    rx.accordion.root(
        rx.accordion.item(header="First Item", content="The first accordion item's content"),
        rx.accordion.item(
            header="Second Item", content="The second accordion item's content",
        ),
        rx.accordion.item(header="Third item", content="The third accordion item's content"),
        collapsible=True,
        width="300px",
        color_scheme="green",
    ),
    direction="row",
    spacing="2"
)
```

### Value

We use the `value` prop to specify the controlled value of the accordion item that we want to activate.
This property should be used in conjunction with the `on_value_change` event argument.

```python demo exec
class AccordionState(rx.State):
    """The app state."""
    value: str = "item_1"
    item_selected: str

    @rx.event
    def change_value(self, value):
        self.value = value
        self.item_selected = f"{value} selected"


def index() -> rx.Component:
    return rx.theme(
        rx.container(
            rx.text(AccordionState.item_selected),
            rx.flex(
                rx.accordion.root(
                    rx.accordion.item(
                        header="Is it accessible?",
                        content=rx.button("Test button"),
                        value="item_1",
                    ),
                    rx.accordion.item(
                        header="Is it unstyled?",
                        content="Yes. It's unstyled by default, giving you freedom over the look and feel.",
                        value="item_2",
                    ),
                    rx.accordion.item(
                        header="Is it finished?",
                        content="It's still in beta, but it's ready to use in production.",
                        value="item_3",
                    ),
                    collapsible=True,
                    width="300px",
                    value=AccordionState.value,
                    on_value_change=lambda value: AccordionState.change_value(value),
                ),
                direction="column",
                spacing="2",
            ),
            padding="2em",
            text_align="center",
        )
    )
```

## AccordionItem

The accordion item contains all the parts of a collapsible section.

## Styling

### Value

```python demo
rx.accordion.root(
    rx.accordion.item(
        header="First Item",
        content="The first accordion item's content",
        value="item_1",
    ),
    rx.accordion.item(
        header="Second Item",
        content="The second accordion item's content",
        value="item_2",
    ),
    rx.accordion.item(
        header="Third item",
        content="The third accordion item's content",
        value="item_3",
    ),
    collapsible=True,
    width="300px",
)
```

### Disable

```python demo
rx.accordion.root(
    rx.accordion.item(
        header="First Item",
        content="The first accordion item's content",
        disabled=True,
    ),
    rx.accordion.item(
        header="Second Item", content="The second accordion item's content",
    ),
    rx.accordion.item(header="Third item", content="The third accordion item's content"),
    collapsible=True,
    width="300px",
    color_scheme="blue",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/disclosure/segmented_control.md`:

```md
---
components:
    - rx.segmented_control.root
    - rx.segmented_control.item
---


# Segmented Control

Segmented Control offers a clear and accessible way to switch between predefined values and views, e.g., "Inbox," "Drafts," and "Sent."

With Segmented Control, you can make mutually exclusive choices, where only one option can be active at a time, clear and accessible. Without Segmented Control, end users might have to deal with controls like dropdowns or multiple buttons that don't clearly convey state or group options together visually.

## Basic Example

The `Segmented Control` component is made up of a `rx.segmented_control.root` which groups `rx.segmented_control.item`.

The `rx.segmented_control.item` components define the individual segments of the control, each with a label and a unique value.

```python demo
rx.vstack(
    rx.segmented_control.root(
        rx.segmented_control.item("Home", value="home"),
        rx.segmented_control.item("About", value="about"),
        rx.segmented_control.item("Test", value="test"),
        on_change=SegmentedState.setvar("control"),
        value=SegmentedState.control,
    ),
    rx.card(
        rx.text(SegmentedState.control, align="left"),
        rx.text(SegmentedState.control, align="center"),
        rx.text(SegmentedState.control, align="right"),
        width="100%",
    ),
)
```

**In the example above:**

`on_change` is used to specify a callback function that will be called when the user selects a different segment. In this case, the `SegmentedState.setvar("control")` function is used to update the `control` state variable when the user changes the selected segment.

`value` prop is used to specify the currently selected segment, which is bound to the `SegmentedState.control` state variable.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/disclosure/tabs.md`:

```md
---
components:
  - rx.tabs.root
  - rx.tabs.list
  - rx.tabs.trigger
  - rx.tabs.content

only_low_level:
  - True

TabsRoot: |
  lambda **props: rx.tabs.root(
      rx.tabs.list(
          rx.tabs.trigger("Account", value="account"),
          rx.tabs.trigger("Documents", value="documents"),
          rx.tabs.trigger("Settings", value="settings"),
      ),
      rx.box(
          rx.tabs.content(
              rx.text("Make changes to your account"),
              value="account",
          ),
          rx.tabs.content(
              rx.text("Update your documents"),
              value="documents",
          ),
          rx.tabs.content(
              rx.text("Edit your personal profile"),
              value="settings",
          ),
      ),
      **props,
  )

TabsList: |
  lambda **props: rx.tabs.root(
      rx.tabs.list(
          rx.tabs.trigger("Account", value="account"),
          rx.tabs.trigger("Documents", value="documents"),
          rx.tabs.trigger("Settings", value="settings"),
          **props,
      ),
      rx.box(
          rx.tabs.content(
              rx.text("Make changes to your account"),
              value="account",
          ),
          rx.tabs.content(
              rx.text("Update your documents"),
              value="documents",
          ),
          rx.tabs.content(
              rx.text("Edit your personal profile"),
              value="settings",
          ),
      ),
  )

TabsTrigger: |
  lambda **props: rx.tabs.root(
      rx.tabs.list(
          rx.tabs.trigger("Account", value="account", **props,),
          rx.tabs.trigger("Documents", value="documents"),
          rx.tabs.trigger("Settings", value="settings"),
      ),
      rx.box(
          rx.tabs.content(
              rx.text("Make changes to your account"),
              value="account",
          ),
          rx.tabs.content(
              rx.text("Update your documents"),
              value="documents",
          ),
          rx.tabs.content(
              rx.text("Edit your personal profile"),
              value="settings",
          ),
      ),
  )

TabsContent: |
  lambda **props: rx.tabs.root(
      rx.tabs.list(
          rx.tabs.trigger("Account", value="account"),
          rx.tabs.trigger("Documents", value="documents"),
          rx.tabs.trigger("Settings", value="settings"),
      ),
      rx.box(
          rx.tabs.content(
              rx.text("Make changes to your account"),
              value="account",
              **props,
          ),
          rx.tabs.content(
              rx.text("Update your documents"),
              value="documents",
              **props,
          ),
          rx.tabs.content(
              rx.text("Edit your personal profile"),
              value="settings",
              **props,
          ),
      ),
  )
---


# Tabs

Tabs are a set of layered sections of content—known as tab panels that are displayed one at a time.
They facilitate the organization and navigation between sets of content that share a connection and exist at a similar level of hierarchy.

## Basic Example

```python demo
rx.tabs.root(
    rx.tabs.list(
        rx.tabs.trigger("Tab 1", value="tab1"),
        rx.tabs.trigger("Tab 2", value="tab2")
    ),
    rx.tabs.content(
        rx.text("item on tab 1"),
        value="tab1",
    ),
    rx.tabs.content(
        rx.text("item on tab 2"),
        value="tab2",
    ),
)

```

The `tabs` component is made up of a `rx.tabs.root` which groups `rx.tabs.list` and `rx.tabs.content` parts.

## Styling

### Default value

We use the `default_value` prop to set a default active tab, this will select the specified tab by default.

```python demo
rx.tabs.root(
    rx.tabs.list(
        rx.tabs.trigger("Tab 1", value="tab1"),
        rx.tabs.trigger("Tab 2", value="tab2")
    ),
    rx.tabs.content(
        rx.text("item on tab 1"),
        value="tab1",
    ),
    rx.tabs.content(
        rx.text("item on tab 2"),
        value="tab2",
    ),
    default_value="tab2",
)
```

### Orientation

We use `orientation` prop to set the orientation of the tabs component to `vertical` or `horizontal`. By default, the orientation
will be set to `horizontal`. Setting this value will change both the visual orientation and the functional orientation.

```md alert info
The functional orientation means for `vertical`, the `up` and `down` arrow keys moves focus between the next or previous tab,
while for `horizontal`, the `left` and `right` arrow keys moves focus between tabs.
```

```md alert warning
# When using vertical orientation, make sure to assign a tabs.content for each trigger.

Defining triggers without content will result in a visual bug where the width of the triggers list isn't constant.
```

```python demo
rx.tabs.root(
    rx.tabs.list(
        rx.tabs.trigger("Tab 1", value="tab1"),
        rx.tabs.trigger("Tab 2", value="tab2")
    ),
    rx.tabs.content(
        rx.text("item on tab 1"),
        value="tab1",
    ),
    rx.tabs.content(
        rx.text("item on tab 2"),
        value="tab2",
    ),
    default_value="tab1",
    orientation="vertical",
)
```

```python demo
rx.tabs.root(
    rx.tabs.list(
        rx.tabs.trigger("Tab 1", value="tab1"),
        rx.tabs.trigger("Tab 2", value="tab2")
    ),
    rx.tabs.content(
        rx.text("item on tab 1"),
        value="tab1",
    ),
    rx.tabs.content(
        rx.text("item on tab 2"),
        value="tab2",
    ),
    default_value="tab1",
    orientation="horizontal",
)
```

### Value

We use the `value` prop to specify the controlled value of the tab that we want to activate. This property should be used in conjunction with the `on_change` event argument.

```python demo exec
class TabsState(rx.State):
    """The app state."""

    value = "tab1"
    tab_selected = ""

    @rx.event
    def change_value(self, val):
        self.tab_selected = f"{val} clicked!"
        self.value = val


def index() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.text(f"{TabsState.value}  clicked !"),
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("Tab 1", value="tab1"),
                    rx.tabs.trigger("Tab 2", value="tab2"),
                ),
                rx.tabs.content(
                        rx.text("items on tab 1"),
                    value="tab1",
                ),
                rx.tabs.content(
                    rx.text("items on tab 2"),
                    value="tab2",
                ),
                default_value="tab1",
                value=TabsState.value,
                on_change=lambda x: TabsState.change_value(x),
            ),
            direction="column",
            spacing="2",
        ),
        padding="2em",
        font_size="2em",
        text_align="center",
    )
```

## Tablist

The Tablist is used to list the respective tabs to the tab component

## Tab Trigger

This is the button that activates the tab's associated content. It is typically used in the `Tablist`

## Styling

### Value

We use the `value` prop to assign a unique value that associates the trigger with content.

```python demo
rx.tabs.root(
    rx.tabs.list(
        rx.tabs.trigger("Tab 1", value="tab1"),
        rx.tabs.trigger("Tab 2", value="tab2"),
        rx.tabs.trigger("Tab 3", value="tab3")
    ),
)
```

### Disable

We use the `disabled` prop to disable the tab.

```python demo
rx.tabs.root(
    rx.tabs.list(
        rx.tabs.trigger("Tab 1", value="tab1"),
        rx.tabs.trigger("Tab 2", value="tab2"),
        rx.tabs.trigger("Tab 3", value="tab3", disabled=True)
    ),
)
```

## Tabs Content

Contains the content associated with each trigger.

## Styling

### Value

We use the `value` prop to assign a unique value that associates the content with a trigger.

```python
rx.tabs.root(
    rx.tabs.list(
        rx.tabs.trigger("Tab 1", value="tab1"),
        rx.tabs.trigger("Tab 2", value="tab2")
    ),
    rx.tabs.content(
        rx.text("item on tab 1"),
        value="tab1",
    ),
    rx.tabs.content(
        rx.text("item on tab 2"),
        value="tab2",
    ),
    default_value="tab1",
    orientation="vertical",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/dynamic-rendering/foreach.md`:

```md

# Foreach

The `rx.foreach` component takes an iterable(list, tuple or dict) and a function that renders each item in the list.
This is useful for dynamically rendering a list of items defined in a state.

```md alert warning
# `rx.foreach` is specialized for usecases where the iterable is defined in a state var.

For an iterable where the content doesn't change at runtime, i.e a constant, using a list/dict comprehension instead of `rx.foreach` is preferred.
```

```python demo exec
from typing import List
class ForeachState(rx.State):
    color: List[str] = ["red", "green", "blue", "yellow", "orange", "purple"]

def colored_box(color: str):
    return rx.box(
        rx.text(color),
        bg=color
    )

def foreach_example():
    return rx.grid(
        rx.foreach(
            ForeachState.color,
            colored_box
        ),
        columns="2",
    )
```

The function can also take an index as a second argument.

```python demo exec
def colored_box_index(color: str, index: int):
    return rx.box(
        rx.text(index),
        bg=color
    )

def foreach_example_index():
    return rx.grid(
        rx.foreach(
            ForeachState.color,
            lambda color, index: colored_box_index(color, index)
        ),
        columns="2",
    )
```

Nested foreach components can be used to render nested lists.

When indexing into a nested list, it's important to declare the list's type as Reflex requires it for type checking.
This ensures that any potential frontend JS errors are caught before the user can encounter them.

```python demo exec
from typing import List

class NestedForeachState(rx.State):
    numbers: List[List[str]] = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def display_row(row):
    return rx.hstack(
        rx.foreach(
            row,
            lambda item: rx.box(
                item,
                border="1px solid black",
                padding="0.5em",
            )
        ),
    )

def nested_foreach_example():
    return rx.vstack(
        rx.foreach(
             NestedForeachState.numbers,
            display_row
        )
    )
```

Below is a more complex example of foreach within a todo list.

```python demo exec
from typing import List
class ListState(rx.State):
    items: List[str] = ["Write Code", "Sleep", "Have Fun"]
    new_item: str

    @rx.event
    def add_item(self):
        self.items += [self.new_item]

    def finish_item(self, item: str):
        self.items = [i for i in self.items if i != item]

def get_item(item):
    return rx.list.item(
        rx.hstack(
            rx.button(
                on_click=lambda: ListState.finish_item(item),
                height="1.5em",
                background_color="white",
                border="1px solid blue",
            ),
            rx.text(item, font_size="1.25em"),
        ),
    )

def todo_example():
    return rx.vstack(
        rx.heading("Todos"),
        rx.input(on_blur=ListState.set_new_item, placeholder="Add a todo...", bg  = "white"),
        rx.button("Add", on_click=ListState.add_item, bg = "white"),
        rx.divider(),
        rx.list.ordered(
            rx.foreach(
                ListState.items,
                get_item,
            ),
        ),
        bg = "#ededed",
        padding = "1em",
        border_radius = "0.5em",
        shadow = "lg"
    )
```

## Dictionaries

Items in a dictionary can be accessed as list of key-value pairs.
Using the color example, we can slightly modify the code to use dicts as shown below.

```python demo exec
from typing import List
class SimpleDictForeachState(rx.State):
    color_chart: dict[int, str] = {
         1 : "blue",
         2: "red",
         3: "green"
    }

def display_color(color: List):
    # color is presented as a list key-value pair([1, "blue"],[2, "red"], [3, "green"])
    return rx.box(rx.text(color[0]), bg=color[1])


def foreach_dict_example():
    return rx.grid(
        rx.foreach(
            SimpleDictForeachState.color_chart,
            display_color
        ),
        columns = "2"
    )
```

Now let's show a more complex example with dicts using the color example.
Assuming we want to display a dictionary of secondary colors as keys and their constituent primary colors as values, we can modify the code as below:

```python demo exec
from typing import List, Dict
class ComplexDictForeachState(rx.State):
    color_chart: Dict[str, List[str]] = {
        "purple": ["red", "blue"],
        "orange": ["yellow", "red"],
        "green": ["blue", "yellow"]
    }

def display_colors(color: List):
    return rx.vstack(
            rx.text(color[0], color=color[0]),
            rx.hstack(
                rx.foreach(
                    color[1], lambda x: rx.box(rx.text(x, color="black"), bg=x)
                )

            )
        )

def foreach_complex_dict_example():
    return rx.grid(
        rx.foreach(
            ComplexDictForeachState.color_chart,
            display_colors
        ),
        columns="2"
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/dynamic-rendering/cond.md`:

```md

# Cond

This component is used to conditionally render components.

The cond component takes a condition and two components.
If the condition is `True`, the first component is rendered, otherwise the second component is rendered.

```python demo exec
class CondState(rx.State):
    show: bool = True

    @rx.event
    def change(self):
        self.show = not (self.show)


def cond_example():
    return rx.vstack(
        rx.button("Toggle", on_click=CondState.change),
        rx.cond(CondState.show, rx.text("Text 1", color="blue"), rx.text("Text 2", color="red")),
    )
```

The second component is optional and can be omitted.
If it is omitted, nothing is rendered if the condition is `False`.

```md video https://youtube.com/embed/ITOZkzjtjUA?start=6040&end=6463
# Video: Conditional Rendering
```

## Negation

You can use the logical operator `~` to negate a condition.

```python
rx.vstack(
    rx.button("Toggle", on_click=CondState.change),
    rx.cond(CondState.show, rx.text("Text 1", color="blue"), rx.text("Text 2", color="red")),
    rx.cond(~CondState.show, rx.text("Text 1", color="blue"), rx.text("Text 2", color="red")),
)
```

## Multiple Conditions

It is also possible to make up complex conditions using the `logical or` (|) and `logical and` (&) operators.

Here we have an example using the var operators `>=`, `<=`, `&`. We define a condition that if a person has an age between 18 and 65, including those ages, they are able to work, otherwise they cannot.

We could equally use the operator `|` to represent a `logical or` in one of our conditions.

```python demo exec
import random

class CondComplexState(rx.State):
    age: int = 19

    @rx.event
    def change(self):
        self.age = random.randint(0, 100)


def cond_complex_example():
    return rx.vstack(
        rx.button("Toggle", on_click=CondComplexState.change),
        rx.text(f"Age: {CondComplexState.age}"),
        rx.cond(
            (CondComplexState.age >= 18) & (CondComplexState.age <=65),
            rx.text("You can work!", color="green"),
            rx.text("You cannot work!", color="red"),
        ),
    )

```

## Nested Conditional

We can also nest `cond` components within each other to create more complex logic. In python we can have an `if` statement that then has several `elif` statements before finishing with an `else`. This is also possible in reflex using nested `cond` components. In this example we check whether a number is positive, negative or zero.

Here is the python logic using `if` statements:

```python
number = 0

if number > 0:
    print("Positive number")

elif number == 0:
    print('Zero')
else:
    print('Negative number')
```

This reflex code that is logically identical:

```python demo exec
import random


class NestedState(rx.State):

    num: int = 0

    def change(self):
        self.num = random.randint(-10, 10)


def cond_nested_example():
    return rx.vstack(
        rx.button("Toggle", on_click=NestedState.change),
        rx.cond(
            NestedState.num > 0,
            rx.text(f"{NestedState.num} is Positive!", color="orange"),
            rx.cond(
                NestedState.num == 0,
                rx.text(f"{NestedState.num} is Zero!", color="blue"),
                rx.text(f"{NestedState.num} is Negative!", color="red"),
            )
        ),
    )

```

Here is a more advanced example where we have three numbers and we are checking which of the three is the largest. If any two of them are equal then we return that `Some of the numbers are equal!`.

The reflex code that follows is logically identical to doing the following in python:

```python
a = 8
b = 10
c = 2

if((a>b and a>c) and (a != b and a != c)):
 print(a, " is the largest!")
elif((b>a and b>c) and (b != a and b != c)):
 print(b, " is the largest!")
elif((c>a and c>b) and (c != a and c != b)):
 print(c, " is the largest!")
else:
 print("Some of the numbers are equal!")
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/dynamic-rendering/match.md`:

```md

# Match

The `rx.match` feature in Reflex serves as a powerful alternative to `rx.cond` for handling conditional statements.
While `rx.cond` excels at conditionally rendering two components based on a single condition,
`rx.match` extends this functionality by allowing developers to handle multiple conditions and their associated components.
This feature is especially valuable when dealing with intricate conditional logic or nested scenarios,
where the limitations of `rx.cond` might lead to less readable and more complex code.

With `rx.match`, developers can not only handle multiple conditions but also perform structural pattern matching,
making it a versatile tool for managing various scenarios in Reflex applications.

## Basic Usage

The `rx.match` function provides a clear and expressive syntax for handling multiple
conditions and their corresponding components:

```python
rx.match(
    condition,
    (case_1, component_1),
    (case_2, component_2),
    ...
    default_component,
)

```

- `condition`: The value to match against.
- `(case_i, component_i)`: A Tuple of matching cases and their corresponding return components.
- `default_component`: A special case for the default component when the condition isn't matched by any of the match cases.

Example

```python demo exec
from typing import List

import reflex as rx


class MatchState(rx.State):
    cat_breed: str = ""
    animal_options: List[str] = ["persian", "siamese", "maine coon", "ragdoll", "pug", "corgi"]


def match_demo():
    return rx.flex(
        rx.match(
            MatchState.cat_breed,
            ("persian", rx.text("Persian cat selected.")),
            ("siamese", rx.text("Siamese cat selected.")),
            ("maine coon", rx.text("Maine Coon cat selected.")),
            ("ragdoll", rx.text("Ragdoll cat selected.")),
            rx.text("Unknown cat breed selected.")
        ),
        rx.select.root(
            rx.select.trigger(),
            rx.select.content(
                rx.select.group(
                    rx.foreach(MatchState.animal_options, lambda x: rx.select.item(x, value=x))
                ),
            ),
            value=MatchState.cat_breed,
            on_change=MatchState.set_cat_breed,

        ),
        direction= "column",
        gap= "2"
    )
```

## Default Case

The default case in `rx.match` serves as a universal handler for scenarios where none of
the specified match cases aligns with the given match condition. Here are key considerations
when working with the default case:

- **Placement in the Match Function**: The default case must be the last non-tuple argument in the `rx.match` component.
  All match cases should be enclosed in tuples; any non-tuple value is automatically treated as the default case. For example:

```python
rx.match(
           MatchState.cat_breed,
           ("persian", rx.text("persian cat selected")),
           rx.text("Unknown cat breed selected."),
           ("siamese", rx.text("siamese cat selected")),
       )
```

The above code snippet will result in an error due to the misplaced default case.

- **Single Default Case**: Only one default case is allowed in the `rx.match` component.
  Attempting to specify multiple default cases will lead to an error. For instance:

```python
rx.match(
           MatchState.cat_breed,
           ("persian", rx.text("persian cat selected")),
           ("siamese", rx.text("siamese cat selected")),
           rx.text("Unknown cat breed selected."),
           rx.text("Another unknown cat breed selected.")
       )
```

- **Optional Default Case for Component Return Values**: If the match cases in a `rx.match` component
  return components, the default case can be optional. In this scenario, if a default case is
  not provided, `rx.fragment` will be implicitly assigned as the default. For example:

```python
rx.match(
           MatchState.cat_breed,
           ("persian", rx.text("persian cat selected")),
           ("siamese", rx.text("siamese cat selected")),
       )
```

In this case, `rx.fragment` is the default case. However, not providing a default case for non-component
return values will result in an error:

```python
rx.match(
           MatchState.cat_breed,
           ("persian", "persian cat selected"),
           ("siamese", "siamese cat selected"),
       )
```

The above code snippet will result in an error as a default case must be explicitly
provided in this scenario.

## Handling Multiple Conditions

`rx.match` excels in efficiently managing multiple conditions and their corresponding components,
providing a cleaner and more readable alternative compared to nested `rx.cond` structures.

Consider the following example:

```python demo exec
from typing import List

import reflex as rx


class MultiMatchState(rx.State):
    animal_breed: str = ""
    animal_options: List[str] = ["persian", "siamese", "maine coon", "pug", "corgi", "mustang", "rahvan", "football", "golf"]

def multi_match_demo():
    return rx.flex(
        rx.match(
            MultiMatchState.animal_breed,
            ("persian", "siamese", "maine coon", rx.text("Breeds of cats.")),
            ("pug", "corgi", rx.text("Breeds of dogs.")),
            ("mustang", "rahvan", rx.text("Breeds of horses.")),
            rx.text("Unknown animal breed")
        ),
        rx.select.root(
            rx.select.trigger(),
            rx.select.content(
                rx.select.group(
                    rx.foreach(MultiMatchState.animal_options, lambda x: rx.select.item(x, value=x))
                ),
            ),
            value=MultiMatchState.animal_breed,
            on_change=MultiMatchState.set_animal_breed,

        ),
        direction= "column",
        gap= "2"
    )
```

In a match case tuple, you can specify multiple conditions. The last value of the match case
tuple is automatically considered as the return value. It's important to note that a match case
tuple should contain a minimum of two elements: a match case and a return value.
The following code snippet will result in an error:

```python
rx.match(
            MatchState.cat_breed,
            ("persian",),
            ("maine coon", rx.text("Maine Coon cat selected")),
        )
```

## Usage as Props

Similar to `rx.cond`, `rx.match` can be used as prop values, allowing dynamic behavior for UI components:

```python demo exec
import reflex as rx


class MatchPropState(rx.State):
    value: int = 0

    @rx.event
    def incr(self):
        self.value += 1

    @rx.event
    def decr(self):
        self.value -= 1


def match_prop_demo_():
    return rx.flex(
        rx.button("decrement", on_click=MatchPropState.decr, background_color="red"),
        rx.badge(
            MatchPropState.value,
            color_scheme= rx.match(
                    MatchPropState.value,
                    (1, "red"),
                    (2, "blue"),
                    (6, "purple"),
                    (10, "orange"),
                    "green"
                ),
                size="2",
        ),
        rx.button("increment", on_click=MatchPropState.incr),
        align_items="center",
        direction= "row",
        gap= "3"
    )
```

In the example above, the background color property of the box component containing `State.value` changes to red when
`state.value` is 1, blue when its 5, green when its 5, orange when its 15 and black for any other value.

The example below also shows handling multiple conditions with the match component as props.

```python demo exec
import reflex as rx


class MatchMultiPropState(rx.State):
    value: int = 0

    @rx.event
    def incr(self):
        self.value += 1

    @rx.event
    def decr(self):
        self.value -= 1


def match_multi_prop_demo_():
    return rx.flex(
        rx.button("decrement", on_click=MatchMultiPropState.decr, background_color="red"),
        rx.badge(
            MatchMultiPropState.value,
            color_scheme= rx.match(
                    MatchMultiPropState.value,
                    (1, 3, 9, "red"),
                    (2, 4, 5, "blue"),
                    (6, 8, 12, "purple"),
                    (10, 15, 20, 25, "orange"),
                    "green"
                ),
                size="2",
        ),
        rx.button("increment", on_click=MatchMultiPropState.incr),
        align_items="center",
        direction= "row",
        gap= "3"
    )
```

```md alert warning
# Usage with Structural Pattern Matching

The `rx.match` component is designed for structural pattern matching. If the value of your match condition evaluates to a boolean (True or False), it is recommended to use `rx.cond` instead.

Consider the following example, which is more suitable for `rx.cond`:\*
```

```python
rx.cond(
    MatchPropState.value == 10,
    "true value",
    "false value"
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/data-display/list.md`:

```md
---
components:
    - rx.list.item
    - rx.list.ordered
    - rx.list.unordered
---


# List

A `list` is a component that is used to display a list of items, stacked vertically by default. A `list` can be either `ordered` or `unordered`. It is based on the `flex` component and therefore inherits all of its props.

`list.unordered` has bullet points to display the list items.

```python demo
rx.list.unordered(
    rx.list.item("Example 1"),
    rx.list.item("Example 2"),
    rx.list.item("Example 3"),
)
```

 `list.ordered` has numbers to display the list items.

```python demo
rx.list.ordered(
    rx.list.item("Example 1"),
    rx.list.item("Example 2"),
    rx.list.item("Example 3"),
)
```

`list.unordered()` and `list.ordered()` can have no bullet points or numbers by setting the `list_style_type` prop to `none`.
This is effectively the same as using the `list()` component.

```python demo
rx.hstack(
    rx.list(
        rx.list.item("Example 1"),
        rx.list.item("Example 2"),
        rx.list.item("Example 3"),
    ),
    rx.list.unordered(
        rx.list.item("Example 1"),
        rx.list.item("Example 2"),
        rx.list.item("Example 3"),
        list_style_type="none",
    )
)
```

Lists can also be used with icons.

```python demo
rx.list(
    rx.list.item(
        rx.icon("circle_check_big", color="green"), " Allowed",
    ),
    rx.list.item(
        rx.icon("octagon_x", color="red"), " Not",
    ),
    rx.list.item(
        rx.icon("settings", color="grey"), " Settings"
    ),
    list_style_type="none",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/data-display/moment.md`:

```md
---
components:
    - rx.moment

---

# Moment

Displaying date and relative time to now sometimes can be more complicated than necessary.

To make it easy, Reflex is wrapping [react-moment](https://www.npmjs.com/package/react-moment)  under `rx.moment`.



## Examples

Using a date from a state var as a value, we will display it in a few different
way using `rx.moment`. 

The `date_now` state var is initialized when the site was deployed. The
button below can be used to update the var to the current datetime, which will
be reflected in the subsequent examples.

```python demo exec
from datetime import datetime, timezone

class MomentState(rx.State):
    date_now: datetime = datetime.now(timezone.utc)

    @rx.event
    def update(self):
        self.date_now = datetime.now(timezone.utc)


def moment_update_example():
    return rx.button("Update", rx.moment(MomentState.date_now), on_click=MomentState.update)
```

### Display the date as-is:

```python demo
rx.moment(MomentState.date_now)
```

### Humanized interval

Sometimes we don't want to display just a raw date, but we want something more instinctive to read. That's when we can use `from_now` and `to_now`.

```python demo
rx.moment(MomentState.date_now, from_now=True)
```

```python demo
rx.moment(MomentState.date_now, to_now=True)
```
You can also set a duration (in milliseconds) with `from_now_during` where the date will display as relative, then after that, it will be displayed as defined in `format`.

```python demo
rx.moment(MomentState.date_now, from_now_during=100000)  # after 100 seconds, date will display normally
```

### Formatting dates

```python demo
rx.moment(MomentState.date_now, format="YYYY-MM-DD")
```

```python demo
rx.moment(MomentState.date_now, format="HH:mm:ss")
```

### Offset Date

With the props `add` and `subtract`, you can pass an `rx.MomentDelta` object to modify the displayed date without affecting the stored date in your state.


```python eval
rx.tabs(
    rx.tabs.list(
        rx.tabs.trigger("Add", value="add"), 
        rx.tabs.trigger("Subtract", value="subtract")
    ),
    rx.tabs.content(docdemo(add_example, comp=eval(add_example)), value="add"),
    rx.tabs.content(docdemo(subtract_example, comp=eval(subtract_example)), value="subtract"),
    default_value="add",
)
```

### Timezones

You can also set dates to display in a specific timezone:

```python demo
rx.vstack(
    rx.moment(MomentState.date_now, tz="America/Los_Angeles"),
    rx.moment(MomentState.date_now, tz="Europe/Paris"),
    rx.moment(MomentState.date_now, tz="Asia/Tokyo"),
)
```

### Client-side periodic update

If a date is not passed to `rx.moment`, it will use the client's current time.

If you want to update the date every second, you can use the `interval` prop.

```python demo
rx.moment(interval=1000, format="HH:mm:ss")
```

Even better, you can actually link an event handler to the `on_change` prop that will be called every time the date is updated:

```python demo exec
class MomentLiveState(rx.State):
    updating: bool = False

    @rx.event
    def on_update(self, date):
        return rx.toast(f"Date updated: {date}")


def moment_live_example():
    return rx.hstack(
        rx.moment(
            format="HH:mm:ss",
            interval=rx.cond(MomentLiveState.updating, 5000, 0),
            on_change=MomentLiveState.on_update,
        ),
        rx.switch(
            is_checked=MomentLiveState.updating,
            on_change=MomentLiveState.set_updating,
        ),
    )
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/data-display/progress.md`:

```md
---
components:
    - rx.progress

Progress: |
    lambda **props: rx.progress(value=50, **props)
---

# Progress

Progress is used to display the progress status for a task that takes a long time or consists of several steps.

## Basic Example

`rx.progress` expects the `value` prop to set the progress value.
`width` is default to 100%, the width of its parent component.

```python demo
rx.vstack(
    rx.progress(value=0),
    rx.progress(value=50),
    rx.progress(value=100),
    width="50%",
)
```

For a dynamic progress, you can assign a state variable to the `value` prop instead of a constant value.

```python demo exec
import asyncio

class ProgressState(rx.State):
    value: int = 0

    @rx.event(background=True)
    async def start_progress(self):
        async with self:
            self.value = 0
        while self.value < 100:
            await asyncio.sleep(0.1)
            async with self:
                self.value += 1


def live_progress():
    return rx.hstack(
        rx.progress(value=ProgressState.value), 
        rx.button("Start", on_click=ProgressState.start_progress),
        width="50%"
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/data-display/callout.md`:

```md
---
components:
    - rx.callout
    - rx.callout.root
    - rx.callout.icon
    - rx.callout.text

Callout: |
    lambda **props: rx.callout("Basic Callout", icon="search", **props)

CalloutRoot: |
    lambda **props: rx.callout.root(
        rx.callout.icon(rx.icon(tag="info")),
        rx.callout.text("You will need admin privileges to install and access this application."),
        **props
    )
---



# Callout

A `callout` is a short message to attract user's attention.

```python demo
rx.callout("You will need admin privileges to install and access this application.", icon="info")
```

The `icon` prop allows an icon to be passed to the `callout` component. See the [**icon** component for all icons that are available.]({docs.library.data_display.icon.path})

## As alert

```python demo
rx.callout("Access denied. Please contact the network administrator to view this page.", icon="triangle_alert", color_scheme="red", role="alert")
```

## Style

### Size

Use the `size` prop to control the size.

```python demo
rx.flex(
    rx.callout("You will need admin privileges to install and access this application.", icon="info", size="3",),
    rx.callout("You will need admin privileges to install and access this application.", icon="info", size="2",),
    rx.callout("You will need admin privileges to install and access this application.", icon="info", size="1",),
    direction="column",
    spacing="3",
    align="start",
)
```

### Variant

Use the `variant` prop to control the visual style. It is set to `soft` by default.

```python demo
rx.flex(
    rx.callout("You will need admin privileges to install and access this application.", icon="info", variant="soft",),
    rx.callout("You will need admin privileges to install and access this application.", icon="info", variant="surface",),
    rx.callout("You will need admin privileges to install and access this application.", icon="info", variant="outline",),
    direction="column",
    spacing="3",
)
```

### Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.

```python demo
rx.flex(
    rx.callout("You will need admin privileges to install and access this application.", icon="info", color_scheme="blue",),
    rx.callout("You will need admin privileges to install and access this application.", icon="info", color_scheme="green",),
    rx.callout("You will need admin privileges to install and access this application.", icon="info", color_scheme="red",),
    direction="column",
    spacing="3",
)
```

### High Contrast

Use the `high_contrast` prop to add additional contrast.

```python demo
rx.flex(
    rx.callout("You will need admin privileges to install and access this application.", icon="info",),
    rx.callout("You will need admin privileges to install and access this application.", icon="info", high_contrast=True,),
    direction="column",
    spacing="3",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/data-display/scroll_area.md`:

```md
---
components:
    - rx.scroll_area

ScrollArea: |
    lambda **props: rx.scroll_area(
        rx.flex(
            rx.text(
                """Three fundamental aspects of typography are legibility, readability, and aesthetics. Although in a non-technical sense "legible" and "readable"are often used synonymously, typographically they are separate but related concepts.""",
                size="5",
            ),
            rx.text(
                """Legibility describes how easily individual characters can be distinguished from one another. It is described by Walter Tracy as "the quality of being decipherable and recognisable". For instance, if a "b" and an "h", or a "3" and an "8", are difficult to distinguish at small sizes, this is a problem of legibility.""",
                size="5",
            ),
            direction="column",
            spacing="4",
            height="100px",
            width="50%",
        ),
        **props
    )

---



# Scroll Area

Custom styled, cross-browser scrollable area using native functionality.

## Basic Example

```python demo
rx.scroll_area(
    rx.flex(
        rx.text(
            """Three fundamental aspects of typography are legibility, readability, and
        aesthetics. Although in a non-technical sense “legible” and “readable”
        are often used synonymously, typographically they are separate but
        related concepts.""",
        ),
        rx.text(
            """Legibility describes how easily individual characters can be
        distinguished from one another. It is described by Walter Tracy as “the
        quality of being decipherable and recognisable”. For instance, if a “b”
        and an “h”, or a “3” and an “8”, are difficult to distinguish at small
        sizes, this is a problem of legibility.""",
        ),
        rx.text(
            """Typographers are concerned with legibility insofar as it is their job to
        select the correct font to use. Brush Script is an example of a font
        containing many characters that might be difficult to distinguish. The
        selection of cases influences the legibility of typography because using
        only uppercase letters (all-caps) reduces legibility.""",
        ),
        direction="column",
        spacing="4",
    ),
    type="always",
    scrollbars="vertical",
    style={"height": 180},

)

```

## Control the scrollable axes

Use the `scrollbars` prop to limit scrollable axes. This prop can take values `"vertical" | "horizontal" | "both"`.

```python demo
rx.grid(
    rx.scroll_area(
        rx.flex(
            rx.text(
                """Three fundamental aspects of typography are legibility, readability, and
        aesthetics. Although in a non-technical sense "legible" and "readable"
        are often used synonymously, typographically they are separate but
        related concepts.""",
                size="2", trim="both",
            ),
            rx.text(
                """Legibility describes how easily individual characters can be
        distinguished from one another. It is described by Walter Tracy as "the
        quality of being decipherable and recognisable". For instance, if a "b"
        and an "h", or a "3" and an "8", are difficult to distinguish at small
        sizes, this is a problem of legibility.""",
                size="2", trim="both",
            ),
            padding="8px", padding_right="48px", direction="column", spacing="4",
        ),
        type="always",
        scrollbars="vertical",
        style={"height": 150}, 
    ),
    rx.scroll_area(
        rx.flex(
            rx.text(
                """Three fundamental aspects of typography are legibility, readability, and
        aesthetics. Although in a non-technical sense "legible" and "readable"
        are often used synonymously, typographically they are separate but
        related concepts.""",
                size="2", trim="both",
            ),
            rx.text(
                """Legibility describes how easily individual characters can be
        distinguished from one another. It is described by Walter Tracy as "the
        quality of being decipherable and recognisable". For instance, if a "b"
        and an "h", or a "3" and an "8", are difficult to distinguish at small
        sizes, this is a problem of legibility.""",
                size="2", trim="both",
            ),
            padding="8px", spacing="4", style={"width": 700},
        ),
        type="always",
        scrollbars="horizontal",
        style={"height": 150}, 
    ),
    rx.scroll_area(
        rx.flex(
            rx.text(
                """Three fundamental aspects of typography are legibility, readability, and
        aesthetics. Although in a non-technical sense "legible" and "readable"
        are often used synonymously, typographically they are separate but
        related concepts.""",
                size="2", trim="both",
            ),
            rx.text(
                """Legibility describes how easily individual characters can be
        distinguished from one another. It is described by Walter Tracy as "the
        quality of being decipherable and recognisable". For instance, if a "b"
        and an "h", or a "3" and an "8", are difficult to distinguish at small
        sizes, this is a problem of legibility.""",
                size="2", trim="both",
            ),
            padding="8px", spacing="4", style={"width": 400},
        ),
        type="always",
        scrollbars="both",
        style={"height": 150}, 
    ),
    columns="3",
    spacing="2",
)
```

## Setting the type of the Scrollbars

The `type` prop describes the nature of scrollbar visibility.

`auto` means that scrollbars are visible when content is overflowing on the corresponding orientation.

`always` means that scrollbars are always visible regardless of whether the content is overflowing.

`scroll` means that scrollbars are visible when the user is scrolling along its corresponding orientation.

`hover` when the user is scrolling along its corresponding orientation and when the user is hovering over the scroll area.

```python demo
rx.grid(
    rx.scroll_area(
        rx.flex(
            rx.text("type = 'auto'",  weight="bold"),
            rx.text(
                """Legibility describes how easily individual characters can be
        distinguished from one another. It is described by Walter Tracy as "the
        quality of being decipherable and recognisable". For instance, if a "b"
        and an "h", or a "3" and an "8", are difficult to distinguish at small
        sizes, this is a problem of legibility.""",
                size="2", trim="both",
            ),
            padding="8px", direction="column", spacing="4",
        ),
        type="auto",
        scrollbars="vertical",
        style={"height": 150}, 
    ),
    rx.scroll_area(
        rx.flex(
            rx.text("type = 'always'",  weight="bold"),
            rx.text(
                """Legibility describes how easily individual characters can be
        distinguished from one another. It is described by Walter Tracy as "the
        quality of being decipherable and recognisable". For instance, if a "b"
        and an "h", or a "3" and an "8", are difficult to distinguish at small
        sizes, this is a problem of legibility.""",
                size="2", trim="both",
            ),
            padding="8px", direction="column", spacing="4",
        ),
        type="always",
        scrollbars="vertical",
        style={"height": 150}, 
    ),
    rx.scroll_area(
        rx.flex(
            rx.text("type = 'scroll'",  weight="bold"),
            rx.text(
                """Legibility describes how easily individual characters can be
        distinguished from one another. It is described by Walter Tracy as "the
        quality of being decipherable and recognisable". For instance, if a "b"
        and an "h", or a "3" and an "8", are difficult to distinguish at small
        sizes, this is a problem of legibility.""",
                size="2", trim="both",
            ),
            padding="8px", direction="column", spacing="4",
        ),
        type="scroll",
        scrollbars="vertical",
        style={"height": 150}, 
    ),
    rx.scroll_area(
        rx.flex(
            rx.text("type = 'hover'",  weight="bold"),
            rx.text(
                """Legibility describes how easily individual characters can be
        distinguished from one another. It is described by Walter Tracy as "the
        quality of being decipherable and recognisable". For instance, if a "b"
        and an "h", or a "3" and an "8", are difficult to distinguish at small
        sizes, this is a problem of legibility.""",
                size="2", trim="both",
            ),
            padding="8px", direction="column", spacing="4",
        ),
        type="hover",
        scrollbars="vertical",
        style={"height": 150}, 
    ),
    columns="4",
    spacing="2",
)

```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/data-display/data_list.md`:

```md
---
components:
    - rx.data_list.root
    - rx.data_list.item
    - rx.data_list.label
    - rx.data_list.value
DataListRoot: |
    lambda **props: rx.data_list.root(
        rx.foreach(
            [["Status", "Authorized"], ["ID", "U-474747"], ["Name", "Developer Success"], ["Email", "foo@reflex.dev"]],
            lambda item: rx.data_list.item(rx.data_list.label(item[0]), rx.data_list.value(item[1])),
        ),
        **props,
    )
DataListItem: |
    lambda **props: rx.data_list.root(
        rx.foreach(
            [["Status", "Authorized"], ["ID", "U-474747"], ["Name", "Developer Success"], ["Email", "foo@reflex.dev"]],
            lambda item: rx.data_list.item(rx.data_list.label(item[0]), rx.data_list.value(item[1]), **props),
        ),
    )
DataListLabel: |
    lambda **props: rx.data_list.root(
        rx.foreach(
            [["Status", "Authorized"], ["ID", "U-474747"], ["Name", "Developer Success"], ["Email", "foo@reflex.dev"]],
            lambda item: rx.data_list.item(rx.data_list.label(item[0], **props), rx.data_list.value(item[1])),
        ),
    )
DataListValue: |
    lambda **props: rx.data_list.root(
        rx.foreach(
            [["Status", "Authorized"], ["ID", "U-474747"], ["Name", "Developer Success"], ["Email", "foo@reflex.dev"]],
            lambda item: rx.data_list.item(rx.data_list.label(item[0]), rx.data_list.value(item[1], **props)),
        ),
    )
---


# Data List

The `DataList` component displays key-value pairs and is particularly helpful for showing metadata.

A `DataList` needs to be initialized using `rx.data_list.root()` and currently takes in data list items: `rx.data_list.item`

```python demo
rx.card(
                rx.data_list.root(
                    rx.data_list.item(
                        rx.data_list.label("Status"),
                        rx.data_list.value(
                            rx.badge(
                                "Authorized",
                                variant="soft",
                                radius="full",
                            )
                        ),
                        align="center",
                    ),
                    rx.data_list.item(
                        rx.data_list.label("ID"),
                        rx.data_list.value(rx.code("U-474747")),
                    ),
                    rx.data_list.item(
                        rx.data_list.label("Name"),
                        rx.data_list.value("Developer Success"),
                        align="center",
                    ),
                    rx.data_list.item(
                        rx.data_list.label("Email"),
                        rx.data_list.value(
                            rx.link(
                                "success@reflex.dev",
                                href="mailto:success@reflex.dev",
                            ),
                        ),
                    ),
                    rx.data_list.item(
                        rx.data_list.label("Company"),
                        rx.data_list.value(
                            rx.link(
                                "Reflex",
                                href="https://reflex.dev",
                            ),
                        ),
                    ),
                ),
            ),
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/data-display/spinner.md`:

```md
---
components:
    - rx.spinner
---

# Spinner

Spinner is used to display an animated loading indicator when a task is in progress.


```python demo
rx.spinner()
```

## Basic Examples

Spinner can have different sizes.

```python demo
rx.vstack(
    rx.hstack(
        rx.spinner(size="1"),
        rx.spinner(size="2"),
        rx.spinner(size="3"),
        align="center",
        gap="1em"
    )
)
```

## Demo with buttons

Buttons have their own loading prop that automatically composes a spinner.

```python demo
rx.button("Bookmark", loading=True)
```

## Spinner inside a button

If you have an icon inside the button, you can use the button's disabled state and wrap the icon in a standalone rx.spinner to achieve a more sophisticated design.

```python demo
rx.button(
    rx.spinner(
        loading=True
    ),
    "Bookmark",
    disabled=True
)
```



```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/data-display/code_block.md`:

```md
---
components:
    - rx.code_block
---


# Code Block

The Code Block component can be used to display code easily within a website.
Put in a multiline string with the correct spacing and specify and language to show the desired code.

```python demo
rx.code_block(
    """def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))""",
    language="python",
    show_line_numbers=True,
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/data-display/callout-ll.md`:

```md
---
components:
    - rx.callout.root
    - rx.callout.icon
    - rx.callout.text
---



# Callout

A `callout` is a short message to attract user's attention.

```python demo
rx.callout.root(
    rx.callout.icon(rx.icon(tag="info")),
    rx.callout.text("You will need admin privileges to install and access this application."),
)
```

The `callout` component is made up of a `callout.root`, which groups `callout.icon` and `callout.text` parts. This component is based on the `div` element and supports common margin props.

The `callout.icon` provides width and height for the `icon` associated with the `callout`. This component is based on the `div` element. See the [**icon** component for all icons that are available.](/docs/library/datadisplay/icon/)

The `callout.text` renders the callout text. This component is based on the `p` element.

## As alert

```python demo
rx.callout.root(
    rx.callout.icon(rx.icon(tag="triangle_alert")),
    rx.callout.text("Access denied. Please contact the network administrator to view this page."),
    color_scheme="red",
    role="alert",
)
```

## Style

### Size

Use the `size` prop to control the size.

```python demo
rx.flex(
    rx.callout.root(
        rx.callout.icon(rx.icon(tag="info")),
        rx.callout.text("You will need admin privileges to install and access this application."),
        size="3",
    ),
    rx.callout.root(
        rx.callout.icon(rx.icon(tag="info")),
        rx.callout.text("You will need admin privileges to install and access this application."),
        size="2",
    ),
    rx.callout.root(
        rx.callout.icon(rx.icon(tag="info")),
        rx.callout.text("You will need admin privileges to install and access this application."),
        size="1",
    ),
    direction="column",
    spacing="3",
    align="start",
)
```

### Variant

Use the `variant` prop to control the visual style. It is set to `soft` by default.

```python demo
rx.flex(
    rx.callout.root(
        rx.callout.icon(rx.icon(tag="info")),
        rx.callout.text("You will need admin privileges to install and access this application."),
        variant="soft",
    ),
    rx.callout.root(
        rx.callout.icon(rx.icon(tag="info")),
        rx.callout.text("You will need admin privileges to install and access this application."),
        variant="surface",
    ),
    rx.callout.root(
        rx.callout.icon(rx.icon(tag="info")),
        rx.callout.text("You will need admin privileges to install and access this application."),
        variant="outline",
    ),
    direction="column",
    spacing="3",
)
```

### Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.

```python demo
rx.flex(
    rx.callout.root(
        rx.callout.icon(rx.icon(tag="info")),
        rx.callout.text("You will need admin privileges to install and access this application."),
        color_scheme="blue",
    ),
    rx.callout.root(
        rx.callout.icon(rx.icon(tag="info")),
        rx.callout.text("You will need admin privileges to install and access this application."),
        color_scheme="green",
    ),
    rx.callout.root(
        rx.callout.icon(rx.icon(tag="info")),
        rx.callout.text("You will need admin privileges to install and access this application."),
        color_scheme="red",
    ),
    direction="column",
    spacing="3",
)
```

### High Contrast

Use the `high_contrast` prop to add additional contrast.

```python demo
rx.flex(
    rx.callout.root(
        rx.callout.icon(rx.icon(tag="info")),
        rx.callout.text("You will need admin privileges to install and access this application."),
    ),
    rx.callout.root(
        rx.callout.icon(rx.icon(tag="info")),
        rx.callout.text("You will need admin privileges to install and access this application."),
        high_contrast=True,
    ),
    direction="column",
    spacing="3",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/data-display/icon.md`:

```md
---
components:
    - rx.lucide.Icon
---


# Icon

The Icon component is used to display an icon from a library of icons. This implementation is based on the [Lucide Icons](https://lucide.dev/icons) where you can find a list of all available icons.


## Icons List

```python eval
lucide_icons()
```

## Basic Example

To display an icon, specify the `tag` prop from the list of available icons.
Passing the tag as the first children is also supported and will be assigned to the `tag` prop.

The `tag` is expected to be in `snake_case` format, but `kebab-case` is also supported to allow copy-paste from [https://lucide.dev/icons](https://lucide.dev/icons).

```python demo
rx.flex(
    rx.icon("calendar"),
    rx.icon(tag="calendar"),
    gap="2",
)
```

## Dynamic Icons

It is not possible to use dynamic values as the `tag` prop, because it is used to import the icon from the Lucide library.
If you have a specific subset of icons you want to use dynamically, define an rx.match with them:

```python
def dynamic_icon(icon_name):
    return rx.match(
        icon_name,
        ("plus", rx.icon("plus")),
        ("minus", rx.icon("minus")),
        ("equal", rx.icon("equal")),
    )
```


You can then use the `dynamic_icon` function to display the icons dynamically.

```python demo
rx.foreach(["plus", "minus", "equal"], dynamic_icon)    
```

## Styling

Icon from Lucide can be customized with the following props `stroke_width`, `size` and `color`.

### Stroke Width

```python demo
rx.flex(
    rx.icon("moon", stroke_width=1),
    rx.icon("moon", stroke_width=1.5),
    rx.icon("moon", stroke_width=2),
    rx.icon("moon", stroke_width=2.5),
    gap="2"
)
```


### Size

```python demo
rx.flex(
    rx.icon("zoom_in", size=15),
    rx.icon("zoom_in", size=20),
    rx.icon("zoom_in", size=25),
    rx.icon("zoom_in", size=30),
    align="center",
    gap="2",
)
```

### Color

Here is an example using basic colors in icons.

```python demo
rx.flex(
    rx.icon("zoom_in", size=18, color="indigo"),
    rx.icon("zoom_in", size=18, color="cyan"),
    rx.icon("zoom_in", size=18, color="orange"),
    rx.icon("zoom_in", size=18, color="crimson"),
    gap="2",
)
```

A radix color with a scale may also be specified using `rx.color()` as seen below.

```python demo
rx.flex(
    rx.icon("zoom_in", size=18, color=rx.color("purple", 1)),
    rx.icon("zoom_in", size=18, color=rx.color("purple", 2)),
    rx.icon("zoom_in", size=18, color=rx.color("purple", 3)),
    rx.icon("zoom_in", size=18, color=rx.color("purple", 4)),
    rx.icon("zoom_in", size=18, color=rx.color("purple", 5)),
    rx.icon("zoom_in", size=18, color=rx.color("purple", 6)),
    rx.icon("zoom_in", size=18, color=rx.color("purple", 7)),
    rx.icon("zoom_in", size=18, color=rx.color("purple", 8)),
    rx.icon("zoom_in", size=18, color=rx.color("purple", 9)),
    rx.icon("zoom_in", size=18, color=rx.color("purple", 10)),
    rx.icon("zoom_in", size=18, color=rx.color("purple", 11)),
    rx.icon("zoom_in", size=18, color=rx.color("purple", 12)),
    gap="2",
)
```

Here is another example using the `accent` color with scales. The `accent` is the most dominant color in your theme.

```python demo
rx.flex(
    rx.icon("zoom_in", size=18, color=rx.color("accent", 1)),
    rx.icon("zoom_in", size=18, color=rx.color("accent", 2)),
    rx.icon("zoom_in", size=18, color=rx.color("accent", 3)),
    rx.icon("zoom_in", size=18, color=rx.color("accent", 4)),
    rx.icon("zoom_in", size=18, color=rx.color("accent", 5)),
    rx.icon("zoom_in", size=18, color=rx.color("accent", 6)),
    rx.icon("zoom_in", size=18, color=rx.color("accent", 7)),
    rx.icon("zoom_in", size=18, color=rx.color("accent", 8)),
    rx.icon("zoom_in", size=18, color=rx.color("accent", 9)),
    rx.icon("zoom_in", size=18, color=rx.color("accent", 10)),
    rx.icon("zoom_in", size=18, color=rx.color("accent", 11)),
    rx.icon("zoom_in", size=18, color=rx.color("accent", 12)),
    gap="2",
)
```


## Final Example

Icons can be used as child components of many other components. For example, adding a magnifying glass icon to a search bar.

```python demo
rx.badge(
    rx.flex(
        rx.icon("search", size=18),
        rx.text("Search documentation...", size="3", weight="medium"),
        direction="row",
        gap="1",
        align="center",
    ),
    size="2",
    radius="full",
    color_scheme="gray",
)
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/data-display/badge.md`:

```md
---
components:
    - rx.badge

Badge: |
    lambda **props: rx.badge("Basic Badge", **props)
---
# Badge


Badges are used to highlight an item's status for quick recognition.

## Basic Example

To create a badge component with only text inside, pass the text as an argument.

```python demo
rx.badge("New")
```

## Styling

```python eval
style_grid(component_used=rx.badge, component_used_str="rx.badge", variants=["solid", "soft", "surface", "outline"], components_passed="England!",)
```

### Size

The `size` prop controls the size and padding of a badge. It can take values of `"1" | "2"`, with default being `"1"`.

```python demo
rx.flex(
    rx.badge("New"),
    rx.badge("New", size="1"),
    rx.badge("New", size="2"),
    align="center",
    spacing="2",
)
```

### Variant

The `variant` prop controls the visual style of the badge. The supported variant types are `"solid" | "soft" | "surface" | "outline"`. The variant default is `"soft"`.

```python demo
rx.flex(
    rx.badge("New", variant="solid"),
    rx.badge("New", variant="soft"),
    rx.badge("New"),
    rx.badge("New", variant="surface"),
    rx.badge("New", variant="outline"),
    spacing="2",
)
```

### Color Scheme

The `color_scheme` prop sets a specific color, ignoring the global theme.

```python demo
rx.flex(
    rx.badge("New", color_scheme="indigo"),
    rx.badge("New", color_scheme="cyan"),
    rx.badge("New", color_scheme="orange"),
    rx.badge("New", color_scheme="crimson"),
    spacing="2",
)
```

### High Contrast

The `high_contrast` prop increases color contrast of the fallback text with the background.

```python demo
rx.flex(
    rx.flex(
        rx.badge("New", variant="solid"),
        rx.badge("New", variant="soft"),
        rx.badge("New", variant="surface"),
        rx.badge("New", variant="outline"),
        spacing="2",
    ),
    rx.flex(
        rx.badge("New", variant="solid", high_contrast=True),
        rx.badge("New", variant="soft", high_contrast=True),
        rx.badge("New", variant="surface", high_contrast=True),
        rx.badge("New", variant="outline", high_contrast=True),
        spacing="2",
    ),
    direction="column",
    spacing="2",
)
```

### Radius

The `radius` prop sets specific radius value, ignoring the global theme. It can take values `"none" | "small" | "medium" | "large" | "full"`.

```python demo
rx.flex(
    rx.badge("New", radius="none"),
    rx.badge("New", radius="small"),
    rx.badge("New", radius="medium"),
    rx.badge("New", radius="large"),
    rx.badge("New", radius="full"),
    spacing="3",
)
```

## Final Example

A badge may contain more complex elements within it. This example uses a `flex` component to align an icon and the text correctly, using the `gap` prop to
ensure a comfortable spacing between the two.

```python demo
rx.badge(
    rx.flex(
        rx.icon(tag="arrow_up"),
        rx.text("8.8%"),
        spacing="1",
    ),
    color_scheme="grass",
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/library/data-display/avatar.md`:

```md
---
components:
    - rx.avatar
Avatar: |
    lambda **props: rx.hstack(rx.avatar(src="/logo.jpg", **props), rx.avatar(fallback="RX", **props), spacing="3")
---
# Avatar


The Avatar component is used to represent a user, and display their profile pictures or fallback texts such as initials.

## Basic Example

To create an avatar component with an image, pass the image URL as the `src` prop.

```python demo
rx.avatar(src="/logo.jpg")
```

To display a text such as initials, set the `fallback` prop without passing the `src` prop.

```python demo
rx.avatar(fallback="RX")
```

## Styling

```python eval
style_grid(component_used=rx.avatar, component_used_str="rx.avatar", variants=["solid", "soft"], fallback="RX")
```

### Size

The `size` prop controls the size and spacing of the avatar. The acceptable size is from `"1"` to `"9"`, with `"3"` being the default.

```python demo
rx.flex(
    rx.avatar(src="/logo.jpg", fallback="RX", size="1"),
    rx.avatar(src="/logo.jpg", fallback="RX", size="2"),
    rx.avatar(src="/logo.jpg", fallback="RX", size="3"),
    rx.avatar(src="/logo.jpg", fallback="RX"),
    rx.avatar(src="/logo.jpg", fallback="RX", size="4"),
    rx.avatar(src="/logo.jpg", fallback="RX", size="5"),
    rx.avatar(src="/logo.jpg", fallback="RX", size="6"),
    rx.avatar(src="/logo.jpg", fallback="RX", size="7"),
    rx.avatar(src="/logo.jpg", fallback="RX", size="8"),
    spacing="1",
)
```

### Variant

The `variant` prop controls the visual style of the avatar fallback text. The variant can be `"solid"` or `"soft"`. The default is `"soft"`.

```python demo
rx.flex(
    rx.avatar(fallback="RX", variant="solid"),
    rx.avatar(fallback="RX", variant="soft"),
    rx.avatar(fallback="RX"),
    spacing="2",
)
```

### Color Scheme

The `color_scheme` prop sets a specific color to the fallback text, ignoring the global theme.

```python demo
rx.flex(
    rx.avatar(fallback="RX", color_scheme="indigo"),
    rx.avatar(fallback="RX", color_scheme="cyan"),
    rx.avatar(fallback="RX", color_scheme="orange"),
    rx.avatar(fallback="RX", color_scheme="crimson"),
    spacing="2",
)
```

### High Contrast

The `high_contrast` prop increases color contrast of the fallback text with the background.

```python demo
rx.grid(
    rx.avatar(fallback="RX", variant="solid"),
    rx.avatar(fallback="RX", variant="solid", high_contrast=True),
    rx.avatar(fallback="RX", variant="soft"),
    rx.avatar(fallback="RX", variant="soft", high_contrast=True),
    rows="2",
    spacing="2",
    flow="column",
)
```

### Radius

The `radius` prop sets specific radius value, ignoring the global theme. It can take values `"none" | "small" | "medium" | "large" | "full"`.

```python demo
rx.grid(
    rx.avatar(src="/logo.jpg", fallback="RX", radius="none"),
    rx.avatar(fallback="RX", radius="none"),
    rx.avatar(src="/logo.jpg", fallback="RX", radius="small"),
    rx.avatar(fallback="RX", radius="small"),
    rx.avatar(src="/logo.jpg", fallback="RX", radius="medium"),
    rx.avatar(fallback="RX", radius="medium"),
    rx.avatar(src="/logo.jpg", fallback="RX", radius="large"),
    rx.avatar(fallback="RX", radius="large"),
    rx.avatar(src="/logo.jpg", fallback="RX", radius="full"),
    rx.avatar(fallback="RX", radius="full"),
    rows="2",
    spacing="2",
    flow="column",
)
```

### Fallback

The `fallback` prop indicates the rendered text when the `src` cannot be loaded.

```python demo
rx.flex(
    rx.avatar(fallback="RX"),
    rx.avatar(fallback="PC"),
    spacing="2",
)
```

## Final Example

As part of a user profile page, the Avatar component is used to display the user's profile picture, with the fallback text showing the user's initials. Text components displays the user's full name and username handle and a Button component shows the edit profile button.

```python demo
rx.flex(
    rx.avatar(src="/logo.jpg", fallback="RU", size="9"),
    rx.text("Reflex User", weight="bold", size="4"),
    rx.text("@reflexuser", color_scheme="gray"),
    rx.button("Edit Profile", color_scheme="indigo", variant="solid"),
    direction="column",
    spacing="1",
)
```

```