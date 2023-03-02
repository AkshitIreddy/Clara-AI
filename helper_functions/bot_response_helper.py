from gen_response_helper import gen_response
from check_relevancy_helper import check_relevancy

bio = "Clara is an enthusiastic and cheerful AI Assistant."

def bot_response(conversation , search_response):
    conversation_string = "\n".join(conversation)
    search_response = check_relevancy(conversation_string , search_response)
    prompt = ""
    if search_response == "":
        prompt = prompt + bio + "\n" + conversation_string + "\nClara:"
        response = gen_response(prompt , "text-davinci-003", ["\\n"], 256).replace("\n" , "")
        return response
    if search_response != "":
        prompt = prompt + bio + "\nAdditional Information: " + search_response + "\n" + conversation_string + "\nClara:"
        response = gen_response(prompt , "text-davinci-003", ["\\n"], 256).replace("\n" , "")
        return response