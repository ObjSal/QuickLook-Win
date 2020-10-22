# Author: Salvador Guerrero
# Repository: https://github.com/ObjSal/QuickLook-Win
from fman import DirectoryPaneCommand
from fman.url import splitscheme, as_human_readable
import subprocess
import os

class quicklook(DirectoryPaneCommand):
	def __call__(self):
		chosen_files = self.get_chosen_files()
		if chosen_files:
			ql_path = os.getenv('LOCALAPPDATA') + "/Programs/QuickLook/QuickLook.exe"
			subprocess.run([ql_path, as_human_readable(chosen_files[0])])
			
