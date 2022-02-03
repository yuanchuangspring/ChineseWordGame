from xpinyin import Pinyin
from colorama import Fore,Back,Style
import random
print("欢迎游玩本游戏！你有十次机会猜一个四字成语，系统将会根据你的答案给予回复，标绿的部分表示该部分在其正确的位置，标黄的部分表示其在答案中但是不在正确的位置上。\n本游戏复刻自https://handle.antfu.me/，请支持原版！")
cs=1
p=Pinyin()
a="行尸走肉、金蝉脱壳、百里挑一、金玉满堂、背水一战、霸王别姬、天上人间、不吐不快、海阔天空、情非得已、满腹经纶、兵临城下、春暖花开、插翅难逃、黄道吉日、天下无双、偷天换日、两小无猜、卧虎藏龙、珠光宝气、簪缨世族、花花公子、绘声绘影、国色天香、相亲相爱、八仙过海、金玉良缘、掌上明珠、皆大欢喜、逍遥法外、摇头摆尾、左顾右盼、大摇大摆、跋山渡水、餐风饮露、水送山迎、赏心顺眼、朝气蓬勃、心狠手辣、起早贪黑、神通泛博、挺拔入云、张灯结彩、欢聚一堂、率土同庆、喜气洋洋、百花怒放、争奇斗艳、花团锦簇、色色俱全、满意洋洋、天长日久、恃势凌人、将信将疑、春回大地、兴致勃勃、精卫填海、愚公移山、百折不挠、一往无前、骨肉之情、息息相关、五颜六色、欢声雷动、欣喜若狂、手舞足蹈、灯火灿烂、春暖花开、春色满园、春景明丽、理直气壮、辩论不休、充满决心、草木皆兵、螳螂捕蝉、鹬蚌相争、眉飞色舞、古今中外、不由自主、心绪不宁、各奔工具、离合悲欢、手足情深、蓬兴旺勃、层次分明、曲折小路、文思火速、伶俐过人、后来居上、按兵不动、操之过急、轻举妄动、兴风作浪、蠢蠢欲动、雷厉风行、闻风远扬、展翅高飞、望而却步、窃窃密语、烟波浩渺、一碧万顷、游人如织、一帆风顺、海不扬波、鸥水相依、海波不惊、揠苗滋长、郑人买履、漫山遍野、绿叶成阴、海枯石烂、树大根深、自在自由、人山人海、情深似海、恩重如山、循序渐进、由浅入深、积少成多、多谋善断、不迟不疾、方寸不乱、金风送爽、雁过留声、秋色恼人、临渴掘井、不由自主、喃喃自语、临危不惧、"
alist=a.split("、")
ran=random.randint(0,len(alist)-1)
answer=alist[ran]
iif=0
while cs<=10:
    cc=input("这是您第"+str(cs)+"次尝试，猜一个成语叭:")
    
    cs=cs+1
    pin=p.get_pinyin(cc,tone_marks="marks",splitter=' ')
    print(pin,"\n",cc)
    print("稍等，正在处理结果...")
    an=list(answer)
    anpin=p.get_pinyin(answer,tone_marks="numbers",splitter=' ').split(" ")
    anpinyin=list(p.get_pinyin(answer,tone_marks="numbers",splitter=' '))
    ccc=list(cc)
    ccpin=p.get_pinyin(cc,tone_marks="numbers",splitter=' ').split(" ")
    ccpinyin=list(p.get_pinyin(cc,tone_marks="numbers",splitter=' '))
    zz=0
    outzi=""
    outpin=""
    for i in ccpin:
        cuncun=list(i)
        for o in cuncun:
            if o in anpin[zz]:
                outpin=outpin+Fore.GREEN+o
            elif o in anpinyin:
                outpin=outpin+Fore.YELLOW+o
            else:
                outpin=outpin+Fore.RESET+o
        outpin=outpin+" "
        zz=zz+1
    print(outpin)
    zz=0
    for i in ccc:
        if i in an and i==an[zz]:
            outzi=outzi+Fore.GREEN+i
            
        elif i in an and i != an[zz]:
            outzi=outzi+Fore.YELLOW+i
        else:
            outzi=outzi+Fore.RESET+i
        zz=zz+1
        outzi=outzi+"   "
    print(outzi)
    print(Fore.RESET)
    if cc == answer:
        print(Fore.GREEN+"恭喜你!回答正确!")
        iif=1
        break
    
if  not iif==1:    
    youan=input("十次机会已经用完，请告诉我你的答案:")
    if youan==answer:
        print(Fore.GREEN+"恭喜你!回答正确!")
    else:
        print(Fore.RED+"回答错误!") 