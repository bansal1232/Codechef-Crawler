import requests,re
import conf
from models import URL

def session_logout(req, page, link):
	# Count total session are currently available
	total_hosts = re.compile('"checkbox" name="(.*?)"')
	hosts = total_hosts.findall(page.text)
	payload={} # Create Dictionary
	for val in hosts[:-1]:
		payload[val]=val[4:-1]


	form_build_val = re.search('"form_build_id" id="(.*?)"', page.text).group(1)
	form_token_val = re.search('"form_token".*? value="(.*?)"', page.text).group(1)
	
	payload.update({
	'op':'Disconnect session',
	'form_token':form_token_val,
	'form_build_id': form_build_val,
	'form_id' : 'session_limit_page'
	})

	pg = req.post(link, data=payload)

def codechef_login(req, link):
	print('Logging into {}'.format(link+conf.handle))
	payload={
	conf.user_key: conf.handle,
	conf.pass_key: conf.pass_val,
	conf.form_key: conf.form_val
	}
	
	page =  req.post(link, data=payload)

	if re.search('Logout', page.text):
		print("Log In Successfully")
		if re.search('<div class="help">', page.text):
			print("Please wait until other sessions are being disconnected")
			session_logout(req ,page, link + URL.SESSION)
	else:
		raise SystemExit('Login messed up at some point, please check you ACCOUNT Details!')

def codechef_logout(req, link):
	page = req.get(link)
	if page.status_code == 200:
		print("Your session has been Successfully Logged Out")
	else:
		print ("Logged out messed up at some point")

def get_rating(req, handle):
	print('Fetching the overall Ratings')
	from bs4 import BeautifulSoup
	try:
		url = URL.BASE + 'users/' + handle
		r = req.get(url)
		soup = BeautifulSoup(r.content, 'lxml')
		t = soup.find('aside', class_='sidebar small-4 columns pr0')
		overall = t.find('div',attrs={'class':'rating-number'})
		Ratings = t.findAll('td')
		print('\tOverall Rating = {}\n\tIndividual Ratings\n\tLong Challenge =  {}\n\tCook Off   \t   = {}\n\tLunch Time     = {}'.format(overall.text, Ratings[1].text, Ratings[5].text, Ratings[9].text))
	except:
		print('Rating not available right now! Please check your Internet Connection')