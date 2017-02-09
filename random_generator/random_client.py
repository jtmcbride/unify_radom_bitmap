import os
from PIL import Image


class RandomGenerator():

	def __init__(self):
		pass


	def get_ints(self, amount, min_val=0, max_val=255, col=3):
		"""fetch random integers from random API and store them as instance variables"""
		url = "curl 'https://www.random.org/integers/?num=%d&min=%d&max=%d&col=%d&base=10&format=plain'" % (amount, min_val, max_val, col)

		response = os.popen(url).read()
		if response.startswith("Error:"):
			raise Exception(response)
		else:
			self.random_ints = response
			return response
			


	def create_image(self, x_dim=128, y_dim=128,):
		self.get_ints(9999)
		if self.random_ints:
			rgb = self.format_rgb_response(self.random_ints)
			rgb = np.random.randint(0, 255, (128*128, 3))
			img = Image.new('RGB', (128,128), "black")
			pix = img.load()
			count = 0
			# set pixel rgb values to stored random ints
			for i in range(img.size[0]):
				for j in range(img.size[1]):
					pix[i,j] = tuple(rgb[count])
					count += 1

					if count > len(rgb) - 1:
						count = 0
						self.get_ints(9999)
						rgb = self.format_rgb_response(self.random_ints)

			img.save("randBMP.bmp")
		else:
			return None


	def format_rgb_response(self, response):
		"""formats random ints into sets of rgb tuples"""
		rgb = map(lambda x: tuple(x.split("\t")), response.split("\n"))
		rgb.pop()
		return rgb

