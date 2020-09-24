# Google Colab Hookup

To make a notebook available in google colab, add this to the notebook:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)

``markdown
    [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)
``
# Vim Bindings

**Please note that all keys are lowercase unless `Shift` is explicitly indicated.**
For example, `Y, Y` is two lowercase `y`s, `Shift-Y, Y` is one uppercase `Y` followed by a lowercase `y`.

Shortcuts this extension introduces:

## Vim Ex commands

| Command  | Action                     |
| -------  | ------                     |
| :w[rite] | Save Notebook              |
| :q[uit]  | Enter Jupyter command mode |

## Vim command bindings

| Chord          | Action                    |
| -----          | -------                   |
| Ctrl-O, U      | Undo Cell Action          |
| -              | Split Cell at Cursor      |
| Ctrl-O, -      | Split Cell at Cursor      |
| Ctrl-O, D      | Cut Cell                  |
| Ctrl-O, Y      | Copy Cell                 |
| Ctrl-O, P      | Paste Cell                |
| Ctrl-Shift-J   | Extend Marked Cells Below |
| Ctrl-Shift-K   | Extend Marked Cells Above |
| Ctrl-O, O      | Insert Cell Below         |
| Ctrl-O, Ctrl-O | Insert Cell Above         |
| Ctrl-J         | Select Cell Below         |
| Ctrl-K         | Select Cell Above         |
| Ctrl-O, G      | Select First Cell         |
| Ctrl-O, Ctrl-G | Select Last Cell          |
| Ctrl-E         | Move Cell Down            |
| Ctrl-Y         | Move Cell Up              |
| Ctrl-O, Z, Z   | Center Cell               |
| Ctrl-G         | Show Tooltip              |
| Command/Ctrl-1 | Code Cell Mode            |
| Command/Ctrl-2 | Markdown Cell Mode        |
| Command/Ctrl-3 | Raw Cell Mode             |
| Shift-Escape   | Leave Vim Mode            |

## Jupyter command bindings

| Chord   | Action            |
| -----   | ------            |
| G, G    | Select First Cell |
| Shift-G | Select Last Cell  |
| D, D    | Delete Cell       |
| Y, Y    | Yank (Copy) Cell  |
| P       | Paste Cell        |
| Shift-P | Paste Cell Above  |
| O       | Insert Cell       |
| Shift-O | Insert Cell Above |
| U       | Undo Cell Action  |
| Ctrl-E  | Move Cells Down   |
| Ctrl-Y  | Move Cells Up     |
| Z, Z    | Center Cell       |
