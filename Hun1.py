# -*- coding: utf-8 -*-
#Bot

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile

ehun = LINETCR.LINE()
#ehun.login(qr=True)
ehun.login(token="Di sini token kamu ")
ehun.loginResult()

Creator = ehun

print "Success"

reload(sys)
sys.setdefaultencoding('utf-8')

selfMessage ="""
╔═════════════════════════
║            ☆☞ S E L F ☜☆
╠═════════════════════════
╠➩〘Hi〙
|☆Curl
|☆Ourl
|☆Setpoin
|☆Lastpoin
╠➩〘Me〙
╠➩〘Mymid〙
╠➩〘Mid @〙
╠➩〘SearchID: (ID LINE)〙
╠➩〘Checkdate (DD/MM/YY)〙
╠➩〘Kalender〙
╠➩〘Steal contact〙
╠➩〘Pp @〙
╠➩〘Cover @〙
╠➩〘Auto like〙
╠➩〘Scbc Text〙
╠➩〘Cbc Text〙
╠➩〘Gbc Text〙
╠➩〘Getbio @〙
╠➩〘Getinfo @〙
╠➩〘Getname @〙
╠➩〘Getprofile @〙
╠➩〘Getcontact @〙
╠➩〘Getvid @〙
╠➩〘Friendlist〙
╠➩〘Micadd @〙
╠➩〘Micdel @〙
╠➩〘Miclist〙
╠═════════════════════════
║    by Ehun http://line.me/ti/p/~sarehun
╚═════════════════════════
"""

botMessage ="""
╔═════════════════════════
║             ☆☞ B O T ☜☆
╠═════════════════════════
╠➩〘Absen〙
╠➩〘Respon〙
╠➩〘Runtime〙
╠➩〘Mycopy @〙
╠➩〘Copycontact〙
╠➩〘Mybackup〙
╠➩〘Mybio (Text)〙
╠➩〘Myname (Text)〙
╠➩〘@bye〙
╠➩〘Bot on/off〙

╠═════════════════════════
║    by Ehun http://line.me/ti/p/~sarehun
╚═════════════════════════
"""

mediaMessage ="""
╔═════════════════════════
║           ☆☞ M E D I A ☜☆
╠═════════════════════════
╠➩〘Gift〙
╠➩〘Gift1 @ s/d Gift10 @〙
╠➩〘Giftbycontact〙
╠➩〘Gif gore〙
╠➩〘Google: (Text)〙
╠➩〘Playstore NamaApp〙
╠➩〘Fancytext: Text〙
╠➩〘/musik Judul-Penyanyi〙
╠➩〘/lirik Judul-Penyanyi〙
╠➩〘/musrik Judul-Penyanyi〙
╠➩〘/ig UrsnameInstagram〙
╠➩〘Checkig UrsnameInstagram〙
╠➩〘/apakah Text (Kerang Ajaib)〙
╠➩〘/kapan Text (Kerang Ajaib)〙
╠➩〘/hari Text (Kerang Ajaib)〙
╠➩〘/berapa Text (Kerang Ajaib)〙
╠➩〘/berapakah Text〙
╠➩〘Youtubelink: Judul Video〙
╠➩〘Youtubevideo: Judul Video〙
╠➩〘Youtubesearch: Judul Video〙
╠➩〘Image NamaGambar〙
╠➩〘Say-id Text〙
╠➩〘Say-en Text〙
╠➩〘Say-jp Text〙
╠➩〘Image NamaGambar〙
╠➩〘Tr-id Text (Translate En Ke ID〙
╠➩〘Tr-en Text (Translate ID Ke En〙
╠➩〘Tr-th Text (Translate ID Ke Th〙
╠➩〘Id@en Text (Translate ID Ke En〙
╠➩〘Id@th Text (Translate ID Ke TH〙
╠➩〘En@id Text (Translate En Ke ID〙
╠═════════════════════════
║   by Ehun http://line.me/ti/p/~sarehun
╚═════════════════════════
"""

groupMessage ="""
╔═════════════════════════
║           ☆☞ G R O U P ☜☆
╠═════════════════════════
╠➩〘Welcome〙
╠➩〘Say welcome〙
╠➩〘Invite creator〙
╠➩〘Setview〙
╠➩〘Viewseen〙
╠➩〘Gn: (NamaGroup)〙
╠➩〘Tag all〙
╠➩〘Recover〙
╠➩〘Cancel〙
╠➩〘Cancelall〙
╠➩〘Gcreator〙
╠➩〘Ginfo〙
╠➩〘Gurl〙
╠➩〘List group〙
╠➩〘Pict group: (NamaGroup)〙
╠➩〘Spam: (Text)〙
╠➩〘Add all〙
╠➩〘Kick: (Mid)〙
╠➩〘Invite: (Mid)〙
╠➩〘Invite〙
╠➩〘Memlist〙
╠➩〘Getgroup image〙
╠➩〘Urlgroup Image〙
╠═════════════════════════
║  by Ehun http://line.me/ti/p/~sarehun
╚═════════════════════════
"""
Ehun="ub3808de9f7df35f57fb366d157f9790a"

setMessage ="""
╔═════════════════════════
║              ☆☞ S E T ☜☆
╠═════════════════════════
╠➩〘Sambutan on/off〙
╠➩〘Mimic on/off〙
╠➩〘Url on/off〙
╠➩〘Alwaysread on/off〙
╠➩〘Sider on/off〙
╠➩〘Contact on/off〙
╠➩〘Sticker on〙
╠➩〘Simisimi on/off〙
╠═════════════════════════
║    by Ehun http://line.me/ti/p/~sarehun
╚═════════════════════════
"""

creatorMessage ="""
╔═════════════════════════
║         ☆☞ C R E A T O R ☜☆
╠═════════════════════════
╠➩〘Crash〙
╠➩〘Kickall〙
╠➩〘Bc: (Text)〙
╠➩〘Join group: (NamaGroup〙
╠➩〘Leave group: (NamaGroup〙
╠➩〘Leave all group〙
╠➩〘Tag on/off〙
╠➩〘Bot restart〙
╠➩〘Turn off〙
|> [#hun]
|> [#virus]
|> [Smule]
╠═════════════════════════
║      by Ehun http://line.me/ti/p/~sarehun
╚═════════════════════════
"""

adminMessage ="""
╔═════════════════════════
║            ☆☞ A D M I N ☜☆
╠═════════════════════════
╠➩〘Allprotect on/off〙
╠➩〘Ban〙
╠➩〘Unban〙
╠➩〘Ban @〙
╠➩〘Unban @〙
╠➩〘Ban list〙
╠➩〘Clear ban〙
╠➩〘Kill〙
╠➩〘Kick @〙
╠➩〘Set member: (Jumblah)〙
╠➩〘Ban group: (NamaGroup〙
╠➩〘Del ban: (NamaGroup〙
╠➩〘List ban〙
╠➩〘Kill ban〙
╠➩〘Glist〙
╠➩〘Glistmid〙
╠➩〘Details group: (Gid)〙
╠➩〘Cancel invite: (Gid)〙
╠➩〘Invitemeto: (Gid)〙
╠➩〘Acc invite〙
╠➩〘Removechat〙
╠➩〘Qr on/off〙
╠➩〘Autokick on/off〙
╠➩〘Autocancel on/off〙
╠➩〘Invitepro on/off〙
╠➩〘Join on/off〙
╠➩〘Joincancel on/off〙
╠➩〘Respon1 on/off〙
╠➩〘Respon2 on/off〙
╠➩〘Respon3 on/off〙
╠➩〘Responkick on/off〙
╠═════════════════════════
║    by Ehun http://line.me/ti/p/~sarehun
╚═════════════════════════
"""

helpMessage ="""
╔═════════════════════════
║              ☆☞ H E L P ☜☆
╠═════════════════════════
╠➩〘Help self〙
╠➩〘Help bot〙
╠➩〘Help group〙
╠➩〘Help set〙
╠➩〘Help media〙
╠➩〘Help admin〙
╠➩〘Help creator〙
╠➩〘Owner〙
╠➩〘Pap owner〙
╠➩〘Speed〙
╠➩〘Speed test〙
╠➩〘Status〙
|> [Setpoin]
|> [Laspoin]
|> [Sider on/On sider]
|> [Sider off]
|> [Haloo/Tag/Tagall/Tag all]
╠═════════════════════════
║     by Ehun http://line.me/ti/p/sarehun
╚═════════════════════════
"""


KAC=[ehun]
mid = ehun.getProfile().mid
Bots=[mid]
Creator=["ub3808de9f7df35f57fb366d157f9790a"]
admin=["ub3808de9f7df35f57fb366d157f9790a"]

contact = ehun.getProfile()
backup1 = ehun.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

responsename = ehun.getProfile().displayName


wait = {
    "LeaveRoom":True,
    "Bot":True,
    "AutoJoin":False,
    "AutoJoinCancel":False,
    "memberscancel":30,
    "Members":1,
    "AutoCancel":False,
    "AutoKick":False,
    'pap':{},
    'invite':{},
    'steal':{},
    'gift':{},
    'copy':{},    
    'likeOn':{},
    'detectMention':True,
    'detectMention2':False,
    'detectMention3':False,
    'kickMention':False,  
    'sticker':True,
    'timeline':True,
    'sider1':"CCTV Jones 😂😂😂",
    "Timeline":True,
    "comment":"Bot Auto Like ©By : Ehun\nContact Me : 👉 line.me/ti/p/~sarehun",
    "commentOn":True,
    "commentBlack":{},
    "message":"Thx For Add Me (^_^)\nInvite Me To Your Group ヘ(^_^)ヘ",    
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":False,
    "Contact":False,
    "Sambutan":True,
    "inviteprotect":False,    
    "alwaysRead":False,    
    "pname":{},
    "pro_name":{},
    "Sider":False,
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{}
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }
    
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }    

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False    

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True


def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')
            
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       ehun.sendMessage(msg)
    except Exception as error:
       print error          
                        
       

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def bot(op):
    try:

        if op.type == 0:
            return

        if op.type == 5:
           if wait["autoAdd"] == True:
              ehun.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                ehun.sendText(op.param1,str(wait["message"]))


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+ str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e

        if op.type == 55:
            try:
               if op.param1 in wait2['readPoint']:
                 Name = ehun.getContact(op.param2).displayName
                 if Name in wait2['readMember'][op.param1]:
                    pass
                 else:
                    wait2['readMember'][op.param1] += "\n[•]" + Name + "\nOn Jam : " + datetime.today().strftime('%H:%M:%S')
                    wait2['ROM'][op.param1][op.param2] #= "[•]" + Name
               else:
                 ehun.sendText
            except:
                 pass


        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = ehun.getContact(op.param2). displayName
                            if Name in cctv['sidermem'][op.param1] + "\n" + datetime.today().strftime('%H:%M:%S'):
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name + "\n" + datetime.today().strftime('%H:%M:%S')
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        ehun.sendText(op.param1, "Waktu Sider\nJam   :    " + datetime.today().strftime('%H:%M:%S') + "\n~~~~~~~~~~~~~~~~\nHaii Kak\n" + "☞ " + Name + " ☜" + "\nNgintip Aja Niih. . .\nChat Kek Idiih (-__-)   ")
                                        time.sleep(0.0001)
                                        summon(op.param1,[op.param2])
                                    else:
                                        ehun.sendText(op.param1, "Waktu Sider\nJam   :    " + datetime.today().strftime('%H:%M:%S') + "\n~~~~~~~~~~~~~~~~\nHaii kak\n" + "☞ " + Name + " ☜" + "\nBetah Banget Jadi Penonton. . .\nChat Napa (-__-)   ")
                                        time.sleep(0.0001)
                                        summon(op.param1,[op.param2])
                                else:
                                    ehun.sendText(op.param1, "Waktu Sider\nJam   :    " + datetime.today().strftime('%H:%M:%S') + "\n~~~~~~~~~~~~~~~~\nHaii kak\n" + "☞ " + Name + " ☜" + "\nNgapain Kak Ngintip Aja???\nSini Gabung Chat...   ")
                                    time.sleep(0.0001)
                                    summon(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass
     

	if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = ehun.getGroup(op.param1)
                    except:
                        pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        ehun.updateGroup(G)
                    except:
                        pass
                    else:
                        if op.param2 in Bots + Creator:
                            try:
                                ehun.sendText(op.param1,"Hai kak" + ehun.getContact(op.param2).displayName + "\nJangn Tukar Nama Group (-_-) \nMaaf Aku kick Kamu")
                                ehun.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
                            
        if op.type == 22:
            ehun.leaveRoom(op.param1)

        if op.type == 21:
            ehun.leaveRoom(op.param1)

        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    ehun.acceptGroupInvitation(op.param1)

		    
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = ehun.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        ehun.acceptGroupInvitation(op.param1)
                        ehun.sendText(op.param1,"Maaf " + ehun.getContact(op.param2).displayName + "\nMember Kurang Dari 30 Orang\nUntuk Info, Silahkan Chat Owner Kami!")
                        ehun.leaveGroup(op.param1)                        
		    else:
                        ehun.acceptGroupInvitation(op.param1)
			ehun.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
                        		    
 
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = ehun.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        ehun.rejectGroupInvitation(op.param1)
		    else:
                        ehun.acceptGroupInvitation(op.param1)
			ehun.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        ehun.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			ehun.cancelGroupInvitation(op.param1, [op.param3])
			ehun.sendText(op.param1, "Blacklist Detected")
		    else:
			pass
			
        if op.type == 13:
            if op.param2 not in Creator:
             if op.param2 not in admin:
              if op.param2 not in Bots:
                if op.param2 in Creator:
                 if op.param2 in admin:
                  if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    ehun.cancelGroupInvitation(op.param1,[op.param3])
                    ehun.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Creator:
                     if op.param2 not in admin:
                      if op.param2 not in Bots:
                        if op.param2 in Creator:
                         if op.param2 in admin:
                          if op.param2 in Bots:
                            pass

        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Creator:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in Creator:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               ehun.kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    ehun.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        ehun.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        ehun.inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Creator:
			        if op.param2 in Bots:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Creator:
		            if op.param2 in Creator:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass


                if mid in op.param3:
                    if op.param2 in Creator:
                      if op.param2 in Bots:
                        pass
                    try:
                        ehun.kickoutFromGroup(op.param1,[op.param2])
			ehun.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    ehun.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

 
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ehun.kickoutFromGroup(op.param1,[op.param2])
			ehun.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                ehun.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        ehun.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    ehun.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Creator:
		 if op.param2 in admin:
		  if op.param2 in Bots:
		   pass		
		else:
                    ehun.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            ginfo = ehun.getGroup(op.param1)
            contact = ehun.getContact(op.param2)
            #ehun.getContact(op.param2).displayName
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            ehun.sendMessage(c)
            ehun.sendText(op.param1,"Jam  :" + datetime.today().strftime('%H:%M:%S') + "\nHallo kak" + ehun.getContact(op.param2).displayName + "\nWelcome To ☞ " + str(ginfo.name) + " ☜ \nBudayakan Cek Note\nDan Semoga Betah di Sini . (p′︵‵。) 🤗 \nCreator>>" + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
            gCreator = ginfo.creator.mid
            msg = Message(to=op.param1, from_=None, text=None,contentType=13)
            msg.contentMetadata = {'mid': gCreator}
            ehun.sendMessage(msg)
            print "MEMBER JOIN TO GROUP"

            
        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            ehun.sendText(op.param1,"Good Bye " + ehun.getContact(op.param2).displayName +  "\nSee You Next Time . . . (p′︵‵。) 🤗")
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13269542",
                                    "STKPKGID": "1329191",
                                    "STKVER": "1" }                
            ehun.sendMessage(d)                  
            print "MEMBER HAS LEFT THE GROUP"
            
        if op.type == 26:
            msg = op.message
            
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        ehun.sendText(msg.to,text)             
            
            
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                               ehun.sendText(msg.to,data['result']['response'].encode('utf-8'))

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = ehun.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Aku Bilang Jangan Ngetag Lagi " + cName + "\nAku Kick Kamu! Sorry, Byee!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  ehun.sendText(msg.to,ret_)
                                  ehun.kickoutFromGroup(msg.to,[msg.from_])
                                  break                              

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = ehun.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Ada apa kak        \n" + cName + "\nNgapain ngtag-Tag Aku\nKalo Penting Langsung Pc Aja", "Kak\n" + cName + "\nJangn tag aku\nKaknaksir aku ya (-_-)", "Jangan Suka Tag Aku kak\n" + cName + "\nKamu Siapa ?"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                 ehun.sendText(msg.to,ret_)
                                 msg.contentType = 7
                                 msg.text = None
                                 msg.contentMetadata = {"STKID" : '13636219',  "STKPKGID" : '1340317', "STKVER" : '1'}
                                 ehun.sendMessage(msg)
                                 break   
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:          
                    contact = ehun.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Sekali lagi nge tag gw sumpahin jomblo seumur hidup!","Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","Woii " + cName + " Jangan Ngetag, Riibut!"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  ehun.sendText(msg.to,ret_)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID" :  '15027642',
                                                       "STKPKGID" : '1384991',
                                                       "STKVER": "1" }
                                  ehun.sendMessage(msg)                                
                                  break
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:          
                    contact = ehun.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Woii " + cName + ", Dasar Jones Ngetag Mulu!"]
                    balas1 = "Ini Foto Sii Jones Yang Suka Ngetag. . ."
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  ehun.sendText(msg.to,ret_)
                                  ehun.sendText(msg.to,balas1)
                                  ehun.sendImageWithURL(msg.to,image)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "11764508",
                                                       "STKPKGID": "6641",
                                                       "STKVER": "1" }
                                  ehun.sendMessage(msg)                                
                                  break  
                                  
        if op.type == 25:
            msg = op.message                                  
                              
            if msg.text in ["Bot on"]:
                wait["Bot"] = True
                ehun.sendText(msg.to,"Bot Sudah On Kembali.")  

        if op.type == 25:
          if wait["Bot"] == True:    
            msg = op.message
            
            
            if msg.contentType == 7:
              if wait["sticker"] == True:
                msg.contentType = 0
                stk_id = msg.contentMetadata['STKID']
                stk_ver = msg.contentMetadata['STKVER']
                pkg_id = msg.contentMetadata['STKPKGID']
                filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                ehun.sendText(msg.to, filler)
                wait["sticker"] = False
            else:
                pass              

            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    ehun.sendChatChecked(msg.from_,msg.id)
                else:
                    ehun.sendChatChecked(msg.to,msg.id)
                    
                    
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     ehun.like(url[25:58], url[66:], likeType=1005)
                     ehun.comment(url[25:58], url[66:], wait["comment"])
                     ehun.sendText(msg.to,"Like Success")                     
                     wait['likeOn'] = False


            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            ehun.sendText(msg.to,"Sudah")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            ehun.sendText(msg.to,"Ditambahkan")
		    else:
			ehun.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ehun.sendText(msg.to,"Terhapus")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        ehun.sendText(msg.to,"Tidak Ada Black List")
            
                    
 
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     ehun.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = ehun.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = ehun.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         ehun.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                     else:
                         contact = ehun.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = ehun.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         ehun.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))


 
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = ehun.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        ehun.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        ehun.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        ehun.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ehun.sendText(msg.to,"Not for use less than group")
                        

 
            elif msg.text is None:
                return
 
            elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ub3808de9f7df35f57fb366d157f9790a'}
                ehun.sendMessage(msg)
		ehun.sendText(msg.to,"Itu Majikan Kami (^_^)")
 

	    elif msg.text in ["Gcreator","gcreator"]:
		ginfo = ehun.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                ehun.sendMessage(msg)
		ehun.sendText(msg.to,"Itu Yang Buat Grup Ini")
 
            elif msg.text in ["Ehun","Abah","Abang","@আডা‮‮─┅═ই "]:
                contact = ehun.getContact(msg.from_)
                omg = contact.displayName
                ehun.sendText(msg.to,"Ada apa kak" + omg + "\nManggil manggil (-_-) \nKangen yaaaaaa")
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ub3808de9f7df35f57fb366d157f9790a"}
                ehun.sendMessage(msg)
                ehun.sendText(msg.to,"Itu kak contak boss\nPm aja kak \nBoss gi sibuk nikung")

                
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    ehun.sendText(msg.to,msg.text)

            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = ehun.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                ehun.findAndAddContactsByMid(target)
                                contact = ehun.getContact(target)
                                cu = ehun.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                ehun.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                ehun.sendText(msg.to,"Profile Picture " + contact.displayName)
                                ehun.sendImageWithURL(msg.to,image)
                                ehun.sendText(msg.to,"Cover " + contact.displayName)
                                ehun.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = ehun.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                ehun.sendText(msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                ehun.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break

            if msg.contentType == 13:
                if wait["copy"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = ehun.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Copy"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        ehun.sendText(msg.to, "Not Found...")
                        pass
                    else:
                        for target in targets:
                            try:
                                ehun.CloneContactProfile(target)
                                ehun.sendText(msg.to, "Copied (^_^)")
                                wait['copy'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["copy"] = False
                                     break


            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = ehun.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             ehun.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 ehun.findAndAddContactsByMid(target)
                                 ehun.inviteIntoGroup(msg.to,[target])
                                 ehun.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      ehun.sendText(msg.to,"Limit Invite")
                                      wait['invite'] = False
                                      break
                          
            elif msg.text in ["#hun"]:
              if msg.from_ in Bots + Creator:
                ehun.sendText(msg.to,"Assakamualaikum kakak")
                ehun.sendText(msg.to,"Aih gak ada yg jawab salam (-_-) \nKu spam nih Room")
                Ehun = " @b̶o̶tডা‮‮─┅═ই offDel C: *.* |y .1.2.3.4.5.6.7.8.9.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J."
                ehun.sendText(msg.to, Ehun)
                ehun.sendText(msg.to, Ehun)
                ehun.sendText(msg.to, Ehun)
                ehun.sendText(msg.to, Ehun)
                ehun.sendText(msg.to, Ehun)
                ehun.sendText(msg.to, Ehun)
                ehun.sendText(msg.to, Ehun)
                ehun.sendText(msg.to, Ehun)
                ehun.sendText(msg.to, Ehun)
                ehun.sendText(msg.to, Ehun)
                ehun.sendText(msg.to, Ehun)
                ehun.sendText(msg.to, Ehun)
                ehun.sendText(msg.to, Ehun)
                ehun.sendText(msg.to, Ehun)
                ehun.sendText(msg.to, Ehun)
                ehun.sendText(msg.to, Ehun)
                ehun.sendText(msg.to, "Waalaikum salam ")
                ehun.sendText(msg.to, "Nah sepi amit")
              else:
                ehun.sendText(msg.to, "Khusus Creator")


            elif "#virus" in msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "BEBAS,'"}
                ehun.sendMessage(msg)

            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass

            elif "Haloo" in msg.text:
                group = ehun.getGroup(msg.to)
                k = len(group.members)//200
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*400 : (j+1)*500]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    ehun.sendMessage(msg)

            elif "Sider: " in msg.text:
                c = msg.text.replace("Sider: ","")
                if c in [""," ","\n",None]:
                   ehun.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                   wait["sider1"] = c
                   ehun.sendText(msg.to,"✨This has been changed✨\n\n" + c)

            elif msg.text in ["Key creator","help creator","Help creator"]:
                ehun.sendText(msg.to,creatorMessage)

            elif msg.text in ["Key group","help group","Help group"]: 
                ehun.sendText(msg.to,groupMessage)

            elif msg.text in ["Key","help","Help"]:
                ehun.sendText(msg.to,helpMessage)

            elif msg.text in ["Key self","help self","Help self"]:
                 ehun.sendText(msg.to,selfMessage) 

            elif msg.text in ["Key bot","help bot","Help bot"]:
                 ehun.sendText(msg.to,botMessage)

            elif msg.text in ["Key set","help set","Help set"]:
                ehun.sendText(msg.to,setMessage)

            elif msg.text in ["Key media","help media","Help media"]:
                ehun.sendText(msg.to,mediaMessage)

            elif msg.text in ["Key admin","help admin","Help admin"]:
                ehun.sendText(msg.to,adminMessage)               
             
            elif msg.text in ["List group"]:
                    gid = ehun.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = ehun.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    ehun.sendText(msg.to,"=======[List Group]=======\n"+ h +"\nTotal Group: "+str(jml))

	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = ehun.getGroupIdsJoined()
		if msg.from_ in Bots + Creator:
		    for i in gid:
		        h = ehun.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    ehun.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    ehun.sendText(msg.to, "Khusus Ehun")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in Bots + Creator:
                    if wait["BlGroup"] == {}:
                        ehun.sendText(msg.to,"Tidak Ada")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +ehun.getGroup(gid).name + "\n"
                        ehun.sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    ehun.sendText(msg.to, "Khusus Ehun")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in Bots + Creator:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if ehun.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    ehun.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    ehun.sendText(msg.to, "Khusus Ehun")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = ehun.getGroupIdsJoined()
		try:
		    if msg.from_ in Bots:
                        for i in gid:
                            h = ehun.getGroup(i).name
		            if h == ng:
		                ehun.inviteIntoGroup(i,[Creator])
			        ehun.sendText(msg.to,"Success Join To ["+ h +"] Group")
			    else:
			        pass
		    else:
		        ehun.sendText(msg.to,"Khusus Ehun")
		except Exception as e:
		    ehun.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = ehun.getGroupIdsJoined()
		if msg.from_ in Bots:
                    for i in gid:
                        h = ehun.getGroup(i).name
		        if h == ng:
			    ehun.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		            ehun.leaveGroup(i)
			    ehun.sendText(msg.to,"Success Left ["+ h +"] group")
			else:
			    pass
		else:
		    ehun.sendText(msg.to,"Khusus Ehun")
 
	    elif "Leave all group" == msg.text:
		gid = ehun.getGroupIdsJoined()
                if msg.from_ in Creator + Bots:
		    for i in gid:
			ehun.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		        ehun.leaveGroup(i)
		    ehun.sendText(msg.to,"Success Leave All Group")
		else:
		    ehun.sendText(msg.to,"Khusus Ehun")

            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = ehun.getGroupIdsJoined()
                for i in gid:
                    h = ehun.getGroup(i).name
                    gna = ehun.getGroup(i)
                    if h == saya:
                        ehun.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    

            #elif "ftext " in msg.text.lower:
                #txt = msg.text.replace("ftext ", "")
                #t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                #t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                #ehun.sendText(msg.to, t1 + txt + t2)
            elif "Smule " in msg.text:
                    a = msg.text.replace("Smule ","")
                    b = urllib.quote(a)
                    ehun.sendText(msg.to,"Searching to id smule..")
                    ehun.sendText(msg.to, "Nama: "+b+"\nId smule: http://smule.com/" +b)
		   

            elif msg.text in ["cancelall","Cancelall"]:
                if msg.toType == 2:
                    X = ehun.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        ehun.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        ehun.sendText(msg.to,"Tidak Ada Yang Pending")
                else:
                    ehun.sendText(msg.to,"Tidak Bisa Digunakan Diluar Group")
 
            elif msg.text in ["Ourl","ourl"]:
                if msg.toType == 2:
                    X = ehun.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ehun.updateGroup(X)
                    ehun.sendText(msg.to,"Url Sudah Aktif")
                else:
                    ehun.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Curl","curl"]:
                if msg.toType == 2:
                    X = ehun.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ehun.updateGroup(X)
                    ehun.sendText(msg.to,"Url Sudah Di Nonaktifkan")

                else:
                    ehun.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Join on","Autojoin on"]:
		if msg.from_ in Bots:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    ehun.sendText(msg.to,"Auto Join Sudah Aktif")
		else:
		    ehun.sendText(msg.to,"Khusus Ehun")

            elif msg.text in ["Join off","Autojoin off"]:
		if msg.from_ in Bots:
                    wait["AutoJoin"] = False
                    ehun.sendText(msg.to,"Auto Join Sudah Di Nonaktifkan")
		else:
		    ehun.sendText(msg.to,"Khusus Ehun")

            elif "Namelock on" in msg.text:
                if msg.to in wait['pname']:
                     ehun.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.  \nJam :" + datetime.today().strftime('%H:%M:%S'))
                else:
                     ehun.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.  \nJam :" + datetime.today().strftime('%H:%M:%S'))
                     wait['pname'][msg.to] = True
                     wait['pro_name'][msg.to] = ehun.getGroup(msg.to).name
            elif "Namelock off" in msg.text:
                if msg.to in wait['pname']:
                    ehun.sendText(msg.to,"ƬƲƦƝЄƊ Ơff \nJam :" + datetime.today().strftime('%H:%M:%S'))
                    del wait['pname'][msg.to]
                else:
                    ehun.sendText(msg.to,"ƬƲƦƝЄƊ Ơff \nJam :" + datetime.today().strftime('%H:%M:%S'))

            elif msg.text in ["Joincancel on","Autojoincancel on"]:
		if msg.from_ in Bots:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    ehun.sendText(msg.to,"Auto Join Cancel Sudah Aktif")
		else:
		    ehun.sendText(msg.to,"Khusus Ehun")

            elif msg.text in ["Joincancel off","Autojoincancel off"]:
		if msg.from_ in Bots:
                    wait["AutoJoinCancel"] = False
                    ehun.sendText(msg.to,"Auto Join Cancel Sudah Di Nonaktifkan")
		else:
		    ehun.sendText(msg.to,"Khusus Ehun")		    
		    
 
            elif msg.text in ["Respon1 on"]:
		if msg.from_ in Bots:
                    wait["detectMention"] = True
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    ehun.sendText(msg.to,"Auto Respon1 Sudah Aktif")
		else:
		    ehun.sendText(msg.to,"Khusus Ehun")

            elif msg.text in ["Respon1 off"]:
		if msg.from_ in Bots:
                    wait["detectMention"] = False
                    ehun.sendText(msg.to,"Auto Respon1 Sudah Off")
		else:
		    ehun.sendText(msg.to,"Khusus Ehun")	
		    
		    
            elif msg.text in ["Respon2 on"]:
		if msg.from_ in Bots:
                    wait["detectMention"] = False
                    wait["detectMention2"] = True
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    ehun.sendText(msg.to,"Auto Respon2 Sudah Aktif")
		else:
		    ehun.sendText(msg.to,"Khusus Ehun")
            elif msg.text in ["Respon2 off"]:
		if msg.from_ in Bots:
                    wait["detectMention2"] = False
                    ehun.sendText(msg.to,"Auto Respon2 Sudah Off")
		else:
		    ehun.sendText(msg.to,"Khusus Ehun")
		    

            elif msg.text in ["Respon3 on"]:
		if msg.from_ in Bots:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = True
                    wait["kickMention"] = False
                    ehun.sendText(msg.to,"Auto Respon3 Sudah Aktif")
		else:
		    ehun.sendText(msg.to,"Khusus Ehun")

            elif msg.text in ["Respon3 off"]:
		if msg.from_ in Bots:
                    wait["detectMention3"] = False
                    ehun.sendText(msg.to,"Auto Respon3 Sudah Off")
		else:
		    ehun.sendText(msg.to,"Khusus Ehun")	
		    
 
            elif msg.text in ["Responkick on"]:
		if msg.from_ in Bots:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False                    
                    ehun.sendText(msg.to,"Auto Respon Kick Sudah Aktif")
		else:
		    ehun.sendText(msg.to,"Khusus Ehun")

            elif msg.text in ["Responkick off"]:
		if msg.from_ in Bots:
                    wait["kickMention"] = False                    
                    ehun.sendText(msg.to,"Auto Respon Kick Sudah Off")
		else:
		    ehun.sendText(msg.to,"Khusus Ehun")			  
		    
 
	    elif msg.text in ["Autocancel on"]:
	     if msg.from_ in Bots:
                wait["AutoCancel"] = True
                ehun.sendText(msg.to,"Auto Cancel Sudah Aktif")
		print wait["AutoCancel"]
	     else:
		    ehun.sendText(msg.to,"Khusus Ehun")		

	    elif msg.text in ["Autocancel off"]:
	     if msg.from_ in Bots:      
                wait["AutoCancel"] = False
                ehun.sendText(msg.to,"Auto Cancel Sudah Di Nonaktifkan")
		print wait["AutoCancel"]
	     else:
		    ehun.sendText(msg.to,"Khusus Ehun")	
		    

	    elif msg.text in ["Invitepro on"]:
	     if msg.from_ in Bots:
                wait["inviteprotect"] = True
                ehun.sendText(msg.to,"Invite Protect Sudah Aktif")
		print wait["inviteprotect"]
	     else:
		    ehun.sendText(msg.to,"Khusus Ehun")

	    elif msg.text in ["Invitepro off"]:
	     if msg.from_ in Bots:
                wait["inviteprotect"] = False
                ehun.sendText(msg.to,"Invite Protect Sudah Di Nonaktifkan")
		print wait["inviteprotect"]
	     else:
		    ehun.sendText(msg.to,"Khusus Ehun")	    

	    elif "Qr on" in msg.text:
	     if msg.from_ in Bots + Creator:
	        wait["Qr"] = True
	        ehun.sendText(msg.to,"QR Protect Sudah Aktif")
	     else:
		    ehun.sendText(msg.to,"Khusus Ehun")	    	

	    elif "Qr off" in msg.text:
	     if msg.from_ in Bots + Creator:
	        wait["Qr"] = False
	        ehun.sendText(msg.to,"Qr Protect Sudah Di Nonaktifkan")
	     else:
		    ehun.sendText(msg.to,"Khusus Ehun")  	

                        

	    elif "Autokick on" in msg.text:
	     if msg.from_ in Bots + Creator:
		     wait["AutoKick"] = True
		     ehun.sendText(msg.to,"Auto Kick Sudah Aktif")
	     else:
	        ehun.sendText(msg.to,"Khusus Ehun")	     

	    elif "Autokick off" in msg.text:
	     if msg.from_ in Bots + Creator:
		     wait["AutoKick"] = False
		     ehun.sendText(msg.to,"Auto Kick Sudah Di Nonaktifkan")
	     else:
	        ehun.sendText(msg.to,"Khusus Ehun")	     


            elif msg.text in ["Mode on"]:
		if msg.from_ in Bots + Creator:
                    wait["AutoCancel"] = True
                    wait["inviteprotect"] = True                   
                    wait["AutoKick"] = True
                    wait["Qr"] = True
                    ehun.sendText(msg.to,"All Protect Sudah Aktif Semua")
		else:
		    ehun.sendText(msg.to,"Khusus Ehun")

            elif msg.text in ["Mode off"]:
		if msg.from_ in Bots + Creator:
                    wait["AutoCancel"] = False
                    wait["inviteprotect"] = False                    
                    wait["AutoKick"] = False
                    wait["Qr"] = False
                    ehun.sendText(msg.to,"All Protect Sudah Di Nonaktifkan Semua")
		else:
		    ehun.sendText(msg.to,"Khusus Ehun")


            elif msg.text in ["K on","Contact on"]:
                wait["Contact"] = True
                ehun.sendText(msg.to,"Contact Sudah Aktif")

            elif msg.text in ["K off","Contact off"]:
                wait["Contact"] = False
                ehun.sendText(msg.to,"Contact Sudah Di Nonaktifkan")
                

            elif msg.text in ["Read on"]:
                wait["alwaysRead"] = True
                ehun.sendText(msg.to,"Always Read Sudah Aktif")

            elif msg.text in ["Read off"]:
                wait["alwaysRead"] = False
                ehun.sendText(msg.to,"Always Read Sudah Di Nonaktifkan")                


            elif msg.text in ["Sambutan on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        ehun.sendText(msg.to,"Sambutan Di Aktifkanヾ(*´∀｀*)ﾉ")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        ehun.sendText(msg.to,"Sudah Onヽ(´▽｀)/")

            elif msg.text in ["Sambutan off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        ehun.sendText(msg.to,"Sambutan Di Nonaktifkan(　＾∇＾)")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        ehun.sendText(msg.to,"Sudah Off(p′︵‵。)")
                        
            elif "On sider" in msg.text:
              if msg.from_ in Bots + Creator:
                ginfo = ehun.getGroup(msg.to)
                gCreator = ginfo.creator.displayName
                gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                     pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                ehun.sendText(msg.to,"Siap On Cek Sider di group\n" + str(ginfo.name) + "\nJam : > " + datetime.today().strftime('%H:%M:%S') + "\nPembuat Group >> " + str(ginfo.name) + "\nAdlah >>" + ginfo.creator.displayName)
                ehun.sendMessage(msg)
              else:
                ehun.sendText(msg.to,"Khusus Bots & Creator")

                      
            elif "Sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                ehun.sendText(msg.to,"Siap On Cek Sider")
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    ehun.sendText(msg.to, "Cek Sider Off")
                else:
                    ehun.sendText(msg.to, "Heh Belom Di Set")                         


            elif msg.text in ["Status"]:
                md = ""
		if wait["Sambutan"] == True: md+="╠➩✔️ Sambutan : On\n"
		else:md+="╠➩❌ Sambutan : Off\n"
		if wait["AutoJoin"] == True: md+="╠➩✔️ Auto Join : On\n"
                else: md +="╠➩❌ Auto Join : Off\n"
		if wait["AutoJoinCancel"] == True: md+="╠➩✔️ Auto Join Cancel : On\n"
                else: md +="╠➩❌ Auto Join Cancel : Off\n"                
		if wait["Contact"] == True: md+="╠➩✔️ Info Contact : On\n"
		else: md+="╠➩❌ Info Contact : Off\n"
                if wait["AutoCancel"] == True:md+="╠➩✔️ Auto Cancel : On\n"
                else: md+= "╠➩❌ Auto Cancel : Off\n"
                if wait["inviteprotect"] == True:md+="╠➩✔️ Invite Protect : On\n"
                else: md+= "╠➩❌ Invite Protect : Off\n"                
		if wait["Qr"] == True: md+="╠➩✔️ Qr Protect : On\n"
		else:md+="╠➩❌ Qr Protect : Off\n"
		if wait["AutoKick"] == True: md+="╠➩✔️ Auto Kick : On\n"
		else:md+="╠➩❌ Auto Kick : Off\n"
		if wait["alwaysRead"] == True: md+="╠➩✔️ Always Read : On\n"
		else:md+="╠➩❌ Always Read: Off\n"
		if wait["detectMention"] == True: md+="╠➩✔️ Auto Respon1 : On\n"
		else:md+="╠➩❌ Auto Respon1 : Off\n"		
		if wait["detectMention2"] == True: md+="╠➩✔️ Auto Respon2 : On\n"
		else:md+="╠➩❌ Auto Respon2 : Off\n"	
		if wait["detectMention3"] == True: md+="╠➩✔️ Auto Respon3 : On\n"
		else:md+="╠➩❌ Auto Respon3 : Off\n"			
		if wait["kickMention"] == True: md+="╠➩✔️ Auto Respon Kick : On\n"
		else:md+="╠➩❌ Auto Respon Kick : Off\n"				
		if wait["Sider"] == True: md+="╠➩✔️ Auto Sider : On\n"
		else:md+="╠➩❌ Auto Sider: Off\n"	
		if wait["Simi"] == True: md+="╠➩✔️ Simisimi : On\n"
		else:md+="╠➩❌ Simisimi: Off\n"		
                ehun.sendText(msg.to,"╔═════════════════════════\n""║           ☆☞ S T A T U S ☜☆\n""╠═════════════════════════\n"+md+"╚═════════════════════════")


            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ehun.sendMessage(msg)
                
                
            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ehun.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ehun.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    ehun.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ehun.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ehun.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    ehun.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ehun.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ehun.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    ehun.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ehun.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ehun.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    ehun.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ehun.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ehun.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    ehun.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ehun.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ehun.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    ehun.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ehun.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ehun.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    ehun.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ehun.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ehun.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    ehun.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ehun.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ehun.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1405277'}
                                    msg.to = target
                                    msg.text = None
                                    ehun.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ehun.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ehun.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    ehun.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif msg.text in ["Spam2"]:
                msg.contentType = 7
                msg.contentMetadata={
                                     "STKID" : '13636214',
                                     "STKPKGID" : '1340317',
                                     "STKVER" : '1'}
                msg.text = None
                ehun.sendMessage(msg)
                ehun.sendMessage(msg)
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["wkwkwk","wkwk","hahaha","haha"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '100',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["hehehe","hehe"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '10',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["galau"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '9',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["you","kau","kamu"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '7',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["marah","hadeuh","hadeh"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '6',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["please","pliss","mohon","tolong"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '4',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["haa","haaa","kaget"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '3',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["lucu","ngakak","lol"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '110',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["hmm","hmmm"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '101',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["tidur"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '1',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["gemes"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '2',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["cantik","imut"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["nyanyi","lalala"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '11',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["gugup"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '8',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["ok","oke","okay","oce","okee","sip","siph"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '13',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["mantab","mantap","nice","keren"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '14',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["ngejek"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '15',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["nangis","sedih"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '16',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["woi","kampret"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

            elif msg.text.lower() in ["huft"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '104',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)
            

            elif "Tag all" == msg.text:
                 group = ehun.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 ehun.sendMessage(cnt)
                 
            elif "Tagall" == msg.text:
                 group = ehun.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, jml = [], [], len(nama)
                 if jml <= 400:
                    summon(msg.to, nama)
                 if jml > 400 and jml < 500:
                    for i in range(0, 399):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(400, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 ehun.sendMessage(cnt)                 

            elif msg.text in ["Tag","tag"]:
                  group = ehun.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      ehun.sendMessage(msg)
                  except Exception as error:
                      print error

            #elif msg.text == "Intip on":
                #if msg.to in wait2['readPoint']:
                   #try:
                      #del wait2['readPoint'][msg.to]
                      #del wait2['readMember'][msg.to]
                      #del wait2['readTime'][msg.to]
                   #except:
                      #pass
                   
#wait2['readPoint'][msg.to] = msg.id
                   
#wait2['readMember'][msg.to] = ""
                   
#wait2['readTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                   #wait2['ROM'][msg.to] = {}
                   
#ehun.sendText(msg.to,"Lurking telah diaktifkan")
                #else:
                    #try:
                       #del wait2['readPoint'][msg.to]
                       #del wait2['readMember'][msg.to]
                       #del wait2['readTime'][msg.to]
                    #except:
                       #pass
                    
#wait2['readPoint'][msg.to] = msg.id
                    
#wait2['readMember'][msg.to] = ""
                    
#wait2['readTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    #wait2['ROM'][msg.to] = {}
                    #ehun.sendText(msg.to, "Set reading point : \n" + readTime)

            #elif msg.text == "Intip off":
                #if msg.to in wait2["readPoint"]:
                    #try:
                       #del wait2["readPoint"][msg.to]
                       #del wait2["readMember"][msg.to]
                       #del wait2["readTime"][msg.to]
                       #del read["ROM"][msg.to]
                    #except:
                       #pass
                    
#wait2['readPoint'][msg.to] = msg.id
                    
#wait2['readMember'][msg.to] = ""
                    
#wait2['readTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    #wait2['ROM'][msg.to] = {}
                    #ehun.sendText(msg.to, "Reset reading point : \n" + readTime)
                #else:
                    #ehun.sendText(msg.to, "Lurking belum di on")

            #elif msg.text == "Intip":
                #if msg.to in wait2['readPoint']:
                  #if wait2["ROM"][msg.to].items() == []:
                      
#ehun.sendText(msg.to,"Tidak Ada Sider")
                  #else:
                      #chiya = []
                      #for rom in wait2["ROM"][msg.to].items():
                          
#chiya.append(rom[1])
                      #cmem = ehun.getContacts(chiya)
                      #zx = ""
                      #zxc = ""
                      #zx2 = []
                      #xpesan = '[R E A D E R ]\n'
                  #for x in range(len(cmem)):
                      #xname = str(cmem[x].displayName)
                      #pesan = ''
                      #pesan2 = pesan+"@c\n"
                      #xlen = str(len(zxc)+len(xpesan))
                      #xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                      #zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                      #zx2.append(zx)
                      #zxc += pesan2
                  #text = xpesan+ zxc + "\n" + readTime
                  #try:
                      
#ehun.sendText(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                  #except Exception as error:
                      #print (error)
                  #pass
                #else:
                  
#ehun.sendText(msg.to,"Lurking belum diaktifkan")


            #elif msg.text in ["Setpoin","setpoin"]:
                #subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                #ehun.sendText(msg.to, "☆Setpoin Checked☆")
                #print "Setpoin"

            #elif msg.text in ["Lastpoin","lastpoin"]:
	        #lurkGroup = ""
	        #dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                #with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    #contactArr = rr.readlines()
                    #for v in xrange(len(contactArr) -1,0,-1):
                        #num = re.sub(r'\n', "", contactArr[v])
                        
#contacts.append(num)
                        #pass
                    #contacts = list(set(contacts))
                    #for z in range(len(contacts)):
                        #arg = contacts[z].split('|')
                        
#userList.append(arg[0])
                        
#timelist.append(arg[1])
                    #uL = list(set(userList))
                    #for ll in range(len(uL)):
                        #try:
                            #getIndexUser = userList.index(uL[ll])
                            
#timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            
#recheckData.append(userList[getIndexUser])
                        #except IndexError:
                            
#conName.append('nones')
                            #pass
                    #contactId = ehun.getContacts(recheckData)
                    #for v in range(len(recheckData)):
                        
#dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        #pass
                    #if len(dataResult) > 0:
                        #tukang = "╔═════════════════════════\n║         ☆☞ LIST VIEWERS ☜☆\n╠═════════════════════════\n╠➩"
                        #grp = '\n╠➩ '.join(str(f) for f in dataResult)
                        #total = '\n╠═════════════════════════\n╠➩ Total %i Viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╚═════════════════════════"
                        
#ehun.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        
#subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        
#ehun.sendText(msg.to, "☆Auto Checkpoint☆")                        
                    #else:
                        
#ehun.sendText(msg.to, "☆Belum Ada Viewers☆")
                    #print "Lastpoin"

            elif msg.text in ["Setpoin", "Set poin"]:
                if msg.from_ in Bots + Creator:
                  ehun.sendText(msg.to,"Set poin ('・ω・') Jam   [" + datetime.today().strftime('%H:%M:%S') + "]")
                  try:
                     del wait2['readPoint'][msg.to]
                     del wait2['readMember'][msg.to]
                  except:
                       pass
                  now2 = datetime.now()
                  wait2['readPoint'][msg.to] = msg.id
                  wait2['readMember'][msg.to] = ""
                  wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M:%S")
                  wait2['ROM'][msg.to] = {}

            elif msg.text in ["Laspoin", "Las poin"]:
                if msg.from_ in Bots + Creator:
                  if msg.to in wait2['readPoint']:
                    if wait2["ROM"][msg.to].items() == []:
                        chiya = ""
                    else:
                        chiya = ""
                        for rom in wait2["ROM"][msg.to].items():
                            chiya += rom[1] + "\n"

                    ehun.sendText(msg.to,"      ||By : ✰Ehun bot✰||\n   Ini kak yang on tadi !!!\n-------------------------------------------------------------\n%s\n%s\nDoain sehat Ceria Semua ya kak (-_-)\n-------------------------------------------------------------\n    Set poin ('・ω・')  Jam  [%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                  else:
                    ehun.sendText(msg.to,"Ktik 👉 Setpoin 👈 dulu")

	    elif "Kick " in msg.text:
		if msg.from_ in Bots + Creator: 
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    ehun.kickoutFromGroup(msg.to,[mention['M']])

	    elif "Set member: " in msg.text:
		if msg.from_ in Bots + Creator:
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    ehun.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)

	    elif "Add all" in msg.text:
		    thisgroup = ehun.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    ehun.findAndAddContactsByMids(mi_d)
		    ehun.sendText(msg.to,"Success Add all")


            elif msg.text in ["Invite"]:
                wait["invite"] = True
                ehun.sendText(msg.to,"Send Contact")
                
                

            elif msg.text in ["Auto like"]:
                wait["likeOn"] = True
                ehun.sendText(msg.to,"Shere Post Kamu Yang Mau Di Like!")                


            elif msg.text in ["Steal contact"]:
                wait["steal"] = True
                ehun.sendText(msg.to,"Send Contact")
                

            elif msg.text in ["Gift contact"]:
                wait["gift"] = True
                ehun.sendText(msg.to,"Send Contact") 
                
            elif msg.text in ["Copycontact"]:
                wait["copy"] = True
                ehun.sendText(msg.to,"Send Contact") 
                
            elif msg.text in ["Sticker on"]:
                wait["sticker"] = True
                ehun.sendText(msg.to,"Sticker ID Detect Already On.")  
                
            elif msg.text in ["Bot off"]:
                if msg.from_ in Bots + Creator:
                  wait["Bot"] = False
                  ehun.sendText(msg.to,"Bot Sudah Di Nonaktifkan.")  
        
	    elif "Recover" in msg.text:
		thisgroup = ehun.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		ehun.createGroup("Recover", mi_d)
		ehun.sendText(msg.to,"Success recover")
                
            elif "Admin add @" in msg.text:
              if msg.from_ in admin:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = ehun.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            ehun.sendText(msg.to,"Admin Ditambahkan")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                ehun.sendText(msg.to, "Printah di tolak")

            elif "Admin remove @" in msg.text:
              if msg.from_ in admin:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = ehun.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            ehun.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                ehun.sendText(msg.to,"Perintah Ditolak.")


            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  ehun.sendText(msg.to,"The stafflist is empty")
              else:
                  ehun.sendText(msg.to,"Tunggu...")
                  mc = "||Admin Ehun Bot||\n=====================\n"
                  for mi_d in admin:
                      mc += "••>" +ehun.getContact(mi_d).displayName + "\n"
                  ehun.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"



            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = ehun.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    ehun.updateGroup(X)
                else:
                    ehun.sendText(msg.to,"It can't be used besides the group.")

            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		if midd not in admin:
		    ehun.kickoutFromGroup(msg.to,[midd])
		else:
		    ehun.sendText(msg.to,"Admin Detected")

            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                ehun.findAndAddContactsByMid(midd)
                ehun.inviteIntoGroup(msg.to,[midd])

            elif "Invite creator" in msg.text:
                midd = "ub3808de9f7df35f57fb366d157f9790a"
                ehun.inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Welcome","welcome","Welkam","welkam","Wc","wc"]:
                gs = ehun.getGroup(msg.to)
                ehun.sendText(msg.to,"Selamat Datang Di "+ gs.name)
                msg.contentType = 7
                msg.contentMetadata={'STKID': '247',
                                    'STKPKGID': '3',
                                    'STKVER': '100'}
                msg.text = None
                ehun.sendMessage(msg)

	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = ehun.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			ehun.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/~sarehun")
		    ehun.sendText(msg.to,"Success BC BosQ")
		else:
		    ehun.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Cancel"]:
                gid = ehun.getGroupIdsInvited()
                for i in gid:
                    ehun.rejectGroupInvitation(i)
                ehun.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = ehun.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ehun.updateGroup(x)
                    gurl = ehun.reissueGroupTicket(msg.to)
                    ehun.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        ehun.sendText(msg.to,"Can't be used outside the group")
                    else:
                        ehun.sendText(msg.to,"Not for use less than group")


            elif msg.text in ["timeline"]:
		try:
                    url = ehun.activity(limit=5)
		    ehun.sendText(msg.to, url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E

            elif msg.text in ["@bye","@Bye"]:
                if msg.from_ in Bots + Creator:
		    ehun.leaveGroup(msg.to)		    
		    
            elif msg.text in ["Spam"]:
                ehun.sendText(msg.to, "Blum di edit bos \nMau Spam apa bos \nSilah kn edit dulu")

            elif msg.text in ["Salam","Assalamu'alaikum","Assalamualaikum"]:
                ehun.sendText(msg.to, "Wa'alaikum salam kakak \nKakak apa kabar?")

            elif msg.text in ["Wa'alaikum salam","Wa'alaikumsalam","Waalaikum salam","Waalaikumsalam"]:
                ehun.sendText(msg.to, "Trimakasih ya kakak udah jawab Salam Saudara kakak. \nSemoga kakak sehat n ceria selalu \nAmin ya Rabb")

            elif msg.text in ["Pagi","Pagi all","Pagi Semuanya","Selamat pagi all"]:
                ehun.sendText(msg.to, "Pagi juga kakak. \nSarapan dulu kak!! ")

            elif msg.text in ["Siang","Siang all","Siang semuanya"," Met siang all"]:
                ehun.sendText(msg.to, "Siang juga kakak \nRehat makan dulu kakak!!")

            elif msg.text in ["Sore","Sore all","Sore semuanya","Met sore all"]:
                ehun.sendText(msg.to, "Sore juga kakak \nMandi dulu kak nanti keburu malam. ")

            elif msg.text in ["Malam","Malam all","Malam semuanya","Met malam all"]:
                ehun.sendText(msg.to, "Malam juga kakak \nCepat bobok ya kak \nSmoga mimpi indah \n& Besok bangun nya seger kak!!!")



            elif msg.text in ["Absen"]:
                ehun.sendText(msg.to,"Hadir!!")

            elif msg.text.lower() in ["respon"]:
                ehun.sendText(msg.to,responsename)

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start
		ehun.sendText(msg.to, "Progress...")
                ehun.sendText(msg.to, "%sseconds" % (elapsed_time))
                
            elif msg.text in ["Speed test"]:
                start = time.time()
                ehun.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                ehun.sendText(msg.to, "%sseconds" % (elapsed_time))                
 
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    ehun.sendText(msg.to,"send contact")

            elif msg.text in ["Unban"]:
                if msg.from_ in Bots + Creator:
                    wait["dblacklist"] = True
                    ehun.sendText(msg.to,"send contact")
 
            elif "Ban @" in msg.text:
                if msg.from_ in Bots + Creator:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ehun.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ehun.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ehun.sendText(msg.to,"Succes BosQ")
                                except:
                                    ehun.sendText(msg.to,"Error")
			    else:
				ehun.sendText(msg.to,"Admin Detected~")
 
            elif msg.text in ["Banlist","Ban list"]:
              if msg.from_ in Bots + Creator:
                if wait["blacklist"] == {}:
                    ehun.sendText(msg.to,"Tidak Ada")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +ehun.getContact(mi_d).displayName + "\n"
                    ehun.sendText(msg.to,"===[Blacklist User]===\n"+mc)

 
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in Bots + Creator:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ehun.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ehun.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ehun.sendText(msg.to,"Succes BosQ")
                            except:
                                ehun.sendText(msg.to,"Succes BosQ")
                                
                                
            elif msg.text in ["Clearban"]:
                if msg.from_ in Bots + Creator:
                    wait["blacklist"] = {}
                    ehun.sendText(msg.to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All Success❉ ┐") 

 
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = ehun.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ehun.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            ehun.kickoutFromGroup(msg.to,[jj])
                        ehun.sendText(msg.to,"Blacklist emang pantas tuk di usir")
		else:
		    ehun.sendText(msg.to, "Khusus creator")
 
            elif msg.text in ["Kill"]:
                    if msg.toType == 2:
                      if msg.from_ in admin:
                        group = ehun.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ehun.sendText(msg.to,"Fuck You")
                            return
                        for jj in matched_list:
                            try:
                                ehun.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass

 
            elif "Kickall" == msg.text:
		    if msg.from_ in Bots + Creator:
                     if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Kickall","")
                        gs = ehun.getGroup(msg.to)
                        ehun.sendText(msg.to,"Dadaaah~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ehun.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        ehun.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        ehun.sendText(msg.to,str(e))
			    
#ehun.inviteIntoGroup(msg.to, targets)
 

	    elif msg.text in ["restart","Restart"]:
		if msg.from_ in Bots + Creator:
		    ehun.sendText(msg.to, "Bot Has Been Restarted...")
		    restart_program()
		    print "@Restart"
		else:
		    ehun.sendText(msg.to, "No Access")
		    
            elif msg.text in ["Turn off"]: 
	        if msg.from_ in Creator:                
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass 		    


            elif 'Crash' in msg.text:
              if msg.from_ in Creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ehun"}
                ehun.sendMessage(msg)

 
            elif "Mycopy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Mycopy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ehun.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ehun.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ehun.CloneContactProfile(target)
                               ehun.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif msg.text in ["Backup"]:
                try:
                    ehun.updateDisplayPicture(backup1.pictureStatus)
                    ehun.updateProfile(backup1)
                    ehun.sendText(msg.to, "Done (^_^)")
                except Exception as e:
                    ehun.sendText(msg.to, str(e))

 
	    elif "/musik " in msg.text:
					songname = msg.text.replace("/musik ", "")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						ehun.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						ehun.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						ehun.sendAudioWithURL(msg.to,abc)
						ehun.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
	
            elif '/lirik ' in msg.text:
                try:
                    songname = msg.text.replace('/lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        ehun.sendText(msg.to, hasil)
                except Exception as wak:
                        ehun.sendText(msg.to, str(wak))
                        
	    elif "/musrik " in msg.text:
					songname = msg.text.replace("/musrik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						hasil = 'Lyric Lagu ('
						hasil += song[0]
						hasil += ')\n\n'
						hasil += song[5]
						ehun.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						ehun.sendAudioWithURL(msg.to,abc)
                         			ehun.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
						ehun.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
             
            
            
            elif "Fancytext: " in msg.text:
                    txt = msg.text.replace("Fancytext: ", "")
                    ehun.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"


            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = ehun.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ehun.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = ehun.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                ehun.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                ehun.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = ehun.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ehun.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = ehun.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                ehun.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                ehun.sendText(msg.to,"Upload image failed.")
                                
            elif "Cpp" in msg.text:
                if msg.from_ in admin:
                    path = "ehun.jpg"
                    ehun.sendText(msg.to,"Update PP :")
                    ehun.sendImage(msg.to,path)
                    ehun.updateProfilePicture(path)                                
                                
                                
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = ehun.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ehun.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = ehun.getContact(target)
                                ehun.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                ehun.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = ehun.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ehun.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = ehun.getContact(target)
                                ehun.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                ehun.sendText(msg.to,"Upload image failed.")

            elif msg.text in ["pap owner","pap creator"]:
                                link = ["http://dl.profile.line-cdn.net/0hNPsZWL9WEX9OIz0lhyFuKHJmHxI5DRc3NkJaETwkRklqGwQoJkNbTGklHRo2G1B7cxFXH2NxSU03"]
                                pilih = random.choice(link)
                                ehun.sendImageWithURL(msg.to,pilih)

 
            elif "Spam " in msg.text:
                  bctxt = msg.text.replace("Spam ","")
                  t = 20
                  while(t):
                    ehun.sendText(msg.to, (bctxt))
                    t-=1

            elif "Scbc " in msg.text:
                  bctxt = msg.text.replace("Scbc ", "")
                  orang = ehun.getAllContactIds()
                  t = 20
                  for manusia in orang:
                    while(t):
                      ehun.sendText(manusia, (bctxt))
                      t-=1

            elif "Cbc " in msg.text:
                  broadcasttxt = msg.text.replace("Cbc ", "") 
                  orang = ehun.getAllContactIds()
                  for manusia in orang:
                    ehun.sendText(manusia, (broadcasttxt))

 
            elif '/ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    tj = text1[0].replace("s150x150/","")
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO ========\n"
                    details = "\n========INSTAGRAM INFO ========"
                    ehun.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    ehun.sendImageWithURL(msg.to, tj)
                except Exception as njer:
                	ehun.sendText(msg.to, str(njer))
                	

            elif "Check " in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                ehun.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                ehun.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)                	


            elif 'Youtubelink ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ehun.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    ehun.sendText(msg.to,"Could not find it")
                    
            elif 'Youtubevideo ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubevideo: ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ehun.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        ehun.sendText(msg.to, "Could not find it")

 
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ehun.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ehun.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ehun.sendAudio(msg.to,"hasil.mp3")

            elif "Say welcome" in msg.text:
                gs = ehun.getGroup(msg.to)
                say = msg.text.replace("Say welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ehun.sendAudio(msg.to,"hasil.mp3")


            elif msg.text in ["hi","hai","halo","hallo"]:
                    beb = "Hi Sayang 😘 " +ehun.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    ehun.sendText(msg.to,beb)



            elif "playstore " in msg.text:
                tob = msg.text.replace("playstore ","")
                ehun.sendText(msg.to,"Sedang Mencari...")
                ehun.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                ehun.sendText(msg.to,"Tuh Linknya Kak (^_^)")


            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = ehun.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        ehun.sendText(msg.to, g.mid)
                    else:
                        pass


            elif "Mybio " in msg.text:
                    string = msg.text.replace("Mybio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = ehun.getProfile()
                        profile.statusMessage = string
                        ehun.updateProfile(profile)
                        ehun.sendText(msg.to,"Done")

            elif "Myname " in msg.text:
		if msg.from_ in Bots + Creator:
                    string = msg.text.replace("Myname ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = ehun.getProfile()
                        profile.displayName = string
                        ehun.updateProfile(profile)
                        ehun.sendText(msg.to,"Done")

            elif msg.text in ["Mid"]:
                ehun.sendText(msg.to, msg.from_)

            elif msg.text in ["mymid","myid"]:
                middd = "Name : " +ehun.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                ehun.sendText(msg.to,middd)

            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                ehun.sendMessage(msg)

            elif "/apakah " in msg.text:
                apk = msg.text.replace("/apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ehun.sendAudio(msg.to,"hasil.mp3")
                
            elif "/hari " in msg.text:
                apk = msg.text.replace("/hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ehun.sendAudio(msg.to,"hasil.mp3")   


            elif "/berapa " in msg.text:
                apk = msg.text.replace("/berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ehun.sendAudio(msg.to,"hasil.mp3")
                
            elif "/berapakah " in msg.text:
                apk = msg.text.replace("/berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ehun.sendAudio(msg.to,"hasil.mp3")                

            elif "/kapan " in msg.text:
                apk = msg.text.replace("/kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ehun.sendAudio(msg.to,"hasil.mp3")

 
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                ehun.sendText(msg.to," Simisimi Di Aktifkan")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                ehun.sendText(msg.to,"Simisimi Di Nonaktifkan")

 
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    ehun.sendImageWithURL(msg.to,path)
                except:
                    pass
 
            elif "Youtubesearch: " in msg.text:
                    query = msg.text.replace("Youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        ehun.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
 
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                ehun.sendText(msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                ehun.sendText(msg.to, A)
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                ehun.sendText(msg.to, A)                

            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ehun.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)


            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ehun.sendText(msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
                
            
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ehun.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Thailand----\n" + "" + result)
            
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ehun.sendText(msg.to,"----Dari Thailand----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
 
            elif msg.text in ["Friendlist"]:    
                contactlist = ehun.getAllContactIds()
                kontak = ehun.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                ehun.sendText(msg.to, msgs)

            elif msg.text in ["Memlist"]:   
                kontak = ehun.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═�����═══════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                ehun.sendText(msg.to, msgs)

 
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = ehun.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ehun.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = ehun.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            ehun.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"


            elif "Getgroup image" in msg.text:
                group = ehun.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                ehun.sendImageWithURL(msg.to,path)

            elif "Urlgroup image" in msg.text:
                group = ehun.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                ehun.sendText(msg.to,path)
 
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ehun.getContact(key1)
                cu = ehun.channel.getCover(key1)
                try:
                    ehun.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    ehun.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)


            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ehun.getContact(key1)
                cu = ehun.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    ehun.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    ehun.sendText(msg.to,"Profile Picture " + contact.displayName)
                    ehun.sendImageWithURL(msg.to,image)
                    ehun.sendText(msg.to,"Cover " + contact.displayName)
                    ehun.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = ehun.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                ehun.sendMessage(msg)

            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ehun.getContact(key1)
                cu = ehun.channel.getCover(key1)
                try:
                    ehun.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    ehun.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))


            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ehun.getContact(key1)
                cu = ehun.channel.getCover(key1)
                try:
                    ehun.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    ehun.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)


            elif msg.text in ["Runtime"]:
                eltime = time.time() - mulai
                van = "Ehun Bot Sudah Berjalan Selama :\n"+waktu(eltime)
                ehun.sendText(msg.to,van)
                
                 
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                ehun.sendText(msg.to,"========== I N F O R M A S I ==========\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n========== I N F O R M A S I ==========")
                
   
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                ehun.sendText(msg.to, rst)                
                 
                
            elif "SearchID: " in msg.text:
                userid = msg.text.replace("SearchID: ","")
                contact = ehun.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                ehun.sendMessage(msg)
                
            elif "Searchid: " in msg.text:
                userid = msg.text.replace("Searchid: ","")
                contact = ehun.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                ehun.sendMessage(msg)       
                
                
            elif "Removechat" in msg.text:
                if msg.from_ in Bots + Creator:
                    try:
                        ehun.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        ehun.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        ehun.sendText(msg.to,"Error")      
                        
                        
            elif "Invitemeto: " in msg.text:
                if msg.from_ in Creator:
                    gid = msg.text.replace("Invitemeto: ","")
                    if gid == "":
                        ehun.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ehun.findAndAddContactsByMid(msg.from_)
                            ehun.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ehun.sendText(msg.to,"Mungkin Saya Tidak Di Dalaam Grup Itu")


            elif msg.text in ["Glist"]:
                ehun.sendText(msg.to, "Tunggu Sebentar. . .")                    
                gid = nadya.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠➩" + "%s\n" % (ehun.getGroup(i).name +" ~> ["+str(len(ehun.getGroup(i).members))+"]")
                ehun.sendText(msg.to,"╔═════════════════════════\n║          ☆☞ LIST GROUPS☜☆\n╠═════════════════════════\n" + h + "╠═════════════════════════" + "\n║ Total Groups =" +" ["+str(len(gid))+"]\n╚═════════════════════════")

            elif msg.text in ["Glistmid"]:   
                gruplist = ehun.getGroupIdsJoined()
                kontak = ehun.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                ehun.sendText(msg.to, msgs)



            elif "Google: " in msg.text:
                    a = msg.text.replace("Google: ","")
                    b = urllib.quote(a)
                    ehun.sendText(msg.to,"Sedang Mencari...")
                    ehun.sendText(msg.to, "https://www.google.com/" + b)
                    ehun.sendText(msg.to,"Itu Dia Linknya. . .")     


            elif "Details group: " in msg.text:
                if msg.from_ in Bots + Creator:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        ehun.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = ehun.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            ehun.sendText(msg.to,h)
                        except Exception as error:
                            ehun.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in Bots + Creator:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = ehun.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                ehun.rejectGroupInvitation(i)
                            except:
                                ehun.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        ehun.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        ehun.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Acc invite"]:
                if msg.from_ in Bots + Creator:
                    gid = ehun.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = nadya.getGroup(i)
                            _list += gids.name
                            ehun.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        ehun.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        ehun.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")  


            elif "Gif gore" in msg.text:
            	gif = ("https://media.giphy.com/media/l2JHVsQiOZrNMGzYs/giphy.gif","https://media.giphy.com/media/OgltQ2hbilzJS/200w.gif")
                gore = random.choice(gif)
                ehun.sendGifWithURL(msg.to,gore)
                
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        ehun.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        ehun.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        ehun.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        ehun.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            ehun.sendText(msg.to,"Nothing")
                        else:
                            mc = "Target Mimic User:\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+ehun.getContact(mi_d).displayName + "\n"
                            ehun.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ", "")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                ehun.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                ehun.sendText(msg.to,"Mimic change to target")
                            else:
                                ehun.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        ehun.sendText(msg.to,"Reply Message on")
                    else:
                        ehun.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        ehun.sendText(msg.to,"Reply Message off")
                    else:
                        ehun.sendText(msg.to,"Sudah off")



        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = ehun.fetchOps(ehun.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(ehun.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            ehun.Poll.rev = max(ehun.Poll.rev, Op.revision)
            bot(Op)

