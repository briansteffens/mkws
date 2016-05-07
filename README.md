# mkws

Quickly generate throwaway tmux development environments for quick tests,
calculations, etc.

This is for when you want to quickly test a line of c code or something and
want to type one command to make a directory, a basic source code file, open
that in a tmux session, and compile/run the program.

## Installation

To install manually:

```bash
git clone https://github.com/briansteffens/mkws
cd mkws
sudo make install
```

Or, if using Arch, you can get it from the
[AUR](https://aur.archlinux.org/packages/mkws/).

## Usage

Start a c workspace in a generated directory name (`c`, `c_2`, `c_3`, etc):

```bash
mkws init c
```

Start a python3 workspace in a specific directory:

```bash
mkws init python3 my_ws
```

Reopen a previous workspace (from the workspace directory):

```bash
mkws open
```

## Templates

Available templates are located in [mkws/templates/](mkws/templates/).
