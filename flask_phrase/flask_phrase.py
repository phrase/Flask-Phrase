from __future__ import print_function
try:
    from flask.ext.babel import gettext as gettext_original, ngettext as ngettext_original
    from flask import current_app
except ImportError:
    print("Flask-Babel is required.")

def phrase_enabled():
    return current_app.config['PHRASE_ENABLED']

def phrase_jinja(): 
    current_app.jinja_env.install_gettext_callables(
        gettext,
        ngettext,
        ewstyle=True
    )

def phrase_key(msgid):
    return current_app.config['PHRASE_PREFIX'] + 'phrase_' + msgid + current_app.config['PHRASE_SUFFIX']

def gettext(msgid):
    phrase_jinja()
    if phrase_enabled():
        return phrase_key(msgid)
    else:
        return gettext_original(msgid)

def ngettext(msgid):
    phrase_jinja()
    if phrase_enabled():
        return phrase_key(msgid)
    else:
        return ngettext_original(msgid)
