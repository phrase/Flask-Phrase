from flask import Flask, render_template
from flask_phrase import gettext, ngettext, lazy_gettext
from flask_babel import Babel

app = Flask(__name__)
app.config['PHRASEAPP_ENABLED'] = True # Also adjust `phraseEnabled` in demo/templates/index.html if you change this
app.config['PHRASEAPP_PREFIX'] = "{{__"
app.config['PHRASEAPP_SUFFIX'] = "__}}"
babel = Babel(app)

@app.route("/")
def hello_world():
    hero_title = gettext(u'hero_title')
    advantages_text = gettext(u'advantages_text')
    integrate_title = gettext(u'integrate_title')
    create_this_key = gettext(u'create_this_key')
    integrate_text = gettext(u'integrate_text')

    variable_key = gettext(u'variable_key', value=42)
    ngettext_variable_key = ngettext(u'ngettext_variable_key', 'ngettext_variable_key_plural', 3)
    success_message = lazy_gettext(u'success_message')

    return render_template(
        'index.html',
        hero_title=hero_title,
        advantages_text=advantages_text,
        integrate_title=integrate_title,
        create_this_key=create_this_key,
        integrate_text=integrate_text,
        variable_key=variable_key,
        ngettext_variable_key=ngettext_variable_key,
        success_message=success_message
    )
