d={}
print('wellcom to the best dictionary every')
while True:
    print('make dictionary')
    print('list all vocab')
    print('english to chinese')
    print('chinese to english')
    print('test')
    print('leave')
    
    option = input('what is your choice?')
    
    if option == 6:
        break
    elif option ==1:
        while True:
            voc = input('english vocab please(perss 0 to leave)')
            if voc == '0':
                break
            if voc not in d:
                voc_ch = input('chinese')
                d[voc] = voc_ch
            else:
                print('already there')
    elif option == '2':
        s = sorted(d)
        print(s)
        for i in s:
            print(i,':'.d[i])
    elif option == '3':
        while True:
            voc = input('please insert english(0 to leave)')
            if voc == '0':
                break
            if voc in d:
                print(voc,"'s chinese is")
            else:
                print('there is no such word')
    elif option =='4':
        got = False
        ch = input('please insert chinese(0 to leave)')
        if ch == '0':
            break
        for k,v in d.items():
            if ch==v:
                print (ch,"'s english is ",k)
                got = True
            if got ==False:
                print('there is no such word')
    elif option == '5':
        score=0
        for k,v in d.items():
            print(v)
            ans = input()
            if ans ==k:
                score += 1
                print('good')
            else:
                print('bad')
        print('you have ',score)
        

            
            