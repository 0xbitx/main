from main.config.module_info import ModuleInfo
from main.softwares.browsers.mozilla import Mozilla


class Thunderbird(Mozilla):

    def __init__(self):
        self.path = '.thunderbird'
        ModuleInfo.__init__(self, 'Thunderbird', 'mails')
