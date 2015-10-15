from base_page import BasePage

class DashBoardPage(BasePage):
	def greeking_link(self):
		return self.by_class_name('userinfo') 
	