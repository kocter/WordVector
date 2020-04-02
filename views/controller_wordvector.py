from flask import request
from flask_restplus import Resource, Namespace, fields
from services.CWordVectorTools import my_bag_of_words
# *******************************************************************************************************
# Контроллер содержит обработку запросов на текстовые операции.                                         *
# @author Селетков И.П. 2019 1118.                                                                      *
# *******************************************************************************************************

ns_text_tools = Namespace('text tools', description='Text clearing tools')



# *******************************************************************************************************
# Получение вектора.                                                                                 *
# *******************************************************************************************************
@ns_text_tools.route('/wordvector')
@ns_text_tools.response(404, 'not found.')
class CTextStemming(Resource):
    def post(self):
        text = request.data.decode("utf-8")
        print(my_bag_of_words(text))
        return my_bag_of_words(text)


