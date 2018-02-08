class URL():
	BASE = 'https://www.codechef.com/'
	SESSION = 'session/limit/'
	LOGOUT = '/logout'
	
	def __init__(self, name='', link=''):
		self.name=name
		self.link=link
		self.problems=[]
