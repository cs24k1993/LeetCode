while True:
    try:
        b = []
        str = input()
        for i in str:
            if i.isdigit():
                i = '*'+i+'*'
                b.append(i)
            else:
                b.append(i)
        print("".join(b).replace("**", ""))
    except:
        break