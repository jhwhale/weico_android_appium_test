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

class Notify(unittest.TestCase,BasicOperation):
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
			self.driver.find_element_by_id("tab_icons_disc_layout").click()
			time.sleep(3)
		except:
			time.sleep(2)

	def tearDown(self):
		while True:
			try:
				self.driver.find_element_by_id("tab_icons_disc_layout")
				break
			except:
				self.driver.back()
				try:
					self.driver.find_element_by_id("ed_btn_negative").click()
				except:
					pass


	# def test_010_search(self):
	# 	self.driver.find_element_by_id("channel_head_search_layout").click()
	# 	self.driver.find_element_by_id("act_search_input").send_keys("weico")
	# 	TouchAction(self.driver).press(x=1000,y=1800).release().perform()#press search button on keyboard
	# 	time.sleep(2)
	# 	name = self.driver.find_element_by_id("searched_name_display").get_attribute("text")
	# 	content = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
	# 	pattern = re.compile("(W|w)eico")
	# 	self.assertTrue(pattern.search(content) != None)
	# 	self.assertTrue(pattern.search(name) != None)

	def test_011_deleteSearchHistory(self):
		self.driver.find_element_by_id("channel_head_search_layout").click()
		try:
			history1 = self.driver.find_element_by_id("search_history_text").get_attribute("text")
			self.driver.find_element_by_id("item_history_remove").click()
		except:
			self.skipTest("There's no search history.")
		try:
			history2 = self.driver.find_element_by_id("search_history_text").get_attribute("text")
			self.assertNotEqual(history1,history2,"Fail to delete the last search history.")
		except:
			pass

	def test_012_hotSearch(self):
		self.driver.find_element_by_id("channel_head_search_layout").click()
		hotSearch = self.driver.find_element_by_id("item_search_hot_left")
		hotSearchText = hotSearch.get_attribute("text")
		hotSearch.click()
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,'index_item_weibo_content')))
		content = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		if not self.isTwoStringSimilar(hotSearchText,content):
			self.fail("The search result is not relative with the keyword.")

	def test_013_hotSearchMore(self):
		self.driver.find_element_by_id("channel_head_search_layout").click()
		self.driver.find_element_by_id("act_search_hot_more").click()
		time.sleep(1)
		hotSearches = self.driver.find_elements(by ='id', value ='item_search_hot_text')
		hotSearch = hotSearches[random.randint(0,len(hotSearches)-1)]
		hotSearchText = hotSearch.get_attribute("text")
		hotSearch.click()
		time.sleep(5)
		content = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		if not self.isTwoStringSimilar(hotSearchText,content):
			self.fail("The search result is not relative with the keyword.")
		
	def test_014_showAllSearchHistory(self):
		self.driver.find_element_by_id("channel_head_search_layout").click()
		while True:
			try:
				self.driver.find_element_by_id("search_history_clear").click()#show all search history
				break
			except:
				leftSearches = self.driver.find_elements(by ='id', value ='item_search_hot_left')
				rightSearches = self.driver.find_elements(by ='id', value = 'item_search_hot_right')
				for i in [0,1]:
					leftSearches[i].click()
					self.driver.find_element_by_id("act_cancel_btn").click()
					self.driver.find_element_by_id("channel_head_search_layout").click()
					rightSearches[i].click()
					self.driver.find_element_by_id("act_cancel_btn").click()
					self.driver.find_element_by_id("channel_head_search_layout").click()

		TouchAction(self.driver).press(x=500,y=500).move_to(x=0,y=-100).release().perform()
		time.sleep(1)
		self.driver.find_element_by_id("search_history_clear").click()#clear all records
		try:
			self.driver.find_element_by_id("search_history_text")
		except:
			pass
		else:
			self.fail("Fail to clear all search records.")


	def test_02_scanQR(self):
		self.driver.find_element_by_id("channel_qr_code").click()
		try:
			self.driver.find_element_by_id("viewfinder_view")
			self.driver.find_element_by_id("status_view").click()
		except:
			self.fail("Cannot open QR code scanner.")

	# #会闪退
	# def test_03_nearbyWeibo(self):
	# 	self.driver.find_element_by_id("discovery_nearby").click()
	# 	WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"solt_layout")))
	# 	self.driver.find_element_by_id("location_textview")
	# 	self.driver.find_element_by_id("mapview")
	# 	self.driver.find_element_by_id("location_weibo")
	# 	self.driver.find_element_by_id("location_user")
	# 	self.driver.find_element_by_id("location_close").click()
	# #会闪退
	# def test_04_nearbyUser(self):
	# 	self.driver.find_element_by_id("discovery_nearby").click()
	# 	self.driver.find_element_by_id("location_user").click()
		
	def test_05_hotWeibo(self):
		self.driver.find_element_by_id("discovery_hot").click()
		self.driver.find_element_by_id("hot_category_slide_right_open").click()
		n = random.randint(1,24)
		m = random.randint(0,n)
		while n>0:
			i = random.randint(1,24)
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.TextView["+str(i)+"]").click()
			n -=1
		TouchAction(self.driver).press(x= 540, y=150).release().perform()
		while m>0:
			TouchAction(self.driver).press(x=800, y=800).move_to(x=-700,y=0).wait(1000).release().perform()
			m-=1
		time.sleep(2)
		TouchAction(self.driver).press(x=540,y=1600).move_to(x=0,y=-1000).wait(1000).release().perform()
		time.sleep(2)
		displayedCategoryNum = self.getElementNum("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.TextView[","]")
		for j in range(1,displayedCategoryNum+1):
			category = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.TextView["+str(j)+"]")
			if category.is_selected():
				currentCategory = category.get_attribute("text")
				break
		try:
			self.driver.find_element_by_id("index_item_weibo_content")
		except:
			msg = "There's no weibo in %s hot category." % currentCategory
			self.skipTest(msg)

	def test_060_hotTopic_join(self):
		for t in range(0,10):
			i = random.randint(1,3)
			topic = self.driver.find_element_by_id("discovery_topic_"+str(i))
			topicText = topic.get_attribute("text")
			topic.click()
			time.sleep(3)
			try:
				self.driver.find_element_by_id("tag_content_bg")
				break
			except:
				self.driver.find_element_by_id("backImageView").click()
			if t == 9:
				self.skipTest("Cannot load weibo in hot topic.")
		self.driver.find_element_by_id("join_topic_layout").click()
		self.composeWeibo("test_060_hotTopic_join")
		self.driver.find_element_by_id("send_ok").click()
		time.sleep(30)
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		time.sleep(2)
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		time.sleep(3)
		weiboText = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		self.assertIn(topicText,weiboText)

	def test_061_hotTopic_report(self):#举报。。
		for t in range(0,10):
			i = random.randint(1,3)
			topic = self.driver.find_element_by_id("discovery_topic_"+str(i))
			topicText = topic.get_attribute("text")
			topic.click()
			time.sleep(3)
			try:
				self.driver.find_element_by_id("tag_content_bg")
				break
			except:
				self.driver.find_element_by_id("backImageView").click()
			if t == 9:
				self.skipTest("Cannot load weibo in hot topic.")
		self.driver.find_element_by_id("tag_more").click()
		self.driver.find_element_by_name(u"举报").click()

	def test_062_hotTopic_fav(self):
		for t in range(0,10):
			i = random.randint(1,3)
			topic = self.driver.find_element_by_id("discovery_topic_"+str(i))
			topicText = topic.get_attribute("text")
			topic.click()
			time.sleep(3)
			try:
				self.driver.find_element_by_id("tag_content_bg")
				break
			except:
				self.driver.find_element_by_id("backImageView").click()
			if t == 9:
				self.skipTest("Cannot load weibo in hot topic.")
		self.driver.find_element_by_id("tag_more").click()
		self.driver.find_element_by_name(u"收藏").click()
		weibo_author = self.driver.find_element_by_id("tag_item_screen_name").get_attribute("text")
		weibo_content = self.driver.find_element_by_id("tag_item_weibo_content").get_attribute("text")
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		time.sleep(2)
		self.driver.find_element_by_id("favour").click()
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, "index_item_weibo_layout")))
		favorite_weibo_author = self.driver.find_element_by_id("index_item_screen_name").get_attribute("text")
		favorite_weibo_content = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		self.assertEqual(weibo_author, favorite_weibo_author, "The weibo author is not the same one.")
		self.assertEqual(weibo_content,favorite_weibo_content,"The weibo is not marked as favorite successfully.")

	def test_063_hotTopic_share(self):
		for t in range(0,10):
			i = random.randint(1,3)
			topic = self.driver.find_element_by_id("discovery_topic_"+str(i))
			topicText = topic.get_attribute("text")
			topic.click()
			time.sleep(3)
			try:
				self.driver.find_element_by_id("tag_content_bg")
				break
			except:
				self.driver.find_element_by_id("backImageView").click()
			if t == 9:
				self.skipTest("Cannot load weibo in hot topic.")
		author = self.driver.find_element_by_id("tag_item_screen_name").get_attribute("text")
		self.driver.find_element_by_id("tag_more").click()
		self.driver.find_element_by_name(u"分享").click()
		self.driver.find_element_by_id("share_img").click()#name = Sina Message
		self.driver.find_element_by_id("searchmessage_edittext").send_keys("test")
		self.driver.find_element_by_id("friends_item_avatar_mask").click()
		content = self.driver.find_element_by_id("msg_text").get_attribute("text")
		self.driver.find_element_by_id("send_layout").click()
		self.assertIn(author,content,"Fail to share the weibo in hot topic to friend by direct message.")

	def test_064_hotTopic_praise(self):
		for t in range(0,10):
			i = random.randint(1,3)
			topic = self.driver.find_element_by_id("discovery_topic_"+str(i))
			topicText = topic.get_attribute("text")
			topic.click()
			time.sleep(3)
			try:
				self.driver.find_element_by_id("tag_content_bg")
				break
			except:
				self.driver.find_element_by_id("backImageView").click()
			if t == 9:
				self.skipTest("Cannot load weibo in hot topic.")
		praiseButton = self.driver.find_element_by_id("tag_item_praise")
		praiseButton.click()
		self.assertTrue(praiseButton.is_selected())


	def test_065_hotTopic_repost(self):
		typeText = "test_065_hotTopic_repost"
		for t in range(0,10):
			i = random.randint(1,3)
			topic = self.driver.find_element_by_id("discovery_topic_"+str(i))
			topicText = topic.get_attribute("text")
			topic.click()
			time.sleep(3)
			try:
				self.driver.find_element_by_id("tag_content_bg")
				break
			except:
				self.driver.find_element_by_id("backImageView").click()
			if t == 9:
				self.skipTest("Cannot load weibo in hot topic.")
		self.driver.find_element_by_id("tag_item_repost").click()
		self.driver.find_element_by_id("compose_view_wrap").send_keys(typeText)
		#add pic
		self.driver.find_element_by_id("buttonCam").click()
		self.driver.find_element_by_id("albumPreview").click()
		self.driver.find_element_by_id("send_ok").click()
		self.driver.find_element_by_id("backImageView").click()
		time.sleep(15)
		#验证
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		time.sleep(1)
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"index_item_weibo_content")))
		content = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		self.assertIn(typeText,content)
		self.assertIn("http://",content,"Failed to add image to repost weibo.")

	def test_066_hotTopic_comment(self):
		typeText = "test_066_hotTopic_comment"
		for t in range(0,10):
			i = random.randint(1,3)
			topic = self.driver.find_element_by_id("discovery_topic_"+str(i))
			topicText = topic.get_attribute("text")
			topic.click()
			time.sleep(3)
			try:
				self.driver.find_element_by_id("tag_content_bg")
				break
			except:
				self.driver.find_element_by_id("backImageView").click()
			if t == 9:
				self.skipTest("Cannot load weibo in hot topic.")
		content = self.driver.find_element_by_id("tag_item_weibo_content").get_attribute("text")
		self.driver.find_element_by_id("tag_item_comment").click()
		time.sleep(2)
		self.composeComments(typeText)
		self.driver.find_element_by_id("send_ok").click()
		self.driver.find_element_by_id("backImageView").click()
		time.sleep(15)
		#验证
		self.driver.find_element_by_id("tab_icons_msg_layout").click()
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("tab_two").click()
		time.sleep(5)
		comment = self.driver.find_element_by_id("index_item_content").get_attribute("text").strip()
		retweetContent = self.driver.find_element_by_id("index_item_reweeted_content").get_attribute("text")
		self.assertIn(typeText,comment)
		self.assertIn(content,retweetContent)


	def test_07_allHotTopics(self):
		self.driver.find_element_by_id("discovery_topic_4").click()
		time.sleep(2)
		TouchAction(self.driver).press(x=500,y=800).move_to(x=0,y=-100).release().perform()
		i = random.randint(1,8)
		topicLink = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout["+str(i)+"]/android.widget.RelativeLayout[1]/android.widget.TextView[1]")
		topicText = topicLink.get_attribute("text")
		topicLink.click()
		title = self.driver.find_element_by_id("tag_timeline_title").get_attribute("text")
		self.assertIn(title,topicText)

	def test_080_hotVideo_fullscreen(self):
		self.driver.find_element_by_id("discovery_video_1").click()
		time.sleep(2)
		normalSize = self.driver.find_element_by_id("surface_container").size
		try:
			self.driver.find_element_by_id("fullscreen").click()
		except:
			self.driver.find_element_by_id("surface_container").click()
			self.driver.find_element_by_id("fullscreen").click()
		fullscreenSize = self.driver.find_element_by_id("surface_container").size
		self.assertGreater(fullscreenSize['width'],normalSize['width'])
		self.assertGreater(fullscreenSize['height'],normalSize['height'])

	def test_081_hotVideo_like(self):
		self.driver.find_element_by_id("discovery_video_2").click()
		time.sleep(3)
		likeBtn = self.driver.find_element_by_id("like_textview")
		dislikeBtn = self.driver.find_element_by_id("tread_textview")
		likeNumBefore = int(likeBtn.get_attribute("text"))
		likeBtn.click()
		likeNumAfter = int(likeBtn.get_attribute("text"))
		self.assertGreater(likeNumAfter,likeNumBefore,"Like button is invalid.")
		while True:
			try:
				self.driver.find_element_by_id("detail_like_nums").click()
				break
			except:
				TouchAction(self.driver).press(x=500,y=1200).move_to(x=0,y=-200).wait(1000).release().perform()
				time.sleep(2)
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"detail_item_screenname")))
		names = []
		itemNum = self.getElementNum("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[","]/android.widget.TextView[1]")
		for i in range(1,itemNum+1):
			nickname = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout["+str(i)+"]/android.widget.TextView[1]").get_attribute("text")
			names.append(nickname)
		#dislike
		dislikeNumBefore = int(dislikeBtn.get_attribute("text"))
		dislikeBtn.click()
		dislikeNumAfter = int(dislikeBtn.get_attribute("text"))
		likeNumAfterDislike = int(likeBtn.get_attribute("text"))
		self.assertGreater(dislikeNumAfter,dislikeNumBefore,"Dislike button is invalid.")
		self.assertIn(u"Test怪蜀黍", names)

	def test_082_hotVideo_autoPlay(self):
		self.driver.find_element_by_id("item_dsv_more").click()
		time.sleep(5)
		thumb1 = self.driver.find_elements(by='id', value="thumb")#only paused video has thumb
		thumbNum1 = len(thumb1)
		container1 = self.driver.find_elements(by='id',value='surface_container')
		containerNum1 = len(container1)
		#get status of auto play under wifi
		self.driver.back()
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		self.driver.find_element_by_id("button_icon_setting").click()
		self.driver.find_element_by_name("Read Habit").click()
		autoPlayBtn = self.driver.find_element_by_id("video_wifi_auto_play_check")
		autoPlayStatus1 = autoPlayBtn.is_selected()
		if autoPlayStatus1:
			self.assertLess(thumbNum1,containerNum1)
		else:
			self.assertEqual(thumbNum1,containerNum1)
		#切换自动播放开关
		autoPlayBtn.click()
		autoPlayStatus2 = autoPlayBtn.is_selected()
		#返回
		while True:
			try:
				self.driver.find_element_by_id("tab_icons_disc_layout").click()
				break
			except:
				self.driver.back()
		self.driver.find_element_by_id("item_dsv_more").click()
		time.sleep(5)
		thumb2 = self.driver.find_elements(by='id', value="thumb")
		thumbNum2 = len(thumb2)
		container2 = self.driver.find_elements(by='id',value='surface_container')
		containerNum2 = len(container2)
		if autoPlayStatus2:
			self.assertLess(thumbNum2,containerNum2)
		else:
			self.assertEqual(thumbNum2,containerNum2)

	def test_083_hotVideoList_fav(self):
		self.driver.find_element_by_id("item_dsv_more").click()
		# time.sleep(5)
		self.driver.find_element_by_id("item_more").click()
		self.driver.find_element_by_id("index_item_fav_del").click()
		#验证
		weibo_author = self.driver.find_element_by_id("item_author").get_attribute("text")
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		time.sleep(2)
		self.driver.find_element_by_id("favour").click()
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, "index_item_weibo_layout")))
		favorite_weibo_author = self.driver.find_element_by_id("index_item_screen_name").get_attribute("text")
		self.driver.find_element_by_id("back").click()
		self.assertEqual(weibo_author, favorite_weibo_author, "The weibo author is not the same one.")

	# invalid case
	# def test_084_hotVideoList_like(self):
	# 	self.driver.find_element_by_id("item_dsv_more").click()
	# 	# time.sleep(5)
	# 	self.driver.find_element_by_id("item_more").click()
	# 	self.driver.find_element_by_id("index_item_praise").click()
	# 	#验证
	# 	self.driver.find_element_by_id("item_source").click()
	# 	while True:
	# 		try:
	# 			self.driver.find_element_by_id("detail_like_nums").click()
	# 			break
	# 		except:
	# 			TouchAction(self.driver).press(x=500,y=1200).move_to(x=0,y=-200).wait(1000).release().perform()
	# 			time.sleep(2)
	# 	time.sleep(3)
	# 	TouchAction(self.driver).press(x=500,y=800).move_to(x=0,y=-100).release().perform()
	# 	likedOnes = self.driver.find_elements(by ='id', value ='detail_item_screenname')
	# 	names = []
	# 	for likedOne in likedOnes:
	# 		nickname = likedOne.get_attribute("text")
	# 		names.append(nickname)
	# 	self.assertIn(u"Test怪蜀黍", names)

	def test_085_hotVideoList_repost(self):
		typeText = "test_085_hotVideo_repost"
		self.driver.find_element_by_id("item_dsv_more").click()
		time.sleep(5)
		self.driver.find_element_by_id("item_more").click()
		self.driver.find_element_by_id("index_item_repost").click()
		self.driver.find_element_by_id("compose_view_wrap").send_keys(typeText)
		#add pic
		self.driver.find_element_by_id("buttonCam").click()
		self.driver.find_element_by_id("albumPreview").click()
		self.driver.find_element_by_id("send_ok").click()
		time.sleep(15)
		#验证
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		time.sleep(1)
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		time.sleep(3)
		content = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		self.assertIn(typeText,content,"The weibo is failed to send.")

	def test_086_hotVideoList_comment(self):
		typeText = "test_086_hotVideo_comment"
		self.driver.find_element_by_id("item_dsv_more").click()
		time.sleep(5)
		self.driver.find_element_by_id("item_more").click()
		self.driver.find_element_by_id("index_item_comment").click()
		self.driver.find_element_by_id("compose_view_wrap").send_keys(typeText)
		self.driver.find_element_by_id("buttonCam").click()
		self.driver.find_element_by_id("albumPreview").click()
		self.driver.find_element_by_id("send_ok").click()
		time.sleep(15)
		#验证
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("tab_icons_msg_layout").click()
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("tab_two").click()
		time.sleep(5)
		content = self.driver.find_element_by_id("index_item_content").get_attribute("text").strip()
		self.assertIn(typeText,content)


	def test_087_hotVideoList_fullscreen(self):
		self.driver.find_element_by_id("item_dsv_more").click()
		# time.sleep(5)
		normalSize = self.driver.find_element_by_id("surface_container").size
		try:
			self.driver.find_element_by_id("fullscreen").click()
		except:
			self.driver.find_element_by_id("surface_container").click()
			self.driver.find_element_by_id("fullscreen").click()
		fullscreenSize = self.driver.find_element_by_id("surface_container").size
		self.assertGreater(fullscreenSize['width'],normalSize['width'])
		self.assertGreater(fullscreenSize['height'],normalSize['height'])

	def test_088_hotVideo_refresh(self):
		for i in range(0,3):
			try:
				self.driver.find_element_by_id("item_dsv_change_ll")
				break
			except:
				TouchAction(self.driver).press(x=500,y=800).move_to(x=0,y=-80).wait(1000).release().perform()
			if i == 2:
				self.skipTest("Cannot find the refresh button.")
		videoName1 = self.driver.find_element_by_id("video_name").get_attribute("text")
		videoDetail1 = self.driver.find_element_by_id("video_detail").get_attribute("text")
		self.driver.find_element_by_id("item_dsv_change_ll").click()
		time.sleep(2)
		videoName2 = self.driver.find_element_by_id("video_name").get_attribute("text")
		videoDetail2 = self.driver.find_element_by_id("video_detail").get_attribute("text")
		self.assertNotEqual(videoName1,videoName2,"Fail to refresh the video in discovery page.")
		self.assertNotEqual(videoDetail1,videoDetail2,"Fail to refresh the video in discovery page.")



	def test_10_editChannels(self):
		for i in range(0,3):
			try:
				self.driver.find_element_by_id("channelEdit").click()
				break
			except:
				TouchAction(self.driver).press(x=500,y=800).move_to(x=0,y=-50).wait(1000).release().perform()
			if i == 2:
				self.skipTest("Cannot find edit channel button.")
		icons = self.driver.find_elements(by = 'id', value = 'imageView')
		index = random.sample(range(0,len(icons)),8)
		for idx in index:
			icons[idx].click()
		#sorting
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("closeBtn").click()
		channel1 = self.driver.find_element_by_id("textView").get_attribute("text")
		TouchAction(self.driver).long_press(x=154,y=563).move_to(x=800,y=1000).release().perform()
		channel2 = self.driver.find_element_by_id("textView").get_attribute("text")
		self.driver.find_element_by_id("save_channels").click()
		print channel1,channel2
		firstChannel = self.driver.find_element_by_id("textView").get_attribute("text")
		self.assertNotEqual(channel2,firstChannel)

	def test_11_unsubscribeChannel(self):
		while True:
			try:
				chn = self.driver.find_element_by_id("textView")
				break
			except:
				TouchAction(self.driver).press(x=540,y=1600).move_to(x=0,y=-100).release().perform()
		chn_text = chn.get_attribute("text")
		chn.click()
		# chn_title = self.driver.find_element_by_id("channel_title_group").get_attribute("text")
		self.driver.find_element_by_id("channel_unsubscribe").click()
		time.sleep(1)
		self.driver.find_element_by_id("tab_icons_disc_layout").click()
		time.sleep(3)
		TouchAction(self.driver).press(x=540,y=1600).move_to(x=0,y=-100).release().perform()
		subscribedChns = self.driver.find_elements(by = 'id',value = 'textView')
		subscribedChnsText = []
		for i in range(0,len(subscribedChns)):
			subscribedChnsText.append(subscribedChns[i].get_attribute("text"))
		self.assertNotIn(chn_text,subscribedChnsText,"Fail to unsubscribe the channel %s" % chn_text)
	

	def test_12_recommendedApps(self):
		for i in range(0,3):
			try:
				self.driver.find_element_by_id("weico_app_recommend_container")
				self.driver.find_element_by_id("weico_app_recommend_text")
				break
			except:
				TouchAction(self.driver).press(x=540,y=1600).move_to(x=0,y=-600).release().perform()
			if i == 2:
				self.fail("There's no recommended app.")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Notify)
    unittest.TextTestRunner(verbosity=2).run(suite)			