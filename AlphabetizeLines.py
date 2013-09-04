import sublime, sublime_plugin

class AlphabetizeLinesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for sel in self.view.sel():
			self.view.replace(edit, sel, '\n'.join(sorted(self.view.substr(sel).split('\n'))))