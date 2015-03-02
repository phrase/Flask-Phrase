# Flask-Phrase

This adapter lets you connect your [Flask](http://flask.pocoo.org/) application to [PhraseApp](https://phraseapp.com) and integrate the powerful [In-Context-Editor](http://demo.phraseapp.com/) into your apps.

## How does it work?

Flask-Phrase provides In-Context translating facilities to your Flask app by hooking into [Flask-Babel's](https://pythonhosted.org/Flask-Babel/) gettext function. It exposes the underlying key names to the JavaScript editor that is provided by PhraseApp.

To get started with PhraseApp you need to [sign up for a free account](https://phraseapp.com/signup).

## Install and Setup

Install the package with pip:

    pip install Flask-Phrase


Add the following to your Flask app configuration (app.config or config.py file)

    PHRASE_ENABLED = True
    PHRASE_PREFIX = '{{__'
    PHRASE_SUFFIX = '__}}'

Your app code should look something like this:

    from flask import Flask, [...]
    from flask.ext.babel import Babel
    from flask_phrase import Phrase, gettext, ngettext
    app = Flask(__name__)
    babel = Babel(app)
    phrase = Phrase(app)

Last step: add the PhraseApp JavaScript snippet to your base layout file with the folling tag. This should go inside the <head> section of your template file:

    <script>
      var phrase_auth_token = 'YOUR_PHRASEAPP_TOKEN';
      (function() {
        var phraseapp = document.createElement('script'); phraseapp.type = 'text/javascript'; phraseapp.async = true;
        phraseapp.src = ['https://', 'phraseapp.com/assets/phrase/0.1/app.js?', new Date().getTime()].join('');
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(phraseapp, s);
      })();
    </script>

## Usage

Set the PHRASE_ENABLED to True/False to enable or disable In-Context-Editing. When set to False, it will fall back to standard Flask-Babel's gettext functions. Disable PhraseApp for production environments at any time!

## Resources
* [Step-by-Step Guide on Flask-Babel and Flask-Phrase](http://localize-software.phraseapp.com/posts/python-localization-for-flask-applications/)
* [Flask-Phrase Demo Application](https://github.com/phrase/flask-demo-application).
* [Localization Guides and Software Translation Best Practices](http://localize-software.phraseapp.com/)
* [Contact PhraseApp Team](https://phraseapp.com/en/contact)

