# Application Notes

## Pre-commit hooks

Added `pre-commit` to `requirements.txt` so run `pip3 install -r requirements.txt` to install before continuing below.

The run this on the command-line to install the pre-commit hooks:

```bash
pre-commit install
```

Pre-commit docs [here](https://pre-commit.com/#install)

This will now run git pre-commit hooks.

To run pre-commit hooks at any time:

```bash
pre-commit run --all-files
```
