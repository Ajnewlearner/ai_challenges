
def morsegenerator(code):
    gen = []
    i = 1
    for ch in code:
        if ch == 'a' or 'A':
            print('.-')
        if ch == 'b':
            print('-...')
        if ch == 'c':
            print('-.-.')
        if ch == 'd':
            print('-..')
        if ch == 'e':
            print('.')
        if ch == 'f':
            print('..-.')
        if ch == 'g':
            print('--.')
        if ch == 'h':
            print('....')
        if ch == 'i':
            print('..')
        if ch == 'j':
            print('.---')
        if ch == 'k':
            print('-.-')
        if ch == 'l':
            print('.-.-')
        if ch == 'm':
            print('--')
        if ch == 'n':
            print('-.')
        if ch == 'o':
            print('---')
        if ch == 'p':
            print('.--.')
        if ch == 'q':
            print('--.-')
        if ch == 'r':
            print('.-.')
        if ch == 's':
            print('...')
        if ch == 't':
            print('-')
        if ch == 'u':
            print('..-')
        if ch == 'v':
            print('._')
        if ch == 'x':
            print('._')
        if ch == 'y':
            print('-.--')
        if ch == 'z':
            print('._')
        # gen 
        gen[i] = ch
        i = i + 1   
    return         
           
    




# morse = morsegenerator()
code = 'Ayush'
print(morsegenerator(code))    