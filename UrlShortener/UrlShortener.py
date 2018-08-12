import pyshorteners as ps

class ClsShortener:
	
	def __init__(self, *args, **kwargs):
		self.s = ps.Shortener('Tinyurl')

	def update_url(self,url):
		if url.startswith('http'):
			sh_url = self.s.short(url)
			return sh_url
		else:
			http_url = 'http://' + url
			#print(http_url)
			sh_url = self.s.short(http_url)
			return sh_url

if __name__ == '__main__':
	ClsShortener()