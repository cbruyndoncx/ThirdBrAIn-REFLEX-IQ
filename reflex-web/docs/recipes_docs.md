Project Path: recipes

Source Tree:

```
recipes
├── layout
│   ├── footer.md
│   ├── navbar.md
│   └── sidebar.md
├── others
│   ├── dark_mode_toggle.md
│   ├── chips.md
│   ├── checkboxes.md
│   ├── speed_dial.md
│   └── pricing_cards.md
├── auth
│   ├── signup_form.md
│   └── login_form.md
└── content
    ├── top_banner.md
    ├── multi_column_row.md
    ├── grid.md
    ├── stats.md
    └── forms.md

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/recipes/layout/footer.md`:

```md

# Footer Bar

A footer bar is a common UI element located at the bottom of a webpage. It typically contains information about the website, such as contact details and links to other pages or sections of the site.

## Basic

```python demo exec toggle
def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)

def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading("PRODUCTS", size="4", weight="bold", as_="h3"),
        footer_item("Web Design", "/#"),
        footer_item("Web Development", "/#"),
        footer_item("E-commerce", "/#"),
        footer_item("Content Management", "/#"),
        footer_item("Mobile Apps", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column"
    )

def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading("RESOURCES", size="4", weight="bold", as_="h3"),
        footer_item("Blog", "/#"),
        footer_item("Case Studies", "/#"),
        footer_item("Whitepapers", "/#"),
        footer_item("Webinars", "/#"),
        footer_item("E-books", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column"
    )

def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)

def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="3",
        justify="end",
        width="100%"
    )

def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.image(src="/logo.jpg", width="2.25em", height="auto", border_radius="25%"),
                        rx.heading("Reflex", size="7", weight="bold"),
                        align_items="center"
                    ),
                    rx.text("© 2024 Reflex, Inc", size="3", white_space="nowrap", weight="medium"),
                    spacing="4",
                    align_items=["center", "center", "start"]
                ),
                footer_items_1(),
                footer_items_2(),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%"
            ),
            rx.divider(),
            rx.hstack(
                rx.hstack(
                    footer_item("Privacy Policy", "/#"),
                    footer_item("Terms of Service", "/#"),
                    spacing="4",
                    align="center",
                    width="100%"
                ),
                socials(),
                justify="between",
                width="100%"
            ),
            spacing="5",
            width="100%"
        ),
        width="100%"
    )
```

## Newsletter form

```python demo exec toggle
def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)

def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading("PRODUCTS", size="4", weight="bold", as_="h3"),
        footer_item("Web Design", "/#"),
        footer_item("Web Development", "/#"),
        footer_item("E-commerce", "/#"),
        footer_item("Content Management", "/#"),
        footer_item("Mobile Apps", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column"
    )

def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading("RESOURCES", size="4", weight="bold", as_="h3"),
        footer_item("Blog", "/#"),
        footer_item("Case Studies", "/#"),
        footer_item("Whitepapers", "/#"),
        footer_item("Webinars", "/#"),
        footer_item("E-books", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column"
    )

def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)

def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="3",
        justify_content=["center", "center", "end"],
        width="100%"
    )

def footer_newsletter() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                footer_items_1(),
                footer_items_2(),
                rx.vstack(
                    rx.text("JOIN OUR NEWSLETTER", size="4",
                            weight="bold"),
                    rx.hstack(
                        rx.input(placeholder="Your email address", type="email", size="3"),
                        rx.icon_button(rx.icon("arrow-right", padding="0.15em"), size="3"),
                        spacing="1",
                        justify="center",
                        width="100%"
                    ),
                    align_items=["center", "center", "start"],
                    justify="center",
                    height="100%"
                ),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%"
            ),
            rx.divider(),
            rx.flex(
                rx.hstack(
                    rx.image(src="/logo.jpg", width="2em", height="auto", border_radius="25%"),
                    rx.text("© 2024 Reflex, Inc", size="3", white_space="nowrap", weight="medium"),
                    spacing="2",
                    align="center",
                    justify_content=["center", "center", "start"],
                    width="100%"
                ),
                socials(),
                spacing="4",
                flex_direction=["column", "column", "row"],
                width="100%"
            ),
            spacing="5",
            width="100%"
        ),
        width="100%"
    )
```

## Three columns

```python demo exec toggle
def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)

def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading("PRODUCTS", size="4", weight="bold", as_="h3"),
        footer_item("Web Design", "/#"),
        footer_item("Web Development", "/#"),
        footer_item("E-commerce", "/#"),
        footer_item("Content Management", "/#"),
        footer_item("Mobile Apps", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column"
    )

def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading("RESOURCES", size="4", weight="bold", as_="h3"),
        footer_item("Blog", "/#"),
        footer_item("Case Studies", "/#"),
        footer_item("Whitepapers", "/#"),
        footer_item("Webinars", "/#"),
        footer_item("E-books", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column"
    )

def footer_items_3() -> rx.Component:
    return rx.flex(
        rx.heading("ABOUT US", size="4", weight="bold", as_="h3"),
        footer_item("Our Team", "/#"),
        footer_item("Careers", "/#"),
        footer_item("Contact Us", "/#"),
        footer_item("Privacy Policy", "/#"),
        footer_item("Terms of Service", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column"
    )

def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)

def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="3",
        justify_content=["center", "center", "end"],
        width="100%"
    )

def footer_three_columns() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                footer_items_1(),
                footer_items_2(),
                footer_items_3(),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%"
            ),
            rx.divider(),
            rx.flex(
                rx.hstack(
                    rx.image(src="/logo.jpg", width="2em", height="auto", border_radius="25%"),
                    rx.text("© 2024 Reflex, Inc", size="3", white_space="nowrap", weight="medium"),
                    spacing="2",
                    align="center",
                    justify_content=["center", "center", "start"],
                    width="100%"
                ),
                socials(),
                spacing="4",
                flex_direction=["column", "column", "row"],
                width="100%"
            ),
            spacing="5",
            width="100%"
        ),
        width="100%"
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/recipes/layout/navbar.md`:

```md

# Navigation Bar

A navigation bar, also known as a navbar, is a common UI element found at the top of a webpage or application.
It typically provides links or buttons to the main sections of a website or application, allowing users to easily navigate and access the different pages.

Navigation bars are useful for web apps because they provide a consistent and intuitive way for users to navigate through the app.
Having a clear and consistent navigation structure can greatly improve the user experience by making it easy for users to find the information they need and access the different features of the app.


```md video https://youtube.com/embed/ITOZkzjtjUA?start=2365&end=2627
# Video: Example of Using the Navbar Recipe
```

## Basic

```python demo exec toggle
def navbar_link(text: str, url: str) -> rx.Component:
	return rx.link(rx.text(text, size="4", weight="medium"), href=url)

def navbar() -> rx.Component:
	return rx.box(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/logo.jpg", width="2.25em", height="auto", border_radius="25%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.hstack(
					navbar_link("Home", "/#"),
					navbar_link("About", "/#"),
					navbar_link("Pricing", "/#"),
					navbar_link("Contact", "/#"),
					justify="end",
					spacing="5"
				),
				justify="between",
				align_items="center"
			),
		),
		rx.mobile_and_tablet(
			rx.hstack(
				rx.hstack(
					rx.image(src="/logo.jpg", width="2em",
							 height="auto", border_radius="25%"),
					rx.heading("Reflex", size="6", weight="bold"), align_items="center"),
				rx.menu.root(
					rx.menu.trigger(rx.icon("menu", size=30)),
					rx.menu.content(
						rx.menu.item("Home"),
						rx.menu.item("About"),
						rx.menu.item("Pricing"),
						rx.menu.item("Contact"),
					),
					justify="end"
				),
				justify="between",
				align_items="center"
			),
		),
		bg=rx.color("accent", 3),
		padding="1em",
		# position="fixed",
		# top="0px",
		# z_index="5",
		width="100%"
	)
```


## Dropdown

```python demo exec toggle
def navbar_link(text: str, url: str) -> rx.Component:
	return rx.link(rx.text(text, size="4", weight="medium"), href=url)

def navbar_dropdown() -> rx.Component:
	return rx.box(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/logo.jpg", width="2.25em", height="auto", border_radius="25%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.hstack(
					navbar_link("Home", "/#"),
					rx.menu.root(
						rx.menu.trigger(
							rx.button(rx.text("Services", size="4", weight="medium"), rx.icon(
								"chevron-down"), weight="medium", variant="ghost", size="3"),
						),
						rx.menu.content(
							rx.menu.item("Service 1"),
							rx.menu.item("Service 2"),
							rx.menu.item("Service 3"),
						),
					),
					navbar_link("Pricing", "/#"),
					navbar_link("Contact", "/#"),
					justify="end",
					spacing="5"
				),
				justify="between",
				align_items="center"
			),
		),
		rx.mobile_and_tablet(
			rx.hstack(
				rx.hstack(
					rx.image(src="/logo.jpg", width="2em", height="auto", border_radius="25%"),
					rx.heading("Reflex", size="6", weight="bold"), align_items="center"),
				rx.menu.root(
					rx.menu.trigger(rx.icon("menu", size=30)),
					rx.menu.content(
						rx.menu.item("Home"),
						rx.menu.sub(
							rx.menu.sub_trigger("Services"),
							rx.menu.sub_content(
								rx.menu.item("Service 1"),
								rx.menu.item("Service 2"),
								rx.menu.item("Service 3"),
							),
						),
						rx.menu.item("About"),
						rx.menu.item("Pricing"),
						rx.menu.item("Contact"),
					),
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		bg=rx.color("accent", 3),
		padding="1em",
		# position="fixed",
		# top="0px",
		# z_index="5",
		width="100%"
	)
```

## Search bar

```python demo exec toggle
def navbar_searchbar() -> rx.Component:
	return rx.box(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/logo.jpg", width="2.25em", height="auto", border_radius="25%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.input(
					rx.input.slot(rx.icon("search")),
					placeholder="Search...",
					type="search", size="2",
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		rx.mobile_and_tablet(
			rx.hstack(
				rx.hstack(
					rx.image(src="/logo.jpg", width="2em", height="auto", border_radius="25%"),
					rx.heading("Reflex", size="6", weight="bold"), align_items="center"),
				rx.input(
					rx.input.slot(rx.icon("search")),
					placeholder="Search...",
					type="search", size="2",
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		bg=rx.color("accent", 3),
		padding="1em",
		# position="fixed",
		# top="0px",
		# z_index="5",
		width="100%"
	)
```

## Icons

```python demo exec toggle
def navbar_icons_item(text: str, icon: str, url: str) -> rx.Component:
	return rx.link(rx.hstack(rx.icon(icon), rx.text(text, size="4", weight="medium")), href=url)

def navbar_icons_menu_item(text: str, icon: str, url: str) -> rx.Component:
	return rx.link(rx.hstack(rx.icon(icon, size=16), rx.text(text, size="3", weight="medium")), href=url)

def navbar_icons() -> rx.Component:
	return rx.box(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/logo.jpg", width="2.25em", height="auto", border_radius="25%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.hstack(
					navbar_icons_item("Home", "home", "/#"),
					navbar_icons_item("Pricing", "coins", "/#"),
					navbar_icons_item("Contact", "mail", "/#"),
					navbar_icons_item("Services", "layers", "/#"),
					spacing="6",
				),
				justify="between",
				align_items="center"
			),
		),
		rx.mobile_and_tablet(
			rx.hstack(
				rx.hstack(
					rx.image(src="/logo.jpg", width="2em", height="auto", border_radius="25%"),
					rx.heading("Reflex", size="6", weight="bold"), align_items="center"),
				rx.menu.root(
					rx.menu.trigger(rx.icon("menu", size=30)),
					rx.menu.content(
						navbar_icons_menu_item("Home", "home", "/#"),
						navbar_icons_menu_item("Pricing", "coins", "/#"),
						navbar_icons_menu_item("Contact", "mail", "/#"),
						navbar_icons_menu_item("Services", "layers", "/#"),
					),
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		bg=rx.color("accent", 3),
		padding="1em",
		# position="fixed",
		# top="0px",
		# z_index="5",
		width="100%"
	)
```

## Buttons

```python demo exec toggle
def navbar_link(text: str, url: str) -> rx.Component:
	return rx.link(rx.text(text, size="4", weight="medium"), href=url)

def navbar_buttons() -> rx.Component:
	return rx.box(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/logo.jpg", width="2.25em", height="auto", border_radius="25%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.hstack(
					navbar_link("Home", "/#"),
					navbar_link("About", "/#"),
					navbar_link("Pricing", "/#"),
					navbar_link("Contact", "/#"),
					spacing="5",
				),
				rx.hstack(
					rx.button("Sign Up", size="3", variant="outline"),
					rx.button("Log In", size="3"),
					spacing="4",
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		rx.mobile_and_tablet(
			rx.hstack(
				rx.hstack(
					rx.image(src="/logo.jpg", width="2em", height="auto", border_radius="25%"),
					rx.heading("Reflex", size="6", weight="bold"), align_items="center"),
				rx.menu.root(
					rx.menu.trigger(rx.icon("menu", size=30)),
					rx.menu.content(
						rx.menu.item("Home"),
						rx.menu.item("About"),
						rx.menu.item("Pricing"),
						rx.menu.item("Contact"),
						rx.menu.separator(),
						rx.menu.item("Log in"),
						rx.menu.item("Sign up"),
					),
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		bg=rx.color("accent", 3),
		padding="1em",
		# position="fixed",
		# top="0px",
		# z_index="5",
		width="100%"
	)
```

## User profile

```python demo exec toggle
def navbar_link(text: str, url: str) -> rx.Component:
	return rx.link(rx.text(text, size="4", weight="medium"), href=url)

def navbar_user() -> rx.Component:
	return rx.box(
		rx.desktop_only(
			rx.hstack(
				rx.hstack(
					rx.image(src="/logo.jpg", width="2.25em", height="auto", border_radius="25%"),
					rx.heading("Reflex", size="7", weight="bold"), align_items="center"),
				rx.hstack(
					navbar_link("Home", "/#"),
					navbar_link("About", "/#"),
					navbar_link("Pricing", "/#"),
					navbar_link("Contact", "/#"),
					spacing="5",
				),
				rx.menu.root(
                    rx.menu.trigger(rx.icon_button(
                        rx.icon("user"), size="2", radius="full")),
                    rx.menu.content(
                        rx.menu.item("Settings"),
                        rx.menu.item("Earnings"),
                        rx.menu.separator(),
                        rx.menu.item("Log out"),
                    ),
                    justify="end",
                ),
				justify="between",
				align_items="center"
			),
		),
		rx.mobile_and_tablet(
			rx.hstack(
				rx.hstack(
					rx.image(src="/logo.jpg", width="2em", height="auto", border_radius="25%"),
					rx.heading("Reflex", size="6", weight="bold"), align_items="center"),
				rx.menu.root(
					rx.menu.trigger(rx.icon_button(
                        rx.icon("user"), size="2", radius="full")),
                    rx.menu.content(
                        rx.menu.item("Settings"),
                        rx.menu.item("Earnings"),
                        rx.menu.separator(),
                        rx.menu.item("Log out"),
                    ),
					justify="end",
				),
				justify="between",
				align_items="center"
			),
		),
		bg=rx.color("accent", 3),
		padding="1em",
		# position="fixed",
		# top="0px",
		# z_index="5",
		width="100%"
	)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/recipes/layout/sidebar.md`:

```md

# Sidebar

Similar to a navigation bar, a sidebar is a common UI element found on the side of a webpage or application. It typically contains links to different sections of the site or app.

## Basic

```python demo exec toggle
def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
	return rx.link(
		rx.hstack(
			rx.icon(icon),
			rx.text(text, size="4"),
			width="100%",
			padding_x="0.5rem",
			padding_y="0.75rem",
			align="center",
			style={
				"_hover": {
					"bg": rx.color("accent", 4),
					"color": rx.color("accent", 11),
				},
				"border-radius": "0.5em",
			},
		),
		href=href,
		underline="none",
		weight="medium",
		width="100%"
	)

def sidebar_items() -> rx.Component:
	return rx.vstack(
		sidebar_item("Dashboard", "layout-dashboard", "/#"),
		sidebar_item("Projects", "square-library", "/#"),
		sidebar_item("Analytics", "bar-chart-4", "/#"),
		sidebar_item("Messages", "mail", "/#"),
		spacing="1",
		width="100%"
	)

def sidebar() -> rx.Component:
	return rx.box(
		rx.desktop_only(
			rx.vstack(
				rx.hstack(
					rx.image(src="/logo.jpg", width="2.25em",
								height="auto", border_radius="25%"),
					rx.heading("Reflex", size="7", weight="bold"),
					align="center",
					justify="start",
					padding_x="0.5rem",
					width="100%"
				),
				sidebar_items(),
				spacing="5",
				#position="fixed",
				# left="0px",
				# top="0px",
				# z_index="5",
				padding_x="1em",
				padding_y="1.5em",
				bg=rx.color("accent", 3),
				align="start",
				#height="100%",
				height="650px",
				width="16em",
			),
		),
		rx.mobile_and_tablet(
			rx.drawer.root(
				rx.drawer.trigger(rx.icon("align-justify", size=30)),
				rx.drawer.overlay(z_index="5"),
				rx.drawer.portal(
					rx.drawer.content(
						rx.vstack(
							rx.box(
								rx.drawer.close(rx.icon("x", size=30)),
								width="100%",
							),
							sidebar_items(),
							spacing="5",
							width="100%",
						),
						top="auto",
						right="auto",
						height="100%",
						width="20em",
						padding="1.5em",
						bg=rx.color("accent", 2)
					),
					width="100%",
				),
				direction="left"
			),
			padding="1em",
		),
	)
```

## Bottom user profile

```python demo exec toggle
def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
	return rx.link(
		rx.hstack(
			rx.icon(icon),
			rx.text(text, size="4"),
			width="100%",
			padding_x="0.5rem",
			padding_y="0.75rem",
			align="center",
			style={
				"_hover": {
					"bg": rx.color("accent", 4),
					"color": rx.color("accent", 11),
				},
				"border-radius": "0.5em",
			},
		),
		href=href,
		underline="none",
		weight="medium",
		width="100%"
	)

def sidebar_items() -> rx.Component:
	return rx.vstack(
		sidebar_item("Dashboard", "layout-dashboard", "/#"),
		sidebar_item("Projects", "square-library", "/#"),
		sidebar_item("Analytics", "bar-chart-4", "/#"),
		sidebar_item("Messages", "mail", "/#"),
		spacing="1",
		width="100%"
	)

def sidebar_bottom_profile() -> rx.Component:
	return rx.box(
		rx.desktop_only(
			rx.vstack(
				rx.hstack(
					rx.image(src="/logo.jpg", width="2.25em",
								height="auto", border_radius="25%"),
					rx.heading("Reflex", size="7", weight="bold"),
					align="center",
					justify="start",
					padding_x="0.5rem",
					width="100%"
				),
				sidebar_items(),
				rx.spacer(),
				rx.vstack(
					rx.vstack(
						sidebar_item("Settings", "settings", "/#"),
						sidebar_item("Log out", "log-out", "/#"),
						spacing="1",
						width="100%"
					),
					rx.divider(),
					rx.hstack(
						rx.icon_button(rx.icon("user"), size="3", radius="full"),
						rx.vstack(
							rx.box(
								rx.text("My account", size="3", weight="bold"),
								rx.text("user@reflex.dev", size="2", weight="medium"),
								width="100%"
							),
							spacing="0",
							align="start",
							justify="start",
							width="100%"
						),
						padding_x="0.5rem",
						align="center",
						justify="start",
						width="100%",
					),
					width="100%",
					spacing="5",
				),
				spacing="5",
				#position="fixed",
				# left="0px",
				# top="0px",
				# z_index="5",
				padding_x="1em",
				padding_y="1.5em",
				bg=rx.color("accent", 3),
				align="start",
				#height="100%",
				height="650px",
				width="16em",
			),
		),
		rx.mobile_and_tablet(
			rx.drawer.root(
				rx.drawer.trigger(rx.icon("align-justify", size=30)),
				rx.drawer.overlay(z_index="5"),
				rx.drawer.portal(
					rx.drawer.content(
						rx.vstack(
							rx.box(
							rx.drawer.close(rx.icon("x", size=30)),
							width="100%",
							),
							sidebar_items(),
							rx.spacer(),
							rx.vstack(
								rx.vstack(
									sidebar_item("Settings", "settings", "/#"),
									sidebar_item("Log out", "log-out", "/#"),
									width="100%",
									spacing="1",
								),
								rx.divider(margin="0"),
								rx.hstack(
									rx.icon_button(rx.icon("user"), size="3", radius="full"),
									rx.vstack(
										rx.box(
											rx.text("My account", size="3", weight="bold"),
											rx.text("user@reflex.dev", size="2", weight="medium"),
											width="100%"
										),
										spacing="0",
										justify="start",
										width="100%",
									),
									padding_x="0.5rem",
									align="center",
									justify="start",
									width="100%",
								),
								width="100%",
								spacing="5",
							),
							spacing="5",
							width="100%",
						),
						top="auto",
						right="auto",
						height="100%",
						width="20em",
						padding="1.5em",
						bg=rx.color("accent", 2)
					),
					width="100%",
				),
				direction="left"
			),
			padding="1em",
		),
	)
```

## Top user profile

```python demo exec toggle
def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
	return rx.link(
		rx.hstack(
			rx.icon(icon),
			rx.text(text, size="4"),
			width="100%",
			padding_x="0.5rem",
			padding_y="0.75rem",
			align="center",
			style={
				"_hover": {
					"bg": rx.color("accent", 4),
					"color": rx.color("accent", 11),
				},
				"border-radius": "0.5em",
			},
		),
		href=href,
		underline="none",
		weight="medium",
		width="100%"
	)

def sidebar_items() -> rx.Component:
	return rx.vstack(
		sidebar_item("Dashboard", "layout-dashboard", "/#"),
		sidebar_item("Projects", "square-library", "/#"),
		sidebar_item("Analytics", "bar-chart-4", "/#"),
		sidebar_item("Messages", "mail", "/#"),
		spacing="1",
		width="100%"
	)

def sidebar_top_profile() -> rx.Component:
	return rx.box(
		rx.desktop_only(
			rx.vstack(
				rx.hstack(
					rx.icon_button(rx.icon("user"), size="3", radius="full"),
                    rx.vstack(
						rx.box(
							rx.text("My account", size="3", weight="bold"),
							rx.text("user@reflex.dev", size="2", weight="medium"),
							width="100%"
						),
						spacing="0",
						justify="start",
						width="100%",
					),
                    rx.spacer(),
                    rx.icon_button(rx.icon("settings"), size="2",
                                   variant="ghost", color_scheme="gray"),
                    padding_x="0.5rem",
                    align="center",
                    width="100%",
                ),
				sidebar_items(),
				rx.spacer(),
				sidebar_item("Help & Support", "life-buoy", "/#"),
				spacing="5",
				#position="fixed",
				# left="0px",
				# top="0px",
				# z_index="5",
				padding_x="1em",
				padding_y="1.5em",
				bg=rx.color("accent", 3),
				align="start",
				#height="100%",
				height="650px",
				width="16em",
			),
		),
		rx.mobile_and_tablet(
			rx.drawer.root(
				rx.drawer.trigger(rx.icon("align-justify", size=30)),
				rx.drawer.overlay(z_index="5"),
				rx.drawer.portal(
					rx.drawer.content(
						rx.vstack(
							rx.box(
								rx.drawer.close(rx.icon("x", size=30)),
								width="100%",
							),
							sidebar_items(),
							rx.spacer(),
							rx.vstack(
								sidebar_item("Help & Support", "life-buoy", "/#"),
								rx.divider(margin="0"),
								rx.hstack(
									rx.icon_button(rx.icon("user"), size="3", radius="full"),
									rx.vstack(
										rx.box(
											rx.text("My account", size="3", weight="bold"),
											rx.text("user@reflex.dev", size="2", weight="medium"),
											width="100%"
										),
										spacing="0",
										justify="start",
										width="100%",
									),
									padding_x="0.5rem",
									align="center",
									justify="start",
									width="100%",
								),
								width="100%",
								spacing="5",
							),
							spacing="5",
							width="100%",
						),
						top="auto",
						right="auto",
						height="100%",
						width="20em",
						padding="1.5em",
						bg=rx.color("accent", 2)
					),
					width="100%",
				),
				direction="left"
			),
			padding="1em",
		),
	)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/recipes/others/dark_mode_toggle.md`:

```md

# Dark Mode Toggle

The Dark Mode Toggle component lets users switch between light and dark themes.

```python demo exec toggle
import reflex as rx
from reflex.style import set_color_mode, color_mode

def dark_mode_toggle() -> rx.Component:
    return rx.segmented_control.root(
        rx.segmented_control.item(
            rx.icon(tag="monitor", size=20),
            value="system",
        ),
        rx.segmented_control.item(
            rx.icon(tag="sun", size=20),
            value="light",
        ),
        rx.segmented_control.item(
            rx.icon(tag="moon", size=20),
            value="dark",
        ),
        on_change=set_color_mode,
        variant="classic",
        radius="large",
        value=color_mode,
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/recipes/others/chips.md`:

```md

# Chips

Chips are compact elements that represent small pieces of information, such as tags or categories. They are commonly used to select multiple items from a list or to filter content.

## Status

```python demo exec toggle
from reflex.components.radix.themes.base import LiteralAccentColor

status_chip_props = {
    "radius": "full",
    "variant": "outline",
    "size": "3",
}

def status_chip(status: str, icon: str, color: LiteralAccentColor) -> rx.Component:
    return rx.badge(
        rx.icon(icon, size=18),
        status,
        color_scheme=color,
        **status_chip_props,
    )

def status_chips_group() -> rx.Component:
    return rx.hstack(
        status_chip("Info", "info", "blue"),
        status_chip("Success", "circle-check", "green"),
        status_chip("Warning", "circle-alert", "yellow"),
        status_chip("Error", "circle-x", "red"),
        wrap="wrap",
		spacing="2",
    )
```

## Single selection

```python demo exec toggle
chip_props = {
    "radius": "full",
    "variant": "soft",
    "size": "3",
    "cursor": "pointer",
    "style": {"_hover": {"opacity": 0.75}},
}

available_items = ["2:00", "3:00", "4:00", "5:00"]

class SingleSelectionChipsState(rx.State):
    selected_item: str = ""

def unselected_item(item: str) -> rx.Component:
    return rx.badge(
        item,
        color_scheme="gray",
        **chip_props,
        on_click=SingleSelectionChipsState.setvar("selected_item", item),
    )

def selected_item(item: str) -> rx.Component:
    return rx.badge(
        rx.icon("check", size=18),
        item,
        color_scheme="mint",
        **chip_props,
        on_click=SingleSelectionChipsState.setvar("selected_item", ""),
    )

def item_chip(item: str) -> rx.Component:
    return rx.cond(
        SingleSelectionChipsState.selected_item == item,
        selected_item(item),
        unselected_item(item),
    )

def item_selector() -> rx.Component:
    return rx.vstack(
        rx.hstack(
			rx.icon("clock", size=20),
			rx.heading(
				"Select your reservation time:", size="4"
			),
			spacing="2",
			align="center",
			width="100%",
        ),
        rx.hstack(
            rx.foreach(available_items, item_chip),
            wrap="wrap",
            spacing="2",
        ),
		align_items="start",
        spacing="4",
        width="100%",
    )
```

## Multiple selection

This example demonstrates selecting multiple skills from a list. It includes buttons to add all skills, clear selected skills, and select a random number of skills.

```python demo exec toggle
import random
from reflex.components.radix.themes.base import LiteralAccentColor

chip_props = {
    "radius": "full",
    "variant": "surface",
    "size": "3",
    "cursor": "pointer",
    "style": {"_hover": {"opacity": 0.75}},
}

skills = [
    "Data Management",
    "Networking",
    "Security",
    "Cloud",
    "DevOps",
    "Data Science",
    "AI",
    "ML",
    "Robotics",
    "Cybersecurity",
]

class BasicChipsState(rx.State):
    selected_items: list[str] = skills[:3]

    @rx.event
    def add_selected(self, item: str):
        self.selected_items.append(item)

    @rx.event
    def remove_selected(self, item: str):
        self.selected_items.remove(item)

    @rx.event
    def add_all_selected(self):
        self.selected_items = list(skills)

    @rx.event
    def clear_selected(self):
        self.selected_items.clear()

    @rx.event
    def random_selected(self):
        self.selected_items = random.sample(skills, k=random.randint(1, len(skills)))

def action_button(icon: str, label: str, on_click: callable, color_scheme: LiteralAccentColor) -> rx.Component:
    return rx.button(
        rx.icon(icon, size=16),
        label,
        variant="soft",
        size="2",
        on_click=on_click,
        color_scheme=color_scheme,
        cursor="pointer",
    )

def selected_item_chip(item: str) -> rx.Component:
    return rx.badge(
        item,
        rx.icon("circle-x", size=18),
        color_scheme="green",
        **chip_props,
        on_click=BasicChipsState.remove_selected(item),
    )

def unselected_item_chip(item: str) -> rx.Component:
    return rx.cond(
        BasicChipsState.selected_items.contains(item),
        rx.fragment(),
        rx.badge(
            item,
            rx.icon("circle-plus", size=18),
            color_scheme="gray",
            **chip_props,
            on_click=BasicChipsState.add_selected(item),
        ),
    )

def items_selector() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.hstack(
                rx.icon("lightbulb", size=20),
                rx.heading(
                    "Skills" + f" ({BasicChipsState.selected_items.length()})", size="4"
                ),
                spacing="1",
                align="center",
                width="100%",
				justify_content=["end", "start"],
            ),
            rx.hstack(
                action_button(
                    "plus", "Add All", BasicChipsState.add_all_selected, "green"
                ),
                action_button(
                    "trash", "Clear All", BasicChipsState.clear_selected, "tomato"
                ),
                action_button(
                    "shuffle", "", BasicChipsState.random_selected, "gray"
                ),
                spacing="2",
                justify="end",
                width="100%",
            ),
            justify="between",
            flex_direction=["column", "row"],
            align="center",
			spacing="2",
			margin_bottom="10px",
            width="100%",
        ),
        # Selected Items
        rx.flex(
            rx.foreach(
                BasicChipsState.selected_items,
                selected_item_chip,
            ),
            wrap="wrap",
			spacing="2",
			justify_content="start",
        ),
        rx.divider(),
        # Unselected Items
        rx.flex(
            rx.foreach(skills, unselected_item_chip),
            wrap="wrap",
			spacing="2",
			justify_content="start",
        ),
		justify_content="start",
		align_items="start",
        width="100%",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/recipes/others/checkboxes.md`:

```md

# Smart Checkboxes Group

A smart checkboxes group where you can track all checked boxes, as well as place a limit on how many checks are possible.

## Recipe

```python eval
rx.center(rx.image(src="/gallery/smart_checkboxes.gif"))
```

This recipe use a `dict[str, bool]` for the checkboxes state tracking.
Additionally, the limit that prevent the user from checking more boxes than allowed with a computed var.

```python
class CBoxeState(rx.State):
    
    choices: dict[str, bool] = \{k: False for k in ["Choice A", "Choice B", "Choice C"]}
    _check_limit = 2

    def check_choice(self, value, index):
        self.choices[index] = value

    @rx.var
    def choice_limit(self):
        return sum(self.choices.values()) >= self._check_limit

    @rx.var
    def checked_choices(self):
        choices = [l for l, v in self.choices.items() if v]
        return " / ".join(choices) if choices else "None"

import reflex as rx


def render_checkboxes(values, limit, handler):
    return rx.vstack(
            rx.foreach(
                values,
                lambda choice: rx.checkbox(
                    choice[0],
                    checked=choice[1],
                    disabled=~choice[1] & limit,
                    on_change=lambda val: handler(val, choice[0]),
                ),
            )
    )


def index() -> rx.Component:
    
    return rx.center(
        rx.vstack(
            rx.text("Make your choices (2 max):"),
            render_checkboxes(
                CBoxeState.choices,
                CBoxeState.choice_limit,
                CBoxeState.check_choice,
            ),
            rx.text("Your choices: ", CBoxeState.checked_choices),
        ),
        height="100vh",
    )
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/recipes/others/speed_dial.md`:

```md

# Speed Dial

A speed dial is a component that allows users to quickly access frequently used actions or pages. It is often used in the bottom right corner of the screen.

# Vertical

```python demo exec toggle
class SpeedDialVertical(rx.ComponentState):
	is_open: bool = False

	@rx.event
	def toggle(self, value: bool):
		self.is_open = value

	@classmethod
	def get_component(cls, **props):
		def menu_item(icon: str, text: str) -> rx.Component:
			return rx.tooltip(
				rx.icon_button(
					rx.icon(icon, padding="2px"),
					variant="soft",
					color_scheme="gray",
					size="3",
					cursor="pointer",
					radius="full",
				),
				side="left",
				content=text,
			)

		def menu() -> rx.Component:
			return rx.vstack(
				menu_item("copy", "Copy"),
				menu_item("download", "Download"),
				menu_item("share-2", "Share"),
				position="absolute",
				bottom="100%",
				spacing="2",
				padding_bottom="10px",
				left="0",
				direction="column-reverse",
				align_items="center",
			)

		return rx.box(
			rx.box(
				rx.icon_button(
					rx.icon(
						"plus",
						style={
							"transform": rx.cond(cls.is_open, "rotate(45deg)", "rotate(0)"),
							"transition": "transform 150ms cubic-bezier(0.4, 0, 0.2, 1)",
						},
					),
					variant="solid",
					color_scheme="blue",
					size="3",
					cursor="pointer",
					radius="full",
					position="relative",
				),
				rx.cond(
					cls.is_open,
					menu(),
				),
				position="relative",
			),
			on_mouse_enter=cls.toggle(True),
			on_mouse_leave=cls.toggle(False),
			on_click=cls.toggle(~cls.is_open),
			style={"bottom": "15px", "right": "15px"},
			position="absolute",
			# z_index="50",
			**props,
		)

speed_dial_vertical = SpeedDialVertical.create

def render_vertical():
	return rx.box(
		speed_dial_vertical(),
		height="250px",
		position="relative",
		width="100%",
	)
```

# Horizontal

```python demo exec toggle
class SpeedDialHorizontal(rx.ComponentState):
	is_open: bool = False

	@rx.event
	def toggle(self, value: bool):
		self.is_open = value

	@classmethod
	def get_component(cls, **props):
		def menu_item(icon: str, text: str) -> rx.Component:
			return rx.tooltip(
				rx.icon_button(
					rx.icon(icon, padding="2px"),
					variant="soft",
					color_scheme="gray",
					size="3",
					cursor="pointer",
					radius="full",
				),
				side="top",
				content=text,
			)

		def menu() -> rx.Component:
			return rx.hstack(
				menu_item("copy", "Copy"),
				menu_item("download", "Download"),
				menu_item("share-2", "Share"),
				position="absolute",
				bottom="0",
				spacing="2",
				padding_right="10px",
				right="100%",
				direction="row-reverse",
				align_items="center",
			)

		return rx.box(
			rx.box(
				rx.icon_button(
					rx.icon(
						"plus",
						style={
							"transform": rx.cond(cls.is_open, "rotate(45deg)", "rotate(0)"),
							"transition": "transform 150ms cubic-bezier(0.4, 0, 0.2, 1)",
						},
						class_name="dial",
					),
					variant="solid",
					color_scheme="green",
					size="3",
					cursor="pointer",
					radius="full",
					position="relative",
				),
				rx.cond(
					cls.is_open,
					menu(),
				),
				position="relative",
			),
			on_mouse_enter=cls.toggle(True),
			on_mouse_leave=cls.toggle(False),
			on_click=cls.toggle(~cls.is_open),
			style={"bottom": "15px", "right": "15px"},
			position="absolute",
			# z_index="50",
			**props,
		)

speed_dial_horizontal = SpeedDialHorizontal.create

def render_horizontal():
	return rx.box(
		speed_dial_horizontal(),
		height="250px",
		position="relative",
		width="100%",
	)
```

# Vertical with text

```python demo exec toggle
class SpeedDialVerticalText(rx.ComponentState):
	is_open: bool = False

	@rx.event
	def toggle(self, value: bool):
		self.is_open = value

	@classmethod
	def get_component(cls, **props):
		def menu_item(icon: str, text: str) -> rx.Component:
			return rx.hstack(
				rx.text(text, weight="medium"),
				rx.icon_button(
					rx.icon(icon, padding="2px"),
					variant="soft",
					color_scheme="gray",
					size="3",
					cursor="pointer",
					radius="full",
					position="relative",
				),
				opacity="0.75",
				_hover={
					"opacity": "1",
				},
				align_items="center",
			)

		def menu() -> rx.Component:
			return rx.vstack(
				menu_item("copy", "Copy"),
				menu_item("download", "Download"),
				menu_item("share-2", "Share"),
				position="absolute",
				bottom="100%",
				spacing="2",
				padding_bottom="10px",
				right="0",
				direction="column-reverse",
				align_items="end",
				justify_content="end",
			)

		return rx.box(
			rx.box(
				rx.icon_button(
					rx.icon(
						"plus",
						style={
							"transform": rx.cond(cls.is_open, "rotate(45deg)", "rotate(0)"),
							"transition": "transform 150ms cubic-bezier(0.4, 0, 0.2, 1)",
						},
						class_name="dial",
					),
					variant="solid",
					color_scheme="crimson",
					size="3",
					cursor="pointer",
					radius="full",
					position="relative",
				),
				rx.cond(
					cls.is_open,
					menu(),
				),
				position="relative",
			),
			on_mouse_enter=cls.toggle(True),
			on_mouse_leave=cls.toggle(False),
			on_click=cls.toggle(~cls.is_open),
			style={"bottom": "15px", "right": "15px"},
			position="absolute",
			# z_index="50",
			**props,
		)

speed_dial_vertical_text = SpeedDialVerticalText.create

def render_vertical_text():
	return rx.box(
		speed_dial_vertical_text(),
		height="250px",
		position="relative",
		width="100%",
	)
```

# Reveal animation

```python demo exec toggle
class SpeedDialReveal(rx.ComponentState):
	is_open: bool = False

	@rx.event
	def toggle(self, value: bool):
		self.is_open = value

	@classmethod
	def get_component(cls, **props):
		def menu_item(icon: str, text: str) -> rx.Component:
			return rx.tooltip(
				rx.icon_button(
					rx.icon(icon, padding="2px"),
					variant="soft",
					color_scheme="gray",
					size="3",
					cursor="pointer",
					radius="full",
					style={
						"animation": rx.cond(cls.is_open, "reveal 0.3s ease both", "none"),
						"@keyframes reveal": {
							"0%": {
								"opacity": "0",
								"transform": "scale(0)",
							},
							"100%": {
								"opacity": "1",
								"transform": "scale(1)",
							},
						},
					},
				),
				side="left",
				content=text,
			)

		def menu() -> rx.Component:
			return rx.vstack(
				menu_item("copy", "Copy"),
				menu_item("download", "Download"),
				menu_item("share-2", "Share"),
				position="absolute",
				bottom="100%",
				spacing="2",
				padding_bottom="10px",
				left="0",
				direction="column-reverse",
				align_items="center",
			)

		return rx.box(
			rx.box(
				rx.icon_button(
					rx.icon(
						"plus",
						style={
							"transform": rx.cond(cls.is_open, "rotate(45deg)", "rotate(0)"),
							"transition": "transform 150ms cubic-bezier(0.4, 0, 0.2, 1)",
						},
						class_name="dial",
					),
					variant="solid",
					color_scheme="violet",
					size="3",
					cursor="pointer",
					radius="full",
					position="relative",
				),
				rx.cond(
					cls.is_open,
					menu(),
				),
				position="relative",
			),
			on_mouse_enter=cls.toggle(True),
			on_mouse_leave=cls.toggle(False),
			on_click=cls.toggle(~cls.is_open),
			style={"bottom": "15px", "right": "15px"},
			position="absolute",
			# z_index="50",
			**props,
		)

speed_dial_reveal = SpeedDialReveal.create

def render_reveal():
	return rx.box(
		speed_dial_reveal(),
		height="250px",
		position="relative",
		width="100%",
	)
```

# Menu

```python demo exec toggle
class SpeedDialMenu(rx.ComponentState):
    is_open: bool = False

    @rx.event
    def toggle(self, value: bool):
        self.is_open = value

    @classmethod
    def get_component(cls, **props):
        def menu_item(icon: str, text: str) -> rx.Component:
            return rx.hstack(
                rx.icon(icon, padding="2px"),
                rx.text(text, weight="medium"),
                align="center",
                opacity="0.75",
                cursor="pointer",
                position="relative",
                _hover={
                    "opacity": "1",
                },
                width="100%",
                align_items="center",
            )

        def menu() -> rx.Component:
            return rx.box(
                rx.card(
                    rx.vstack(
                        menu_item("copy", "Copy"),
                        rx.divider(margin="0"),
                        menu_item("download", "Download"),
                        rx.divider(margin="0"),
                        menu_item("share-2", "Share"),
                        direction="column-reverse",
                        align_items="end",
                        justify_content="end",
                    ),
                    box_shadow="0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)",
                ),
                position="absolute",
                bottom="100%",
                right="0",
                padding_bottom="10px",
            )

        return rx.box(
            rx.box(
                rx.icon_button(
                    rx.icon(
                        "plus",
                        style={
                            "transform": rx.cond(cls.is_open, "rotate(45deg)", "rotate(0)"),
                            "transition": "transform 150ms cubic-bezier(0.4, 0, 0.2, 1)",
                        },
                        class_name="dial",
                    ),
                    variant="solid",
                    color_scheme="orange",
                    size="3",
                    cursor="pointer",
                    radius="full",
                    position="relative",
                ),
                rx.cond(
                    cls.is_open,
                    menu(),
                ),
                position="relative",
            ),
			on_mouse_enter=cls.toggle(True),
			on_mouse_leave=cls.toggle(False),
			on_click=cls.toggle(~cls.is_open),
            style={"bottom": "15px", "right": "15px"},
            position="absolute",
            # z_index="50",
            **props,
        )


speed_dial_menu = SpeedDialMenu.create

def render_menu():
	return rx.box(
		speed_dial_menu(),
		height="250px",
		position="relative",
		width="100%",
	)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/recipes/others/pricing_cards.md`:

```md

# Pricing Cards

A pricing card shows the price of a product or service. It typically includes a title, description, price, features, and a purchase button.

## Basic

```python demo exec toggle
def feature_item(text: str) -> rx.Component:
    return rx.hstack(rx.icon("check", color=rx.color("grass", 9)), rx.text(text, size="4"))

def features() -> rx.Component:
    return rx.vstack(
        feature_item("24/7 customer support"),
        feature_item("Daily backups"),
        feature_item("Advanced analytics"),
        feature_item("Customizable templates"),
        feature_item("Priority email support"),
        width="100%",
        align_items="start",
    )

def pricing_card_beginner() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text("Beginner", weight="bold", size="6"),
            rx.text("Ideal choice for personal use & for your next project.", size="4", opacity=0.8, align="center"),
            rx.hstack(
                rx.text("$39", weight="bold", font_size="3rem", trim="both"),
                rx.text("/month", size="4", opacity=0.8, trim="both"),
                width="100%",
                align_items="end",
                justify="center"
            ),
            width="100%",
            align="center",
            spacing="6",
        ),
        features(),
        rx.button("Get started", size="3", variant="solid", width="100%", color_scheme="blue"),
        spacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        background=rx.color("gray", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        justify="center",
        border_radius="0.5rem",
    )
```

## Comparison cards

```python demo exec toggle
def feature_item(feature: str) -> rx.Component:
    return rx.hstack(
        rx.icon("check", color=rx.color("blue", 9), size=21),
        rx.text(feature, size="4", weight="regular"),
    )


def standard_features() -> rx.Component:
    return rx.vstack(
        feature_item("40 credits for image generation"),
        feature_item("Credits never expire"),
        feature_item("High quality images"),
        feature_item("Commercial license"),
        spacing="3",
        width="100%",
        align_items="start",
    )


def popular_features() -> rx.Component:
    return rx.vstack(
        feature_item("250 credits for image generation"),
        feature_item("+30% Extra free credits"),
        feature_item("Credits never expire"),
        feature_item("High quality images"),
        feature_item("Commercial license"),
        spacing="3",
        width="100%",
        align_items="start",
    )


def pricing_card_standard() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.text(
                    "$14.99",
                    trim="both",
                    as_="s",
                    size="3",
                    weight="regular",
                    opacity=0.8,
                ),
                rx.text("$3.99", trim="both", size="6", weight="regular"),
                width="100%",
                spacing="2",
                align_items="end",
            ),
            height="35px",
            align_items="center",
            justify="between",
            width="100%",
        ),
        rx.text(
            "40 Image Credits",
            weight="bold",
            size="7",
            width="100%",
            text_align="left",
        ),
        standard_features(),
        rx.spacer(),
        rx.button(
            "Purchase",
            size="3",
            variant="outline",
            width="100%",
            color_scheme="blue",
        ),
        spacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        background=rx.color("gray", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        min_height="475px",
        border_radius="0.5rem",
    )


def pricing_card_popular() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.text(
                    "$69.99",
                    trim="both",
                    as_="s",
                    size="3",
                    weight="regular",
                    opacity=0.8,
                ),
                rx.text("$18.99", trim="both", size="6", weight="regular"),
                width="100%",
                spacing="2",
                align_items="end",
            ),
            rx.badge(
                "POPULAR",
                size="2",
                radius="full",
                variant="soft",
                color_scheme="blue",
            ),
            align_items="center",
            justify="between",
            height="35px",
            width="100%",
        ),
        rx.text(
            "250 Image Credits",
            weight="bold",
            size="7",
            width="100%",
            text_align="left",
        ),
        popular_features(),
        rx.spacer(),
        rx.button("Purchase", size="3", width="100%", color_scheme="blue"),
        spacing="6",
        border=f"1.5px solid {rx.color('blue', 6)}",
        background=rx.color("blue", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        min_height="475px",
        border_radius="0.5rem",
    )


def pricing_cards() -> rx.Component:
    return rx.flex(
        pricing_card_standard(),
        pricing_card_popular(),
        spacing="4",
        flex_direction=["column", "column", "row"],
        width="100%",
        align_items="center",
    )
```


```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/recipes/auth/signup_form.md`:

```md

# Sign up Form

The sign up form is a common component in web applications. It allows users to create an account and access the application's features. This page provides a few examples of sign up forms that you can use in your application.
## Default

```python demo exec toggle
def signup_default() -> rx.Component:
	return rx.card(
		rx.vstack(
			rx.center(
				rx.image(src="/logo.jpg", width="2.5em", height="auto", border_radius="25%"),
				rx.heading("Create an account", size="6", as_="h2", text_align="center", width="100%"),
				direction="column",
				spacing="5",
				width="100%"
			),
			rx.vstack(
				rx.text("Email address", size="3", weight="medium", text_align="left", width="100%"),
				rx.input(placeholder="user@reflex.dev", type="email", size="3", width="100%"),
				justify="start",
				spacing="2",
				width="100%"
			),
			rx.vstack(
				rx.text("Password", size="3", weight="medium", text_align="left", width="100%"),
				rx.input(placeholder="Enter your password", type="password", size="3", width="100%"),
				justify="start",
				spacing="2",
				width="100%"
			),
			rx.box(
				rx.checkbox(
					"Agree to Terms and Conditions",
					default_checked=True,
					spacing="2"
				),
				width="100%"
			),
			rx.button("Register", size="3", width="100%"),
			rx.center(
				rx.text("Already registered?", size="3"),
				rx.link("Sign in", href="#", size="3"),
				opacity="0.8",
				spacing="2",
				direction="row"
			),
			spacing="6",
			width="100%"
		),
		size="4",
		max_width="28em",
		width="100%"
	)
```

## Icons

```python demo exec toggle
def signup_default_icons() -> rx.Component:
	return rx.card(
		rx.vstack(
			rx.center(
				rx.image(src="/logo.jpg", width="2.5em", height="auto", border_radius="25%"),
				rx.heading("Create an account", size="6", as_="h2", text_align="center", width="100%"),
				direction="column",
				spacing="5",
				width="100%"
			),
			rx.vstack(
				rx.text("Email address", size="3", weight="medium", text_align="left", width="100%"),
				rx.input(rx.input.slot(rx.icon("user")), placeholder="user@reflex.dev", type="email", size="3", width="100%"),
				justify="start",
				spacing="2",
				width="100%"
			),
			rx.vstack(
				rx.text("Password", size="3", weight="medium", text_align="left", width="100%"),
				rx.input(rx.input.slot(rx.icon("lock")), placeholder="Enter your password", type="password", size="3", width="100%"),
				justify="start",
				spacing="2",
				width="100%"
			),
			rx.box(
				rx.checkbox(
					"Agree to Terms and Conditions",
					default_checked=True,
					spacing="2"
				),
				width="100%"
			),
			rx.button("Register", size="3", width="100%"),
			rx.center(
				rx.text("Already registered?", size="3"),
				rx.link("Sign in", href="#", size="3"),
				opacity="0.8",
				spacing="2",
				direction="row",
				width="100%"
			),
			spacing="6",
			width="100%"
		),
		max_width="28em",
		size="4",
		width="100%"
	)
```

## Third-party auth


```python demo exec toggle
def signup_single_thirdparty() -> rx.Component:
	return rx.card(
		rx.vstack(
			rx.flex(
				rx.image(src="/logo.jpg", width="2.5em", height="auto", border_radius="25%"),
				rx.heading("Create an account", size="6", as_="h2", text_align="left", width="100%"),
				rx.hstack(
					rx.text("Already registered?", size="3", text_align="left"),
					rx.link("Sign in", href="#", size="3"),
					spacing="2",
					opacity="0.8",
					width="100%"
				),
				direction="column",
				justify="start",
				spacing="4",
				width="100%"
			),
			rx.vstack(
				rx.text("Email address", size="3", weight="medium", text_align="left", width="100%"),
				rx.input(rx.input.slot(rx.icon("user")), placeholder="user@reflex.dev", type="email", size="3", width="100%"),
				justify="start",
				spacing="2",
				width="100%"
			),
			rx.vstack(
				rx.text("Password", size="3", weight="medium", text_align="left", width="100%"),
				rx.input(rx.input.slot(rx.icon("lock")), placeholder="Enter your password", type="password", size="3", width="100%"),
				justify="start",
				spacing="2",
				width="100%"
			),
			rx.box(
				rx.checkbox(
					"Agree to Terms and Conditions",
					default_checked=True,
					spacing="2"
				),
				width="100%"
			),
			rx.button("Register", size="3", width="100%"),
			rx.hstack(
				rx.divider(margin="0"),
				rx.text("Or continue with", white_space="nowrap", weight="medium"),
				rx.divider(margin="0"),
				align="center",
				width="100%"
			),
			rx.button(
				rx.icon(tag="github"),
				"Sign in with Github",
				variant="outline",
				size="3",
				width="100%"
			),
			spacing="6",
			width="100%"
		),
		size="4",
		max_width="28em",
		width="100%"
	)
```

## Multiple third-party auth

```python demo exec toggle
def signup_multiple_thirdparty() -> rx.Component:
	return rx.card(
		rx.vstack(
			rx.flex(
				rx.image(src="/logo.jpg", width="2.5em", height="auto", border_radius="25%"),
				rx.heading("Create an account", size="6", as_="h2", width="100%"),
				rx.hstack(
					rx.text("Already registered?", size="3", text_align="left"),
					rx.link("Sign in", href="#", size="3"),
					spacing="2",
					opacity="0.8",
					width="100%"
				),
				justify="start",
				direction="column",
				spacing="4",
				width="100%"
			),
			rx.vstack(
				rx.text("Email address", size="3", weight="medium", text_align="left", width="100%"),
				rx.input(rx.input.slot(rx.icon("user")), placeholder="user@reflex.dev", type="email", size="3", width="100%"),
				justify="start",
				spacing="2",
				width="100%"
			),
			rx.vstack(
				rx.text("Password", size="3", weight="medium", text_align="left", width="100%"),
				rx.input(rx.input.slot(rx.icon("lock")), placeholder="Enter your password", type="password", size="3", width="100%"),
				justify="start",
				spacing="2",
				width="100%"
			),
			rx.box(
				rx.checkbox(
					"Agree to Terms and Conditions",
					default_checked=True,
					spacing="2"
				),
				width="100%"
			),
			rx.button("Register", size="3", width="100%"),
			rx.hstack(
				rx.divider(margin="0"),
				rx.text("Or continue with", white_space="nowrap", weight="medium"),
				rx.divider(margin="0"),
				align="center",
				width="100%"
			),
			rx.center(
                rx.icon_button(
                    rx.icon(tag="github"),
                    variant="soft",
                    size="3"
                ),
                rx.icon_button(
                    rx.icon(tag="facebook"),
                    variant="soft",
                    size="3"
                ),
                rx.icon_button(
                    rx.icon(tag="twitter"),
                    variant="soft",
                    size="3"
                ),
                spacing="4",
                direction="row",
                width="100%"
            ),
			spacing="6",
			width="100%"
		),
		size="4",
		max_width="28em",
		width="100%"
	)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/recipes/auth/login_form.md`:

```md

# Login Form

The login form is a common component in web applications. It allows users to authenticate themselves and access their accounts. This recipe provides examples of login forms with different elements, such as third-party authentication providers.

## Default

```python demo exec toggle
def login_default() -> rx.Component:
	return rx.card(
		rx.vstack(
			rx.center(
				rx.image(src="/logo.jpg", width="2.5em", height="auto", border_radius="25%"),
				rx.heading("Sign in to your account", size="6", as_="h2", text_align="center", width="100%"),
				direction="column",
				spacing="5",
				width="100%"
			),
			rx.vstack(
				rx.text("Email address", size="3", weight="medium", text_align="left", width="100%"),
				rx.input(placeholder="user@reflex.dev", type="email", size="3", width="100%"),
				justify="start",
				spacing="2",
				width="100%"
			),
			rx.vstack(
				rx.hstack(
					rx.text("Password", size="3", weight="medium"),
					rx.link("Forgot password?", href="#", size="3"),
					justify="between",
					width="100%"
				),
				rx.input(placeholder="Enter your password", type="password", size="3", width="100%"),
				spacing="2",
				width="100%"
			),
			rx.button("Sign in", size="3", width="100%"),
			rx.center(
				rx.text("New here?", size="3"),
				rx.link("Sign up", href="#", size="3"),
				opacity="0.8",
				spacing="2",
				direction="row"
			),
			spacing="6",
			width="100%"
		),
		size="4",
		max_width="28em",
		width="100%"
	)
```

## Icons

```python demo exec toggle
def login_default_icons() -> rx.Component:
	return rx.card(
		rx.vstack(
			rx.center(
				rx.image(src="/logo.jpg", width="2.5em", height="auto", border_radius="25%"),
				rx.heading("Sign in to your account", size="6", as_="h2", text_align="center", width="100%"),
				direction="column",
				spacing="5",
				width="100%"
			),
			rx.vstack(
				rx.text("Email address", size="3", weight="medium", text_align="left", width="100%"),
				rx.input(rx.input.slot(rx.icon("user")), placeholder="user@reflex.dev", type="email", size="3", width="100%"),
				spacing="2",
				width="100%"
			),
			rx.vstack(
				rx.hstack(
					rx.text("Password", size="3", weight="medium"),
					rx.link("Forgot password?", href="#", size="3"),
					justify="between",
					width="100%"
				),
				rx.input(rx.input.slot(rx.icon("lock")), placeholder="Enter your password", type="password", size="3", width="100%"),
				spacing="2",
				width="100%"
			),
			rx.button("Sign in", size="3", width="100%"),
			rx.center(
				rx.text("New here?", size="3"),
				rx.link("Sign up", href="#", size="3"),
				opacity="0.8",
				spacing="2",
				direction="row",
				width="100%"
			),
			spacing="6",
			width="100%"
		),
		max_width="28em",
		size="4",
		width="100%"
	)
```

## Third-party auth

```python demo exec toggle
def login_single_thirdparty() -> rx.Component:
	return rx.card(
		rx.vstack(
			rx.flex(
				rx.image(src="/logo.jpg", width="2.5em", height="auto", border_radius="25%"),
				rx.heading("Sign in to your account", size="6", as_="h2", text_align="left", width="100%"),
				rx.hstack(
					rx.text("New here?", size="3", text_align="left"),
					rx.link("Sign up", href="#", size="3"),
					spacing="2",
					opacity="0.8",
					width="100%"
				),
				direction="column",
				justify="start",
				spacing="4",
				width="100%"
			),
			rx.vstack(
				rx.text("Email address", size="3", weight="medium", text_align="left", width="100%"),
				rx.input(rx.input.slot(rx.icon("user")), placeholder="user@reflex.dev", type="email", size="3", width="100%"),
				justify="start",
				spacing="2",
				width="100%"
			),
			rx.vstack(
				rx.hstack(
					rx.text("Password", size="3", weight="medium"),
					rx.link("Forgot password?", href="#", size="3"),
					justify="between",
					width="100%"
				),
				rx.input(rx.input.slot(rx.icon("lock")), placeholder="Enter your password", type="password", size="3", width="100%"),
				spacing="2",
				width="100%"
			),
			rx.button("Sign in", size="3", width="100%"),
			rx.hstack(
				rx.divider(margin="0"),
				rx.text("Or continue with", white_space="nowrap", weight="medium"),
				rx.divider(margin="0"),
				align="center",
				width="100%"
			),
			rx.button(
				rx.icon(tag="github"),
				"Sign in with Github",
				variant="outline",
				size="3",
				width="100%"
			),
			spacing="6",
			width="100%"
		),
		size="4",
		max_width="28em",
		width="100%"
	)
```

## Multiple third-party auth

```python demo exec toggle
def login_multiple_thirdparty() -> rx.Component:
	return rx.card(
		rx.vstack(
			rx.flex(
				rx.image(src="/logo.jpg", width="2.5em", height="auto", border_radius="25%"),
				rx.heading("Sign in to your account", size="6", as_="h2", width="100%"),
				rx.hstack(
					rx.text("New here?", size="3", text_align="left"),
					rx.link("Sign up", href="#", size="3"),
					spacing="2",
					opacity="0.8",
					width="100%"
				),
				justify="start",
				direction="column",
				spacing="4",
				width="100%"
			),
			rx.vstack(
				rx.text("Email address", size="3", weight="medium", text_align="left", width="100%"),
				rx.input(rx.input.slot(rx.icon("user")), placeholder="user@reflex.dev", type="email", size="3", width="100%"),
				spacing="2",
				justify="start",
				width="100%"
			),
			rx.vstack(
				rx.hstack(
					rx.text("Password", size="3", weight="medium"),
					rx.link("Forgot password?", href="#", size="3"),
					justify="between",
					width="100%"
				),
				rx.input(rx.input.slot(rx.icon("lock")), placeholder="Enter your password", type="password", size="3", width="100%"),
				spacing="2",
				width="100%"
			),
			rx.button("Sign in", size="3", width="100%"),
			rx.hstack(
				rx.divider(margin="0"),
				rx.text("Or continue with", white_space="nowrap", weight="medium"),
				rx.divider(margin="0"),
				align="center",
				width="100%"
			),
			rx.center(
                rx.icon_button(
                    rx.icon(tag="github"),
                    variant="soft",
                    size="3"
                ),
                rx.icon_button(
                    rx.icon(tag="facebook"),
                    variant="soft",
                    size="3"
                ),
                rx.icon_button(
                    rx.icon(tag="twitter"),
                    variant="soft",
                    size="3"
                ),
                spacing="4",
                direction="row",
                width="100%"
            ),
			spacing="6",
			width="100%"
		),
		size="4",
		max_width="28em",
		width="100%"
	)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/recipes/content/top_banner.md`:

```md

# Top Banner

Top banners are used to highlight important information or features at the top of a page. They are typically designed to grab the user's attention and can be used for announcements, navigation, or key messages.

## Basic

```python demo exec toggle
class TopBannerBasic(rx.ComponentState):
    hide: bool = False

    @rx.event
    def toggle(self):
        self.hide = not self.hide

    @classmethod
    def get_component(cls, **props):
        return rx.cond(
            ~cls.hide,
            rx.hstack(
                rx.flex(
                    rx.badge(
                        rx.icon("megaphone", size=18),
                        padding="0.30rem",
                        radius="full",
                    ),
                    rx.text(
                        "ReflexCon 2024 - ",
                        rx.link(
                            "Join us at the event!",
                            href="#",
                            underline="always",
                            display="inline",
                            underline_offset="2px",
                        ),
                        weight="medium",
                    ),
                    align="center",
                    margin="auto",
                    spacing="3",
                ),
                rx.icon(
                    "x",
                    cursor="pointer",
                    justify="end",
                    flex_shrink=0,
                    on_click=cls.toggle,
                ),
                wrap="nowrap",
                # position="fixed",
                justify="between",
                width="100%",
                # top="0",
                align="center",
                left="0",
                # z_index="50",
                padding="1rem",
                background=rx.color("accent", 4),
                **props,
            ),
            # Remove this in production
            rx.icon_button(
                rx.icon("eye"),
                cursor="pointer",
                on_click=cls.toggle,
            ),
        )

top_banner_basic = TopBannerBasic.create
```

## Sign up

```python demo exec toggle
class TopBannerSignup(rx.ComponentState):
    hide: bool = False

    @rx.event
    def toggle(self):
        self.hide = not self.hide

    @classmethod
    def get_component(cls, **props):
        return rx.cond(
            ~cls.hide,
                rx.flex(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.text(
                        "Web apps in pure Python. Deploy with a single command.",
                        weight="medium",
                    ),
                    rx.flex(
                        rx.button(
                            "Sign up",
                            cursor="pointer",
                            radius="large",
                        ),
                        rx.icon(
                            "x",
                            cursor="pointer",
                            justify="end",
                            flex_shrink=0,
                            on_click=cls.toggle,
                        ),
                        spacing="4",
                        align="center",
                    ),
                wrap="nowrap",
                # position="fixed",
                flex_direction=["column", "column", "row"],
                justify_content=["start", "space-between"],
                width="100%",
                # top="0",
                spacing="2",
                align_items=["start", "start", "center"],
                left="0",
                # z_index="50",
                padding="1rem",
                background=rx.color("accent", 4),
                **props,
            ),
            # Remove this in production
            rx.icon_button(
                rx.icon("eye"),
                cursor="pointer",
                on_click=cls.toggle,
            ),
        )

top_banner_signup = TopBannerSignup.create
```

## Gradient

```python demo exec toggle
class TopBannerGradient(rx.ComponentState):
    hide: bool = False

    @rx.event
    def toggle(self):
        self.hide = not self.hide

    @classmethod
    def get_component(cls, **props):
        return rx.cond(
            ~cls.hide,
                rx.flex(
                    rx.text(
                        "The new Reflex version is now available! ",
                        rx.link(
                            "Read the release notes",
                            href="#",
                            underline="always",
                            display="inline",
                            underline_offset="2px",
                        ),
                        align_items=["start", "center"],
                        margin="auto",
                        spacing="3",
                        weight="medium",
                    ),
                    rx.icon(
                        "x",
                        cursor="pointer",
                        justify="end",
                        flex_shrink=0,
                        on_click=cls.toggle,
                ),
                wrap="nowrap",
                # position="fixed",
                justify="between",
                width="100%",
                # top="0",
                align="center",
                left="0",
                # z_index="50",
                padding="1rem",
                background=f"linear-gradient(99deg, {rx.color('blue', 4)}, {rx.color('pink', 3)}, {rx.color('mauve', 3)})",
                **props,
            ),
            # Remove this in production
            rx.icon_button(
                rx.icon("eye"),
                cursor="pointer",
                on_click=cls.toggle,
            ),
        )

top_banner_gradient = TopBannerGradient.create
```

## Newsletter

```python demo exec toggle
class TopBannerNewsletter(rx.ComponentState):
    hide: bool = False

    @rx.event
    def toggle(self):
        self.hide = not self.hide

    @classmethod
    def get_component(cls, **props):
        return rx.cond(
            ~cls.hide,
            rx.flex(
                rx.text(
                    "Join our newsletter",
                    text_wrap="nowrap",
                    weight="medium",
                ),
                rx.input(
                    rx.input.slot(rx.icon("mail")),
                    rx.input.slot(
                        rx.icon_button(
                            rx.icon(
                                "arrow-right",
                                padding="0.15em",
                            ),
                            cursor="pointer",
                            radius="large",
                            size="2",
                            justify="end",
                        ),
                        padding_right="0",
                    ),
                    placeholder="Your email address",
                    type="email",
                    size="2",
                    radius="large",
                ),
                rx.icon(
                    "x",
                    cursor="pointer",
                    justify="end",
                    flex_shrink=0,
                    on_click=cls.toggle,
                ),
                wrap="nowrap",
                # position="fixed",
                flex_direction=["column", "row", "row"],
                justify_content=["start", "space-between"],
                width="100%",
                # top="0",
                spacing="2",
                align_items=["start", "center", "center"],
                left="0",
                # z_index="50",
                padding="1rem",
                background=rx.color("accent", 4),
                **props,
            ),
            # Remove this in production
            rx.icon_button(
                rx.icon("eye"),
                cursor="pointer",
                on_click=cls.toggle,
            ),
        )

top_banner_newsletter = TopBannerNewsletter.create
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/recipes/content/multi_column_row.md`:

```md

# Multi-column and row layout

A simple responsive multi-column and row layout. We specify the number of columns/rows to the `flex_direction` property as a list. The layout will automatically adjust the number of columns/rows based on the screen size.

For details, see the [responsive docs page]({styling.responsive.path}).

## Column

```python demo
rx.flex(
	rx.box(bg=rx.color("accent", 3), width="100%", height="100%"),
	rx.box(bg=rx.color("accent", 5), width="100%", height="100%"),
	rx.box(bg=rx.color("accent", 7), width="100%", height="100%"),
	bg=rx.color("accent", 10),
	spacing="4",
	padding="1em",
	flex_direction=["column", "column", "row"],
	height="600px",
	width="100%",
)
```

```python demo
rx.flex(
	rx.box(bg=rx.color("accent", 3), width="100%", height="100%"),
	rx.box(bg=rx.color("accent", 5), width=["100%", "100%", "50%"], height=["50%", "50%", "100%"]),
	rx.box(bg=rx.color("accent", 7), width="100%", height="100%"),
	rx.box(bg=rx.color("accent", 9), width=["100%", "100%", "50%"], height=["50%", "50%", "100%"]),
	bg=rx.color("accent", 10),
	spacing="4",
	padding="1em",
	flex_direction=["column", "column", "row"],
	height="600px",
	width="100%",
)
```

## Row

```python demo
rx.flex(
	rx.flex(
		rx.box(bg=rx.color("accent", 3), width=["100%", "100%", "50%"], height="100%"),
		rx.box(bg=rx.color("accent", 5), width=["100%", "100%", "50%"], height="100%"),
		width="100%",
		height="100%",
		spacing="4",
		flex_direction=["column", "column", "row"],
	),
	rx.box(bg=rx.color("accent", 7), width="100%", height="50%"),
	rx.box(bg=rx.color("accent", 9), width="100%", height="50%"),
	bg=rx.color("accent", 10),
	spacing="4",
	padding="1em",
	flex_direction="column",
	height="600px",
	width="100%",
)
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/recipes/content/grid.md`:

```md

# Grid

A simple responsive grid layout. We specify the number of columns to the `grid_template_columns` property as a list. The grid will automatically adjust the number of columns based on the screen size.

For details, see the [responsive docs page]({styling.responsive.path}).

## Cards

```python demo
rx.grid(
    rx.foreach(
        rx.Var.range(12),
        lambda i: rx.card(f"Card {i + 1}", height="10vh"),
    ),
	gap="1rem",
    grid_template_columns=["1fr", "repeat(2, 1fr)", "repeat(2, 1fr)", "repeat(3, 1fr)", "repeat(4, 1fr)"],
    width="100%"
)
```

## Inset cards

```python demo
rx.grid(
	rx.foreach(
		rx.Var.range(12),
		lambda i: rx.card(
			rx.inset(
				rx.image(
					src="/reflex_banner.png",
					width="100%",
					height="auto",
				),
				side="top",
				pb="current"
			),
			rx.text(
				f"Card {i + 1}",
			),
		),
	),
	gap="1rem",
	grid_template_columns=["1fr", "repeat(2, 1fr)", "repeat(2, 1fr)", "repeat(3, 1fr)", "repeat(4, 1fr)"],
	width="100%"
)
```

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/recipes/content/stats.md`:

```md

# Stats

Stats cards are used to display key metrics or data points. They are typically used in dashboards or admin panels.

## Variant 1

```python demo exec toggle
from reflex.components.radix.themes.base import LiteralAccentColor

def stats(stat_name: str = "Users", value: int = 4200, prev_value: int = 3000, icon: str = "users", badge_color: LiteralAccentColor = "blue") -> rx.Component:
	percentage_change = round(((value - prev_value) / prev_value) * 100, 2) if prev_value != 0 else 0 if value == 0 else float('inf')
	change = "increase" if value > prev_value else "decrease"
	arrow_icon = "trending-up" if value > prev_value else "trending-down"
	arrow_color = "grass" if value > prev_value else "tomato"
	return rx.card(
		rx.vstack(
			rx.hstack(
				rx.badge(
					rx.icon(tag=icon, size=34),
					color_scheme=badge_color,
					radius="full",
					padding="0.7rem"
				),
				rx.vstack(
					rx.heading(f"{value:,}", size="6", weight="bold"),
					rx.text(stat_name, size="4", weight="medium"),
					spacing="1",
					height="100%",
					align_items="start",
					width="100%"
				),
				height="100%",
				spacing="4",
				align="center",
				width="100%",
			),
			rx.hstack(
				rx.hstack(
					rx.icon(tag=arrow_icon, size=24, color=rx.color(arrow_color, 9)),
					rx.text(f"{percentage_change}%", size="3", color=rx.color(arrow_color, 9), weight="medium"),
					spacing="2",
					align="center",
				),
				rx.text(f"{change} from last month", size="2", color=rx.color("gray", 10)),
				align="center",
				width="100%",
			),
			spacing="3",
		),
		size="3",
		width="100%",
		max_width="21rem"
	)
```

## Variant 2

```python demo exec toggle
from reflex.components.radix.themes.base import LiteralAccentColor

def stats_2(stat_name: str = "Orders", value: int = 6500, prev_value: int = 12000, icon: str = "shopping-cart", icon_color: LiteralAccentColor = "pink") -> rx.Component:
	percentage_change = round(((value - prev_value) / prev_value) * 100, 2) if prev_value != 0 else 0 if value == 0 else float('inf')
	arrow_icon = "trending-up" if value > prev_value else "trending-down"
	arrow_color = "grass" if value > prev_value else "tomato"
	return rx.card(
		rx.hstack(
			rx.vstack(
				rx.hstack(
                    rx.hstack(
                        rx.icon(tag=icon, size=22, color=rx.color(icon_color, 11)),
                        rx.text(stat_name, size="4", weight="medium", color=rx.color("gray", 11)),
                        spacing="2",
                        align="center",
                    ),
                    rx.badge(
                        rx.icon(tag=arrow_icon, color=rx.color(arrow_color, 9)),
                        rx.text(f"{percentage_change}%", size="2", color=rx.color(arrow_color, 9), weight="medium"),
                        color_scheme=arrow_color,
                        radius="large",
                        align_items="center",
                    ),
                    justify="between",
                    width="100%",
                ),
				rx.hstack(
					rx.heading(f"{value:,}", size="7", weight="bold"),
					rx.text(f"from {prev_value:,}", size="3", color=rx.color("gray", 10)),
					spacing="2",
					align_items="end",
				),
				align_items="start",
				justify="between",
				width="100%",
			),
			align_items="start",
			width="100%",
			justify="between",
		),
		size="3",
		width="100%",
		max_width="21rem",
	)
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/recipes/content/forms.md`:

```md

## Forms

Forms are a common way to gather information from users. Below are some examples.

For more details, see the [form docs page]({library.forms.form.path}).

## Event creation

```python demo exec toggle
def form_field(label: str, placeholder: str, type: str, name: str) -> rx.Component:
	return rx.form.field(
		rx.flex(
			rx.form.label(label),
			rx.form.control(
				rx.input(
					placeholder=placeholder,
					type=type
				),
				as_child=True,
			),
			direction="column",
			spacing="1",
		),
		name=name,
		width="100%"
	)

def event_form() -> rx.Component:
	return rx.card(
		rx.flex(
			rx.hstack(
				rx.badge(
					rx.icon(tag="calendar-plus", size=32),
					color_scheme="mint",
					radius="full",
					padding="0.65rem"
				),
				rx.vstack(
					rx.heading("Create an event", size="4", weight="bold"),
					rx.text("Fill the form to create a custom event", size="2"),
					spacing="1",
					height="100%",
					align_items="start"
				),
				height="100%",
				spacing="4",
				align_items="center",
				width="100%",
			),
			rx.form.root(
				rx.flex(
					form_field("Event Name", "Event Name",
							   "text", "event_name"),
					rx.flex(
						form_field("Date", "", "date", "event_date"),
						form_field("Time", "", "time", "event_time"),
						spacing="3",
						flex_direction="row",
					),
					form_field("Description", "Optional", "text", "description"),
					direction="column",
					spacing="2",
				),
				rx.form.submit(
					rx.button("Create"),
					as_child=True,
					width="100%",
				),
				on_submit=lambda form_data: rx.window_alert(form_data.to_string()),
				reset_on_submit=False,
			),
			width="100%",
			direction="column",
			spacing="4",
		),
		size="3",
	)
```

## Contact

```python demo exec toggle
def form_field(label: str, placeholder: str, type: str, name: str) -> rx.Component:
	return rx.form.field(
		rx.flex(
			rx.form.label(label),
			rx.form.control(
				rx.input(
					placeholder=placeholder,
					type=type
				),
				as_child=True,
			),
			direction="column",
			spacing="1",
		),
		name=name,
		width="100%"
	)

def contact_form() -> rx.Component:
	return rx.card(
		rx.flex(
			rx.hstack(
				rx.badge(
					rx.icon(tag="mail-plus", size=32),
					color_scheme="blue",
					radius="full",
					padding="0.65rem"
				),
				rx.vstack(
					rx.heading("Send us a message", size="4", weight="bold"),
					rx.text("Fill the form to contact us", size="2"),
					spacing="1",
					height="100%",
				),
				height="100%",
				spacing="4",
				align_items="center",
				width="100%",
			),
			rx.form.root(
                rx.flex(
                    rx.flex(
                        form_field("First Name", "First Name",
                                   "text", "first_name"),
                        form_field("Last Name", "Last Name",
                                   "text", "last_name"),
                        spacing="3",
                        flex_direction=["column", "row", "row"],
                    ),
                    rx.flex(
                        form_field("Email", "user@reflex.dev",
                                   "email", "email"),
                        form_field("Phone", "Phone", "tel", "phone"),
                        spacing="3",
                        flex_direction=["column", "row", "row"],
                    ),
                    rx.flex(
                        rx.text("Message", style={
                            "font-size": "15px", "font-weight": "500", "line-height": "35px"}),
                        rx.text_area(
                            placeholder="Message",
                            name="message",
                            resize="vertical",
                        ),
                        direction="column",
                        spacing="1",
                    ),
                    rx.form.submit(
                        rx.button("Submit"),
                        as_child=True,
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                on_submit=lambda form_data: rx.window_alert(
                    form_data.to_string()),
                reset_on_submit=False,
            ),
			width="100%",
			direction="column",
			spacing="4",
		),
		size="3",
	)
```
```