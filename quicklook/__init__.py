# Author: Salvador Guerrero
# Repository: https://github.com/ObjSal/QuickLook-Win
from fman import DirectoryPaneCommand
from fman.url import splitscheme, as_human_readable
import subprocess

class quicklook(DirectoryPaneCommand):
	def __call__(self):
		chosen_files = self.get_chosen_files()
		if chosen_files:
			subprocess.run(["C:/Users/salva/AppData/Local/Programs/QuickLook/QuickLook.exe", as_human_readable(chosen_files[0])])
			
