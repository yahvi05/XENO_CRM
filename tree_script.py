import os

def p(s, m=4, i={'.git', 'node_modules', 'target', '__pycache__', 'venv', '.idea', '.vscode', '.gemini'}):
    for r, d, f in os.walk(s):
        d[:] = [x for x in d if x not in i]
        l = r.replace(s, '').count(os.sep)
        if l > m: continue
        print('    ' * l + os.path.basename(r) + '/')
        for x in f: print('    ' * (l + 1) + x)

p(r'c:\Users\DWARAKESH\Downloads\Yahvi XENO\XENO PROJECT')
