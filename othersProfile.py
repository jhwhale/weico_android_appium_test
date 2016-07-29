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
		time.sleep(3)

	def tearDown(self):
		while True:
			try:
				self.driver.find_element_by_id("tab_icons_home_layout")
				break
			except:
				self.driver.back()
				try:
					self.driver.find_element_by_id("ed_btn_negative").click()
				except:
					pass

	def test_01_searchWeibo(self):
		typeText = "weico"
		self.driver.find_element_by_id("search_weibo").click()
		self.driver.find_element_by_id("search_edittext").send_keys(typeText)
		TouchAction(self.driver).press(x=1000,y=1800).release().perform()
		try:
			content = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text").lower()
			self.assertIn(typeText,content)
		except:
			self.skipTest("Cannot search out any weibo.")

	def test_02_openAvatar(self):
		self.driver.find_element_by_id("personal_image").click()
		try:
			self.driver.find_element_by_id("mine_photo")
		except:
			self.fail("cannot open other person's avatar.")

	def test_03_chat(self):
		self.driver.find_element_by_id("send_message").click()
		try:
			self.driver.find_element_by_id("msg_list_view")
			self.driver.find_element_by_id("text_tool_bar")
		except:
			self.fail("Cannot open conversation view.")


	def test_04_followUnfollow(self):
		followBtn = self.driver.find_element_by_id("add_follow")
		if followBtn.get_attribute("text") in ("Following",u"已关注","Friends"):
			followBtn.click()
			time.sleep(2)
			self.driver.find_element_by_id("dialog_confirm").click()
		followBtn.click()
		self.driver.find_element_by_id("add_ok").click()
		self.assertIn(followBtn.get_attribute("text"),("Following",u"已关注","Friends"))

	def test_05_following(self):
		self.driver.find_element_by_id("personal_friends_layout").click()
		self.driver.find_element_by_id("friends_item_image")
		self.driver.find_element_by_id("friends_item_screen_name").click()
		self.driver.find_element_by_id("back").click()
		self.driver.find_element_by_id("incommon_layout").click()
		try:
			commonFriend = self.driver.find_element_by_id("friends_item_screen_name")
			commonFriendName = commonFriend.get_attribute("text")
			commonFriend.click()
			title = self.driver.find_element_by_id("title_name").get_attribute("text")
			self.assertEqual(commonFriendName,title)
		except:
			print "There's no friend in common."

	def test_06_followers(self):
		self.driver.find_element_by_id("personal_followers_layout").click()
		# self.driver.find_element_by_id("friends_item_image")
		self.driver.find_element_by_id("friends_item_screen_name").click()
		self.driver.find_element_by_id("back").click()
		self.driver.find_element_by_id("headerFollower").click()
		try:
			commonFriend = self.driver.find_element_by_id("friends_item_screen_name")
			commonFriendName = commonFriend.get_attribute("text")
			commonFriend.click()
			title = self.driver.find_element_by_id("title_name").get_attribute("text")
			self.assertEqual(commonFriendName,title)
		except:
			print "He/She doesn't have any friend."


	def test_07_info(self):
		try:
			self.driver.find_element_by_id("profile_header_sliding_tab")
		except:
			self.skipTest("There's no more info.")
		TouchAction(self.driver).press(x=900,y=600).move_to(x=-800,y=0).release().perform()


	def test_08_atTa(self):
		name = self.driver.find_element_by_id("title_name").get_attribute("text")
		self.driver.find_element_by_id("more").click()
		self.driver.find_element_by_id("at_personal_layout").click()
		time.sleep(2)
		weibo = self.driver.find_element_by_id("editText").get_attribute("text")
		if not self.isTwoStringSimilar(weibo,name):
			self.fail("Cannot @%s" % name)

	# #invalid case 无法验证
	# def test_09_copyNickname(self):
	# 	self.driver.find_element_by_id("more").click()
	# 	self.driver.find_element_by_id("copynickname_personal_layout").click()
	# 	time.sleep(3)
	# 	self.driver.find_element_by_id("others_edit").click()
	# 	self.driver.execute_script('sendKeyEvent(50,AndroidKeyMetastate.META_CTRL_ON)')

	def test_10_editNote(self):
		typeText = "test_10_editNote"
		self.driver.find_element_by_id("more").click()
		time.sleep(2)
		self.driver.find_element_by_id("others_edit").send_keys(typeText)
		while True:
			try:
				self.driver.find_element_by_id("tab_icons_home_layout")
				break
			except:
				self.driver.back()
		self.driver.find_element_by_id("index_item_avatar_mask").click()
		time.sleep(2)
		name = self.driver.find_element_by_id("title_name").get_attribute("text")
		self.assertIn(typeText,name)

	def test_11_groupSettings(self):
		self.driver.find_element_by_id("more").click()
		self.driver.find_element_by_id("setting_layout").click()
		self.driver.find_element_by_id("itemlayout").click()
		self.driver.find_element_by_id("back").click()

	# invalid case
	# def test_12_block(self):
	# 	self.driver.find_element_by_id("more").click()
	# 	self.driver.find_element_by_id("blacklist_personal_layout").click()
	# 	self.driver.find_element_by_id("dialog_cancel").click()
	# 	self.driver.find_element_by_id("blacklist_personal_layout").click()
	# 	self.driver.find_element_by_id("dialog_confirm").click()
	# 	time.sleep(3)
	# 	TouchAction(self.driver).press(x=540,y=1600).release().perform()

	def test_13_allWeibo(self):
		self.driver.find_element_by_id("all_weibo").click()
		time.sleep(2)
		try:
			self.driver.find_element_by_id("index_item_weibo_content")
		except:
			self.fail("Cannot load weibo.")
		
	def test_14_originalWeibo(self):
		self.driver.find_element_by_id("original_weibo").click()
		time.sleep(2)
		TouchAction(self.driver).press(x=540,y=1600).move_to(x=0,y=-1200).release().perform()
		try:
			self.driver.find_element_by_id("index_retweeted_content_background")
		except:
			pass
		else:
			self.fail("There's not only original weibo under 'original' tab.")

	def test_15_album(self):
		for i in range(0,9):
			self.driver.find_element_by_id("album").click()
			time.sleep(2)
			try:
				self.driver.find_element_by_id("item_picture")
				break
			except:
				self.driver.back()
			if i==8:
				self.skipTest("Cannot load pictures in album.")
		TouchAction(self.driver).press(x=500,y=1200).move_to(x=0,y=-600).release().perform()
		self.driver.find_element_by_id("item_picture").click()
		for i in range(0,9):
			TouchAction(self.driver).press(x=720,y=800).move_to(x=-360,y=0).release().perform()
			time.sleep(1)
			TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-600).wait(1000).release().perform()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(othersProfile)
    unittest.TextTestRunner(verbosity=2).run(suite)