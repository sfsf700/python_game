import random
pl_pos =  1
com_pos = 1
def banmen():
    print(" ・"*(pl_pos-1) + "Python" + " ・"*(30-pl_pos)+"Goal")
    print(" ・"*(com_pos-1) + "Ruby" + " ・"*(30-com_pos)+"Goal")
    
banmen()
print(" すごろく、スタート")
while True:
    input("Enterを押すとコマが進みます")
    pl_pos = pl_pos + random.randint(1,6)
    if pl_pos > 30:
        pl_pos = 30
    banmen()
    if pl_pos == 30:
        print("  Pythonの勝ちです！")
        break
    input("Enterを押すとコマが進みます")
    com_pos = com_pos + random.randint(1,6)
    if pl_pos > 30:
        pl_pos = 30
    banmen()
    if pl_pos == 30:
        print(" Rubyの勝ちです！")
        break
