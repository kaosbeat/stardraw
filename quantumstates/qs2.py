import lib.neigbour as nb019
import lib.starDraw as sd
import lib.asciistage as ast
import time

kaotec = nb019.displayText("XX;01;99")
quan = nb019.displayText("qu;an;tm")
states = nb019.displayText("st;at;es")
kaoteclogo = nb019.displayText(" [;]<;> ")

zeros = nb019.displayText("OO:OO:OO")
asterisks = nb019.displayText("**;**;**")

seq = [quan,states,kaoteclogo,zeros,asterisks]
i = 0
ast.clearstage()
time.sleep(4)
while i < len(seq):
    ast.clearstage()
    ast.printMultilineonstage(seq[i%len(seq)], 10, ast.lines-10)
    ast.gotoline(0)
    time.sleep(2)
    i +=1

while True:
    ast.clearstage()
    ast.printMultilineonstage(nb019.displayBits(nb019.randomOneBits()), 10, ast.lines-10)
    ast.gotoline(0)
    time.sleep(0.3)
    ast.clearstage()
    ast.printMultilineonstage(nb019.displayBits(nb019.randomZeroBits()), 10, ast.lines-10)
    ast.gotoline(0)
    time.sleep(0.3)
        


