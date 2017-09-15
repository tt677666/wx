#!/usr/bin/env python
# coding:utf8
import sys
reload(sys)
sys.setdefaultencoding( "utf8" )

import itchat

from itchat.content import *
from itchat import *

import threading,time,requests,ConfigParser,os,pickle,shelve


conf = ConfigParser.ConfigParser()
conf.read("wx.conf")
conf.add_section("new_section")
conf.set("new_section", "start_flag", "stop")
conf.set("new_section", "reserve_time", "60")
conf.write(open("wx.conf","w"))

qun_name = u'微信群聊test'
qun_id = ''



#日志记录模块
def logg(log_str):
	with open('log.txt','a') as f:
		f.write(time.strftime('%Y-%m-%d_%H-%M-%S')+' '+log_str+'\n\r')

		
#按照长度2切割下注的号码		
def cut_num(num):
	tmp_list = []
	tmp1_list = []
	#长度判断，必为偶数
	if len(num)%2 != 0:
		return False
	#循环按照长度切割
	while len(num)>0:
		tmp_list.append(num[:2])
		num = num[2:]
	for k in tmp_list:
		#重复判断
		tmp1_list = tmp_list
		tmp1_list.remove(k)
		for l in tmp1_list:
			if k == l:
				return False
			else :
				pass
		try:
			k = int(k)
			#抓换为整数后范围判断
			if k >20 or k < 1:
				return false
		except:
			return False
	
	return True
		
		
#检测用户发送的投注格式是否正确
def format_check(user_msg):
	rule_num = user_msg.split(' ')[2]
	lottle_num = user_msg.split(' ')[3]
	if rule_num == 'a1':
		if len(lottle_num) == 2 and  cut_num(lottle_num) = True:
			return True
		else:
			return False
	if rule_num == 'b1':
		if len(lottle_num) == 4 and  cut_num(lottle_num) = True:
			return True
		else:
			return False
	if rule_num == 'c1' or rule_num == 'z1' or rule_num == 'z2':
		if len(lottle_num) == 6 and  cut_num(lottle_num) = True:
			return True
		else:
			return False
	if rule_num == 'd1':
		if len(lottle_num) == 8 and  cut_num(lottle_num) = True:
			return True
		else:
			return False
	if rule_num == 'e1':
		if len(lottle_num) == 10 and  cut_num(lottle_num) = True:
			return True
		else:
			return False
	if rule_num == 'f1' or rule_num == 'f2':
		if len(lottle_num) == 12 and  cut_num(lottle_num) = True:
			return True
		else:
			return False
	if rule_num == 'g1' or rule_num == 'g2' or rule_num == 'g3':
		if len(lottle_num) == 14 and  cut_num(lottle_num) = True:
			return True
		else:
			return False
	if rule_num == 'h1' or rule_num == 'h2' or rule_num == 'h3'  or rule_num == 'h4':
		if len(lottle_num) == 16 and  cut_num(lottle_num) = True:
			return True
		else:
			return False
	else:
		return False

#获取消息后判断用户是否存在于用户积分表(dict方式)中
def user_money(user_name):

	try:
		f = shelve.open('user.db','c')
		if f.has_key[user_name]:
			pass
		else:
			f[user_name] = 0
	finally:
		f.close()


#检测聊天记录是否以"touzhu"开头,如果是则将消息检测后存入"lottle_order.txt"表(文本),并将消息计入日志
def check_order(usr,content):
	if content.split(' ')[0] == 'touzhu':
		if format_check(content) == True:
			with open ('lottle_order.txt','a') as f:
				f.write(usr+ ' ' +content + '\n')
		else:
			print 'format wrong'
			
		
	
def init_data():

	global qun_id,qun_name
	itchat.auto_login(False)
	chatrooms = itchat.get_chatrooms(update=True, contactOnly=True)
	for k in chatrooms:
		if k['NickName'] == qun_name:
			qun_id = k['UserName']

			
			
	chatroom_ids = [c['UserName'] for c in chatrooms]
	#print chatroom_ids
	#print '正在监测的群聊：', len(chatrooms), '个'
	print ' '.join([item['NickName'] for item in chatrooms])


def network_time(ts):
	ltime= time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
	ttime=time.localtime(time.mktime(ltime)+8*60*60)
	dat="%u-%02u-%02u"%(ttime.tm_year,ttime.tm_mon,ttime.tm_mday)
	tm="%02u:%02u:%02u"%(ttime.tm_hour,ttime.tm_min,ttime.tm_sec)
	return dat + ' ' + tm

def convert2timestamp(a):
	timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
	timeStamp = int(time.mktime(timeArray)) 
	return timeStamp



# 自动回复文本等类别的群聊消息
# isGroupChat=True表示为群聊消息
@itchat.msg_register([TEXT, SHARING], isGroupChat=True)
def group_reply_text(msg):
	# 消息来自于哪个群聊
	chatroom_id = msg['FromUserName']
	# 发送者的昵称
	username = msg['ActualNickName']

	# 消息并不是来自于需要同步的群
	if not chatroom_id in chatroom_ids:
		return

	if msg['Type'] == TEXT:
		content = msg['Content']
	elif msg['Type'] == SHARING:
		content = msg['Text']

	# 根据消息类型转发至其他需要同步消息的群聊
	if msg['Type'] == TEXT:
		for item in chatrooms:
			if item['UserName'] == chatroom_id:
				user_money(username)
				check_order(username,msg['Content'])
				print (username, msg['Content']), item['UserName']
				#itchat.send('%s\n%s' % (username, msg['Content']), item['UserName'])


def reply():
	itchat.run()

def kaijiang(qun_id):
	result_tmp = ''
	while True:
		while True:
			try:
				r = requests.post('http://sxhb.ws1.zs-zc.net/api/AwardNum/LottAwardInfoList',{'lott': '07', 'page': '1'})
				result = r.json()[0]['RaffleNumber']
				result_time_hour = int(r.json()[0]['CreateTime'].split(' ')[1].split(':')[0])
				result_time_min = int(r.json()[0]['CreateTime'].split(' ')[1].split(':')[1])
				
				break
			except:
				print 'connection  failed'
				time.sleep(2)

		# 取开奖时间的小时和分钟值，如果晚于21:50,则证明本日投注结束
		if result_time_hour == 21 and result_time_min >= 50:
			print u'非投注时间范围'
		else:
			print u'投注时间范围'
			if result_tmp != result:
				#itchat.send('%s\n%s\n%s\n%s' % (u'======== 开奖结果========',r.json()[0]['CreateTime'], r.json()[0]['IssueName'],result), qun_id)
				#开始统计上轮中奖结果（需要reply线程记录上轮的投注消息）
				#告诉reply线程开始响应下轮投注消息
				time.sleep(1)
				conf.set("new_section", "start_flag", "start")
				result_tmp = result
		time.sleep(15)
if __name__ == "__main__":
	init_data()
	t = threading.Thread(target=kaijiang,args=(qun_id,))
	t.start()
	z = threading.Thread(target=reply,args=())
	z.start()