"""11/1/25
栈(Stack)
    栈是一个数据集合,只能于一端进行插入或删除
    特点:LIFO(last-in,first-out)也叫先进后出或后进先出
    支持进栈(push)出栈(pop)取栈顶(gettop)
    用列表的append与pop方法即可实现栈的操作
"""
# 下面建立一个类做栈,忘记内容可回顾object章节
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) > 0:     # 判断不为空的列表
            return self.stack.pop()
        else:
            return None
        
    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]   # 获取栈顶元素,也就是列表最后一个-1
        else:
            return None
    
    def is_empty(self):
        return len(self.stack) == 0   # 判断栈空(其实是返回长度与0比较后的结果布尔值,或者看作整体拿过去)
        
new_stack = Stack()
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
print(new_stack.pop())
"""
栈的应用-括号匹配问题
原理:将左括号进栈,下一个若为匹配的右括号,则刚才的左括号出栈
遍历完整个字符串后若栈为空,则全都匹配
"""
def brace_match(s):
    """
    --确定键入内容应为字符串--
    """
    astack = Stack()
    dictionary = {"}":"{","]":"[",")":"("}
    for ch in s:
        if ch in {"(","[","{"}:    # 这是一个集合
            astack.push(ch)        # 输入为左括号则入栈
        else:    # 如果是右括号
            if astack.is_empty():   # 若栈为空,新加入的右括号无法匹配,直接退出
                return False
            elif astack.get_top() == dictionary[ch]: # 这个情况下输入ch为右括号
                                    #判断里边栈顶已有左括号是否匹配
                astack.pop()        # 匹配则左括号出栈
            else:
                return False        # 不匹配还是退出
    # 在执行完以上操作后判断栈是否为空,若仍有元素则说明不匹配
    if astack.is_empty():
        return True
    else:
        return False
    
print(brace_match("({}{{([])}})"))