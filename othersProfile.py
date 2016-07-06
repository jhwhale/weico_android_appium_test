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

class othersProfile(unittest.TestCase,BasicOperation):
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
		self.driver.find_element_by_id("tab_icons_home_layout").click()
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"index_item_avatar_mask")))
		time.sleep(3)
		self.driver.find_element_by_id("index_item_avatar_mask").click()

	def tearDown(self):
		self.driver.find_element_by_id("back").click()
		time.sleep(3)

	def test_01_genderLocation(self):
		self.assertNotEqual(self.driver.find_element_by_id("personal_location").get_attribute("text"),"")

	# def test_02_openAvatar(self):
	# 	self.driver.find_element_by_id("personal_image").click()
	# 	try:
	# 		self.driver.find_element_by_id("mine_photo")
	# 	except:
	# 		self.fail("cannot open other person's avatar.")
	# 	TouchAction(self.driver).press(x=540,y=1500).release().perform()

	# def test_03_chat(self):
	# 	self.driver.find_element_by_id("send_message").click()
	# 	self.sendDM("hello")
	# 	self.driver.find_element_by_id("detail_title_goback").click()

	# def test_04_followUnfollow(self):
	# 	followBtn = self.driver.find_element_by_id("add_follow")
	# 	if followBtn.get_attribute("text") in ("Following",u"已关注"):
	# 		followBtn.click()
	# 		self.driver.find_element_by_id("dialog_confirm").click()
	# 	followBtn.click()
	# 	self.driver.find_element_by_id("add_ok").click()
	# 	self.assertIn(followBtn.get_attribute("text"),("Following",u"已关注"))

	# def test_05_following(self):
	# 	self.driver.find_element_by_id("personal_friends_layout").click()
	# 	self.driver.find_element_by_id("friends_item_image")
	# 	self.driver.find_element_by_id("friends_item_screen_name").click()
	# 	self.driver.find_element_by_id("back").click()
	# 	self.driver.find_element_by_id("incommon_layout").click()
	# 	try:
	# 		self.driver.find_element_by_id("friends_item_image").click()
	# 		self.driver.find_element_by_id("back").click()
	# 	except:
	# 		print "There's no friend in common."
	# 	self.driver.find_element_by_id("back").click()
	# 	self.driver.find_element_by_id("back").click()

	# def test_06_followers(self):
	# 	self.driver.find_element_by_id("personal_followers_layout").click()
	# 	self.driver.find_element_by_id("friends_item_image")
	# 	self.driver.find_element_by_id("friends_item_screen_name").click()
	# 	self.driver.find_element_by_id("back").click()
	# 	self.driver.find_element_by_id("headerFollower").click()
	# 	try:
	# 		self.driver.find_element_by_id("friends_item_image").click()
	# 		self.driver.find_element_by_id("back").click()
	# 	except:
	# 		print "He/She doesn't have any friend."
	# 	self.driver.find_element_by_id("back").click()
	# 	self.driver.find_element_by_id("back").click()

	# def test_07_info(self):
	# 	try:
	# 		self.driver.find_element_by_id("profile_header_sliding_tab")
	# 	except:
	# 		self.skipTest("There's no more info.")
	# 	TouchAction(self.driver).press(x=900,y=600).move_to(x=-800,y=0).release().perform()


	# def test_08_atTa(self):
	# 	name = self.driver.find_element_by_id("title_name").get_attribute("text")
	# 	self.driver.find_element_by_id("more").click()
	# 	self.driver.find_element_by_id("at_personal_layout").click()
	# 	weibo = self.driver.find_element_by_id("editText").get_attribute("text")
	# 	self.driver.find_element_by_id("send_ok").click()
	# 	time.sleep(5)
	# 	TouchAction(self.driver).press(x=540,y=1600).release().perform()
	# 	self.assertIn(name,weibo)

	# def test_09_copyNickname(self):
	# 	self.driver.find_element_by_id("more").click()
	# 	self.driver.find_element_by_id("copynickname_personal_layout").click()
	# 	time.sleep(3)
	# 	TouchAction(self.driver).press(x=540,y=1600).release().perform()

	def test_10_editNote(self):
		self.driver.find_element_by_id("more").click()
		try:
			self.driver.find_element_by_id("others_edit").send_keys("test_10_editNote")
			time.sleep(1)
			TouchAction(self.driver).press(x=540,y=1600).release().perform()
		except:
			TouchAction(self.driver).press(x=540,y=1600).release().perform()
			self.skipTest("Cannot edit node.")

	def test_11_groupSettings(self):
		self.driver.find_element_by_id("more").click()
		try:
			self.driver.find_element_by_id("setting_layout").click()
			self.driver.find_element_by_id("itemlayout").click()
			self.driver.find_element_by_id("back").click()
			time.sleep(2)
			TouchAction(self.driver).press(x=540,y=1600).release().perform()
		except:
			TouchAction(self.driver).press(x=540,y=1600).release().perform()
			self.skipTest("Cannot set group.")
		
	def test_12_block(self):
		self.driver.find_element_by_id("more").click()
		self.driver.find_element_by_id("blacklist_personal_layout").click()
		self.driver.find_element_by_id("dialog_cancel").click()
		self.driver.find_element_by_id("blacklist_personal_layout").click()
		self.driver.find_element_by_id("dialog_confirm").click()
		time.sleep(3)
		TouchAction(self.driver).press(x=540,y=1600).release().perform()

	def test_13_allWeibo(self):
		self.driver.find_element_by_id("all_weibo").click()
		time.sleep(2)
		TouchAction(self.driver).press(x=540,y=1600).move_to(x=0,y=-1200).release().perform()
		
	def test_14_originalWeibo(self):
		self.driver.find_element_by_id("original_weibo").click()
		time.sleep(2)
		TouchAction(self.driver).press(x=540,y=1600).move_to(x=0,y=-1200).release().perform()
		try:
			self.driver.find_element_by_id("index_retweeted_content_background")
		except:
			print "Only original weibo is found."
		else:
			self.fail("There's not only original weibo under 'original' tab.")

	def test_15_album(self):
		self.driver.find_element_by_id("album").click()
		self.driver.find_element_by_id("item_picture")
		self.driver.find_element_by_id("back").click()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(othersProfile)
    unittest.TextTestRunner(verbosity=2).run(suite)