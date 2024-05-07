import lib.neigbour as nb019
import lib.starDraw as sd
import lib.asciistage as ast
import time

n=0
while n < 100:
    # print(nb019.genOneBits())
    ast.clearstage()




    ast.printMultilineonstage(nb019.displayBits(nb019.randomZeroBits()), 10, ast.lines-10)
    ast.gotoline(0)
    time.sleep(0.3)
    n+=1

# ast.printMultilineonstage(nb019.displayBits(nb019.genOneBits()), 10, ast.lines-10)

