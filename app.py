from flask import Flask
from flask_restplus import Api
from views.controller_wordvector import ns_text_tools
from views.controller_lifecycle import ns_lifecycle

app = Flask(__name__)

api = Api(
    app,
    version='1.0',
    title='Text tools',
    description='The microservice for creating a vector'
)

# Подключаем все пространства имён.
api.add_namespace(ns_text_tools, path="/vector")
api.add_namespace(ns_lifecycle, path="/lifecycle")