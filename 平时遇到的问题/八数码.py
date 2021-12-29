#从指定状态到目标转态最小步骤
#012 345 678 ---->876 543 210
#第一个问题，我怎么知道这玩意能转换到额的
#已知不考虑移动的情况下，总共的结果有9！按照道理讲，这个玩意应该包含了所有的可能的状态了
#假设一定可以通过移动实现这一目标------>怎么定义基元操作
#mov[(1,0),(-1,0),(0,1),(0,-1)]代表用棋盘的左上角（坐标）代表所处的位置
# 需要有一个栈来保存初始空格位置的上下左右数据
#结果是一个状态
#每次的移动就相当与pop栈对应的cansewer的状态也需要发生改变
#每次移动都需要检测cansewer的状态与result的状态是否相同
#找到相同的情况时记录step
#判断栈内容是否为空不为空的话回退（回溯canswer的状态）到上一级pop（栈内元素已经该变了）
#min(step)
canswer=[]
result=[]
def judge_answer():
    for i,j in enumerate(canswer):
        if canswer[j]!=result[j]:
            return False
    return True

             