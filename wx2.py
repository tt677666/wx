#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")



import itchat

from itchat.content import *
from itchat import *

import threading,time,requests,ConfigParser,os,shelve



#qun_name = u'微信群聊test'
qun_id = ''
#chatroom_ids = {}
#chatrooms = {}

def mange_config(action,sectio,p,flag):
	cfg = ConfigParser.ConfigParser()
	cfg.read("wx.conf")
	if action =='get':
		return cfg.get(sectio,p)
	if action =='set':
		cfg.set(sectio, p, flag)
	else:
		pass
	cfg.write(open("wx.conf","w"))
#write log
def logg(log_str):
	fname = 'log_'+time.strftime('%Y-%m-%d')+'.log'
	with open(fname,'a') as f:
		f.write(time.strftime('%Y-%m-%d_%H-%M-%S')+' '+log_str+'\n\r')



def lottle_check_zu3(user_lottle,real_lottle):
	tmp_list=[]
	result = False
	while len(user_lottle)>0:
		tmp_list.append(user_lottle[:2])
		user_lottle = user_lottle[2:]
	for l in tmp_list:
		if l in real_lottle.split(' ')[:3]:
			result = True
		else:
			result = False
	return result

def lottle_check_qian3(user_lottle,real_lottle):
	tmp_list=[]
	result = False
	while len(user_lottle)>0:
		tmp_list.append(user_lottle[:2])
		user_lottle = user_lottle[2:]
	if tmp_list == real_lottle.split(' ')[:3]:
		result = True
	else:
		result = False
	return result
	
def lottle_check_ren1(user_lottle,real_lottle):
	tmp_list=[]
	result = False
	while len(user_lottle)>0:
		tmp_list.append(user_lottle[:2])
		user_lottle = user_lottle[2:]
	if tmp_list == real_lottle.split(' ')[:1]:
		result = True
	else:
		result = False
	return result
	
def lottle_check(user_lottle,real_lottle):
	tmp_list=[]
	result = False
	mactch_times = 0
	while len(user_lottle)>0:
		tmp_list.append(user_lottle[:2])
		user_lottle = user_lottle[2:]
	for l in tmp_list:
		if l in real_lottle.split(' '):
			mactch_times = mactch_times + 1
		else:
			result = False
	return mactch_times

def winning_check(lottle):
	flags = mange_config('get','new_section','lottle_flag','nothing')
	with open('lottle_order.txt','r') as f:
		for l in f.readlines():
			if flags.find(l.split(' ')[2]) >=0 :
				if l.split(' ')[2] == 'ren1':
					if lottle_check_ren1(l.split(' ')[3],lottle):
						user_add_money(l.split(' ')[0],24*int(l.split(' ')[4]))
						
				if l.split(' ')[2] == 'ren2':
					if lottle_check(l.split(' ')[3],lottle) == 2:
						user_add_money(l.split(' ')[0],8*int(l.split(' ')[4]))
						
				if l.split(' ')[2] == 'ren3':
					if lottle_check(l.split(' ')[3],lottle) == 3:
						user_add_money(l.split(' ')[0],24*int(l.split(' ')[4]))
						
				if l.split(' ')[2] == 'ren4':
					if lottle_check(l.split(' ')[4],lottle) == 4:
						user_add_money(l.split(' ')[0],80*int(l.split(' ')[4]))
						
				if l.split(' ')[3] == 'ren5':
					if lottle_check(l.split(' ')[3],lottle) == 5:
						user_add_money(l.split(' ')[0],320*int(l.split(' ')[4]))
						
				if l.split(' ')[2] == '6-5':
					if lottle_check(l.split(' ')[3],lottle) == 5:
						user_add_money(l.split(' ')[0],320*int(l.split(' ')[4]))
					if lottle_check(l.split(' ')[3],lottle) == 6:
						user_add_money(l.split(' ')[0],1920*int(l.split(' ')[4]))
				'''
				if l.split(' ')[2] == '6-5':
					if lottle_check(l.split(' ')[3],lottle) == 6:
						user_add_money(l.split(' ')[0],1920*int(l.split(' ')[4]))
				'''
						
				if l.split(' ')[2] == '7-5':
					if lottle_check(l.split(' ')[3],lottle) == 5:
						user_add_money(l.split(' ')[0],320*int(l.split(' ')[4]))
					if lottle_check(l.split(' ')[3],lottle) == 6:
						user_add_money(l.split(' ')[0],1920*int(l.split(' ')[4]))
					if lottle_check(l.split(' ')[3],lottle) == 7:
						user_add_money(l.split(' ')[0],6720*int(l.split(' ')[4]))
				'''
				if l.split(' ')[2] == 'g2':
					if lottle_check(l.split(' ')[3],lottle) == 6:
						user_add_money(l.split(' ')[0],1920*int(l.split(' ')[4]))
						
				if l.split(' ')[2] == 'g3':
					if lottle_check(l.split(' ')[3],lottle) == 7:
						user_add_money(l.split(' ')[0],6720*int(l.split(' ')[4]))
				'''
				if l.split(' ')[2] == '8-5':
					if lottle_check(l.split(' ')[3],lottle) == 5:
						user_add_money(l.split(' ')[0],320*int(l.split(' ')[4]))
					if lottle_check(l.split(' ')[3],lottle) == 6:
						user_add_money(l.split(' ')[0],1920*int(l.split(' ')[4]))
					if lottle_check(l.split(' ')[3],lottle) == 7:
						user_add_money(l.split(' ')[0],6720*int(l.split(' ')[4]))
					if lottle_check(l.split(' ')[3],lottle) == 8:
						user_add_money(l.split(' ')[0],17920*int(l.split(' ')[4]))
				'''
				if l.split(' ')[2] == 'h2':
					if lottle_check(l.split(' ')[3],lottle) == 6:
						user_add_money(l.split(' ')[0],1920*int(l.split(' ')[4]))
						
				if l.split(' ')[2] == 'h3':
					if lottle_check(l.split(' ')[3],lottle) == 7:
						user_add_money(l.split(' ')[0],6720*int(l.split(' ')[4]))
						
				if l.split(' ')[2] == 'h4':
					if lottle_check(l.split(' ')[3],lottle) == 8:
						user_add_money(l.split(' ')[0],17920*int(l.split(' ')[4]))
				'''
				if l.split(' ')[2] == 'zu3':
					if lottle_check_zu3(l.split(' ')[3],lottle):
						user_add_money(l.split(' ')[0],1300*int(l.split(' ')[4]))
						
				if l.split(' ')[2] == 'qian3':
					if lottle_check_qian3(l.split(' ')[3],lottle):
						user_add_money(l.split(' ')[0],8000*int(l.split(' ')[4]))
			else:
				print 'this lottle flags closed'
	#清空投注记录表
	with open('lottle_order.txt','w') as f:
		f.truncate()

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
def format_check(usr,user_msg):
	flags = mange_config('get','new_section','lottle_flag','nothing')
	rule_num = user_msg.split(' ')[1]
	try:
		times = int(user_msg.split(' ')[3])
	except:
		return False
	print user_msg,times
	#print 'rule_num is ', rule_num,type(rule_num) 
	lottle_num = user_msg.split(' ')[2]
	#print 'lottle_num is ', lottle_num,type(lottle_num)
	if rule_num == 'ren1' and flags.find(rule_num)>=0:
		print 'i am in'
		if len(lottle_num) == 2 and  cut_num(lottle_num) == True and user_min_money(usr,2*times) == True:
			print 'i\'m in'
			return True
		else:
			return False
	if rule_num == 'ren2' and flags.find(rule_num)>=0:
		if len(lottle_num) == 4 and  cut_num(lottle_num) == True and user_min_money(usr,2*times) == True :
			return True
		else:
			return False
	if rule_num == 'ren3' or rule_num == 'zu3' or rule_num == 'qian3' and flags.find(rule_num)>=0:
		if len(lottle_num) == 6 and  cut_num(lottle_num) == True and user_min_money(usr,2*times) == True:
			return True
		else:
			return False
	if rule_num == 'ren4'  and flags.find(rule_num)>=0:
		if len(lottle_num) == 8 and  cut_num(lottle_num) == True and user_min_money(usr,2*times) == True:
			return True
		else:
			return False
	if rule_num == 'ren5' and flags.find(rule_num)>=0:
		if len(lottle_num) == 10 and  cut_num(lottle_num) == True and user_min_money(usr,2*times) == True:
			return True
		else:
			return False
	if rule_num == '6-5' and flags.find(rule_num)>=0:
		if len(lottle_num) == 12 and  cut_num(lottle_num) == True and user_min_money(usr,12*times) == True:
			return True
		else:
			return False
	if rule_num == '7-5'  and flags.find(rule_num)>=0:
		if len(lottle_num) == 14 and  cut_num(lottle_num) == True and user_min_money(usr,42*times) == True:
			return True
		else:
			return False
	if rule_num == '8-5' and flags.find(rule_num)>=0:
		if len(lottle_num) == 16 and  cut_num(lottle_num) == True and user_min_money(usr,112*times) == True:
			return True
		else:
			return False
	else:
		return False

#获取消息后判断用户是否存在于用户积分表(dict方式)中
def user_money(user_name):
	user_name = user_name.encode('utf-8')
	result = False
	try:
		f = shelve.open('user.db','c')
		
		if f.has_key(user_name):
			result = True
		else:
			f[user_name] = int(0)
			result = False
	finally:
		f.close()
	return result

def user_add_money(user_name,count):
	user_name = user_name.encode('utf-8')
	try:
		f = shelve.open('user.db','c')
		if f.has_key(user_name):
			f[user_name] = f[user_name] + int(count) 
		else:
			print 'user_add_money not found user'
	finally:
		f.close()
		
def user_min_money(user_name,count):

	user_name = user_name.encode('utf-8')
	result = True
	print count
	try:
		f = shelve.open('user.db','c')
		if f.has_key(user_name):
			if f[user_name] - int(count) >= 0:
				f[user_name] = f[user_name] - int(count)
			else:
				result = False
				print (u'余额不足')
	finally:
		f.close()		
	
	return result

def set_manage_flag(usr_name,content):
	content = content.encode('utf-8')
	#name = conf.get("new_section","manage_name")
	print 'in set_manage_flag'
	if content.split(' ')[1] == 'moshi':
		print 'in set moshi'
		mange_config('set','new_section','lottle_flag',content.split(' ')[2])
	if content.split(' ')[1] == 'yanchi':
		print 'in set yanchi'
		mange_config('set','new_section','delay_time',content.split(' ')[2])
	else:
		print u'unknow manage command'

def get_usr_count(usr_name):
	'i am in get_usr_count'
	print usr_name
	usr_name = usr_name.encode('utf-8')
	try:
		f = shelve.open('user.db','c')
		if f.has_key(usr_name):
			print usr_name
			itchat.send('%s\n%s\n%s' % (u'======== 查询结果========',time.strftime('%Y-%m-%d %H:%M:%S'), f[usr_name]), qun_id)
			#print ('%s\n%s\n%s' % ('======== user_money_result========',time.strftime('%Y-%m-%d %H:%M:%S'), f[usr_name]), qun_id)
		else:
			print 'not found user'
	finally:
		f.close()		
	
#检测聊天记录是否以"touzhu"开头,如果是则将消息检测后存入"lottle_order.txt"表(文本),并将消息计入日志
def check_order(usr,content):
	global qun_id
	content = content.encode('utf-8')
	
	name = mange_config('get','new_section','manage_name','nothing')
	
	if content.split(' ')[0] == 'touzhu':
		if format_check(usr,content) == True:
			with open ('lottle_order.txt','a') as f:
				f.write(usr+ ' ' +content + '\n')
		else:
			itchat.send('%s' % (u'==格式错误or余额不足or模式已关闭=='), qun_id)
			#print u'格式错误,余额不足,模式已关闭'

def check_and_do_manage(usr,content):
	'i am in check_and_do_manage'
	content = content.encode('utf-8')
	name = mange_config('get','new_section','manage_name','nothing')
	if content.split(' ')[0] == 'guanli'  and usr == name:
		set_manage_flag(usr,content)
	if content.split(' ')[0] == 'shangfen' and usr == name:
		user_add_money(content.split(' ')[1],content.split(' ')[2])
	if content.split(' ')[0] == 'jianfen' and usr == name:
		user_min_money(content.split(' ')[1],content.split(' ')[2])
	if content == 'chaxun':
		'i am in chaxun_if'
		get_usr_count(usr)


def init_data():

	global qun_id
	
	if os.path.exists('wx.conf'):
		mange_config('set','new_section','start_flag','stop')
	if os.path.exists('wx.conf') is False:
		conf = ConfigParser.ConfigParser()
		conf.read("wx.conf")
		conf.add_section("new_section")
		conf.set("new_section", "start_flag", "stop")
		conf.set("new_section", "delay_time", "60")
		conf.set("new_section", "lottle_flag", "ren1 ren2 ren3 ren4 ren5 6-5 7-5 8-5 zu3 qian3")
		conf.write(open("wx.conf","w"))
	if os.path.exists('lottle_order.txt'):
		with open('lottle_order.txt','w') as f:
			f.truncate()
	if os.path.exists('lottle_order.txt') is False:
		with open('lottle_order.txt','w') as f:
			pass

	
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
@itchat.msg_register([TEXT, SHARING,NOTE], isGroupChat=True)
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
	
	if msg['Type'] == NOTE:
		itchat.send('%s\n%s\n%s\n%s' % (u'======== 欢迎加入========',msg['Content'].split('\"')[3], u'请修改群昵称为自己的微信号',u'否则您将无法正常使用某些功能'), qun_id)
		logg(msg['Content'].split('\"')[3] + '请修改群昵称为自己的微信号')
		
	# 根据消息类型转发至其他需要同步消息的群聊
	if msg['Type'] == TEXT:
		for item in chatrooms:
			if item['UserName'] == chatroom_id:
				
				if user_money(username):
					if msg['Content'].split(' ')[0] == 'touzhu':
						if mange_config('get','new_section','start_flag','nothing')  == 'start':
							check_order(username,msg['Content'])
						if mange_config('get','new_section','start_flag','nothing')  == 'stop':
							itchat.send('%s' % (u'======== 封板期间,无法投注========'), qun_id)
							#print('%s' % ('======== lottle_stop,cannot do it========'), qun_id)
							
					if msg['Content'].split(' ')[0] == 'guanli':
						check_and_do_manage(username,msg['Content'])
						
					if msg['Content'].split(' ')[0] == 'shangfen':
						check_and_do_manage(username,msg['Content'])
						
					if msg['Content'].split(' ')[0] == 'jianfen':
						check_and_do_manage(username,msg['Content'])
						
					if msg['Content'].split(' ')[0] == 'chaxun':
						check_and_do_manage(username,msg['Content'])
						
				print (username, msg['Content']), item['UserName']


def reply():
	itchat.run()

def kaijiang(qun_id):
	result_tmp = 'tmp_str'
	while True:
		while True:
			try:
				r = requests.post('http://sxhb.ws1.zs-zc.net/api/AwardNum/LottAwardInfoList',{'lott': '07', 'size': '20'})
				#r = requests.get('http://45.32.50.28:9999')
				result = r.json()[0]['RaffleNumber']
				result_time_hour = int(r.json()[0]['CreateTime'].split(' ')[1].split(':')[0])
				result_time_min = int(r.json()[0]['CreateTime'].split(' ')[1].split(':')[1])
				
				break
			except:
				print 'connection  failed'
				time.sleep(2)

		# 取开奖时间的小时和分钟值，如果晚于21:50,则证明本日投注结束
		if result_time_hour == 21 and result_time_min >= 50:
			#print u' 非投注时间范围'
			pass
		else:
			#print u'投注时间范围'
			if result_tmp != 'tmp_str':
				if result_tmp != result:
					print 1
					itchat.send('%s\n%s\n%s\n%s\n%s\n%s' % (u'======== 开奖结果========',r.json()[0]['CreateTime'], r.json()[0]['IssueName'],result,u'走势图','http://sxhb.wx.zs-zc.net/AwardNum/HappyTenMin?lott=07'), qun_id)
					#print('%s\n%s\n%s\n%s' % ('======== lottole_result========',r.json()[0]['CreateTime'], r.json()[0]['IssueName'],result), qun_id)
					mange_config('set','new_section','start_flag','stop')
					#开始统计上轮中奖结果（需要reply线程记录上轮的投注消息）
					winning_check(result)
					#告诉reply线程开始响应下轮投注消息
					time.sleep(1)
					mange_config('set','new_section','start_flag','start')
					itchat.send('%s\n%s\n' % (u'======== 开始投注========',int(r.json()[0]['IssueName'])+1), qun_id)
					#print('%s\n%s\n' % ('======== start_lotlle========',int(r.json()[0]['IssueName'])+1), qun_id)
					time_to_sleep = 600 - (convert2timestamp(network_time(r.headers['Date'])) - convert2timestamp(r.json()[0]['CreateTime'])) - 15 - int(mange_config('get','new_section','delay_time','nothing'))
					time.sleep(time_to_sleep)
					mange_config('set','new_section','start_flag','stop')
					itchat.send('%s\n%s\n%s' % (u'======== 系统封板========',time.strftime('%Y-%m-%d %H:%M:%S'),u'以上投注有效,现在停止接单'), qun_id)
					#print('%s\n%s\n%s' % ('======== stop_lootle========',time.strftime('%Y-%m-%d %H:%M:%S'),'haha'), qun_id)
			result_tmp = result
		time.sleep(15)
if __name__ == "__main__":
	init_data()
	
	itchat.auto_login(False)
	chatrooms = itchat.get_chatrooms(update=True, contactOnly=True)
	for k in chatrooms:
		#if k['NickName'] == qun_name:
		qun_id = k['UserName']

	chatroom_ids = [c['UserName'] for c in chatrooms]
	#print chatroom_ids
	#print '正在监测的群聊：', len(chatrooms), '个'
	print ' '.join([item['NickName'] for item in chatrooms])
	
	t = threading.Thread(target=kaijiang,args=(qun_id,))
	t.start()
	z = threading.Thread(target=reply,args=())
	z.start()