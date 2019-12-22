# Template for CLIs Using PyInvoke

Use this as a template for creating CLIs using Python's Invoke framework.

>**NOTE**: This CLI template is brought to you by the lovely instructions provided [here](http://docs.pyinvoke.org/en/1.3/concepts/library.html).

## Getting Started

1. Change root package name `clitemplate` to the name of your choice

2. Update `name` in `config.yml`

3. Update app version in `_version.py` as needed

4. Add additional global constants to `definitions.py` as needed

5. In `main.py`, replace instances of `mycliname` with your own CLI name.

6. In `MANIFEST.in`, replace `clitemplate` in `recursive-include clitemplate *` with the root package name (i.e. the value from #1)

7. Update `requirements.txt` as needed

8. In `setup.py`:

    a) Replace all instances of `clitemplate` with the root package name (i.e. the value from #1)
    
    b) Replace all instances of `mycliname` with the value defined in #5

## Building the project

To build this project, simply use the [`dzbuild` util](https://github.com/d0-labs/d0-build-utils):

```bash
# Have to reload the shell in order to pick up the new CLI
cd <working_dir>
dzbuild python;source ~/.config/fish/config.fish
```


## Invoking the CLI

To use the `<mycliname>` CLI, check out some sample commands

```bash
<mycliname> --version
<mycliname> --list
<mycliname> test -g "What's up?"
```

## Running invoke tasks

Since the invoke tasks are all housed in the `clitemplate` package as part of a custom collection, `invoke` won't find the tasks through the usual `invoke --list` command.

Instead, you need to specify the name of the collection, which in our case is `clitemplate`, as per below:

```bash
invoke --collection=clitemplate --list
```