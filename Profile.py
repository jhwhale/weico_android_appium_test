#coding=utf-8
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time, unittest, sys, os, random,re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from BasicOperation import BasicOperation

class Profile(unittest.TestCase,BasicOperation):
	@classmethod
	def setUpClass(cls):
		desired_caps = {}
		desired_caps['appium-version'] = '1.0'
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '5.0'
		desired_caps['deviceName'] = 'OnePlus'
		#desired_caps['app'] = os.path.abspath('/Users/eico/Downloads/Weico-weico-release.apk')
		desired_caps['appPackage'] = 'com.eico.weico'
		desired_caps['appActivity'] = 'com.eico.weico.activity.MainFragmentActivity'

		cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def setUp(self):
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"album")))


	def tearDown(self):
		while True:
			try:
				self.driver.find_element_by_id("tab_icons_prof_layout")
				break
			except:
				self.driver.back()
				try:
					self.driver.find_element_by_id("ed_btn_negative").click()
				except:
					pass

	def test_01_me_following(self):
		self.driver.find_element_by_id("personal_friends_layout").click()
		self.driver.find_element_by_id("friends_isfriends").click()
		self.driver.find_element_by_id("ed_btn_positive").click()
		self.driver.find_element_by_id("friends_item_image").click()
		status = self.driver.find_element_by_id("add_follow").get_attribute("text")
		self.driver.find_element_by_id("add_follow").click()
		self.assertIn(status,("Follow",u"加关注"))

	def test_02_me_followers(self):
		self.driver.find_element_by_id("personal_followers_layout").click()
		self.driver.find_element_by_id("friends_isfriends").click()
		self.driver.find_element_by_id("friends_item_image").click()
		status = self.driver.find_element_by_id("add_follow").get_attribute("text")
		#恢复
		self.driver.find_element_by_id("add_follow").click()
		self.driver.find_element_by_id("dialog_confirm").click()
		self.assertIn(status,("Friends",u"相互关注"))

	def test_031_me_changeAvatar_camera(self):
		self.driver.find_element_by_id("personal_more_layout").click()
		self.driver.find_element_by_name(u"更换头像").click()
		self.driver.find_element_by_id("camera_function").click()
		time.sleep(2)
		self.driver.find_element_by_id("com.android.camera2:id/shutter_button").click()
		time.sleep(5)
		self.driver.find_element_by_id("com.android.camera2:id/done_button").click()
		time.sleep(2)
		self.driver.find_element_by_name("Done").click()

	def test_032_me_changeAvatar_album(self):
		self.driver.find_element_by_id("personal_more_layout").click()
		self.driver.find_element_by_name(u"更换头像").click()
		self.driver.find_element_by_id("photo_album_function").click()
		time.sleep(2)
		self.driver.find_element_by_id("com.google.android.apps.plus:id/tile_row").click()
		time.sleep(2)
		self.driver.find_element_by_name("Done").click()

	# # invalid case
	# def test_04_editProfile(self):
	# 	typeText = time.strftime("%Y-%m-%d %w %X", time.localtime())+"\n"
	# 	TouchAction(self.driver).press(x=800,y=800).move_to(x=-600,y=0).release().perform()
	# 	intr = self.driver.find_element_by_id("personal_description")
	# 	intrText1 = intr.get_attribute("text")
	# 	web = self.driver.find_element_by_id("personal_email")
	# 	webURL1 = web.get_attribute("text")
	# 	TouchAction(self.driver).press(x=200,y=800).move_to(x=600,y=0).release().perform()

	# 	self.driver.find_element_by_id("personal_more_layout").click()
	# 	self.driver.find_element_by_name(u"编辑个人资料").click()
	# 	self.driver.find_element_by_id("editorfinish").click()
	# 	# gender = self.driver.find_element_by_id("profile_sex_edittext").get_attribute("text")
	# 	# self.driver.find_element_by_id("profile_sex_edittext").click()
	# 	# if gender == "M":
	# 	# 	self.driver.find_element_by_id("sex_f").click()
	# 	# else:
	# 	# 	self.driver.find_element_by_id("sex_m").click()
	# 	self.driver.find_element_by_id("profile_blog_edittext").send_keys(typeText)
	# 	time.sleep(1)
	# 	TouchAction(self.driver).press(x=500,y=800).move_to(x=0,y=-300).release().perform()
	# 	time.sleep(1)
	# 	self.driver.find_element_by_id("proflie_description_edittext").send_keys(typeText)
	# 	self.driver.find_element_by_id("editorfinish").click()
	# 	time.sleep(3)
	# 	TouchAction(self.driver).press(x=800,y=800).move_to(x=-600,y=0).release().perform()
	# 	intrText2 = intr.get_attribute("text")
	# 	webURL2 = web.get_attribute("text")
	# 	self.assertNotEqual(intrText1,intrText2)
	# 	self.assertNotEqual(webURL1,webURL2)


	def test_05_group(self):
		typeText = "test_05_group"
		#create new group
		self.driver.find_element_by_id("personal_more_layout").click()
		self.driver.find_element_by_name(u"分组设置").click()
		self.driver.find_element_by_id("newgroup").click()
		self.driver.find_element_by_id("edit_group").send_keys(typeText)
		# TouchAction(self.driver).press(x=1000,y=1700).release().perform()
		# time.sleep(1)
		self.driver.find_element_by_id("dialog_confirm").click()
		time.sleep(1)
		#去边栏验证
		self.driver.find_element_by_id("back").click()
		self.driver.find_element_by_id("tab_icons_home_layout").click()
		self.driver.find_element_by_id("index_title_groups").click()
		groupInSlider1 = self.driver.find_elements(by = 'id',value = 'group_name')
		TouchAction(self.driver).press(x=300,y=1000).move_to(x=0,y=-600).release().perform()
		groupInSlider2 = self.driver.find_elements(by = 'id',value = 'group_name')
		groupInSlider = list(set(groupInSlider1+groupInSlider2))
		groupTextsInSlider =[]
		for i in range(0,len(groupInSlider)):
			groupTextInSlider = groupInSlider[i].get_attribute("text")
			groupTextsInSlider.append(groupTextInSlider)
		self.assertIn(typeText,groupTextsInSlider)
		#remove the new group
		self.driver.back()
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		self.driver.find_element_by_id("personal_more_layout").click()
		self.driver.find_element_by_name(u"分组设置").click()
		while True:
			try:
				self.driver.find_element_by_name(typeText).click()
				break
			except:
				TouchAction(self.driver).press(x=540,y=1600).move_to(x=0,y=-600).release().perform()
		self.driver.find_element_by_id("dialog_confirm").click()
		#去边栏验证
		self.driver.find_element_by_id("back").click()
		self.driver.find_element_by_id("tab_icons_home_layout").click()
		self.driver.find_element_by_id("index_title_groups").click()
		groupInSlider3 = self.driver.find_elements(by = 'id',value = 'group_name')
		TouchAction(self.driver).press(x=300,y=1000).move_to(x=0,y=-600).release().perform()
		groupInSlider4 = self.driver.find_elements(by = 'id',value = 'group_name')
		groupInSlider = list(set(groupInSlider3+groupInSlider4))
		groupTextsInSlider =[]
		for i in range(0,len(groupInSlider)):
			groupTextInSlider = groupInSlider[i].get_attribute("text")
			groupTextsInSlider.append(groupTextInSlider)
		self.assertNotIn(typeText,groupTextsInSlider)
				
	def test_06_exit(self):
		self.driver.find_element_by_id("personal_more_layout").click()
		self.driver.find_element_by_name(u"登出").click()
		accounts = self.driver.find_elements(by ='id',value='account_manager_name')
		names=[]
		for i in range(0,len(accounts)):
			name = accounts[i].get_attribute("text")
			names.append(name)
		self.assertIn(u"Test怪蜀黍",names)


	def test_07_me_allWeibo(self):
		self.driver.find_element_by_id("all_weibo").click()
		time1 = self.driver.find_element_by_id("index_item_created_at").get_attribute("text")
		self.driver.find_element_by_id("index_item_delete").click()
		self.driver.find_element_by_id("ed_btn_positive").click()
		time2 = self.driver.find_element_by_id("index_item_created_at").get_attribute("text")
		self.assertNotEqual(time1,time2)
		
	def test_08_me_originalWeibo(self):
		self.driver.find_element_by_id("original_weibo").click()
		time.sleep(5)
		try:
			self.driver.find_element_by_id("index_retweeted_content_background")
		except:
			pass
		else:
			self.fail("Find retweeted weibo in original weibo list.")
		time1 = self.driver.find_element_by_id("index_item_created_at").get_attribute("text")
		self.driver.find_element_by_id("index_item_delete").click()
		self.driver.find_element_by_id("ed_btn_positive").click()
		time2 = self.driver.find_element_by_id("index_item_created_at").get_attribute("text")
		self.assertNotEqual(time1,time2)

	def test_091_me_album_openWeibo(self):
		for i in range(0,9):
			self.driver.find_element_by_id("album").click()
			time.sleep(2)
			try:
				self.driver.find_element_by_id("item_picture").click()
				break
			except:
				self.driver.back()
			if i==8:
				self.skipTest("Cannot load pictures in album.")
		status = self.driver.find_element_by_id("statusText")
		statusText = status.get_attribute("text")
		status.click()
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"detail_status_layout")))
		TouchAction(self.driver).press(x=800,y=400).move_to(x=0,y=600).release().perform()
		time.sleep(2)
		weiboText = self.driver.find_element_by_id("detail_status_content").get_attribute("text")
		if not self.isTwoStringSimilar(weiboText,statusText):
			self.fail("Cannot open related weibo from album.")

	def test_092_me_album_repost(self):
		typeText = "test_092_me_album_repost"
		for i in range(0,9):
			self.driver.find_element_by_id("album").click()
			time.sleep(2)
			try:
				self.driver.find_element_by_id("item_picture").click()
				break
			except:
				self.driver.back()
			if i==8:
				self.skipTest("Cannot load pictures in album.")
		self.driver.find_element_by_id("single_image_options").click()
		self.driver.find_element_by_name("Repost").click()
		self.driver.find_element_by_id("compose_view_wrap").send_keys(typeText)
		self.driver.find_element_by_id("send_ok").click()
		while True:
			try:
				self.driver.find_element_by_id("tab_icons_prof_layout").click()
				break
			except:
				self.driver.back()
		time.sleep(5)
		content = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		picSize = self.driver.find_element_by_id("index_item_weibo_content_image").size
		self.assertIn(typeText,content)
		self.assertNotEqual(picSize,{318,318})


	def test_093_me_album_save(self):
		for i in range(0,9):
			self.driver.find_element_by_id("album").click()
			time.sleep(2)
			try:
				self.driver.find_element_by_id("item_picture").click()
				break
			except:
				self.driver.back()
			if i==8:
				self.skipTest("Cannot load pictures in album.")
		self.driver.find_element_by_id("single_image_options").click()
		self.driver.find_element_by_name("Save").click()

	def test_094_me_album_identifyQR(self):
		for i in range(0,9):
			self.driver.find_element_by_id("album").click()
			time.sleep(2)
			try:
				self.driver.find_element_by_id("item_picture").click()
				break
			except:
				self.driver.back()
			if i==8:
				self.skipTest("Cannot load pictures in album.")
		self.driver.find_element_by_id("single_image_options").click()
		self.driver.find_element_by_name("Identify qr").click()
		try:
			self.driver.find_element_by_id("ed_btn_negative").click()
		except:
			self.skipTest("There's no QR code in the picture.")

	def test_095_me_album_flicking(self):
		for i in range(0,9):
			self.driver.find_element_by_id("album").click()
			time.sleep(2)
			try:
				self.driver.find_element_by_id("item_picture").click()
				break
			except:
				self.driver.back()
			if i==8:
				self.skipTest("Cannot load pictures in album.")
		i = random.randint(0,24)
		while i>=0:
			TouchAction(self.driver).press(x=720,y=800).move_to(x=-360,y=0).release().perform()
			time.sleep(1)
			TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-600).wait(1000).release().perform()
			i-=1

	def test_10_me_favorites(self):
		self.driver.find_element_by_id("favour").click()
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"index_item_weibo_content")))
		weibo1Text = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		self.driver.find_element_by_id("index_item_source").click()
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"detail_title_fav")))
		star = self.driver.find_element_by_id("detail_title_fav")
		star.click()
		time.sleep(2)
		self.assertFalse(star.is_selected())
		self.driver.find_element_by_id("detail_title_goback").click()
		self.driver.find_element_by_id("back").click()
		self.driver.find_element_by_id("favour").click()
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"index_item_weibo_content")))
		weibo2Text = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		self.assertNotEqual(weibo1Text,weibo2Text)

	def test_11_me_searchMyWeibo(self):
		typeText = "weico"
		self.driver.find_element_by_id("button_icon_search").click()
		self.driver.find_element_by_id("search_edittext").send_keys(typeText)
		TouchAction(self.driver).press(x=1000,y=1800).release().perform()
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"index_item_weibo_content")))
		content = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text").lower()
		self.assertIn(typeText,content)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Profile)
    unittest.TextTestRunner(verbosity=2).run(suite)