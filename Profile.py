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
		try:
			self.driver.find_element_by_id("tab_icons_prof_layout").click()
			time.sleep(2)
		except:
			time.sleep(2)

	def tearDown(self):
		time.sleep(3)

	def test_01_me_following(self):
		self.driver.find_element_by_id("personal_friends_layout").click()
		self.driver.find_element_by_id("friends_isfriends").click()
		self.driver.find_element_by_id("dialog_confirm").click()
		self.driver.find_element_by_id("friends_item_image").click()
		status = self.driver.find_element_by_id("add_follow").get_attribute("text")
		self.driver.find_element_by_id("back").click()
		self.driver.find_element_by_id("back").click()
		self.assertIn(status,("Follow",u"加关注"))

	def test_02_me_followers(self):
		self.driver.find_element_by_id("personal_followers_layout").click()
		self.driver.find_element_by_id("friends_isfriends").click()
		self.driver.find_element_by_id("friends_item_image").click()
		status = self.driver.find_element_by_id("add_follow").get_attribute("text")
		self.assertIn(status,("Friends",u"相互关注"))
		self.driver.find_element_by_id("back").click()
		self.driver.find_element_by_id("back").click()

	def test_031_me_changeAvatar_camera(self):
		self.driver.find_element_by_id("personal_more_layout").click()
		self.driver.find_element_by_id("change_avatar").click()
		self.driver.find_element_by_id("camera_function").click()
		time.sleep(2)
		TouchAction(self.driver).press(x=120,y=1650).wait(1000).release().perform()
		time.sleep(2)
		self.driver.find_element_by_id("content").click()
		time.sleep(2)
		self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.ImageView[2]").click()
		time.sleep(2)
		TouchAction(self.driver).press(x=150,y=80).release().perform()
		time.sleep(2)
		TouchAction(self.driver).press(x= 540, y=1600).release().perform()

	def test_032_me_changeAvatar_album(self):
		self.driver.find_element_by_id("personal_more_layout").click()
		self.driver.find_element_by_id("change_avatar").click()
		self.driver.find_element_by_id("photo_album_function").click()
		time.sleep(2)
		TouchAction(self.driver).press(x=300,y=400).release().perform()
		time.sleep(2)
		TouchAction(self.driver).press(x=800,y=400).release().perform()
		time.sleep(2)
		TouchAction(self.driver).press(x=150,y=80).release().perform()
		time.sleep(2)
		TouchAction(self.driver).press(x= 540, y=1600).release().perform()

	# def test_04_editProfile(self):
	# 	info1 = self.driver.find_element_by_id("personal_location").get_attribute("text")
	# 	self.driver.find_element_by_id("personal_more_layout").click()
	# 	self.driver.find_element_by_id("edit_detail").click()
	# 	self.driver.find_element_by_id("editorfinish").click()
	# 	gender = self.driver.find_element_by_id("profile_sex_edittext").get_attribute("text")
	# 	self.driver.find_element_by_id("profile_sex_edittext").click()
	# 	if gender == "M":
	# 		self.driver.find_element_by_id("sex_f").click()
	# 	else:
	# 		self.driver.find_element_by_id("sex_m").click()
	# 	self.driver.find_element_by_id("editorfinish").click()
	# 	info2 = self.driver.find_element_by_id("personal_location").get_attribute("text")
	# 	self.assertNotEqual(info1,info2)

	def test_05_group(self):
		self.driver.find_element_by_id("personal_more_layout").click()
		self.driver.find_element_by_id("group_setting").click()
		self.driver.find_element_by_id("newgroup").click()
		self.driver.find_element_by_id("edit_group").send_keys("new group")
		TouchAction(self.driver).press(x=1000,y=1700).release().perform()
		time.sleep(1)
		self.driver.find_element_by_id("dialog_confirm").click()
		time.sleep(1)
		TouchAction(self.driver).press(x=540,y=1600).move_to(x=0,y=-600).release().perform()
		groupName1 = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[10]/android.widget.RelativeLayout[1]/android.widget.TextView[1]").get_attribute("text")
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[10]").click()
		self.driver.find_element_by_id("dialog_confirm").click()
		groupName2 = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[10]/android.widget.RelativeLayout[1]/android.widget.TextView[1]").get_attribute("text")
		self.driver.find_element_by_id("back").click()
		self.assertNotEqual(groupName1,groupName2)
		
	def test_06_exit(self):
		self.driver.find_element_by_id("personal_more_layout").click()
		self.driver.find_element_by_id("exit").click()
		self.driver.find_element_by_id("account_back").click()

	def test_07_me_allWeibo(self):
		self.driver.find_element_by_id("all_weibo").click()
		self.driver.find_element_by_id("index_item_delete").click()
		self.driver.find_element_by_id("positive_button").click()
		
	def test_08_me_originalWeibo(self):
		self.driver.find_element_by_id("original_weibo").click()
		try:
			self.driver.find_element_by_id("index_retweeted_content_background")
		except:
			print "There's only original weibo found"
		self.driver.find_element_by_id("index_item_delete").click()
		self.driver.find_element_by_id("positive_button").click()

	def test_091_me_album_openWeibo(self):
		self.driver.find_element_by_id("album").click()
		self.driver.find_element_by_id("item_picture").click()
		status = self.driver.find_element_by_id("statusText")
		statusText = status.get_attribute("text")
		status.click()
		weiboText = self.driver.find_element_by_id("detail_status_content").get_attribute("text")
		self.driver.find_element_by_id("detail_title_goback").click()
		self.driver.find_element_by_id("single_image_back").click()
		self.driver.find_element_by_id("back").click()
		self.assertEqual(statusText,weiboText)

	def test_092_me_album_repost(self):
		self.driver.find_element_by_id("album").click()
		self.driver.find_element_by_id("item_picture").click()
		self.driver.find_element_by_id("single_image_options").click()
		self.driver.find_element_by_id("custom_item_view1").click()
		self.driver.find_element_by_id("compose_view_wrap").send_keys("test_09_me_album_repost")
		self.driver.find_element_by_id("send_ok").click()
		self.driver.find_element_by_id("single_image_back").click()
		self.driver.find_element_by_id("back").click()

	def test_093_me_album_save(self):
		self.driver.find_element_by_id("album").click()
		self.driver.find_element_by_id("item_picture").click()
		self.driver.find_element_by_id("single_image_options").click()
		self.driver.find_element_by_id("custom_item_view5").click()
		self.driver.find_element_by_id("single_image_back").click()
		self.driver.find_element_by_id("back").click()

	def test_094_me_album_identifyQR(self):
		self.driver.find_element_by_id("album").click()
		self.driver.find_element_by_id("item_picture").click()
		self.driver.find_element_by_id("single_image_options").click()
		self.driver.find_element_by_id("custom_item_view6").click()
		try:
			self.driver.find_element_by_id("negative_button").click()
		except:
			print "There's no QR code in the picture."
		self.driver.find_element_by_id("single_image_back").click()
		self.driver.find_element_by_id("back").click()

	def test_095_me_album_flicking(self):
		self.driver.find_element_by_id("album").click()
		self.driver.find_element_by_id("item_picture").click()
		i = random.randint(0,24)
		while i>=0:
			TouchAction(self.driver).press(x=720,y=800).move_to(x=-360,y=0).release().perform()
			time.sleep(1)
			TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-600).wait(1000).release().perform()
			i-=1
		self.driver.find_element_by_id("single_image_back").click()
		self.driver.find_element_by_id("back").click()

	def test_10_me_favorites(self):
		self.driver.find_element_by_id("favour").click()
		weibo1 = self.driver.find_element_by_id("index_item_weibo_content")
		weibo1Text = weibo1.get_attribute("text")
		weibo1.click()
		star = self.driver.find_element_by_id("detail_title_fav")
		star.click()
		self.assertFalse(star.is_selected())
		self.driver.find_element_by_id("detail_title_goback").click()
		self.driver.find_element_by_id("back").click()
		self.driver.find_element_by_id("favour").click()
		weibo2Text = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		self.driver.find_element_by_id("back").click()
		self.assertNotEqual(weibo1Text,weibo2Text)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Profile)
    unittest.TextTestRunner(verbosity=2).run(suite)