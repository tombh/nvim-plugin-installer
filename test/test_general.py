import time

from neovim import attach

from plugin.nvim_plugin_installer import Main

# You must start an nvim session with:
# `NVIM_LISTEN_ADDRESS=/tmp/nvim` for this to work.
nvim = attach('socket', path='/tmp/nvim')
# Needed to refresh any functions and/or arg definitions.
nvim.command('UpdateRemotePlugins')

# TODO: Don't make external HTTP requests in a test. use something like VCR
def test_api_query():
    plugin = Main(nvim)
    result = plugin.apiQuery('neoma')
    assert result['name'] == 'neomake'
    assert result['short_desc'] == 'Asynchronous linting and make framework for Neovim/Vim'
    assert result['github_url'] == 'https://github.com/neomake/neomake'
    assert result['github_stars'] > 1400

# TODO: Requires manually running *and restarting* a NVIM_LISTEN session :/
def test_buffer_write():
    nvim.command("exec PluginSearch('deopl')")
    # Ensure HTTP request is complete
    # TODO: wait for a specific event rather than the overkill of 5 seconds
    time.sleep(5)
    first_line = nvim.current.buffer[0]
    assert 'deoplete.nvim' in first_line
