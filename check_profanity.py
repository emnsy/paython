import urllib

def read_text():
    quotes=open("c:\py\movie_quotes.txt")
    content_of_file=quotes.read()
    print(content_of_file)
    quotes.close()
    check_profanity(content_of_file)

def check_profanity(text_to_check):
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output=connection.read()
    if 'true' in output:
        print("يوجد كلمات مخلة داخل الفقرة")
    else:
        print("الفقرة خالية من الكلمات المخلة")
    connection.close()

read_text()    
