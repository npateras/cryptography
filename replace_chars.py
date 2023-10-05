import random

def method_rundom_sellect(data_priv2):
    while True:
        random_sellect = random.randint(0, len(data_priv2)-1)
        a = list(data_priv2)[random_sellect]
        if "p" in a or "q" in a or "d" in a or "n" in a or "u" in a:
            return data_priv2[random_sellect] , random_sellect

# def change and def gen_char are together
def change(line):
    while True:
        a = random.randint(0, len(line)-2)
        i = line[a]
        if i=="p" or i=="q" or i=="d" or i=="n" or i=="u":
            me1 = gen_char()
            me2 = gen_char()
            #replase the 2 chars
            line_list = list(line)
            line_list[a] = me1
            line_list[a+1] = me2
            #join list to string
            str_line = ''.join(line_list)
            return str_line

def gen_char():
    mystring = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
    mylist = list(mystring)
    random.shuffle(mylist)
    return mylist[0]
