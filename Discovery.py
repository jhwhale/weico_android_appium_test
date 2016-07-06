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
			time.sleep(2)
		except:
			time.sleep(2)

	def tearDown(self):
		time.sleep(3)

	def test_01_search(self):
		self.driver.find_element_by_id("channel_head_search_layout").click()
		self.driver.find_element_by_id("search_edittext").send_keys("weico")
		self.driver.find_element_by_id("search_goback").click()
		content = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		self.driver.find_element_by_id("search_title_goback").click()
		pattern = re.compile("(W|w)eico")
		self.assertTrue(pattern.search(content) != None)

	def test_02_scanQR(self):
		self.driver.find_element_by_id("channel_qr_code").click()
		self.driver.find_element_by_id("viewfinder_view")
		self.driver.find_element_by_id("status_view").click()

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
		self.driver.find_element_by_id("detail_title_goback").click()

	def test_060_hotTopic_join(self):
		while True:
			i = random.randint(1,3)
			topic = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.LinearLayout["+str(i)+"]/android.widget.TextView[1]")
			topicText = topic.get_attribute("text")
			topic.click()
			try:
				self.driver.find_element_by_id("tag_content_bg")
				break
			except:
				self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("join_topic_layout").click()
		self.composeWeibo("test_06_hotTopic")
		self.driver.find_element_by_id("send_ok").click()
		time.sleep(10)
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		time.sleep(2)
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, "index_item_weibo_content")))
		weiboText = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		#print "topic is %s, weibo is %s"%(topicText,weiboText)
		self.assertIn(topicText,weiboText)

	def test_061_hotTopic_report(self):
		while True:
			i = random.randint(1,3)
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.LinearLayout["+str(i)+"]/android.widget.TextView[1]").click()
			try:
				self.driver.find_element_by_id("tag_content_bg")
				break
			except:
				self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("tag_more").click()
		self.driver.find_element_by_id("repot_tag").click()
		self.driver.find_element_by_id("backImageView").click()

	def test_062_hotTopic_fav(self):
		while True:
			i = random.randint(1,3)
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.LinearLayout["+str(i)+"]/android.widget.TextView[1]").click()
			try:
				self.driver.find_element_by_id("tag_content_bg")
				break
			except:
				self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("tag_more").click()
		self.driver.find_element_by_id("favour_tag").click()
		weibo_author = self.driver.find_element_by_id("tag_item_screen_name").get_attribute("text")
		weibo_content = self.driver.find_element_by_id("tag_item_weibo_content").get_attribute("text")
		#print weibo_author,weibo_content
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		time.sleep(2)
		self.driver.find_element_by_id("favour").click()
		WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, "index_item_weibo_layout")))
		favorite_weibo_author = self.driver.find_element_by_id("index_item_screen_name").get_attribute("text")
		favorite_weibo_content = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		print favorite_weibo_author, favorite_weibo_content
		self.driver.find_element_by_id("back").click()
		self.assertEqual(weibo_author, favorite_weibo_author, "The weibo author is not the same one.")
		self.assertEqual(weibo_content,favorite_weibo_content,"The weibo is not marked as favorite successfully.")

	def test_063_hotTopic_share(self):
		while True:
			i = random.randint(1,3)
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.LinearLayout["+str(i)+"]/android.widget.TextView[1]").click()
			try:
				self.driver.find_element_by_id("tag_content_bg")
				break
			except:
				self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("tag_more").click()
		self.driver.find_element_by_id("share_tag").click()
		self.driver.find_element_by_xpath("//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
		self.driver.find_element_by_id("searchmessage_edittext").send_keys("test")
		self.driver.find_element_by_id("friends_item_avatar_mask").click()
		self.driver.find_element_by_id("send_layout").click()
		self.driver.find_element_by_id("detail_title_goback").click()
		self.driver.find_element_by_id("dm_user_title_goback").click()
		self.driver.find_element_by_id("backImageView").click()

	def test_064_hotTopic_praise(self):
		while True:
			i = random.randint(1,3)
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.LinearLayout["+str(i)+"]/android.widget.TextView[1]").click()
			try:
				self.driver.find_element_by_id("tag_content_bg")
				break
			except:
				self.driver.find_element_by_id("backImageView").click()
		praiseButton = self.driver.find_element_by_id("tag_item_praise")
		praiseButton.click()
		self.assertTrue(praiseButton.is_selected())
		self.driver.find_element_by_id("backImageView").click()

	def test_065_hotTopic_repost(self):
		while True:
			i = random.randint(1,3)
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.LinearLayout["+str(i)+"]/android.widget.TextView[1]").click()
			try:
				self.driver.find_element_by_id("tag_content_bg")
				break
			except:
				self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("tag_item_repost").click()
		self.driver.find_element_by_id("compose_view_wrap").send_keys("test_06_hotTopic_repost")
		self.driver.find_element_by_id("send_ok").click()
		self.driver.find_element_by_id("backImageView").click()

	def test_066_hotTopic_comment(self):
		while True:
			i = random.randint(1,3)
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.LinearLayout["+str(i)+"]/android.widget.TextView[1]").click()
			try:
				self.driver.find_element_by_id("tag_content_bg")
				break
			except:
				self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("tag_item_comment").click()
		self.composeComments("test_06_hotTopic_comment")
		self.driver.find_element_by_id("send_ok").click()
		self.driver.find_element_by_id("backImageView").click()

	def test_07_allHotTopics(self):
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.LinearLayout[4]/android.widget.TextView[1]").click()
		i = random.randint(1,8)
		topicLink = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout["+str(i)+"]/android.widget.RelativeLayout[1]/android.widget.TextView[1]")
		topicText = topicLink.get_attribute("text")
		topicLink.click()
		title = self.driver.find_element_by_id("tag_timeline_title").get_attribute("text")
		self.assertIn(title,topicText)
		self.driver.find_element_by_id("backImageView").click()
		self.driver.find_element_by_id("back").click()

	def test_08_recommendedUser(self):
		i = random.randint(1,5)
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[3]/android.widget.AdapterView[1]/android.widget.LinearLayout["+str(i)+"]/android.widget.ImageView[1]").click()
		self.driver.find_element_by_id("add_follow").click()
		try:
			self.driver.find_element_by_id("add_ok").click()
		except:
			self.driver.find_element_by_id("dialog_confirm").click()
		self.driver.find_element_by_id("back").click()


	def test_09_moreRecommendedUser(self):
		self.driver.find_element_by_id("channel_more").click()
		WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.ID,"friends_item_screen_name")))
		TouchAction(self.driver).press(x=540,y=1600).move_to(x=0,y=-200).release().perform()
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[3]").click()
		self.driver.find_element_by_id("add_follow").click()
		try:
			self.driver.find_element_by_id("add_ok").click()
		except:
			try:
				self.driver.find_element_by_id("dialog_confirm").click()
			except:#黑名单中的用户无法添加好友
				pass
		self.driver.find_element_by_id("back").click()
		self.driver.find_element_by_id("back").click()

	def test_10_editChannels(self):
		self.driver.find_element_by_id("channelEdit").click()
		s = random.randint(0,16)
		while s > 0:
			t = random.randint(1,16)
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout["+str(t)+"]/android.widget.ImageView[1]").click()
			s -= 1
		TouchAction(self.driver).press(x = 540, y = 1600).move_to(x=0,y=-600).release().perform()
		r = random.randint(13,14)
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout["+str(r)+"]/android.widget.ImageView[1]").click()
		#sorting
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("closeBtn").click()
		channel1 = self.driver.find_element_by_id("textView").get_attribute("text")
		TouchAction(self.driver).long_press(x=154,y=563).move_to(x=800,y=1000).release().perform()
		channel2 = self.driver.find_element_by_id("textView").get_attribute("text")
		self.driver.find_element_by_id("save_channels").click()
		print channel1,channel2
		self.assertNotEqual(channel2,channel1)

	def test_11_unsubscribeChannel(self):
		TouchAction(self.driver).press(x=540,y=1600).move_to(x=0,y=-600).release().perform()
		while True:
			i = random.randint(1,20)
			try:
				chn = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.GridView[1]/android.widget.RelativeLayout["+str(i)+"]")
			except:
				continue
			else:
				chn_text = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.GridView[1]/android.widget.RelativeLayout["+str(i)+"]/android.widget.TextView[1]").get_attribute("text")
				chn.click()
				if chn_text == "Apps" or chn_text == u"应用推荐":
					self.driver.find_element_by_id("actionbar_home_left").click()
					continue
				elif chn_text == "More" or chn_text == u"更多":
					self.driver.find_element_by_id("save_channels").click()
					continue
				else:
					chn_title = self.driver.find_element_by_id("channel_title_group").get_attribute("text")
					self.driver.find_element_by_id("channel_unsubscribe").click()
					chn_text2 = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.GridView[1]/android.widget.RelativeLayout["+str(i)+"]/android.widget.TextView[1]").get_attribute("text")
					self.assertEqual(chn_text,chn_title)
					self.assertNotEqual(chn_title,chn_text2)
				break

	def test_12_recommendedApps(self):
		TouchAction(self.driver).press(x=540,y=1600).move_to(x=0,y=-600).release().perform()
		self.driver.find_element_by_id("discovery_rec_app_icon").click()
		self.driver.find_element_by_id("header_exit").click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Notify)
    unittest.TextTestRunner(verbosity=2).run(suite)			