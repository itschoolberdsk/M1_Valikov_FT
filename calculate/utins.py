import constans as const
import calculate_process as calc

def result(a: int, b: int, sign: str):
    if sign == const.PLUS:
        return calc.sum(a, b)
    elif sign == const.DIFFERENCE:
        return calc.minus(a, b)
    elif sign == const.MULTIPLIKATION:
        return calc.mult(a, b)
    elif sign == const.DIVISION:
        return calc.dell(a, b)
    elif sign == const.DEGREE:
        return calc.degree(a, b)

def parseCmd(cmd: str):
    cmd = cmd.split()
    if len(cmd) == 3:
        return (int(cmd[0]), cmd[1], int(cmd[2]))
    elif len(cmd) == 2:
        return (cmd[0], int(cmd[1]))
