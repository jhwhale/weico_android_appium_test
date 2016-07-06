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
		# try:
		# 	self.driver.find_element_by_id("tab_icons_prof_layout").click()
		# 	self.driver.find_element_by_id("button_icon_setting").click()
		# 	time.sleep(2)
		# except:
		# 	time.sleep(2)
		time.sleep(2)

	def tearDown(self):
		time.sleep(3)
		
	def test_01_feedback(self):
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		self.driver.find_element_by_id("button_icon_setting").click()
		self.driver.find_element_by_id("setting_response").click()
		i = random.randint(1,4)
		qa = "feedback_qa"+str(i)
		self.driver.find_element_by_id(qa).click()
		self.driver.find_element_by_id("feedback_content").send_keys("Settings.test_01_feedback")
		self.driver.find_element_by_id("icon_back").click()
		self.driver.find_element_by_id("positive_button").click()
		self.driver.find_element_by_id("setting_response").click()
		self.driver.find_element_by_id("feedback_content").send_keys("This is a test.\n send by case  Settings.test_01_feedback")
		self.driver.find_element_by_id("feedback_send").click()
		self.driver.find_element_by_id("backImageView").click()

	def test_021_drafts_originalWeibo(self):
		self.driver.find_element_by_id("tab_icons_home_img").click()
		drafts = range(4)
		for d in drafts:
			self.driver.find_element_by_id("index_title_compose").click()
			self.composeWeibo("Settings.test_02_drafts.No."+str(d))
			self.driver.find_element_by_id("edit_cancel").click()
			self.driver.find_element_by_id("positive_button").click()
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		self.driver.find_element_by_id("button_icon_setting").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]").click()#select the first draft
		self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.TextView[1]").click()#edit
		self.driver.find_element_by_id("compose_view_wrap").send_keys(" I have edited the draft.")
		#添加照片
		self.driver.find_element_by_id("buttonCam").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]").click()
		time.sleep(2)
		self.driver.find_element_by_id("content").click()
		time.sleep(2)
		self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.ImageView[2]").click()
		self.driver.find_element_by_id("btn_next").click()
		#修改位置
		self.driver.find_element_by_id("textLocation").click()
		WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "title")))
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]").click()
		self.driver.find_element_by_id("send_ok").click() 
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]").click()#select the first draft
		self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.TextView[2]").click()#repost
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"draft_del")))
		self.driver.find_element_by_id("draft_del").click()#delete the first draft
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"draft_clean")))
		self.driver.find_element_by_id("draft_clean").click()#clean all drafts
		self.driver.find_element_by_id("positive_button").click()
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("backImageView").click()

	def test_022_drafts_repostedWeibo(self):
		self.driver.find_element_by_id("tab_icons_home_img").click()
		time.sleep(2)
		drafts = range(4)
		for d in drafts:
			self.driver.find_element_by_id("tab_icons_home_img").click()
			time.sleep(2)
			while True:
				try:
					self.driver.find_element_by_id("index_item_actions").click()
					break
				except:
					TouchAction(self.driver).press(x=500,y=800).move_to(x=0,y=-200).wait(1000).release().perform()
			self.driver.find_element_by_id("index_item_repost").click()
			self.driver.find_element_by_id("compose_view_wrap").send_keys("Settings.test_022_drafts_repostedWeibo.No."+str(d))
			self.driver.find_element_by_id("edit_cancel").click()
			time.sleep(1)
			self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[2]").click()
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		self.driver.find_element_by_id("button_icon_setting").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]").click()#select the first draft
		self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.TextView[1]").click()#edit
		self.driver.find_element_by_id("compose_view_wrap").send_keys(" I have edited the draft.")
		#同时转发评论
		sendComments = random.randint(0,1)
		if sendComments == 1:
			self.driver.find_element_by_id("textLocation").click()
		self.driver.find_element_by_id("send_ok").click()
		#repost draft
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]")))
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]").click()#select the first draft
		self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.TextView[2]").click()#repost
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"draft_del")))
		self.driver.find_element_by_id("draft_del").click()#delete the first draft
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"draft_clean")))
		self.driver.find_element_by_id("draft_clean").click()#clean all drafts
		self.driver.find_element_by_id("positive_button").click()
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("backImageView").click()

	def test_023_draft_comments(self):
		self.driver.find_element_by_id("tab_icons_home_img").click()
		time.sleep(2)
		drafts = range(4)
		for d in drafts:
			self.driver.find_element_by_id("tab_icons_home_img").click()
			time.sleep(2)
			while True:
				try:
					self.driver.find_element_by_id("index_item_actions").click()
					break
				except:
					TouchAction(self.driver).press(x=500,y=800).move_to(x=0,y=-200).wait(1000).release().perform()
			self.driver.find_element_by_id("index_item_comment").click()
			self.driver.find_element_by_id("compose_view_wrap").send_keys("Settings.test_023_draft_comments.No."+str(d))
			self.driver.find_element_by_id("edit_cancel").click()
			time.sleep(1)
			self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[2]").click()
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		self.driver.find_element_by_id("button_icon_setting").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]").click()#select the first draft
		self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.TextView[1]").click()#edit
		self.driver.find_element_by_id("compose_view_wrap").send_keys(" I have edited the draft.")
		#同时转发评论
		forwardComments = random.randint(0,1)
		if forwardComments == 1:
			self.driver.find_element_by_id("textLocation").click()
		self.driver.find_element_by_id("send_ok").click()
		#repost draft
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]")))
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]").click()#select the first draft
		self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.TextView[2]").click()#repost
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"draft_del")))
		self.driver.find_element_by_id("draft_del").click()#delete the first draft
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"draft_clean")))
		self.driver.find_element_by_id("draft_clean").click()#clean all drafts
		self.driver.find_element_by_id("positive_button").click()
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("backImageView").click()

	# def test_031_Notification_msgPush(self):
	# 	self.driver.find_element_by_id("tab_icons_prof_layout").click()
	# 	self.driver.find_element_by_id("button_icon_setting").click()
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]").click()#Notification
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()#msg push
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]").click()#msg settings
	# 	try:
	# 		self.driver.find_element_by_id("listView")#if found, msg push is off
	# 	except:
	# 		TouchAction(self.driver).press(x=540,y=1400).release().perform()#close msg setting
	# 	else:
	# 		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()#msg push
	# 	self.driver.find_element_by_id("backImageView").click()
	# 	self.driver.find_element_by_id("backImageView").click()

	# def test_032_Notification_msgSetting(self):
	# 	self.driver.find_element_by_id("tab_icons_prof_layout").click()
	# 	self.driver.find_element_by_id("button_icon_setting").click()
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]").click()#Notification
	# 	while True:
	# 		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]").click()#msg setting
	# 		try:
	# 			self.driver.find_element_by_id("pop_list")
	# 		except:
	# 			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()#msg push
	# 		else:
	# 			break
	# 	i = random.randint(1,4)
	# 	offSetting = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout["+str(i)+"]/android.widget.TextView[1]")
	# 	off = offSetting.get_attribute("text")
	# 	offSetting.click()
	# 	TouchAction(self.driver).press(x=540,y=1400).release().perform()
	# 	on = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]/android.widget.TextView[2]").get_attribute("text")
	# 	#recover
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]").click()
	# 	offSetting.click()
	# 	TouchAction(self.driver).press(x=540,y=1400).release().perform()
	# 	self.driver.find_element_by_id("backImageView").click()
	# 	self.driver.find_element_by_id("backImageView").click()
	# 	self.assertNotIn(off,on)
		
	# def test_033_Notification_msgSoundVibrate(self):
	# 	self.driver.find_element_by_id("tab_icons_prof_layout").click()
	# 	self.driver.find_element_by_id("button_icon_setting").click()
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]").click()#Notification
	# 	sound_triger = random.randint(0,3)
	# 	vibrate_triger = random.randint(0,3)
	# 	print sound_triger, vibrate_triger
	# 	while sound_triger>0:
	# 		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[3]/android.widget.ImageView[2]").click()
	# 		sound_triger-=1
	# 	while vibrate_triger>0:
	# 		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[4]/android.widget.ImageView[2]").click()
	# 		vibrate_triger-=1
	# 	self.driver.find_element_by_id("backImageView").click()
	# 	self.driver.find_element_by_id("backImageView").click()

	# # def test_04_account(self):
	# # 	self.driver.find_element_by_id("tab_icons_prof_layout").click()
	# # 	self.driver.find_element_by_id("button_icon_setting").click()
	# # 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[3]").click()
	# # 	try:
	# # 		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]").click()#if there're more than one accounts,change account, else add new
	# # 	except:
	# # 		self.driver.find_element_by_id("account_add").click()
	# # 		self.driver.find_element_by_id("sso_button").click()
	# # 		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.NAME,u"请用微博帐号登录")))
	# # 		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.widget.EditText[1]").send_keys("jhwhale@163.com")
	# # 		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.widget.EditText[2]").send_keys("testweico")
	# # 		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[3]").click()
	# # 	WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"tab_icons_prof_layout")))
	# # 	self.driver.find_element_by_id("tab_icons_prof_layout").click()
	# # 	self.driver.find_element_by_id("button_icon_setting").click()
	# # 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[3]").click()
	# # 	#delete account
	# # 	self.driver.find_element_by_id("account_edit").click()
	# # 	if self.driver.find_element_by_id("account_manager_name").get_attribute("text")==u"Test欧巴桑啦啦啦":
	# # 		self.driver.find_element_by_id("account_manager_delete").click()
	# # 	else:
	# # 		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]/android.widget.ImageView[2]").click()
	# # 	self.driver.find_element_by_id("positive_button").click()
	# # 	try:
	# # 		self.driver.find_element_by_id("account_back").click()
	# # 		self.driver.find_element_by_id("backImageView").click()
	# # 	except:
	# # 		pass

	# def test_05_theme(self):
	# 	self.driver.find_element_by_id("tab_icons_prof_layout").click()
	# 	self.driver.find_element_by_id("button_icon_setting").click()
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[4]").click()
	# 	#download new theme
	# 	self.driver.find_element_by_id("act_theme_store").click()
	# 	self.driver.find_element_by_id("item_theme_btn").click()
	# 	WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element((By.ID,"item_theme_btn"),u"使用"))
	# 	self.driver.find_element_by_id("item_theme_btn").click()
	# 	time.sleep(5)
	# 	try:
	# 		self.driver.find_element_by_id("positive_button").click()
	# 	except:
	# 		print "no need to share the theme."

	# def test_061_display_fontAndMargin(self):
	# 	self.driver.find_element_by_id("tab_icons_prof_layout").click()
	# 	self.driver.find_element_by_id("button_icon_setting").click()
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[5]").click()
	# 	font_large = random.randint(0,10)
	# 	font_small = random.randint(0,10)
	# 	margin_large = random.randint(0,23)
	# 	margin_small = random.randint(0,23)
	# 	while font_large>0:
	# 		self.driver.find_element_by_id("font_large").click()
	# 		font_large -=1
	# 		# if EC.is_alert_present():##################
	# 		# 	break
	# 	while font_small>0:
	# 		self.driver.find_element_by_id("font_small").click()
	# 		font_small -=1
	# 	while margin_large>0:
	# 		self.driver.find_element_by_id("margin_large").click()
	# 		margin_large -=1
	# 	while margin_small>0:
	# 		self.driver.find_element_by_id("margin_small").click()
	# 		margin_small -=1
	# 	self.driver.find_element_by_id("back").click()
	# 	self.driver.find_element_by_id("backImageView").click()

	# def test_062_display_hideImage(self):
	# 	self.driver.find_element_by_id("tab_icons_prof_layout").click()
	# 	self.driver.find_element_by_id("button_icon_setting").click()
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[5]").click()
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]").click()#no image shown
	# 	self.driver.find_element_by_id("back").click()
	# 	self.driver.find_element_by_id("backImageView").click()
	# 	self.driver.find_element_by_id("tab_icons_home_layout").click()
	# 	try:
	# 		self.driver.find_element_by_id("index_item_image_label")
	# 	except:
	# 		try:
	# 			self.driver.find_element_by_id("index_item_weibo_content_image")
	# 		except:
	# 			print "Cannot find image as expected."
	# 		else:
	# 			self.fail("There's image found in homepage.")

	# # def test_063_display_showUsername(self):
	# # 	self.driver.find_element_by_id("tab_icons_prof_layout").click()
	# # 	self.driver.find_element_by_id("button_icon_setting").click()
	# # 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[5]").click()
	# # 	while True:
	# # 		try:
	# # 			self.driver.find_element_by_id("show_username").click()
	# # 			break
	# # 		except:
	# # 			TouchAction(self.driver).press(x=540,y=1500).wait(1000).move_to(x=0,y=-45).release().perform()
	# 	# self.driver.find_element_by_id("back").click()
	# 	# self.driver.find_element_by_id("backImageView").click()
	# 	# self.driver.find_element_by_id("tab_icons_home_layout").click()
	# 	# title = self.driver.find_element_by_id("index_title_group").get_attribute("text")
	# 	# self.assertIn(title,("All",u"全部"))

	# # def test_064_display_showAvatar(self):
	# # 	self.driver.find_element_by_id("tab_icons_prof_layout").click()
	# # 	self.driver.find_element_by_id("button_icon_setting").click()
	# # 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[5]").click()
	# # 	while True:
	# # 		try:
	# # 			self.driver.find_element_by_id("show_userhead").click()
	# # 			break
	# # 		except:
	# # 			TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-30).release().perform()
	# # 	self.driver.find_element_by_id("back").click()
	# # 	self.driver.find_element_by_id("backImageView").click()
	# # 	self.driver.find_element_by_id("tab_icons_home_layout").click()
	# # 	try:
	# # 		self.driver.find_element_by_id("index_item_avatar")
	# # 	except:
	# # 		print "Cannot find avatar as expected."
	# # 	else:
	# # 		self.fail("Find avatar in timeline.")

	# def test_065_display_restore(self):
	# 	self.driver.find_element_by_id("tab_icons_prof_layout").click()
	# 	self.driver.find_element_by_id("button_icon_setting").click()
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[5]").click()
	# 	while True:
	# 		try:
	# 			self.driver.find_element_by_id("resore").click()
	# 		except:
	# 			TouchAction(self.driver).press(x=540,y=1500).move_to(x=0,y=-1000).release().perform()
	# 		else:
	# 			break
	# 	self.driver.find_element_by_id("back").click()
	# 	self.driver.find_element_by_id("backImageView").click()
	# 	self.driver.find_element_by_id("tab_icons_home_layout").click()
	# 	i = 3
	# 	while i>0:
	# 		try:
	# 			self.driver.find_element_by_id("index_item_weibo_content_image")
	# 			break
	# 		except:
	# 			TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-100).release().perform()
	# 			i -=1
	# 	if i<=0:
	# 		self.fail("Cannot find image, so display settings is not restored.")

	# def test_071_readHabit_order(self):
	# 	self.driver.find_element_by_id("tab_icons_prof_layout").click()
	# 	self.driver.find_element_by_id("button_icon_setting").click()
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[6]").click()#read habit
	# 	if self.driver.find_element_by_id("shun_xu_liu_lan_check").is_selected():
	# 		self.driver.find_element_by_id("ni_xu_liu_lan").click()
	# 	else:
	# 		self.driver.find_element_by_id("shun_xu_liu_lan").click()
	# 	self.driver.find_element_by_id("icon_back").click()
	# 	self.driver.find_element_by_id("backImageView").click()

	# # def test_072_readHabit_fullScreen(self):
	# # 	if not self.driver.find_element_by_id("quan_ping_yu_lan_check").is_selected():
	# # 		self.driver.find_element_by_id("quan_ping_yu_lan_check").click()
	# # 	self.driver.find_element_by_id("icon_back").click()
	# # 	self.driver.find_element_by_id("backImageView").click()
	# # 	self.driver.find_element_by_id("tab_icons_home_layout").click()
	# # 	time.sleep(2)
	# # 	TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-600).wait(1000).release().perform()
	# # 	time.sleep(2)
	# # 	TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-600).wait(1000).release().perform()
	# # 	try:
	# # 		self.driver.find_element_by_id("tab_bottom_widget")
	# # 	except:
	# # 		try:
	# # 			self.driver.find_element_by_id("home_title_layout")
	# # 		except:
	# # 			print "Homepage is in full screen mode."
	# # 		else:
	# # 			self.fail("Title bar still can be found in homepage.")
	# # 	else:
	# # 		self.fail("Bottom bar still can be found in homepage.")
	# # 	time.sleep(2)	
	# # 	TouchAction(self.driver).press(x=540,y=600).move_to(x=0,y=1200).wait(1000).release().perform()
	# # 	time.sleep(2)
	# # 	TouchAction(self.driver).press(x=540,y=600).move_to(x=0,y=1200).wait(1000).release().perform()
	# # 	self.driver.find_element_by_id("tab_icons_prof_layout").click()
	# # 	self.driver.find_element_by_id("button_icon_setting").click()
	# # 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[6]").click()
	# # 	self.driver.find_element_by_id("quan_ping_yu_lan_check").click()

	# def test_073_readHabit_itemNumber(self):
	# 	self.driver.find_element_by_id("tab_icons_prof_layout").click()
	# 	self.driver.find_element_by_id("button_icon_setting").click()
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[6]").click()#read habit
	# 	while True:
	# 		try:
	# 			self.driver.find_element_by_id("weibo_item_100")
	# 			break
	# 		except:
	# 			TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-1000).release().perform()
	# 	self.driver.find_element_by_id("weibo_item_20").click()
	# 	self.driver.find_element_by_id("weibo_item_50").click()
	# 	self.driver.find_element_by_id("weibo_item_100").click()
	# 	self.driver.find_element_by_id("icon_back").click()
	# 	self.driver.find_element_by_id("backImageView").click()

	# def test_074_readHabit_nightMode(self):
	# 	self.driver.find_element_by_id("tab_icons_prof_layout").click()
	# 	self.driver.find_element_by_id("button_icon_setting").click()
	# 	self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[6]").click()#read habit
	# 	while True:
	# 		try:
	# 			self.driver.find_element_by_id("night_mood_end")
	# 			break
	# 		except:
	# 			TouchAction(self.driver).press(x=540,y=1500).move_to(x=0,y=-1200).release().perform()
	# 	if not self.driver.find_element_by_id("night_mood_check").is_selected():
	# 		self.driver.find_element_by_id("night_mood_check").click()
	# 	self.driver.find_element_by_id("night_mood_start").click()
	# 	TouchAction(self.driver).press(x=400,y=1100).move_to(x=0,y=-500).release().perform()
	# 	TouchAction(self.driver).press(x=600,y=1100).move_to(x=0,y=-500).release().perform()
	# 	self.driver.find_element_by_id("button1").click()#ok
	# 	self.driver.find_element_by_id("night_mood_end").click()
	# 	TouchAction(self.driver).press(x=400,y=1100).move_to(x=0,y=-500).release().perform()
	# 	TouchAction(self.driver).press(x=600,y=1100).move_to(x=0,y=-500).release().perform()
	# 	self.driver.find_element_by_id("button1").click()#ok
	# 	self.driver.find_element_by_id("icon_back").click()
	# 	self.driver.find_element_by_id("backImageView").click()

	def test_08_sounds(self):
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		self.driver.find_element_by_id("button_icon_setting").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[7]").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[3]/android.widget.ImageView[2]").click()
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("backImageView").click()

	def test_09_imageQuality(self):
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		self.driver.find_element_by_id("button_icon_setting").click()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[8]").click()#quality of image uploaded
		i = random.randint(1,4)
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout["+str(i)+"]").click()
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("tab_icons_home_layout").click()
		self.driver.find_element_by_id("index_title_compose").click()
		self.composeWeibo("Settings.test_09_imageQuality")
		self.driver.find_element_by_id("send_ok").click()

	def test_10_QA(self):
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		self.driver.find_element_by_id("button_icon_setting").click()
		while True:
			if self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]").get_attribute("text") == "Q&A":
				self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]").click()#Q&A
				break
			else:
				TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-600).release().perform()
		self.driver.find_element_by_id("back").click()
		self.driver.find_element_by_id("backImageView").click()

	def test_11_aboutWeico(self):
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		self.driver.find_element_by_id("button_icon_setting").click()
		while True:
			if self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]/android.widget.TextView[1]").get_attribute("text") == "About Weico":
				self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[2]").click()#about weico
				break
			else:
				TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-600).release().perform()
		self.driver.find_element_by_id("about_weibo").click()#follow weico's weibo
		self.driver.find_element_by_id("back").click()
		self.driver.find_element_by_id("backImageView").click()

	def test_12_clearCache(self):
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		self.driver.find_element_by_id("button_icon_setting").click()
		while True:
			if self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[5]/android.widget.TextView[1]").get_attribute("text") == "Clear cache":
				self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[5]").click()#clear cache
				break
			else:
				TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-600).release().perform()
		self.driver.find_element_by_id("backImageView").click()

	def test_13_logout(self):
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		self.driver.find_element_by_id("button_icon_setting").click()
		while True:
			try:
				logout = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[6]/android.widget.RelativeLayout[1]/android.widget.TextView[1]")
			except:
				TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-600).release().perform()
			else:
				if logout.get_attribute("text") == "Log out":
					logout.click()
					self.driver.find_element_by_id("positive_button").click()
					break
				else:
					TouchAction(self.driver).press(x=540,y=1200).move_to(x=0,y=-600).release().perform()

		

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Settings)
    unittest.TextTestRunner(verbosity=2).run(suite)