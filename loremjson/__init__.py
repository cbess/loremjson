from flask import Flask
import settings

app = Flask('loremjson')
app.config.from_object('loremjson.settings')

import views