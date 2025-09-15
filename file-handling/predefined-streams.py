import sys

try:
    for line in sys.stdin:
        if(line.rstrip() == 'q'):
            print('You quit.')    
            break

        print('You said', line)
            
except Exception as e:
    print(e)
