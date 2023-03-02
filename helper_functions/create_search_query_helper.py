from gen_response_helper import gen_response

def create_search_query(conversation):
    conversation_string = "\n".join(conversation)
    prompt = conversation_string + "\nGenerate a one line detailed search query for an AI to google to help it gain information and context regarding what the conversation is about and if it is obvious what the conversation is about then generate a search query which when googled will result in information that will help the AI in guiding the user.\nsearch_query:"
    search_query = gen_response(prompt , "text-davinci-003", ["\\n"] , 256).replace("\n" , "").replace('"' , "").replace("'" , "")
    return search_query