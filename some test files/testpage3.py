
tageswords = [['heave', 'v.举起;n.举起'], ['ivory', 'n.象牙'], ['passive', 'adj.被动的'], ['clone', 'n.无性系,无性繁殖,克隆;v.无性繁殖,复制'], ['remedy', 'n.药物,治疗法,补救,赔偿;vt.治疗,补救,矫正,修缮,修补'], ['council', 'n.政务会,理事会,委员会,参议会,讨论会议,顾问班子,立法班子'], ['apt', 'adj.易于...的,有...倾向的,灵敏的,灵巧的,适当的,切题的,敏捷,倾向是'], ['quantify', 'vt.确定数量;v.量化'], ['bewilder', 'vt.使迷惑,使不知所措,使昏乱'], ['census', 'n.人口普查'], ['religious', 'adj.信奉宗教的,虔诚的,宗教上的,修道的,严谨的;n.僧侣,尼姑,修道士'], ['compartment', 'n.间隔间,车厢'], ['offense', 'n.进攻'], ['culminate', 'v.达到顶点'], ['adore', 'v.崇拜,爱慕,(口语)喜爱'], ['pressure', 'n.压,压力,电压,压迫,强制,紧迫'], ['vehicle', 'n.交通工具,车辆,媒介物,传达手段'], ['odor', 'n.气味,名声'], ['pest', 'n.有害物'], ['clasp', 'n.扣子,钩,紧握,抱住;v.扣紧,紧握,搂抱,密切合作'], ['score', 'n.得分,乐谱,抓痕,二十,终点线,刻痕,帐目,起跑线;vt.把...记下,刻划,划线,获得,评价;vi.记分,刻痕,得分'], ['champion', 'n.冠军,拥护者,战士;vt.拥护,支持'], ['calorie', 'n.卡路里'], ['blaze', 'n.火焰,光辉,情感爆发;vi.燃烧,照耀,激发;vt.在树皮上刻路标,公开宣布'], ['flexible', 'adj.柔韧性,易曲的,灵活的,柔软的,能变形的,可通融的'], ['originate', 'vt.引起,发明,发起,创办;vi.起源,发生'], ['verse', 'n.韵文,诗,诗节,诗句,诗篇'], ['clue', 'n.线索'], ['contest', 'n.论争,竞赛;v.,争论,争辩,竞赛,争夺'], ['climax', 'n.高潮,顶点'], ['intelligent', 'adj.聪明的,伶俐的,有才智的,[计]智能的'], ['target', 'n.目标,对象,靶子'], ['boring', 'n.钻(孔);adj.令人厌烦的'], ['proficiency', 'n.熟练,精通,熟练程度'], ['straightforward', 'adj.正直的,坦率的,简单的,易懂的,直接了当的;adv.坦率地'], ['litter', 'n.垃圾,(供动物睡眠或防冻用的)干草,树叶,(一)窝,轿,担架;vt.乱丢,铺草,弄乱;vi.产仔,乱丢垃圾'], ['evolution', 'n.进展,发展,演变,进化'], ['incur', 'v.招致'], ['fossil', 'n.化石,僵化的事物;adj.化石的,陈腐的,守旧的'], ['quartz', 'n.石英'], ['catastrophe', 'n.大灾难,大祸'], ['permeate', 'vt.弥漫,渗透,透过,充满;vi.透入'], ['impart', 'vt.给予(尤指抽象事物),传授,告知,透露'], ['stun', 'vt.使晕倒,使惊吓,打晕;n.晕眩,打昏,惊倒'], ['volume', 'n.卷,册,体积,量,大量,音量'], ['exchange', 'vt.交换,调换,兑换,交流,交易;n.交换,调换,兑换,交流,交易'], ['float', 'n.漂流物,浮舟,浮萍,彩车;vi.浮动,飘浮,散播,摇摆,(计划等)付诸实行;vt.使漂浮,容纳,淹没,发行,用水注满'], ['phase', 'n.阶段,状态,相,相位;v.定相'], ['whirl', 'v.(使)旋转,急动,急走;n.旋转,—连串快速的活动'], ['heel', 'n.脚后跟,踵,跟部']]
choice = "CET6"
targetdict = choice+"_edited1.txt"

with open(targetdict, "r") as fp:
    lines = fp.readlines()

with open(targetdict, "w") as fp:
    for i, line in enumerate(lines):
        # seperate each line into parts so I can get the first item in this line
        oneline = line.strip("\n")
        newoneline = oneline.split()
        # go through each word in the tageswords list
        for items in tageswords:
            # pick the first English word in this item and compare with the first one of first item in the line
            if items[0] == newoneline[0]:
                # if these two are different then keep this line in the file
                print(items[0], newoneline[0])
                del lines[i]

new_file = open("CET6_edited1.txt", "w+")
for line in lines:
    new_file.write(line)
new_file.close()