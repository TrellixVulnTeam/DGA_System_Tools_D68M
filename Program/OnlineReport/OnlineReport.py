import json
import os
import requests
import SessionKey

def installModul():

    modl = ['pandas',
            'xlrd',
            'openpyxl',
            'xlsxwriter',
            'mysql-connector-python',
            'mariadb',
            'brotli',
            'requests',
            ];

    for x in modl:
        os.system(f'venv\Scripts\python.exe venv\Scripts\pip.exe install {x.strip()}');



def api_online_report(email):

    getemail = '';
    getemail=getemail+email;

    esplit = getemail.split('@');

    url_link = 'https://onlinereport.mail.go.th/'
    llogin = 'index.php'
    reportc = 'report-accounts.php'



    api_link =f'https://onlinereport.mail.go.th/event/Accounts.php?type=read&options%5Btake%5D=500&options%5Bskip%5D=0&options%5Bpage%5D=1&options%5Bpa' \
              f'geSize%5D=500&options%5Bfilter%5D%5Blogic%5D=and&options%5Bfilter%5D%5Bfilters%5D%5B0%5D%5Bfield%5D=email&options%5Bfilter%5D%5Bfilters%5D%5B' \
              f'0%5D%5Boperator%5D=contains&options%5Bfilter%5D%' \
              f'5Bfilters%5D%5B0%5D%5Bvalue%5D={esplit[0]}%40{esplit[1]}%09'

    s = requests.session()
    cerf_token = s.get(url_link).cookies['PHPSESSID'];

    login_payload1 = {
        'txtUsername': 'CSC',
        'txtPassword': 'csc@026126060',
        'csrf_token': cerf_token
    }

    header2 = {
        'scheme': 'https',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, utf-8',
        'accept-language': 'en-US,en;q=0.9,th;q=0.8',
        'cookie': 'PHPSESSID='+SessionKey.PHPSESSION,
        'referer': 'https://onlinereport.mail.go.th/report-accounts.php',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }


    try:

        print('\n')
        ps = s.get(api_link, headers=header2, data=login_payload1)
        resoult = ps.content.decode("UTF-8");



        for x in resoult.split(','):

            if "name" in x:
                pgk = x.split(':');
                print(f'"name":"{json.loads(pgk[1])}"');
            else:
                print(x)
    except:
        print("Change Session id")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':\

    #installModul()


    while True:
        try:
            s = input("Email >>")
            api_online_report(s.strip());
        except OSError as errorp:
            print(errorp);

