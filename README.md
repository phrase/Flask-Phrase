# Flask-Phrase

This adapter lets you connect your [Flask](http://flask.pocoo.org/) application to [Phrase](https://phrase.com) and integrate the powerful [In-Context-Editor](http://demo.phrase.com/) into your apps.

## How does it work?

Flask-Phrase provides In-Context translating facilities to your Flask app by hooking into [Flask-Babel's](https://pythonhosted.org/Flask-Babel/) gettext function. It exposes the underlying key names to the JavaScript editor that is provided by Phrase.

To get started with Phrase you need to [sign up for a free account](https://phrase.com/signup).

## Install and Setup

Install the package with pip:

    pip install Flask-Phrase


Add the following to your Flask app configuration (app.config or config.py file)

    PHRASEAPP_ENABLED = True
    PHRASEAPP_PREFIX = '{{__'
    PHRASEAPP_SUFFIX = '__}}'

Your app code should look something like this:

    from flask import Flask, [...]
    from flask.ext.babel import Babel
    from flask_phrase import Phrase, gettext, ngettext
    app = Flask(__name__)
    babel = Babel(app)
    phrase = Phrase(app)

Last step: add the Phrase JavaScript snippet to your base layout file with the folling tag. This should go inside the <head> section of your template file:

    <script>
    window.PHRASEAPP_CONFIG = {
        projectId: "YOUR-PROJECT-ID"
    };
    (function() {
        var phraseapp = document.createElement('script'); phraseapp.type = 'text/javascript'; phraseapp.async = true;
        phraseapp.src = ['https://', 'phraseapp.com/assets/in-context-editor/2.0/app.js?', new Date().getTime()].join('');
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(phraseapp, s);
    })();
    </script>

You can find your Project-ID in the Phrase Translation Center.

## Usage

Set the PHRASEAPP_ENABLED to True/False to enable or disable In-Context-Editing. When set to False, it will fall back to standard Flask-Babel's gettext functions. Disable Phrase for production environments at any time!

## Resources
* [Step-by-Step Guide on Flask-Babel and Flask-Phrase](http://localize-software.phrase.com/posts/python-localization-for-flask-applications/)
* [Flask-Phrase Demo Application](https://github.com/phrase/flask-demo-application).
* [Localization Guides and Software Translation Best Practices](http://localize-software.phrase.com/)
* [Contact Phrase Team](https://phrase.com/en/contact)
