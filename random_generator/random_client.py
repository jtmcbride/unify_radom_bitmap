import requests
from PIL import Image

class RandomGenerator():

	def __init__(self):
		pass


	def get_ints(self, amount, min_val=0, max_val=255):
		"""fetch random integers from random API and store them as instance variables"""
		url = "https://www.random.org/integers/?num=%d&min=%d&max=%d&col=1&base=10&format=plain&rnd=new" % (amount, min_val, max_val)
		print url

		response = requests.get(url)
		if response.status_code == 200:
			self.random_ints = response.content
			return response.content
		else:
			raise Exception(response.content)


	def create_image(self, x_dim=128, y_dim=128,):
		self.get_ints(20)
		if self.random_ints:
			img = Image.new('RGB', (128,128), "black")
			pix = img.load()
			for i in range(img.size[0]):
				for j in range(img.size[1]):
					pix[i,j] = (i, j, 100)
			img.show()
		else:
			return None
