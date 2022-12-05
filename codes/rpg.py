import random

enemies = {"ジャヴァーン": 300, "パイソルジャー": 500, "ルビーン": 50}

def attack(monster):
    
    point = random.randint(30, 200)
    print(monster + "は、スクリプトマンを攻撃した。")
    
    if 100 <= point:
        print("クリティカルヒット!スクリプトマンに" + str(point) + "のダメージ!")
    else:
        print("スクリプトマンに" + str(point) + "のダメージ!")
    return point


def Sqlqueen():
    potion = random.randint(50, 80)
    print("スクリプトマンのHPが" + str(potion) + "回復した!")
    return potion


scriptman = 300

    
for enemy in enemies: #{"エンダードラゴン": 300, "ウォーデン": 500, "スケルトン": 50, "ピグリン": 80}
 
    scriptman -= attack(enemy) # 200 - 50(ランダム) 

    if scriptman < 0:
        print("スクリプトマンは倒れた・・・")
        break
    
    print("スクリプトマンの残りHPは" + str(scriptman) + "。")
        
    if 10 <= scriptman <= 150:
        print("SQLクイーンがスクリプトマンに回復魔法を唱えた!")
        scriptman += Sqlqueen()
        print("スクリプトマンのHPは残り"+ str(scriptman) + "。")

print()

def n_attack(monster):
    attack_point = random.randint(30, 50)
    print("スクリプトマンは" + monster + "に攻撃した!")
    print(monster + "に" + str(attack_point) + "のダメージ" )
    return attack_point
    

if scriptman > 0:
    print("スクリプトマンの反撃!!")
    for enemy in enemies:
        
        if enemy in enemies:
            enemy_hit_point = enemies[enemy]
            enemy_hit_point -= n_attack(enemy)
            print(enemy + "の残りHPは" + str(enemy_hit_point) + "。")