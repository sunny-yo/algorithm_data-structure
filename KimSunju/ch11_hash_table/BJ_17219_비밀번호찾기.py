import sys

sys.stdin = open("input.txt", "r")
SITE, PW = sys.stdin.readline().split()

pw_dic = {}

for i in range(int(SITE)):
    site, pw = sys.stdin.readline().split()
    pw_dic[site] = pw

for i in range(int(PW)):
    site = sys.stdin.readline().rsplit()[0]
    print(pw_dic[site])

''' input.txt
16 4
noj.am IU
acmicpc.net UAENA
startlink.io THEKINGOD
google.com ZEZE
nate.com VOICEMAIL
naver.com REDQUEEN
daum.net MODERNTIMES
utube.com BLACKOUT
zum.com LASTFANTASY
dreamwiz.com RAINDROP
hanyang.ac.kr SOMEDAY
dhlottery.co.kr BOO
duksoo.hs.kr HAVANA
hanyang-u.ms.kr OBLIVIATE
yd.es.kr LOVEATTACK
mcc.hanyang.ac.kr ADREAMER
startlink.io
acmicpc.net
noj.am
mcc.hanyang.ac.kr
'''