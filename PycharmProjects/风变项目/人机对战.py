# 拳皇-人机对战1.0
import time, random

player_victory = 0
enemy_victory = 0

for i in range(1, 4):
    time.sleep(2)  # 让局与局之间有较明显的有时间间隔
    print('  \n——————现在是第 %s 局——————' % i) # 作为局的标记
    # 对比之前：(' \n——————现在是第'+str(i)+'局——————') %格式简洁版本
    player_life = random.randint(100, 150)
    player_attack = random.randint(30, 50)
    enemy_life = random.randint(100, 150)
    enemy_attack = random.randint(30, 50)

    # 展示双方角色的属性
    print('【玩家】\n血量：{}\n攻击：{}'.format(player_life,player_attack)) #format 格式简洁版本
    print('------------------------')
    time.sleep(1)
    print('【敌人】\n' + '血量：' + str(enemy_life) + '\n攻击：' + str(enemy_attack))
    print('------------------------')
    time.sleep(1)

    # 双方PK
    while player_life > 0 and enemy_life > 0:
        player_life = player_life - enemy_attack
        enemy_life = enemy_life - player_attack
        print('你发起了攻击，【敌人】剩余血量' + str(enemy_life))
        print('敌人向你发起了攻击，【玩家】剩余血量' + str(player_life))
        print('-----------------------')
        time.sleep(1.5)

    # 打印最终战果
    if player_life > 0 and enemy_life <= 0:
        player_victory += 1
        print('敌人死翘翘了，你赢了！')
    elif player_life <= 0 and enemy_life > 0:
        enemy_victory += 1
        print('悲催，敌人把你干掉了！')
    else:
        print('哎呀，你和敌人同归于尽了！')

if player_victory > enemy_victory:
    time.sleep(1)
    print('【最终结果：你赢了！】')
elif enemy_victory > player_victory:
    print('【最终结果：你输了！】')
else:
    print('【最终结果：平局！】')



# 石头剪刀布 - 人机对战 2.0

import random

# 出拳
punches = ['石头','剪刀','布']
computer_choice = random.choice(punches)  # 或： computer_choice=punches[random.randint(0,2)]
user_choice = ''
user_choice = input('请出拳：（石头、剪刀、布）')  # 请用户输入选择
while user_choice not in punches:  # 当用户输入错误，提示错误，重新输入
    print('输入有误，请重新出拳')
    user_choice = input()

# 亮拳
print('————战斗过程————')
print('电脑出了：%s' % computer_choice)
print('你出了：%s' % user_choice)

# 胜负
print('—————结果—————')
if user_choice == computer_choice:  # 使用if进行条件判断
    print('平局！')
# 电脑的选择有3种，索引位置分别是：0石头、1剪刀、2布。
# 假设在电脑索引位置上减1，对应：-1布，0石头，1剪刀，皆胜。
elif user_choice == punches[punches.index(computer_choice)-1]:
    print('你赢了！')
else:
    print('你输了！')

