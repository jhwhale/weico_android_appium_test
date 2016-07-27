#coding=utf-8
from appium import webdriver
import random,time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasicOperation():
	def composeWeibo(self,content):
		#self.driver.find_element_by_id("index_title_compose").click()

		#添加文字
		self.driver.find_element_by_id("compose_view_wrap").send_keys(content)
		#添加位置
		WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "textLocation")))
		self.driver.find_element_by_id("textLocation").click()
		try:
			time.sleep(5)
			self.driver.find_element_by_id("title").click()
		except:
			self.driver.find_element_by_id("delete_address").click()
		#添加@
		self.driver.find_element_by_id("buttonAt").click()
		self.driver.find_element_by_id("search_edittext").send_keys("test")
		time.sleep(2)
		self.driver.find_element_by_id("item_user_checked").click()
		self.driver.find_element_by_id("done_button").click()
		#拍摄照片
		self.driver.find_element_by_id("buttonCam").click()
		self.driver.find_element_by_id("cameraPreview").click()
		time.sleep(2)
		self.driver.find_element_by_id("com.android.camera2:id/shutter_button").click()
		time.sleep(5)
		self.driver.find_element_by_id("com.android.camera2:id/done_button").click()
		time.sleep(2)
		photo = range(2,9)#添加7张已有图片
		for i in photo:
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout["+str(i)+"]/android.widget.ImageView[1]").click()
		self.driver.find_element_by_id("btn_next").click()
		#添加表情
		self.driver.find_element_by_id("buttonEmoji").click()
		self.driver.find_element_by_id("newblog_expression_expression").click()
		expression = random.randint(1,10)
		fontexpression = random.randint(1,10)
		try:
			while expression>0:
				i = random.randrange(1,22)
				self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.GridView[1]/android.widget.RelativeLayout[" +str(i)+ "]").click()
				expression-=1
			self.driver.find_element_by_id("newblog_expression_fontexpression").click()
			while fontexpression>0:	
				i = random.randrange(1,22)
				self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.GridView[1]/android.widget.RelativeLayout[" +str(i)+ "]").click()
				fontexpression -= 1
		except:
			time.sleep(5)
			self.driver.find_element_by_id("newblog_expression_back").click()

		# #添加tag
		# self.driver.find_element_by_id("buttonTag").click()
		# self.driver.find_element_by_id("editText").send_keys("weico")
			

	def composeComments(self,comments):
		#add pic
		self.driver.find_element_by_id("buttonCam").click()
		self.driver.find_element_by_id("albumPreview").click()
		# #添加tag
		# self.driver.find_element_by_id("buttonTag").click()
		# self.driver.find_element_by_id("editText").send_keys("weico comments")
		#添加@
		self.driver.find_element_by_id("buttonAt").click()
		self.driver.find_element_by_id("search_edittext").send_keys("test")
		time.sleep(3)
		self.driver.find_element_by_id("item_user_checked").click()
		self.driver.find_element_by_id("done_button").click()
		#添加文字
		self.driver.find_element_by_id("compose_view_wrap").send_keys(comments)
		#添加表情
		self.driver.find_element_by_id("buttonEmoji").click()
		self.driver.find_element_by_id("newblog_expression_expression").click()
		expression = random.randint(1,10)
		while expression>0:
			i = random.randrange(1,22)
			self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.GridView[1]/android.widget.RelativeLayout[" +str(i)+ "]").click()
			expression-=1
		self.driver.find_element_by_id("newblog_expression_fontexpression").click()
		fontexpression = random.randint(1,10)
		while fontexpression>0:	
			i = random.randrange(1,22)
			self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.GridView[1]/android.widget.RelativeLayout[" +str(i)+ "]").click()
			fontexpression -= 1
		#同时转发评论
		forwardComments = random.randint(0,1)
		if forwardComments == 1:
			self.driver.find_element_by_id("textLocation").click()

	def sendDM(self,msg):
		self.driver.find_element_by_id("buttonCam").click()
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("msg_text").send_keys(msg)
		self.driver.find_element_by_id("buttonTag").click()
		self.driver.find_element_by_id("newblog_expression_expression").click()
		expression = random.randint(1,10)
		while expression>0:
			i = random.randrange(1,22)
			self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.GridView[1]/android.widget.RelativeLayout[" +str(i)+ "]/android.widget.ImageView[1]").click()
			expression -=1
		self.driver.find_element_by_id("newblog_expression_fontexpression").click()
		fontexpression = random.randint(1,10)
		while fontexpression>0:
			i = random.randrange(1,22)
			self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.GridView[1]/android.widget.RelativeLayout[" +str(i)+ "]/android.widget.ImageView[1]").click()
			fontexpression -= 1
		self.driver.find_element_by_id("send_layout").click()

	def getElementNum(self,prefix_xpath,postfix_xpath):
		i = 1
		while True:
			xpath = prefix_xpath+str(i)+postfix_xpath
			try:
				self.driver.find_element_by_xpath(xpath)
			except:
				break
			i+=1
		return i-1

	def isTwoStringSimilar(self,str1,str2):
		s1 = str1.lower()
		s2 = str2.lower()
		inChar = 0
		for i in range(0,len(s1)):
			if s1[i] in s2:
				inChar += 1
		similarity = inChar/len(s1)
		if similarity >= 0.5:
			return True
		else:
			return False

