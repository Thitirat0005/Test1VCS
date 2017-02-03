import random
def generate_list():
    alist=[]
    for x in range(random.randint(0,20)):
        alist.append(x)
    return alist
    
"""    
print a generate list
"""

def printIT():
    alist=[]
    alist=generate_list()
    print(alist)
    assert len(alist), "alist is null, please random again"
    assert sum(alist)>=100, "sum of alist < 100"
    
    
def main():
    []
    printIT()
    
"""
IF this script file is called, it will run main() directly
"""

if __name__ == '__main__':
    print("Test printIT():" )
    main()
    
    