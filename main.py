print("IMPORTANT: Internet connection required!!!\n")
try:
    if (__name__!='__main__'):
        exit(1)
    
    else :
        import urllib
        import urllib.request as ur
        import json
        import base64

        print("By Akshit Gupta :) @pwnnrove");
        id = input('Enter Exam ID:')
        url = "https://backendemployer.myamcat.com//assessmentmanagement/newReport/getReportChapter?chapterId=DetailedResponseChapter&outputFormat=json&locale=en-US&reportId=229&defaultChapterId=DetailedResponseChapter&isSvar=0&amcatId=&amcatId="+id
        
        weburl = ur.urlopen(url)
        html = weburl.read()
        data = weburl.getcode()
        urli = weburl.geturl()
        hd = weburl.headers
        inf = weburl.info()


        report = json.loads(html)
        dat = report['data']

        sec = dat['report']

        sert = urllib.parse.unquote(sec)
        js = json.loads(base64.b64decode(sert))

        lp = js['detailedResponse']

        wd = lp[0]['detailedResponse']

        sdl = wd['DR_QuestionsReport']

        wer = sdl['incorrectIndexes']
        print("\nExam name: "+lp[0]['moduleDetails']['moduleName'])
        print("\nIncorrect Attempts are as follows:")
        print(wer)
        print('\nTotal Questions:'+str(wd['DR_McqQuestionStats']['data'][1]['total']))
        print('Correct Questions:'+str(wd['DR_McqQuestionStats']['data'][1]['correct']))
        print('Correct Questions percent:'+str(wd['DR_McqQuestionStats']['data'][1]['percent']))
        print("\nPress enter to exit...")
        input()
        
except ImportError:
    print("Make sure you have python and necessary modules installed");
    exit(1)
except Exception:
    print("Something went wrong!!!")
    exit(1)
