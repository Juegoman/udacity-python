from urllib import request

def read_text():
    text = open(r"")#add location of profanity_text.txt
    text_contents = text.read()
    text.close()
    check_profanity(text_contents)

def check_profanity(text_to_check):
    request_Url = "http://www.wdylike.appspot.com/?q=" + text_to_check.strip().replace(" ", "+")
    connection = request.urlopen(request_Url)
    output = str(connection.read())
    connection.close()

    if (output.find("true") != -1):
        print("The input text has curse words in it!")
    elif (output.find("false")!= -1):
        print("The input text is clean!")
    else:
        print("There was some error.")
        
read_text()
