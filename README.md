# Template for CLIs Using PyInvoke

Use this as a template for creating CLIs using Python's Invoke framework.

>**NOTE**: This CLI template is brought to you by the lovely instructions provided [here](http://docs.pyinvoke.org/en/1.3/concepts/library.html).

## Pre-Requisites

This project uses [Python Poetry](https://python-poetry.org/docs/) for building and packaging the CLI.

1. Install poetry (OSX Install):

    ```bash
    brew install poetry
    poetry --version
    ```

2. Set up your virtual environment:

    More info [here](https://www.infoworld.com/article/3527850/how-to-manage-python-projects-with-poetry.html)

    ```bash
    pip3 install --pre poetry -U # do it once - get the preview version of poetry (https://github.com/python-poetry/poetry/issues/2711#issuecomment-663979034)
    poetry env use python3

    # The above command creates a poetry-managed virtual env here
    ~/Library/Caches/pypoetry/virtualenvs/d0cpyli-<some_identifier>-py3.8/bin
    ```

3. Set up poetry:

    ```bash
    # Interactive mode - will initialize poetry on an existing project
    poetry init

    # Set up the virtual env
    poetry env use python3
    poetry env list # shows your virtual envs associated with this project
    poetry env info --path # shows current poetry env info

    # Add dependencies to pyproject.toml
    poetry add invoke
    poetry add fastapi = "0.46.0"
    poetry add "pulumi-random>=2.0.0,<3.0.0"

    # Add dev dependencies to pyproject.toml
    poetry add -D pytest

    # Installs the python packages in pyproject.toml + itself
    poetry build
    poetry install
    ```


## Getting Started

1. Change root package name `clitemplate` to the name of your choice

2. Update `name` in `config.yml`

3. Add additional global constants to `definitions.py` as needed

4. In `main.py`, replace instances of `mycli` with your own CLI name.

5. Update `pyproject.toml` as needed

6. In `pyproject.toml`:

    a) Replace all instances of `clitemplate` with the root package name (i.e. the value from #1)
    
    b) Replace all instances of `mycli` with the value defined in #5

## Building the project

To build this project, simply use the [`dzbuild` util](https://github.com/d0-labs/d0-build-utils):

```bash
# Have to reload the shell in order to pick up the new CLI
cd <working_dir>
dzbuild python;source ~/.config/fish/config.fish
```


## Invoking the CLI

To use the `<mycli>` CLI, check out some sample commands

```bash
<mycli> --version
<mycli> --list
<mycli> test -g "What's up?"
```

## Running invoke tasks

Since the invoke tasks are all housed in the `clitemplate` package as part of a custom collection, `invoke` won't find the tasks through the usual `invoke --list` command.

Instead, you need to specify the name of the collection, which in our case is `clitemplate`, as per below:

```bash
invoke --collection=clitemplate --list
```

