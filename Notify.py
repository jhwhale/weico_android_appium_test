#coding=utf-8
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time, unittest, sys, os, random
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
			self.driver.find_element_by_id("tab_icons_msg_layout").click()
			time.sleep(2)
		except:
			time.sleep(2)

	def tearDown(self):
		while True:
			try:
				self.driver.find_element_by_id("tab_icons_msg_layout")
				break
			except:
				self.driver.back()

	def test_010_checkAt(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		time.sleep(2)
		for i in range(0,2):
			TouchAction(self.driver).press(x=500,y=1200).move_to(x=0,y=-100).wait(1000).release().perform()
			time.sleep(2)
			content = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
			print content
			self.assertIn(u"@Test怪蜀黍",content,"The weibo doesn't @me.")
				
	def test_011_atMeWeibo_delete(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		weibo1 = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		i = 5
		while i>=0:
			if i != 0:
				try:
					self.driver.find_element_by_id("index_item_delete").click()
					self.driver.find_element_by_id("ed_btn_positive").click()
					break
				except:
					TouchAction(self.driver).press(x=500,y=1200).move_to(x=0,y=-100).wait(1000).release().perform()
					i -= 1
					time.sleep(2)
			else:
				self.skipTest("Cannot delete this weibo.")
		weibo2 = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		self.assertNotEqual(weibo1,weibo2)



	def test_013_atMeWeibo_detail(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		weibo1 = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		self.driver.find_element_by_id("index_item_created_at").click()
		weibo2 = self.driver.find_element_by_id("detail_status_content").get_attribute("text")
		self.assertEqual(weibo2,weibo1)

	def test_014_atMeWeibo_fav(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		TouchAction(self.driver).press(x=500,y=1200).move_to(x=0,y=-100).wait(1000).release().perform()
		i = 3
		while i>=0:
			try:
				self.driver.find_element_by_id("index_item_actions").click()
				self.driver.find_element_by_id("index_item_fav_del").click()
				self.driver.find_element_by_id("index_item_source").click()
				weibo1 = self.driver.find_element_by_id("detail_status_content").get_attribute("text")
				self.driver.back()
				break
			except:
				TouchAction(self.driver).press(x=500,y=1200).move_to(x=0,y=-100).wait(1000).release().perform()
				i -=1
			if i == 0:
				self.skipTest("Cannot add weibo to favour list.")
				break
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		self.driver.find_element_by_id("favour").click()
		weibo2 = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		self.assertEqual(weibo1,weibo2,"Fail to add weibo which @Me to favourite.")

	def test_015_atMeWeibo_like(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		self.driver.find_element_by_id("index_item_actions").click()
		self.driver.find_element_by_id("index_item_praise").click()
		self.driver.find_element_by_id("index_item_source").click()
		time.sleep(2)
		TouchAction(self.driver).press(x=500,y=800).move_to(x=0,y=-200).release().perform()
		self.driver.find_element_by_id("detail_like_nums").click()
		time.sleep(1)
		names = []
		for i in range(2,8):
			try:
				nickname = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout["+str(i)+"]/android.widget.TextView[1]").get_attribute("text")
			except:
				break
			names.append(nickname)
		self.assertIn(u"Test怪蜀黍", names, "Cannot find current account in liked list.")

	def test_016_atMeWeibo_repost(self):
		typeText = "test_016_atMeWeibo_repost"
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		self.driver.find_element_by_id("index_item_actions").click()
		self.driver.find_element_by_id("index_item_repost").click()
		self.driver.find_element_by_id("compose_view_wrap").send_keys(typeText)
		#add pic
		self.driver.find_element_by_id("buttonCam").click()
		self.driver.find_element_by_id("albumPreview").click()
		self.driver.find_element_by_id("send_ok").click()
		#验证
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		time.sleep(1)
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		time.sleep(3)
		content = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		self.assertIn(typeText,content,"The weibo is failed to send.")
		self.assertIn("http://",content,"Failed to add image to repost weibo.")

	def test_017_atMeWeibo_comment(self):
		typeText ="test_017_atMeWeibo_comment"
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		self.driver.find_element_by_id("index_item_actions").click()
		self.driver.find_element_by_id("index_item_comment").click()
		self.composeComments(typeText)
		self.driver.find_element_by_id("send_ok").click()
		#验证
		self.driver.find_element_by_id("tab_icons_msg_layout").click()
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		time.sleep(1)
		self.driver.find_element_by_id("tab_two").click()
		time.sleep(5)
		content = self.driver.find_element_by_id("index_item_content").get_attribute("text").strip()
		self.assertIn(typeText,content,"Failed to add comments from @Me.")
		self.assertTrue(self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[3]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").is_displayed(),"Cannot find the image comment.")


	def test_02_atMeOriginal(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_mid").click()
		for i in range(0,3):
			try:
				self.driver.find_element_by_id("index_retweeted_content_background")
			except:
				TouchAction(self.driver).press(x=500,y=1200).move_to(x=0,y=-100).wait(1000).release().perform()
			else:
				self.fail("Retweeted weibo is found.")

	def test_031_atMeComment_avatar(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		name1 = self.driver.find_element_by_id("index_item_screen_name").get_attribute("text")#name1 id?
		self.driver.find_element_by_id("comment_item_avatar").click()
		name2 = self.driver.find_element_by_id("title_name").get_attribute("text")
		self.driver.find_element_by_id("back").click()
		self.assertEqual(name1,name2)

	def test_032_atMeComment_viewProfile(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		name1 = self.driver.find_element_by_id("index_item_screen_name").get_attribute("text")
		self.driver.find_element_by_id("index_item_time").click()
		self.driver.find_element_by_name("View profile").click()
		name2 = self.driver.find_element_by_id("title_name").get_attribute("text")
		self.assertEqual(name1,name2)

	def test_033_atMeComment_viewWeibo(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		content1 = self.driver.find_element_by_id("index_item_reweeted_content").get_attribute("text")
		self.driver.find_element_by_id("index_item_time").click()
		self.driver.find_element_by_name("View weibo").click()
		content2 = self.driver.find_element_by_id("detail_status_content").get_attribute("text")
		self.assertIn(content2,content1,"Fail to view the weibo in detail page.")

	def test_034_atMeComment_reply(self):
		typeText = "test_034_atMeComment_reply"
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("index_item_time").click()
		self.driver.find_element_by_name("Reply").click()
		self.composeComments(typeText)
		self.driver.find_element_by_id("send_ok").click()
		#验证
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		time.sleep(1)
		self.driver.find_element_by_id("tab_two").click()
		time.sleep(5)
		content = self.driver.find_element_by_id("index_item_content").get_attribute("text").strip()
		self.assertIn(typeText,content,"Failed to reply comment which @Me.")
		self.assertTrue(self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[3]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").is_displayed(),"Cannot find the image comment.")

	def test_035_atMeComment_quickReply(self):
		typeText = "test_035_atMeComment_quickReply"
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("index_item_comment").click()
		self.composeComments(typeText)
		self.driver.find_element_by_id("send_ok").click()
		#验证
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		time.sleep(1)
		self.driver.find_element_by_id("tab_two").click()
		time.sleep(5)
		content = self.driver.find_element_by_id("index_item_content").get_attribute("text").strip()
		self.assertIn(typeText,content,"Failed to reply comment which @Me.")
		self.assertTrue(self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[3]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").is_displayed(),"Cannot find the image comment.")

	def test_036_atMeComment_delete(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		try:
			comment1 = self.driver.find_element_by_id("index_item_content").get_attribute("text")
			self.driver.find_element_by_id("index_item_time").click()
			self.driver.find_element_by_name("Delete").click()
			self.driver.find_element_by_id("ed_btn_positive").click()
			comment2 = self.driver.find_element_by_id("index_item_content").get_attribute("text")
			self.assertNotEqual(comment1,comment2)
		except:
			# TouchAction(self.driver).press(x=100,y=100).release().perform()
			self.skipTest("Cannot delete this comment")

	def test_041_commentFollowing_avatar(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		name1 = self.driver.find_element_by_id("index_item_screen_name").get_attribute("text")
		self.driver.find_element_by_id("comment_item_avatar").click()
		name2 = self.driver.find_element_by_id("title_name").get_attribute("text")
		self.assertEqual(name1,name2)

	def test_042_commentFollowing_viewProfile(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		name1 = self.driver.find_element_by_id("index_item_screen_name").get_attribute("text")
		self.driver.find_element_by_id("index_item_time").click()
		self.driver.find_element_by_name("View profile").click()
		time.sleep(1)
		name2 = self.driver.find_element_by_id("title_name").get_attribute("text")
		self.assertEqual(name1,name2,"Fail to view profile of comment.")

	def test_043_commentFollowing_viewWeibo(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		name1 = self.driver.find_element_by_id("index_item_screen_name").get_attribute("text")
		self.driver.find_element_by_id("index_item_time").click()
		self.driver.find_element_by_name("View weibo").click()
		name2 = self.driver.find_element_by_id("detail_name").get_attribute("text")
		self.assertEqual(name1,name2)

	def test_044_commentFollowing_reply(self):
		typeText = "test_044_commentFollowing_reply"
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		self.driver.find_element_by_id("index_item_time").click()
		self.driver.find_element_by_name("Reply").click()
		self.composeComments(typeText)
		self.driver.find_element_by_id("send_ok").click()
		#验证
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		time.sleep(1)
		self.driver.find_element_by_id("tab_two").click()
		time.sleep(5)
		content = self.driver.find_element_by_id("index_item_content").get_attribute("text").strip()
		self.assertIn(typeText,content,"Failed to reply received comment.")
		self.assertTrue(self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[3]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").is_displayed(),"Cannot find the image comment.")

	def test_045_commentFollowing_quickReply(self):
		typeText = "test_04_commentFollowing"
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		self.driver.find_element_by_id("index_item_comment").click()
		self.composeComments(typeText)
		self.driver.find_element_by_id("send_ok").click()
		#验证
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		time.sleep(1)
		self.driver.find_element_by_id("tab_two").click()
		time.sleep(5)
		content = self.driver.find_element_by_id("index_item_content").get_attribute("text").strip()
		self.assertIn(typeText,content,"Failed to quick reply received comment.")
		self.assertTrue(self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[3]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").is_displayed(),"Cannot find the image comment.")

	def test_051_commentMine_avatar(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("comment_item_avatar").click()
		name = self.driver.find_element_by_id("title_name").get_attribute("text")
		self.assertEqual(u"Test怪蜀黍",name,"The comment is not sent by current account.")

	def test_052_commentMine_viewProfile(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		name1 = self.driver.find_element_by_id("index_item_screen_name").get_attribute("text")
		self.driver.find_element_by_id("index_item_time").click()
		self.driver.find_element_by_name("View profile").click()
		name2 = self.driver.find_element_by_id("title_name").get_attribute("text")
		self.assertEqual(name1,name2,"Fail to view profile of comment.")

	def test_053_commentMine_viewWeibo(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("index_item_time").click()
		self.driver.find_element_by_name("View weibo").click()
		try:
			self.driver.find_element_by_id("detail_status_layout")
		except:
			self.fail("Cannot open weibo from my comment list.")

	def test_054_commentMine_reply(self):
		typeText = "test_054_commentMine_reply"
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("index_item_rightlayout").click()
		self.driver.find_element_by_name("Reply").click()
		self.composeComments(typeText)
		self.driver.find_element_by_id("send_ok").click()
		#验证
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		time.sleep(1)
		self.driver.find_element_by_id("tab_two").click()
		time.sleep(5)
		content = self.driver.find_element_by_id("index_item_content").get_attribute("text").strip()
		self.assertIn(typeText,content,"Failed to reply received comment.")
		self.assertTrue(self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[3]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").is_displayed(),"Cannot find the image comment.")

	def test_055_commentMine_quickReply(self):
		typeText = "test_055_commentMine_quickReply"
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("index_item_comment").click()
		self.composeComments(typeText)
		self.driver.find_element_by_id("send_ok").click()
		#验证
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		time.sleep(1)
		self.driver.find_element_by_id("tab_two").click()
		time.sleep(5)
		content = self.driver.find_element_by_id("index_item_content").get_attribute("text").strip()
		self.assertIn(typeText,content,"Failed to quick reply received comment.")
		self.assertTrue(self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[3]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").is_displayed(),"Cannot find the image comment.")

	def test_056_commentMine_delete(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		comment1 = self.driver.find_element_by_id("index_item_content").get_attribute("text")
		self.driver.find_element_by_id("index_item_time").click()
		self.driver.find_element_by_name("Delete").click()
		self.driver.find_element_by_id("ed_btn_positive").click()
		comment2 = self.driver.find_element_by_id("index_item_content").get_attribute("text")
		self.assertNotEqual(comment1,comment2,"Fail to delete sent comment.")

	def test_06_like(self):
		self.driver.find_element_by_id("msg_like_btn").click()
		content = self.driver.find_element_by_id("praised_item_type_content").get_attribute("text")
		# weibo = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]"
		comment = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[3]/android.widget.TextView[1]"
		if content == "Like weibo":
			try:
				self.driver.find_element_by_xpath(comment)
			except:
				pass
			else:
				self.fail("Find comment when liked weibo.")
		else:
			try:
				self.driver.find_element_by_xpath(comment)
			except:
				self.fail("Cannot find comment when liked comment.")

	def test_070_DMNew(self):
		message = "test_070_DMNew"
		self.driver.find_element_by_id("msg_dm_btn").click()
		self.driver.find_element_by_id("write_message").click()
		self.driver.find_element_by_id("searchmessage_edittext").send_keys("test")
		self.driver.find_element_by_id("friends_screen_name").click()
		self.sendDM(message)
		self.driver.find_element_by_id("detail_title_goback").click()
		self.driver.find_element_by_id("dm_user_title_goback").click()
		self.driver.find_element_by_id("msg_dm_btn").click()
		time.sleep(2)
		msg = self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.TextView[3]").get_attribute("text")
		try:
			self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.SlidingPaneLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[3]")
		except:
			self.fail("Cannot find the image sent by direct message.")
		# finally:
		# 	#clear conversation
		# 	self.driver.find_element_by_id("detail_title_more").click()
		# 	self.driver.find_element_by_name("Clear conversation").click()
		# 	self.driver.find_element_by_id("ed_btn_positive").click()
		self.assertIn(message,msg,"Fail to send direct message.")


	def test_071_DMStranger_avatar(self):
		self.driver.find_element_by_id("msg_dm_btn").click()
		self.driver.find_element_by_id("board_message").click()
		name1 = self.driver.find_element_by_id("directmessage_item_screen_name").get_attribute("text")
		try:
			self.driver.find_element_by_id("directmessage_item_avatar").click()
		except:
			self.skipTest("There's no stranger's direct message.")
		name2 = self.driver.find_element_by_id("title_name").get_attribute("text")
		self.assertIn(name2,name1)

	def test_072_DMStranger_reply(self):
		message = "test_072_DMStranger_reply"
		self.driver.find_element_by_id("msg_dm_btn").click()
		self.driver.find_element_by_id("board_message").click()
		try:
			self.driver.find_element_by_id("directmessage_item_text").click()
		except:
			self.skipTest("There's no stranger's direct message.")
		self.sendDM(message)
		# msg = self.driver.find_element_by_id("msg_content").get_attribute("text")
		try:
			self.driver.find_element_by_id("msg_img")
		except:
			self.fail("Cannot find the image sent by direct message.")
		# finally:
		# 	#clear conversation
		# 	self.driver.find_element_by_id("detail_title_more").click()
		# 	self.driver.find_element_by_name("Clear conversation").click()
		# 	self.driver.find_element_by_id("ed_btn_positive").click()
		# self.assertIn(message,msg,"Fail to reply direct message from stranger.")

	def test_081_DM(self):
		message = "test_08_DM"
		self.driver.find_element_by_id("msg_dm_btn").click()
		self.driver.find_element_by_id("directmessage_item_screen_name").click()
		self.sendDM(message)
		self.driver.find_element_by_id("detail_title_goback").click()
		self.driver.find_element_by_id("msg_dm_btn").click()
		time.sleep(2)
		msg = self.driver.find_element_by_id("directmessage_item_text").get_attribute("text")
		self.assertIn(message,msg)

	def test_082_DM_clearConversation(self):
		self.driver.find_element_by_id("msg_dm_btn").click()
		firstConversation = self.driver.find_element_by_id("directmessage_item_screen_name")
		name1 = firstConversation.get_attribute("text")
		firstConversation.click()
		self.driver.find_element_by_id("detail_title_more").click()
		self.driver.find_element_by_name("Clear conversation").click()
		self.driver.find_element_by_id("ed_btn_positive").click()
		time.sleep(2)
		name2 = firstConversation.get_attribute("text")
		self.assertNotEqual(name2,name1)

	def test_083_DM_kickToBlacklist(self):
		self.driver.find_element_by_id("msg_dm_btn").click()
		self.driver.find_element_by_id("directmessage_item_screen_name").click()
		self.driver.find_element_by_id("detail_title_more").click()
		self.driver.find_element_by_name("To blacklist").click()
		self.driver.find_element_by_id("ed_btn_positive").click()
		self.driver.find_element_by_id("detail_title_goback").click()
		self.driver.find_element_by_id("directmessage_item_avatar").click()
		follow_status1 = self.driver.find_element_by_id("add_follow").get_attribute("text")
		self.driver.find_element_by_id("add_follow").click()
		follow_status2 = self.driver.find_element_by_id("add_follow").get_attribute("text")
		self.assertEqual(follow_status1,follow_status2)

	def test_084_DM_clearConversationFromList(self):
		self.driver.find_element_by_id("msg_dm_btn").click()
		conversation = self.driver.find_element_by_id("directmessage_item_screen_name")
		name1 = conversation.get_attribute("text")
		TouchAction(self.driver).long_press(conversation).wait(1000).perform()
		self.driver.find_element_by_name("Clear conversation").click()
		self.driver.find_element_by_id("ed_btn_positive").click()
		name2 = conversation.get_attribute("text")
		self.assertNotEqual(name1,name2)

	def test_085_DM_kickToBlacklistFromList(self):
		self.driver.find_element_by_id("msg_dm_btn").click()
		conversation = self.driver.find_element_by_id("directmessage_item_screen_name")
		TouchAction(self.driver).long_press(conversation).wait(1000).perform()
		self.driver.find_element_by_name("To blacklist").click()
		self.driver.find_element_by_id("ed_btn_positive").click()
		self.driver.find_element_by_id("directmessage_item_avatar").click()
		follow_status1 = self.driver.find_element_by_id("add_follow").get_attribute("text")
		self.driver.find_element_by_id("add_follow").click()
		follow_status2 = self.driver.find_element_by_id("add_follow").get_attribute("text")
		self.assertEqual(follow_status1,follow_status2)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Notify)
    unittest.TextTestRunner(verbosity=2).run(suite)			