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
conf.set("new_section", "lottle_flag", "a1 b1 c1 d1 e1 f1 f2 g1 g2 g3 h1 h2 h3 h4 z1 z2")
conf.write(open("wx.conf","w"))


qun_name = u'΢��Ⱥ��test'
qun_id = ''



#��־��¼ģ��
def logg(log_str):
	with open('log.txt','a') as f:
		f.write(time.strftime('%Y-%m-%d_%H-%M-%S')+' '+log_str+'\n\r')



def lottle_check_z1(user_lottle,real_lottle):
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

def lottle_check_z2(user_lottle,real_lottle):
	tmp_list=[]
	result = False
	while len(user_lottle)>0:
		tmp_list.append(user_lottle[:2])
		user_lottle = user_lottle[2:]
	if tmp1_list == real_lottle.split(' ')[:3]:
		result = True
	else:
		result = False
	return result
	
def lottle_check(user_lottle,real_lottle):
	tmp_list=[]
	result = False
	while len(user_lottle)>0:
		tmp_list.append(user_lottle[:2])
		user_lottle = user_lottle[2:]
	for l in tmp_list:
		if l in real_lottle.split(' '):
			result = True
		else:
			result = False
	return result

def winning_check(lottle):
	conf = ConfigParser.ConfigParser()
	conf.read("wx.conf")
	flags = conf.get('new_section','lottle_flag')
	with open('lottle_order.txt','r') as f:
		for l in f.readlines():
			if flags.find(l.split(' ')[3]) >=0 :
				if l.split(' ')[3] == 'a1':
					if lottle_check(l.split(' ')[4],lottle):
						user_add_money(l.split(' ')[0],8)
				if l.split(' ')[3] == 'b1':
					if lottle_check(l.split(' ')[4],lottle):
						user_add_money(l.split(' ')[0],16)
				if l.split(' ')[3] == 'c1':
					if lottle_check(l.split(' ')[4],lottle):
						user_add_money(l.split(' ')[0],24)
				if l.split(' ')[3] == 'd1':
					if lottle_check(l.split(' ')[4],lottle):
						user_add_money(l.split(' ')[0],80)
				if l.split(' ')[3] == 'e1':
					if lottle_check(l.split(' ')[4],lottle):
						user_add_money(l.split(' ')[0],320)
				if l.split(' ')[3] == 'f1':
					if lottle_check(l.split(' ')[4],lottle):
						user_add_money(l.split(' ')[0],320)
				if l.split(' ')[3] == 'f2':
					if lottle_check(l.split(' ')[4],lottle):
						user_add_money(l.split(' ')[0],1920)
				if l.split(' ')[3] == 'g1':
					if lottle_check(l.split(' ')[4],lottle):
						user_add_money(l.split(' ')[0],320)
				if l.split(' ')[3] == 'g2':
					if lottle_check(l.split(' ')[4],lottle):
						user_add_money(l.split(' ')[0],1920)
				if l.split(' ')[3] == 'g3':
					if lottle_check(l.split(' ')[4],lottle):
						user_add_money(l.split(' ')[0],6720)
				if l.split(' ')[3] == 'h1':
					if lottle_check(l.split(' ')[4],lottle):
						user_add_money(l.split(' ')[0],320)
				if l.split(' ')[3] == 'h2':
					if lottle_check(l.split(' ')[4],lottle):
						user_add_money(l.split(' ')[0],1920)
				if l.split(' ')[3] == 'h3':
					if lottle_check(l.split(' ')[4],lottle):
						user_add_money(l.split(' ')[0],6720)
				if l.split(' ')[3] == 'h4':
					if lottle_check(l.split(' ')[4],lottle):
						user_add_money(l.split(' ')[0],17920)
				if l.split(' ')[3] == 'z1':
					if lottle_check_z1(l.split(' ')[4],lottle):
						user_add_money(l.split(' ')[0],1300)
				if l.split(' ')[3] == 'z2':
					if lottle_check_z2(l.split(' ')[4],lottle):
						user_add_money(l.split(' ')[0],8000)
			else:
				print 'this lottle flags closed'
			
#���ճ���2�и���ע�ĺ���		
def cut_num(num):
	tmp_list = []
	tmp1_list = []
	#�����жϣ���Ϊż��
	if len(num)%2 != 0:
		return False
	#ѭ�����ճ����и�
	while len(num)>0:
		tmp_list.append(num[:2])
		num = num[2:]
	for k in tmp_list:
		#�ظ��ж�
		tmp1_list = tmp_list
		tmp1_list.remove(k)
		for l in tmp1_list:
			if k == l:
				return False
			else :
				pass
		try:
			k = int(k)
			#ץ��Ϊ������Χ�ж�
			if k >20 or k < 1:
				return false
		except:
			return False
	
	return True
		
		
#����û����͵�Ͷע��ʽ�Ƿ���ȷ
def format_check(usr,user_msg):
	rule_num = user_msg.split(' ')[2]
	lottle_num = user_msg.split(' ')[3]
	if rule_num == 'a1':
		if len(lottle_num) == 2 and  cut_num(lottle_num) == True and user_min_money(usr,2) == True:
			return True
		else:
			return False
	if rule_num == 'b1':
		if len(lottle_num) == 4 and  cut_num(lottle_num) == True and user_min_money(usr,2) == True :
			return True
		else:
			return False
	if rule_num == 'c1' or rule_num == 'z1' or rule_num == 'z2':
		if len(lottle_num) == 6 and  cut_num(lottle_num) == True and user_min_money(usr,2) == True:
			return True
		else:
			return False
	if rule_num == 'd1':
		if len(lottle_num) == 8 and  cut_num(lottle_num) == True and user_min_money(usr,2) == True:
			return True
		else:
			return False
	if rule_num == 'e1':
		if len(lottle_num) == 10 and  cut_num(lottle_num) == True and user_min_money(usr,2) == True:
			return True
		else:
			return False
	if rule_num == 'f1' or rule_num == 'f2':
		if len(lottle_num) == 12 and  cut_num(lottle_num) == True and user_min_money(usr,12) == True:
			return True
		else:
			return False
	if rule_num == 'g1' or rule_num == 'g2' or rule_num == 'g3':
		if len(lottle_num) == 14 and  cut_num(lottle_num) == True and user_min_money(usr,43) == True:
			return True
		else:
			return False
	if rule_num == 'h1' or rule_num == 'h2' or rule_num == 'h3'  or rule_num == 'h4':
		if len(lottle_num) == 16 and  cut_num(lottle_num) == True and user_min_money(usr,112) == True:
			return True
		else:
			return False
	else:
		return False

#��ȡ��Ϣ���ж��û��Ƿ�������û����ֱ�(dict��ʽ)��
def user_money(user_name):
	result = False
	try:
		f = shelve.open('user.db','c')
		if f.has_key[user_name]:
			result = True
		else:
			f[user_name] = int(0)
			result = False
	finally:
		f.close()
	return result


	
def user_add_money(user_name,count):

	try:
		f = shelve.open('user.db','c')
		if f.has_key[user_name]:
			f[user_name] = f[user_name] + int(count) 
	finally:
		f.close()
		
def user_min_money(user_name,count):
	result = True
	try:
		f = shelve.open('user.db','c')
		if f.has_key[user_name]:
			if f[user_name] - count >= 0:
				f[user_name] = f[user_name] - count
			else:
				result = False
				print (u'����')
	finally:
		f.close()		
	
	return result

#��������¼�Ƿ���"touzhu"��ͷ,���������Ϣ�������"lottle_order.txt"��(�ı�),������Ϣ������־
def check_order(usr,content):
	if content.split(' ')[0] == 'guanli':
		pass
	if content.split(' ')[0] == 'touzhu':
		if format_check(usr,content) == True:
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
	#print '���ڼ���Ⱥ�ģ�', len(chatrooms), '��'
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



# �Զ��ظ��ı�������Ⱥ����Ϣ
# isGroupChat=True��ʾΪȺ����Ϣ
@itchat.msg_register([TEXT, SHARING], isGroupChat=True)
def group_reply_text(msg):
	# ��Ϣ�������ĸ�Ⱥ��
	chatroom_id = msg['FromUserName']
	# �����ߵ��ǳ�
	username = msg['ActualNickName']

	# ��Ϣ��������������Ҫͬ����Ⱥ
	if not chatroom_id in chatroom_ids:
		return

	if msg['Type'] == TEXT:
		content = msg['Content']
	elif msg['Type'] == SHARING:
		content = msg['Text']

	# ������Ϣ����ת����������Ҫͬ����Ϣ��Ⱥ��
	if msg['Type'] == TEXT:
		for item in chatrooms:
			if item['UserName'] == chatroom_id:
				
				if user_money(username):
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

		# ȡ����ʱ���Сʱ�ͷ���ֵ���������21:50,��֤������Ͷע����
		if result_time_hour == 21 and result_time_min >= 50:
			print u'��Ͷעʱ�䷶Χ'
		else:
			print u'Ͷעʱ�䷶Χ'
			if result_tmp != result:
				#itchat.send('%s\n%s\n%s\n%s' % (u'======== �������========',r.json()[0]['CreateTime'], r.json()[0]['IssueName'],result), qun_id)
				#��ʼͳ�������н��������Ҫreply�̼߳�¼���ֵ�Ͷע��Ϣ��
				winning_check(result)
				#����reply�߳̿�ʼ��Ӧ����Ͷע��Ϣ
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