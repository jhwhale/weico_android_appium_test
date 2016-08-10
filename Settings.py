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

class Settings(unittest.TestCase,BasicOperation):
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
			self.driver.find_element_by_id("button_icon_setting").click()
			time.sleep(2)
		except:
			time.sleep(2)


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
		
	def test_01_feedback(self):
		typeText = "Settings.test_01_feedback"
		self.driver.find_element_by_id("setting_response").click()
		questions = self.driver.find_elements(by ='id',value ='feedback_q')
		questions[random.randint(0,len(questions)-1)].click()
		answer = self.driver.find_element_by_id("feedback_a").get_attribute("text")
		textView = self.driver.find_element_by_id("feedback_content")
		textView.send_keys(typeText)
		self.driver.find_element_by_id("icon_back").click()
		self.driver.find_element_by_id("ed_btn_positive").click()
		self.driver.find_element_by_id("setting_response").click()
		draft = textView.get_attribute("text")
		textView.send_keys("This is a test.\n Sent by case: Settings.test_01_feedback")
		self.driver.find_element_by_id("feedback_send").click()
		self.assertGreater(len(answer),0)
		self.assertEqual(draft,typeText)


	def test_031_Notification_msg(self):
		allSettings = ['@Me','Comments','DM','New Follow']		
		self.driver.find_element_by_name("Notifications").click()
		msgSettings = self.driver.find_element_by_name("Message setting")
		msgSettings.click()
		try:
			self.driver.find_element_by_id("ed_list")
		except:
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()#msg push
			msgSettings.click()
		checkboxes = self.driver.find_elements(by = 'id',value ='ed_item_checkbox')
		for j in random.sample(range(len(checkboxes)),2):
			checkboxes[j].click()
		checkedSettings = []
		for i in range(len(checkboxes)):
			if checkboxes[i].get_attribute("checked")== "true":
				checkedSettings.append(allSettings[i])
		self.driver.back()
		enabledSettings = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]/android.widget.TextView[2]").get_attribute("text").split(',')
		if enabledSettings != ['']:
			self.assertEqual(enabledSettings,checkedSettings)
		else:
			self.assertEqual(checkedSettings,[])

		
	def test_032_Notification_msgSoundVibrate(self):		
		self.driver.find_element_by_name("Notifications").click()
		sound_triger = random.randint(1,2)
		vibrate_triger = random.randint(1,2)
		while sound_triger>0:
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[3]/android.widget.ImageView[2]").click()
			sound_triger-=1
		while vibrate_triger>0:
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[4]/android.widget.ImageView[2]").click()
			vibrate_triger-=1


	def test_04_account(self):		
		self.driver.find_element_by_name("Accounts").click()
		accounts1 = self.driver.find_elements(by='id',value='account_manager_name')
		if len(accounts1)>1:#if there're more than one accounts,change account, else add new
			accounts1[1].click()
		else:
			self.driver.find_element_by_id("account_add").click()
			self.driver.find_element_by_id("sso_button").click()
			WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.NAME,u"请用微博帐号登录")))
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.widget.EditText[1]").send_keys("jhwhale@163.com")
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.widget.EditText[2]").send_keys("testweico")
			self.driver.find_element_by_name(u"登录").click()
		#delete account
		while True:
			WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.ID,"tab_icons_prof_layout")))
			self.driver.find_element_by_id("tab_icons_prof_layout").click()
			self.driver.find_element_by_id("button_icon_setting").click()
			self.driver.find_element_by_name("Accounts").click()
			if self.driver.find_element_by_id("account_manager_name").get_attribute("text")!=u"Test怪蜀黍":
				self.driver.find_element_by_id("account_edit").click()
				self.driver.find_element_by_id("account_manager_delete").click()
				self.driver.find_element_by_id("ed_btn_positive").click()
			else:
				break

	def test_05_theme(self):
		self.driver.find_element_by_name("Themes").click()
		#download new theme
		self.driver.find_element_by_id("act_theme_store").click()
		self.driver.find_element_by_id("item_theme_btn").click()
		WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element((By.ID,"item_theme_btn"),u"使用"))
		self.driver.find_element_by_id("item_theme_btn").click()
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.NAME,"Share to your friends?")))
		self.driver.find_element_by_id("ed_btn_negative").click()
		
	def test_061_display_fontAndMargin(self):
		self.driver.find_element_by_name("Display").click()
		originalContentHeight = self.driver.find_element_by_id("content").size['height']
		originalNameHeight = self.driver.find_element_by_id("name_view").size['height']
		font_large = random.randint(0,8)
		font_small = random.randint(5,10)
		margin_large = random.randint(0,10)
		margin_small = random.randint(8,18)
		while font_large>0:
			self.driver.find_element_by_id("font_large").click()
			font_large -=1
		contentHeight1 = self.driver.find_element_by_id("content").size['height']
		nameHeight1 = self.driver.find_element_by_id("name_view").size['height']
		while font_small>0:
			self.driver.find_element_by_id("font_small").click()
			font_small -=1
		contentHeight2 = self.driver.find_element_by_id("content").size['height']
		nameHeight2 = self.driver.find_element_by_id("name_view").size['height']
		while margin_large>0:
			self.driver.find_element_by_id("margin_large").click()
			margin_large -=1
		contentHeight3 = self.driver.find_element_by_id("content").size['height']
		nameHeight3 = self.driver.find_element_by_id("name_view").size['height']
		while margin_small>0:
			self.driver.find_element_by_id("margin_small").click()
			margin_small -=1
		contentHeight4 = self.driver.find_element_by_id("content").size['height']
		nameHeight4 = self.driver.find_element_by_id("name_view").size['height']
		self.assertGreater(contentHeight1,originalContentHeight)
		self.assertGreater(nameHeight1,originalNameHeight)
		self.assertLess(contentHeight2,contentHeight1)
		self.assertLess(nameHeight2,nameHeight1)
		self.assertGreater(contentHeight3,contentHeight2)
		self.assertEqual(nameHeight3,nameHeight2)
		self.assertLess(contentHeight4,contentHeight3)
		self.assertEqual(nameHeight4,nameHeight3)


	def test_062_display_hideImage(self):	
		self.driver.find_element_by_name("Display").click()
		self.driver.find_element_by_name("No Image Shown").click()
		self.driver.find_element_by_id("back").click()
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("tab_icons_home_layout").click()
		while True:
			try:
				self.driver.find_element_by_id("index_item_weibo_content_image")
			except:
				try:
					self.driver.find_element_by_id("index_item_image_label")
				except:
					TouchAction(self.driver).press(x=500,y=1000).move_to(x=0,y=-200).release().perform()
					time.sleep(5)
				else:
					break
			else:
				self.fail("There's image found in homepage.")
		

	def test_064_display_showAvatar(self):
		self.driver.find_element_by_name("Display").click()
		for i in range(3):
			try:
				showAvatarBtn = self.driver.find_element_by_id("show_userhead")
				showAvatarBtn.click()
				showAvatarStatus = showAvatarBtn.get_attribute("checked")
				break
			except:
				TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-30).release().perform()
			if i == 2:
				self.skipTest("Cannot focus to show avatar checkbox.")
		self.driver.find_element_by_id("back").click()
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("tab_icons_home_layout").click()
		try:
			self.driver.find_element_by_id("index_item_avatar")
			if showAvatarStatus == False:
				self.fail("Cannot disable show avatar.")
		except:
			if showAvatarStatus == True:
				self.fail("Cannot enable show avatar.")

	def test_065_display_restore(self):	
		self.driver.find_element_by_name("Display").click()
		while True:
			try:
				self.driver.find_element_by_id("resore").click()
				break
			except:
				TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-1000).release().perform()				
		self.driver.find_element_by_id("back").click()
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("tab_icons_home_layout").click()
		i = 3
		while i>0:
			try:
				self.driver.find_element_by_id("index_item_weibo_content_image")
				break
			except:
				TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-100).release().perform()
				i -=1
		if i<=0:
			self.fail("Cannot find image, so display settings is not restored.")

	def test_071_readHabit_order(self):
		self.driver.find_element_by_name("Read Habit").click()#read habit
		if self.driver.find_element_by_id("shun_xu_liu_lan_check").is_selected():
			self.driver.find_element_by_id("ni_xu_liu_lan").click()
			self.assertTrue(self.driver.find_element_by_id("ni_xu_liu_lan_check").is_displayed())
			self.assertFalse(self.driver.find_element_by_id("shun_xu_liu_lan_check").is_displayed())
		else:
			self.driver.find_element_by_id("shun_xu_liu_lan").click()
			self.assertFalse(self.driver.find_element_by_id("ni_xu_liu_lan_check").is_displayed())
			self.assertTrue(self.driver.find_element_by_id("shun_xu_liu_lan_check").is_displayed())


	# # invalid case 通过滑动无法进入全屏
	# def test_072_readHabit_fullScreen(self):
	# 	self.driver.find_element_by_name("Read Habit").click()
	# 	if not self.driver.find_element_by_id("quan_ping_yu_lan_check").is_selected():
	# 		self.driver.find_element_by_id("quan_ping_yu_lan_check").click()
	# 	self.driver.find_element_by_id("icon_back").click()
	# 	self.driver.find_element_by_id("backImageView").click()
	# 	self.driver.find_element_by_id("tab_icons_home_layout").click()
	# 	time.sleep(2)
	# 	TouchAction(self.driver).press(x=540,y=1000).move_to(x=0,y=-600).wait(1000).release().perform()
	# 	time.sleep(2)
	# 	TouchAction(self.driver).press(x=540,y=1000).move_to(x=0,y=-600).wait(1000).release().perform()
	# 	try:
	# 		self.driver.find_element_by_id("tab_bottom_widget")
	# 	except:
	# 		try:
	# 			self.driver.find_element_by_id("home_title_layout")
	# 		except:
	# 			pass
	# 		else:
	# 			self.fail("Title bar still can be found in homepage.")
	# 	else:
	# 		self.fail("Bottom bar still can be found in homepage.")
	# 	time.sleep(2)	
	# 	TouchAction(self.driver).press(x=540,y=600).move_to(x=0,y=1200).wait(1000).release().perform()
	# 	time.sleep(2)
	# 	TouchAction(self.driver).press(x=540,y=600).move_to(x=0,y=1200).wait(1000).release().perform()
	# 	self.driver.find_element_by_id("tab_icons_prof_layout").click()
	# 	self.driver.find_element_by_id("button_icon_setting").click()
	# 	self.driver.find_element_by_name("Read Habit").click()
	# 	self.driver.find_element_by_id("quan_ping_yu_lan_check").click()

	def test_073_readHabit_itemNumber(self):
		self.driver.find_element_by_name("Read Habit").click()
		while True:
			try:
				self.driver.find_element_by_id("weibo_item_100")
				break
			except:
				TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-1000).release().perform()
		self.driver.find_element_by_id("weibo_item_20").click()
		self.driver.find_element_by_id("weibo_item_50").click()
		self.driver.find_element_by_id("weibo_item_100").click()


	def test_074_readHabit_nightMode(self):
		self.driver.find_element_by_name("Read Habit").click()
		while True:
			try:
				self.driver.find_element_by_id("night_mood_end")
				break
			except:
				TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-1000).release().perform()
		if not self.driver.find_element_by_id("night_mood_check").is_selected():
			self.driver.find_element_by_id("night_mood_check").click()
		self.driver.find_element_by_id("night_mood_start").click()
		try:
			self.driver.find_element_by_id("timePickerLayout")
			self.driver.find_element_by_id("button1").click()#ok
		except:
			self.fail("Cannot open start time picker.")
		self.driver.find_element_by_id("night_mood_end").click()
		try:
			self.driver.find_element_by_id("timePickerLayout")
			self.driver.find_element_by_id("button1").click()#ok
		except:
			self.fail("Cannot open start time picker.")
		
	# # invalid case
	# def test_08_sounds(self):
	# 	self.driver.find_element_by_name("Sounds").click()
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()#sound off
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]").click()
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[3]/android.widget.ImageView[2]").click()
	# 	self.driver.find_element_by_id("backImageView").click()
	# 	self.driver.find_element_by_id("backImageView").click()


	def test_09_imageQuality(self):	
		self.driver.find_element_by_name("Quality of image uploaded").click()
		i = random.randint(1,4)
		self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout["+str(i)+"]/android.widget.RadioButton[1]").click()
		

	def test_10_QA(self):
		for i in range(3):
			try:
				self.driver.find_element_by_name("Q&A").click()
				break
			except:
				TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-600).release().perform()
			if i ==2:
				self.fail("Cannot find Q&A.")
		try:
			self.driver.find_element_by_id("title")
			self.driver.find_element_by_name(u"问题：为什么关注和粉丝列表不全？")
		except:
			self.fail("Cannot open Q&A page.")

	def test_11_aboutWeico(self):
		for i in range(3):
			try:
				self.driver.find_element_by_name("About Weico").click()#about weico
				break
			except:
				TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-600).release().perform()
			if i ==2:
				self.fail("Cannot find About Weico.")
		self.driver.find_element_by_id("about_weibo").click()#follow weico's weibo
		self.driver.find_element_by_id("about_app").click()
		try:
			self.driver.find_element_by_name(u"Weico-最具人气的微博客户端")
			self.driver.find_element_by_name("Android")
			self.driver.find_element_by_name("iPhone / iPad")
		except:
			self.fail("Cannot open More Weico production.")

	def test_12_clearCache(self):
		for i in range(3):
			try:
				clearCache = self.driver.find_element_by_name("Clear cache")
				break
			except:
				TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-600).release().perform()
			if i == 2:
				self.fail("Cannot find Clear cache.")
		cache1 = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[6]/android.widget.TextView[2]").get_attribute("text")
		cacheNum1 = float(cache1[:-1])
		clearCache.click()
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.NAME,"Clear cache")))
		cache2 = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[6]/android.widget.TextView[2]").get_attribute("text")
		cacheNum2 = float(cache2[:-1])
		self.assertLess(cacheNum2,cacheNum1)

	def test_13_logout(self):
		for i in range(3):
			try:
				self.driver.find_element_by_name("Log out").click()
				break
			except:
				TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-600).release().perform()
				time.sleep(1)
			if i == 2:
				self.fail("Cannot find Log out button.")
		self.driver.find_element_by_id("ed_btn_negative").click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Settings)
    unittest.TextTestRunner(verbosity=2).run(suite)