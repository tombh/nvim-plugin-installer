# Neovim Plugin Installer

Search and install plugins from inside your editor.

_NB: WIP_

## Installation

`git clone` somewhere and then add that path to your current plugin manager. Eg, for vim-plug;

`Plug 'path/to/git/clone/of/this/repo'`

Then inside neovim run `:UpdateRemotePlugins`

## Usage

Run `:PluginSearch('cool plugin')`

## Development

```bash
pip install -r requirements-dev.txt
pytest
```
