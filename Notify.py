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
		time.sleep(3)

	def test_011_atMeWeibo_delete(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		weibo1 = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		try:
			self.driver.find_element_by_id("index_item_delete").click()
			self.driver.find_element_by_id("positive_button").click()
		except:
			self.skipTest("Cannot delete this weibo.")
		weibo2 = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		self.assertNotEqual(weibo1,weibo2)

	def test_012_atMeWeibo_avatar(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		try:
			self.driver.find_element_by_id("index_item_delete")
		except:
			name1 = self.driver.find_element_by_id("index_item_screen_name").get_attribute("text")
			self.driver.find_element_by_id("index_item_avatar").click()
			name2 = self.driver.find_element_by_id("title_name").get_attribute("text")
			self.driver.find_element_by_id("back").click()
			self.assertEqual(name1,name2)
		else:
			self.skipTest("Cannot open profile by clicking avatar")

	def test_013_atMeWeibo_detail(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		weibo1 = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		self.driver.find_element_by_id("index_item_weibo_content").click()
		weibo2 = self.driver.find_element_by_id("detail_status_content").get_attribute("text")
		self.driver.find_element_by_id("detail_title_goback").click()
		self.assertEqual(weibo2,weibo1)

	def test_014_atMeWeibo_fav(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		self.driver.find_element_by_id("index_item_actions").click()
		self.driver.find_element_by_id("index_item_fav_del").click()
		weibo1 = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		self.driver.find_element_by_id("tab_icons_prof_layout").click()
		self.driver.find_element_by_id("favour").click()
		weibo2 = self.driver.find_element_by_id("index_item_weibo_content").get_attribute("text")
		self.driver.find_element_by_id("back").click()
		self.assertEqual(weibo1,weibo2)

	def test_015_atMeWeibo_praise(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		self.driver.find_element_by_id("index_item_actions").click()
		self.driver.find_element_by_id("index_item_praise").click()

	def test_016_atMeWeibo_repost(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		self.driver.find_element_by_id("index_item_actions").click()
		self.driver.find_element_by_id("index_item_repost").click()
		self.driver.find_element_by_id("compose_view_wrap").send_keys("test_016_atMeWeibo_repost")
		self.driver.find_element_by_id("send_ok").click()

	def test_017_atMeWeibo_comment(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		self.driver.find_element_by_id("index_item_actions").click()
		self.driver.find_element_by_id("index_item_comment").click()
		self.composeComments("test_017_atMeWeibo_comment")
		self.driver.find_element_by_id("send_ok").click()

	def test_02_atMeOriginal(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_mid").click()
		try:
			self.driver.find_element_by_id("index_item_weibo_content")
		except:
			self.skipTest("There's not any original weibo which @ed me")
		else:
			try:
				self.driver.find_element_by_id("index_retweeted_content_background")
			except:
				print "There's only original weibo."
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
		name1 = self.driver.find_element_by_id("index_item_screen_name").get_attribute("text")#name1 id?
		self.driver.find_element_by_id("index_item_rightlayout").click()
		self.driver.find_element_by_id("search_profile").click()
		name2 = self.driver.find_element_by_id("title_name").get_attribute("text")
		self.driver.find_element_by_id("back").click()
		self.assertEqual(name1,name2)

	def test_033_atMeComment_viewWeibo(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("index_item_rightlayout").click()
		self.driver.find_element_by_id("search_status").click()
		self.driver.find_element_by_id("detail_title_goback").click()

	def test_034_atMeComment_reply(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("index_item_rightlayout").click()
		self.driver.find_element_by_id("reply_comment").click()
		self.composeComments("test_034_atMeComment_reply")
		self.driver.find_element_by_id("send_ok").click()

	def test_035_atMeComment_quickReply(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("index_item_comment").click()
		self.composeComments("test_035_atMeComment_quickReply")
		self.driver.find_element_by_id("send_ok").click()

	def test_036_atMeComment_delete(self):
		self.driver.find_element_by_id("msg_at_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		try:
			comment1 = self.driver.find_element_by_id("index_item_content").get_attribute("text")
			self.driver.find_element_by_id("timeline_item_bg").click()
			self.driver.find_element_by_id("delete_comment").click()
			self.driver.find_element_by_id("positive_button").click()
			comment2 = self.driver.find_element_by_id("index_item_content").get_attribute("text")
			self.assertNotEqual(comment1,comment2)
		except:
			TouchAction(self.driver).press(x=100,y=100).release().perform()
			self.skipTest("Cannot delete this comment")

	def test_041_commentFollowing_avatar(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		#click avatar
		self.driver.find_element_by_id("comment_item_avatar").click()
		self.driver.find_element_by_id("back").click()

	def test_042_commentFollowing_viewProfile(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		#view profile
		self.driver.find_element_by_id("index_item_rightlayout").click()
		self.driver.find_element_by_id("search_profile").click()
		self.driver.find_element_by_id("back").click()

	def test_043_commentFollowing_viewWeibo(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		self.driver.find_element_by_id("index_item_rightlayout").click()
		self.driver.find_element_by_id("search_status").click()
		self.driver.find_element_by_id("detail_title_goback").click()

	def test_044_commentFollowing_reply(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		self.driver.find_element_by_id("index_item_rightlayout").click()
		self.driver.find_element_by_id("reply_comment").click()
		self.composeComments("test_044_commentFollowing_reply")
		self.driver.find_element_by_id("send_ok").click()

	def test_045_commentFollowing_quickReply(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_one").click()
		self.driver.find_element_by_id("index_item_comment").click()
		self.composeComments("test_04_commentFollowing")
		self.driver.find_element_by_id("send_ok").click()

	def test_051_commentMine_avatar(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("comment_item_avatar").click()
		self.driver.find_element_by_id("back").click()

	def test_052_commentMine_viewProfile(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("index_item_rightlayout").click()
		self.driver.find_element_by_id("search_profile").click()
		self.driver.find_element_by_id("back").click()

	def test_053_commentMine_viewWeibo(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("index_item_rightlayout").click()
		self.driver.find_element_by_id("search_status").click()
		self.driver.find_element_by_id("detail_title_goback").click()

	def test_054_commentMine_reply(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("index_item_rightlayout").click()
		self.driver.find_element_by_id("reply_comment").click()
		self.composeComments("test_054_commentMine_reply")
		self.driver.find_element_by_id("send_ok").click()

	def test_055_commentMine_quickReply(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("index_item_comment").click()
		self.composeComments("test_055_commentMine_quickReply")
		self.driver.find_element_by_id("send_ok").click()

	def test_056_commentMine_delete(self):
		self.driver.find_element_by_id("msg_cmt_btn").click()
		self.driver.find_element_by_id("tab_two").click()
		self.driver.find_element_by_id("index_item_rightlayout").click()
		self.driver.find_element_by_id("delete_comment").click()
		self.driver.find_element_by_id("positive_button").click()
			
	def test_06_DMNew(self):
		self.driver.find_element_by_id("msg_dm_btn").click()
		self.driver.find_element_by_id("write_message").click()
		self.driver.find_element_by_id("searchmessage_edittext").send_keys("test")
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.eico.weico.lib.swipeweico.SlidingPaneLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]").click()
		self.sendDM("test_06_DMNew")
		self.driver.find_element_by_id("detail_title_goback").click()
		self.driver.find_element_by_id("dm_user_title_goback").click()

	def test_071_DMStranger_avatar(self):
		self.driver.find_element_by_id("msg_dm_btn").click()
		self.driver.find_element_by_id("board_message").click()
		try:
			self.driver.find_element_by_id("directmessage_item_avatar").click()
			self.driver.find_element_by_id("back").click()
		except:
			self.skipTest("There's no stranger's direct message.")
		self.driver.find_element_by_id("stranger_dm_title_goback").click()

	def test_072_DMStranger_reply(self):
		self.driver.find_element_by_id("msg_dm_btn").click()
		self.driver.find_element_by_id("board_message").click()
		try:
			self.driver.find_element_by_id("directmessage_item_text").click()
			self.sendDM("test_072_DMStranger_reply")
			self.driver.find_element_by_id("detail_title_goback").click()
		except:
			self.skipTest("There's no stranger's direct message.")
		self.driver.find_element_by_id("stranger_dm_title_goback").click()

	def test_081_DM(self):
		self.driver.find_element_by_id("msg_dm_btn").click()
		self.driver.find_element_by_id("directmessage_item_screen_name").click()
		self.sendDM("test_08_DM")
		try:
			self.driver.find_element_by_id("msg_img").click()
			self.driver.find_element_by_id("single_image_back").click()
		except:
			print "Cannot find any image"
		self.driver.find_element_by_id("detail_title_goback").click()

	def test_082_DM_clearConversation(self):
		self.driver.find_element_by_id("msg_dm_btn").click()
		firstConversation = self.driver.find_element_by_id("directmessage_item_screen_name")
		name1 = firstConversation.get_attribute("text")
		firstConversation.click()
		self.driver.find_element_by_id("detail_title_more").click()
		self.driver.find_element_by_xpath("//android.widget.ListView[1]/android.widget.TextView[2]").click()
		self.driver.find_element_by_id("positive_button").click()
		time.sleep(2)
		name2 = firstConversation.get_attribute("text")
		self.assertNotEqual(name2,name1)

	def test_083_DM_kickToBlacklist(self):
		self.driver.find_element_by_id("msg_dm_btn").click()
		self.driver.find_element_by_id("directmessage_item_screen_name").click()
		self.driver.find_element_by_id("detail_title_more").click()
		self.driver.find_element_by_xpath("//android.widget.ListView[1]/android.widget.TextView[1]").click()
		self.driver.find_element_by_id("positive_button").click()
		self.driver.find_element_by_id("detail_title_goback").click()
		self.driver.find_element_by_id("directmessage_item_avatar").click()
		follow_status1 = self.driver.find_element_by_id("add_follow").get_attribute("text")
		self.driver.find_element_by_id("add_follow").click()
		follow_status2 = self.driver.find_element_by_id("add_follow").get_attribute("text")
		self.driver.find_element_by_id("back").click()
		self.assertEqual(follow_status1,follow_status2)

	def test_084_DM_clearConversationFromList(self):
		self.driver.find_element_by_id("msg_dm_btn").click()
		conversation = self.driver.find_element_by_id("directmessage_item_screen_name")
		TouchAction(self.driver).long_press(conversation).wait(1000).perform()
		self.driver.find_element_by_xpath("//android.widget.ListView[1]/android.widget.TextView[2]").click()
		self.driver.find_element_by_id("positive_button").click()

	def test_085_DM_kickToBlacklistFromList(self):
		self.driver.find_element_by_id("msg_dm_btn").click()
		conversation = self.driver.find_element_by_id("directmessage_item_screen_name")
		TouchAction(self.driver).long_press(conversation).wait(1000).perform()
		self.driver.find_element_by_xpath("//android.widget.ListView[1]/android.widget.TextView[1]").click()
		self.driver.find_element_by_id("positive_button").click()
		self.driver.find_element_by_id("directmessage_item_avatar").click()
		follow_status1 = self.driver.find_element_by_id("add_follow").get_attribute("text")
		self.driver.find_element_by_id("add_follow").click()
		follow_status2 = self.driver.find_element_by_id("add_follow").get_attribute("text")
		self.driver.find_element_by_id("back").click()
		self.assertEqual(follow_status1,follow_status2)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Notify)
    unittest.TextTestRunner(verbosity=2).run(suite)			