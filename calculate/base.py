import constans as const
import calculate_process as calc
import utins 

def updateCache(a: int, b: int, sign: str):
    global cache
    cache = utins.result(a, b, sign)

cache = 0
while True:
    cmd = input()
    # Условие выхода
    cmd_list = utins.parseCmd(cmd)
    len_cmd_list = len(cmd_list)
    if len_cmd_list != 3 and len_cmd_list != 2:
        # error
        continue
    
    
    if len_cmd_list == 3:
        updateCache(cmd_list[0], cmd_list[2], cmd_list[1])
    elif len_cmd_list == 2 and cache != 0:
        updateCache(cache, cmd_list[1], cmd_list[0])
    
    print(cache)