###
# Copyright (c) 2012, spline
# All rights reserved.
#
#
###

import supybot.conf as conf
import supybot.registry as registry
from supybot.i18n import PluginInternationalization, internationalizeDocstring

_ = PluginInternationalization('Weather')

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Weather', True)


Weather = conf.registerPlugin('Weather')
conf.registerGlobalValue(Weather,'apiKey', registry.String('', ("""Your wunderground.com API key."""), private=True))
conf.registerGlobalValue(Weather,'maxOutput', registry.Integer(4, ("""How many lines by default to output.""")))
conf.registerChannelValue(Weather,'useImperial', registry.Boolean(True, ("""Use imperial units? Defaults to yes.""")))
conf.registerChannelValue(Weather,'disableANSI', registry.Boolean(False, """Do not display any ANSI (color/bold) for channel."""))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=250: