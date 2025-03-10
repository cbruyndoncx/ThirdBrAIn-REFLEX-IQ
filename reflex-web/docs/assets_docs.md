Project Path: assets

Source Tree:

```
assets
├── overview.md
└── upload_and_download_files.md

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/assets/overview.md`:

```md

# Assets

Static files such as images and stylesheets can be placed in `assets/` folder of the project. These files can be referenced within your app.

```md alert
# Assets are copied during the build process.

Any files placed within the `assets/` folder at runtime will not be available to the app
when running in production mode. The `assets/` folder should only be used for static files.
```

## Referencing Assets

To reference an image in the `assets/` simply pass the relative path as a prop.

For example, you can store your logo in your assets folder:

```bash
assets
└── Reflex.svg
```

Then you can display it using a `rx.image` component:

```python demo
rx.image(src="/Reflex.svg", width="5em")
```

```md alert
# Always prefix the asset path with a forward slash `/` to reference the asset from the root of the project, or it may not display correctly on non-root pages.
```

## Favicon

The favicon is the small icon that appears in the browser tab.

You can add a `favicon.ico` file to the `assets/` folder to change the favicon.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/assets/upload_and_download_files.md`:

```md

# Files

In addition to any assets you ship with your app, many web app will often need to receive or send files, whether you want to share media, allow user to import their data, or export some backend data.

In this section, we will cover all you need to know for manipulating files in Reflex.

## Download

If you want to let the users of your app download files from your server to their computer, Reflex offer you two way.

### With a regular link

For some basic usage, simply providing the path to your resource in a `rx.link` will work, and clicking the link will download or display the resource.

```python demo
rx.link("Download", href="/reflex_banner.png")
```

### With `rx.download` event

Using the `rx.download` event will always prompt the browser to download the file, even if it could be displayed in the browser.

The `rx.download` event also allows the download to be triggered from another backend event handler.

```python demo
rx.button(
    "Download",
    on_click=rx.download(url="/reflex_banner.png"),
)
```

`rx.download` lets you specify a name for the file that will be downloaded, if you want it to be different from the name on the server side.

```python demo
rx.button(
    "Download and Rename",
    on_click=rx.download(
        url="/reflex_banner.png",
        filename="different_name_logo.png"
    ),
)
```

If the data to download is not already available at a known URL, pass the `data` directly to the `rx.download` event from the backend.

```python demo exec
import random

class DownloadState(rx.State):
    @rx.event
    def download_random_data(self):
        return rx.download(
            data=",".join([str(random.randint(0, 100)) for _ in range(10)]),
            filename="random_numbers.csv"
        )

def download_random_data_button():
    return rx.button(
        "Download random numbers",
        on_click=DownloadState.download_random_data
    )
```

The `data` arg accepts `str` or `bytes` data, a `data:` URI, `PIL.Image`, or any state Var. If the Var is not already a string, it will be converted to a string using `JSON.stringify`. This allows complex state structures to be offered as JSON downloads.

Reference page for `rx.download` [here]({api_reference.special_events.path}#rx.download).

## Upload

Uploading files to your server let your users interact with your app in a different way than just filling forms to provide data.

The component `rx.upload` let your users upload files on the server.

Here is a basic example of how it is used:

```python
def index():
    return rx.fragment(
        rx.upload(rx.text("Upload files"), rx.icon(tag="upload")),
        rx.button(on_submit=State.<your_upload_handler>)
    )
```

For detailed information, see the reference page of the component [here]({library.forms.upload.path}).

```