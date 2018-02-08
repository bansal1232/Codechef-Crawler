import requests, re, os
from bs4 import BeautifulSoup
from models import URL

def codechef_download(req, handle):
  print('Please be patient, Your codes are downloading')
  if not os.path.exists(handle):
   os.makedirs(handle)
  codechef = 'https://www.codechef.com'
  url = URL.BASE+ '/users/' + handle
  try:
      r = req.get(url)
      soup=BeautifulSoup(r.content, 'lxml')


      t=soup.find('section', class_='rating-data-section problems-solved')
      link=t.findAll('a')
      length = len(link)

      prob_count = 0
      for x in link:
        prob = x.text
        print("Fetching the solved {} problem...".format(prob),end=' ', flush=True)
        pat = re.match('/+[\w]+/',x['href'])
        contest = pat.group(0)
        if contest == '/status/':
          contest='/Practice/'

        # Make directory of contest folder
        if not os.path.exists(handle+'/'+contest):
          os.makedirs(handle+contest)

        nxt_url=codechef+x['href']
        
        rqt = req.get(nxt_url)
        soup = BeautifulSoup(rqt.content,'lxml')
        t = soup.find(href=re.compile("/viewsolution"))
        recall = 0
        while  t == None and recall < 3:
          print("Trying Again", prob)
          rqt = req.get(nxt_url)
          soup=BeautifulSoup(rqt.content, 'lxml')
          t=soup.find(href=re.compile("^/viewsolution"))
          recall += 1
          pass
        
        if t == None:
          print('Something Went wrong, may be solution of',prob,'is not visible or might be there is some network problem')
          continue

        #Forward request to the solution
        headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
        rqt_final=req.get(codechef+t['href'],headers=headers,stream=True)
        soup = BeautifulSoup(rqt_final.content,'lxml')
        
        # Find language
        lang=soup.find('pre')

        # If language is not found, download in .text file
        if lang == None:
          w = open(handle + contest+ prob + '.text')
          code = soup.find('div', id='solutiondiv')
          w.write(code.text)
          print('Language not found,Successfully downloaded in .text file')
          continue

        w = open(handle+contest+prob+'.' + lang['class'][0], 'w')
        
        code=lang.findAll('li')
        for line in code:
          w.write(line.text+'\n')
        
        print("Successfully Downloaded")  
        prob_count += 1
      print("Total number of solved problems: ", prob_count)
      return
  except:
    print("Something might went wrong! Please check your Internet connection")

if __name__=='__main__':
  handle = '' #Write down your handle name
  codechef_download(requests, handle)