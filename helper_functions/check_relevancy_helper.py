from gen_response_helper import gen_response

def check_relevancy(conversation_string , search_response):
    if search_response == "":
        return ""
    prompt = conversation_string + "\nAdditional info: " + search_response + "\nIs this information helpful in replying to the conversation Yes/No:" 
    check = gen_response(prompt , "text-davinci-003", ["\\n"], 10).replace("\n" , "")
    if check == "Yes":
        return search_response
    if check == "No":
        return ""
    return ""