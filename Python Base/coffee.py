def showmenu():
    print()
    print("[Cryptocurrency address search choose menu]")
    for i in range(0, len(menu)):
        print(i+i, ".", menu[i], "\tAddress : ", number[i])
    print()
 
def buy(num):    
    if money < price[num]:
        print("잔액이 부족합니다. 잔액 : %d" %money) 
        return money
    else:
        print(menu[num], " 구입완료")
        balance = money - price[num]
        print("잔액 : ", balance)
        return balance
 
 
if __name__ == '__main__':
 
    menu = ("콜라", "사이다", "생수", "커피")
    price = (500, 400, 300, 700)
    money = 0
    money = int( input("돈을 투입하세요 : ") )
 
    while True:
        showmenu()
        sel = int(input("메뉴 번호를 선택하세요 (종료 : 0) : "))
        if sel == 0:
           break
        elif(sel>=1 and sel <= len(menu)):
           money = buy(sel-1)
        else:
           print("잘못된 메뉴 번호입니다")
 
    print("자판기 종료, 잔액 %d 반환"%money)
