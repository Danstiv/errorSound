import addonHandler
import config
import logHandler
import ui
import tones
from globalPluginHandler import GlobalPlugin
from scriptHandler import script

_t = _
addonHandler.initTranslation()

CONFIG_SPEC = {
    'play_error_sound': 'boolean(default=True)',
}

FUNCTIONS = {
    False: lambda *args, **kwargs: False,
    True: lambda *args, **kwargs: True,
}


class GlobalPlugin(GlobalPlugin):
    scriptCategory = 'Error Sound'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        config.conf.spec['error_sound'] = CONFIG_SPEC
        self.config = config.conf['error_sound']
        logHandler.shouldPlayErrorSound = FUNCTIONS[self.config['play_error_sound']]

    @script(
        description=_('Turn'),
        gesture='kb:nvda+control+e',
    )
    def script_turn(self, gesture):
        self.config['play_error_sound'] = not self.config['play_error_sound']
        logHandler.shouldPlayErrorSound = FUNCTIONS[self.config['play_error_sound']]
        if self.config['play_error_sound']:
            ui.message(_t('on'))
        else:
            ui.message(_t('off'))

    @script(
        description=_('Raise exception'),
        gesture='kb:nvda+alt+control+e',
    )
    def script_raise_exception(self, gesture):
        tones.beep(100, 100)
        raise NotImplementedError
