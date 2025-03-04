Project Path: custom-components

Source Tree:

```
custom-components
├── prerequisites-for-publishing.md
├── command-reference.md
└── overview.md

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/custom-components/prerequisites-for-publishing.md`:

```md
# Python Package Index


In order to publish a Python package, an account with the package index is required. As of **0.4.3**, Reflex only supports publishing to PyPI and TestPyPI. PyPI is short for **Python Package Index**, the official third-party software repository for Python. TestPyPI is a separate instance of index that allows users to test the distribution and installation of the package before publishing it to the real index.

## PyPI

It is straightforward to create accounts and API tokens with PyPI. There is official help on the [PyPI website](https://pypi.org/help/). For a quick reference here, go to the top right corner of the PyPI website and look for the button to register and fill out personal information.

```python eval
rx.center(
  rx.image(src="/custom_components/pypi_register.png", style=image_style, margin_bottom="16px", loading="lazy"),
)
```

A user can use username and password to authenticate with PyPI when publishing. Reflex does not store your PyPI credentials. If an API token is preferred, it can be generated in the account settings.

```python eval
rx.center(
  rx.image(src="/custom_components/pypi_account_settings.png", style=image_style, margin_bottom="16px", loading="lazy"),
)
```

Scroll down to the API tokens section and click on the "Add API token" button. Fill out the form and click "Generate API token".

```python eval
rx.center(
  rx.image(src="/custom_components/pypi_api_tokens.png", style=image_style, width="700px", loading="lazy"),
)
```

## TestPyPI

TestPyPI has the same look and feel as PyPI.

```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/custom-components/command-reference.md`:

```md
# Command Reference


The custom component commands are under `reflex component` subcommand. To see the list of available commands, run `reflex component --help`. To see the manual on a specific command, run `reflex component <command> --help`, for example, `reflex component init --help`.

```python eval
doccmdoutput(
    command="reflex component --help",
    output="""Usage: reflex component [OPTIONS] COMMAND [ARGS]...

  Subcommands for creating and publishing Custom Components.

Options:
  --help  Show this message and exit.

Commands:
  build    Build a custom component.
  init     Initialize a custom component.
  publish  Publish a custom component.
""")
```

## reflex component init

Below is an example of running the `init` command.

```python eval
doccmdoutput(
    command="reflex component init",
    output="""reflex component init
─────────────────────────────────────── Initializing reflex-google-auth project ───────────────────────────────────────
Info: Populating pyproject.toml with package name: reflex-google-auth
Info: Initializing the component directory: custom_components/reflex_google_auth
Info: Creating app for testing: google_auth_demo
──────────────────────────────────────────── Initializing google_auth_demo ────────────────────────────────────────────
[07:58:16] Initializing the app directory.                                                                console.py:85
           Initializing the web directory.                                                                console.py:85
Success: Initialized google_auth_demo
─────────────────────────────────── Installing reflex-google-auth in editable mode. ───────────────────────────────────
Info: Package reflex-google-auth installed!
Custom component initialized successfully!
─────────────────────────────────────────────────── Project Summary ───────────────────────────────────────────────────
[ README.md ]: Package description. Please add usage examples.
[ pyproject.toml ]: Project configuration file. Please fill in details such as your name, email, homepage URL.
[ custom_components/ ]: Custom component code template. Start by editing it with your component implementation.
[ google_auth_demo/ ]: Demo App. Add more code to this app and test.
""",
)
```

The `init` command uses the current enclosing folder name to construct a python package name, typically in the kebab case. For example, if running init in folder `google_auth`, the package name will be `reflex-google-auth`. The added prefix reduces the chance of name collision on PyPI (the Python Package Index), and it indicates that the package is a Reflex custom component. The user can override the package name by providing the `--package-name` option.

The `init` command creates a set of files and folders prefilled with the package name and other details. During the init, the `custom_component` folder is installed locally in editable mode, so a developer can incrementally develop and test with ease. The changes in component implementation is automatically reflected where it is used. Below is the folder structure after the `init` command.

```python eval
rx._x.code_block("""
google_auth/
├── pyproject.toml
├── README.md
├── custom_components/
│   └── reflex_google_auth/
│       ├── google_auth.py
│       └── __init__.py
└── google_auth_demo/
    └── assets/
        google_auth_demo/
        requirements.txt
        rxconfig.py
""",
  language="bash",
  style={
    "border-radius": "12px",
    "border": "1px solid var(--c-slate-4)",
    "background": "var(--c-slate-2)",
    "color": "var(--c-slate-12)",
    "font-family": "Source Code Pro",
    **code
  }
)
```

### pyproject.toml

The `pyproject.toml` is required for the package to build and be published. It is prefilled with information such as the package name, version (`0.0.1`), author name and email, homepage URL. By default the **Apache-2.0** license is used, the same as Reflex. If any of this information requires update, the user can edit the file by hand.

### README

The `README.md` file is created with installation instructions, e.g. `pip install reflex-google-auth`, and a brief description of the package. Typically the `README.md` contains usage examples. On PyPI, the `README.md` is rendered as part of the package page.

### Custom Components Folder

The `custom_components` folder is where the actual implementation is. Do not worry about this folder name: there is no need to change it. It is where `pyproject.toml` specifies the source of the python package is. The published package contains the contents inside it, excluding this folder.

`reflex_google_auth` is the top folder for importable code. The `reflex_google_auth/__init__.py` imports everything from the `reflex_google_auth/google_auth.py`. For the user of the package, the import looks like `from reflex_google_auth import ABC, XYZ`.

`reflex_google_auth/google_auth.py` is prefilled with code example and instructions from the [wrapping react guide]({wrapping_react.overview.path}).

### Demo App Folder

A demo app is generated inside `google_auth_demo` folder with import statements and example usage of the component. This is a regular Reflex app. Go into this directory and start using any reflex commands for testing. The user is encouraged to deploy the demo app, so it can later be included as part of the [Gallery]({gallery.path}).

### Help Manual

The help manual is shown when adding the `--help` option to the command.

```python eval
doccmdoutput(
    command="reflex component init --help",
    output="""Usage: reflex component init [OPTIONS]

  Initialize a custom component.

  Args:     library_name: The name of the library.     install: Whether to
  install package from this local custom component in editable mode.
  loglevel: The log level to use.

  Raises:     Exit: If the pyproject.toml already exists.

Options:
  --library-name TEXT             The name of your library. On PyPI, package
                                  will be published as `reflex-{library-
                                  name}`.
  --install / --no-install        Whether to install package from this local
                                  custom component in editable mode.
                                  [default: install]
  --loglevel [debug|info|warning|error|critical]
                                  The log level to use.  [default:
                                  LogLevel.INFO]
  --help                          Show this message and exit.
""")
```

## reflex component publish

To publish to a package index, a user is required to already have an account with them. As of **0.4.3**, Reflex only supports uploading to PyPI and TestPyPI. Those indices are separate PyPI and TestPyPI should have sufficient documentation on the account creation and how to generate API tokens. We also have a [short guide]({custom_components.overview.path}) covering this topic.

The publish process starts with a build if needed. If the distribution files for the version specified in pyproject.toml file already exist, the command prompts the user to confirm rebuilding the files nor not. After making sure the distribution files are ready, the command proceeds to upload them to the specified python package index.

```python eval
doccmdoutput(
    command="reflex component publish --help",
    output="""
reflex component publish --help
Usage: reflex component publish [OPTIONS]

  Publish a custom component. Must be run from the project root directory
  where the pyproject.toml is.

  Args:     repository: The name of the Python package repository, such pypi,
  testpypi.     token: The token to use for authentication on python package
  repository. If token is provided, no username/password should be provided at
  the same time.     username: The username to use for authentication on
  python package repository.     password: The password to use for
  authentication on python package repository.     loglevel: The log level to
  use.

  Raises:     Exit: If arguments provided are not correct or the publish
  fails.

Options:
  -r, --repository TEXT           The name of the repository. Defaults to
                                  pypi. Only supports pypi and testpypi (Test
                                  PyPI) for now.
  -t, --token TEXT                The API token to use for authentication on
                                  python package repository. If token is
                                  provided, no username/password should be
                                  provided at the same time
  -u, --username TEXT             The username to use for authentication on
                                  python package repository. Username and
                                  password must both be provided.
  -p, --password TEXT             The password to use for authentication on
                                  python package repository. Username and
                                  password must both be provided.
  --build / --no-build            Whether to build the package before
                                  publishing. If the package is already built,
                                  set this to False.  [default: build]
  --loglevel [debug|info|warning|error|critical]
                                  The log level to use.  [default:
                                  LogLevel.INFO]
  --help                          Show this message and exit.
""")
```

## reflex component build

It is not required to run the `build` command separately before publishing. The `publish` command will build the package if it is not already built. The `build` command is provided for the user's convenience.

The `build` command generates the `.tar.gz` and `.whl` distribution files to be uploaded to the desired package index, for example, PyPI. This command must be run at the top level of the project where the `pyproject.toml` file is. As a result of a successful build, there is a new `dist` folder with the distribution files.

```python eval
doccmdoutput(
    command="reflex component build --help",
    output="""reflex component build --help
Usage: reflex component build [OPTIONS]

  Build a custom component. Must be run from the project root directory where
  the pyproject.toml is.

  Args:     loglevel: The log level to use.

  Raises:     Exit: If the build fails.

Options:
  --loglevel [debug|info|warning|error|critical]
                                  The log level to use.  [default:
                                  LogLevel.INFO]
  --help                          Show this message and exit.
""")
```
```

`/home/cb/projects/github/ThirdBrAIn-REFLEX-IQ/reflex-web/docs/custom-components/overview.md`:

```md
# Custom Components Overview


Reflex users create many components of their own: ready to use high level components, or nicely wrapped React components. With **Custom Components**, the community can easily share these components now.

Release **0.4.3** introduces a series of `reflex component` commands that help developers wrap react components, test, and publish them as python packages. As shown in the image below, there are already a few custom components published on PyPI, such as `reflex-spline`, `reflex-webcam`. 

Check out the custom components gallery [here]({custom_components_gallery.path}).


```python eval
rx.center(
  rx.image(src="/custom_components/pypi_reflex_custom_components.png", width="400px", border_radius="15px", border="1px solid"),
)
```

## Prerequisites for Publishing

In order to publish a Python package, an account is required with a python package index, for example, PyPI. The documentation to create accounts and generate API tokens can be found on their websites. For a quick reference, check out our [Prerequisites for Publishing]({custom_components.prerequisites_for_publishing.path}) page.

## Steps to Publishing

Follow these steps to publish the custom component as a python package:

1. `reflex component init`: creates a new custom component project from templates.
2. dev and test: developer implements and tests the custom component.
3. `reflex component publish`: builds and uploads the package to a python package index.

### Initialization

```bash
reflex component init
```

First create a new folder for your custom component project, for example `color_picker`. The package name will be `reflex-color-picker`. The prefix `reflex-` is intentionally added for all custom components for easy search on PyPI. If you prefer a particular name for the package, you can either change it manually in the `pyproject.toml` file or add the `--library-name` option in the `reflex component init` command initially.

Run `reflex component init`, and a set of files and folders will be created in the `color_picker` folder. The `pyproject.toml` file is the configuration file for the project. The `custom_components` folder is where the custom component implementation is. The `color_picker_demo` folder is a demo Reflex app that uses the custom component. If this is the first time of creating python packages, it is encouraged to browse through all the files (there are not that many) to understand the structure of the project.

```bash
color_picker/
├── pyproject.toml            <- Configuration file
├── README.md
├── .gitignore                <- Exclude dist/ and metadata folders
├── custom_components/
│   └── reflex_color_picker/  <- Custom component source directory
│       ├── color_picker.py
│       └── __init__.py
└── color_picker_demo/        <- Demo Reflex app directory
    └── assets/
        color_picker_demo/
        requirements.txt
        rxconfig.py
```

### Develop and Test

After finishing the custom component implementation, the user is encouraged to fully test it before publishing. The generated Reflex demo app `color_picker_demo` is a good place to start. It is a regular Reflex app prefilled with imports and usage of this component. During the init, the `custom_component` folder is installed locally in editable mode, so a developer can incrementally develop and test with ease. The changes in component implementation are automatically reflected in the demo app.

### Publish

```bash
reflex component publish
```

Once ready to publish, execute `reflex component publish` with the credentials in the command options (either `--username` and `--password` together or `--token`). First the command builds the distribution files if they are not already built. The end result is a `dist` folder containing the distribution files. The user does not need to do anything manually with these distribution files. The the command proceeds to publish those files. The same version of the package can only be published once. If already exists, the publish ends in error. The user can go to the `pyproject.toml` file and update the version number as desired. After the `publish` command finishes successfully, the package is uploaded to PyPI. 🎉

```