import urllib.request
import json
import neovim

API_BASE = 'http://vimawesome.com/api/plugins?query='

@neovim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.function('PluginSearch')
    def pluginSearch(self, args):
        result = self.apiQuery(args[0])
        formatted = '%s(%s): %s' % (
            result['name'],
            result['github_stars'],
            result['short_desc']
        )
        # Open new buffer split
        self.vim.command('new')
        # Write to new buffer
        self.vim.current.buffer[0] = formatted

    def apiQuery(self, query):
        result = urllib.request.urlopen('%s%s' % (API_BASE, query))
        payload = json.loads(result.read())
        first = payload['plugins'][0]
        return first

