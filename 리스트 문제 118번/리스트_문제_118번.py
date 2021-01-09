#연습 118번
#일반 카드 갑판에는 52장의 카드
#j(잭),q(퀸),k(킹),s(스페이드),c(클로버),d(다이아몬드),h(하트),T(텐),A
#j(106),q(113),k(107),s(115),c(99),d(100),h(104)
#99 100 104 106 107 113 115
def createDeck():
    card=[]
    for i in range(1,41):
        if i<10:
            if i==1:
                each_card="A"+"s"
            else:
                each_card=str(i)+"s"
            card.append(each_card)
        elif i==10:
            each_card="Ts"
            card.append(each_card)
        elif 10<i<20:
            i=i%10
            if i==1:
                each_card="A"+"c"
            else:
                each_card=str(i)+"c"
            card.append(each_card)
        elif i==20:
             each_card="Tc"
             card.append(each_card)
        elif 20<i<30:
            i=i%10
            if i==1:
                each_card="A"+"d"
            else:
                each_card=str(i)+"d"
            card.append(each_card)
        elif i==30:
            each_card="Td"
            card.append(each_card)
        elif 30<i<40:
            i=i%10
            if i==1:
               each_card="A"+"c"
            else:
                each_card=str(i)+"c"
            card.append(each_card)
        elif i==40:
            each_card="Tc"
            card.append(each_card)
    card_large=["Js","Qs","Ks","Jc","Qc","Kc","Jd","Qd","Kd","Jh","Qh","Kh"]
    for i in card_large:
        card.append(i)
    return card



from random import shuffle
print("본래 카드 순서: ")
print(createDeck())
card=createDeck()
print("랜덤으로 섞게 된 카드 순서: ")
shuffle(card)
print(card)