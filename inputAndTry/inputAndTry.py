import types
list = [1,2,3,45,64,45]
def so():
    while True:
        try:
            str_num = input('input a number:')
            num=float(str_num)
            print(num)
            break   #若输入的正确，则退出，错误执行except下面代码
        except:
            print('您输入的内容不规范，请重新输入：')
    a = num
    if a >8:
        del list[0]
    elif a <= 8:
        print('0000000')
    return list
def main():
    print(list)
    print('**************')
    c=so()
    print(c)

main()