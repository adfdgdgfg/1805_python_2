class ShowError(Exception):

    def __init__(self,len,least):
        self.len = len
        self.least = least


def main():
    try:
        s = input("请输入一个名字")
        if len(s) < 3:
            raise ShowError(len(s),3)
    except ShowError as ret:
        print("至少需要%d位你的字符有%d"%(ret.least,ret.len))  
main()
