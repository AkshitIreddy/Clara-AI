from helper_functions.create_search_query_helper import create_search_query
from helper_functions.web_search_helper import web_search
from helper_functions.bot_response_helper import bot_response

def create_response(conversation):
    search_query = create_search_query(conversation)
    search_response = web_search(search_query)
    reply = bot_response(conversation , search_response)
    return reply
