def checking_card1(card1_suit, card1_number, max_rank_card1, min_rank_card1):
    chances_for_flush = None  # checking for all FLUSH possibilities
    for card in card1_suit:
        check_suit = card1_suit.count(card)
        if check_suit == 5:
            chances_for_flush = True
    if chances_for_flush is True:
        if 14 in card1_number and 13 in card1_number and 12 in card1_number and 11 in card1_number and 10 in card1_number:
            # print("ROYAL FLUSH!!!!")  # returning as ROYAL_FLUSH
            return 9
        elif max_rank_card1 - min_rank_card1 == 4:
            # print("STRAIGHT FLUSH!!!")
            return 8                              # returning STAIGHT_FLUSH
        else:
            # print("FLUSH!!!!")
            return 5  # returning as FLUSH

    chances_for_no_pair = 0  # checking for NO_PAIR
    checking_for_pairs = list()
    for card in card1_number:
        check_number = card1_number.count(card)
        if check_number == 2:
            checking_for_pairs.append(card)
        if check_number == 1:
            chances_for_no_pair += 1
    checking_for_pairs = set(checking_for_pairs)
    if chances_for_no_pair == 5:
        if max_rank_card1 - min_rank_card1 == 4:  # checking for STRAIGHT
            # print("STRAIGHT!!!")
            return 4  # returning as STRAIGHT
        # print("NO PAIR!!!!")
        return 0  # returning as NO_PAIR
    elif chances_for_no_pair == 1 and len(checking_for_pairs) == 2:  # checking for TWO_PAIRS
        # print("TWO PAIRS!!!")
        return 2  # returning as TWO_PAIRS
    elif chances_for_no_pair == 1:  # checking for FOUR_OF_A_KIND
        # print("FOUR OF A KIND!!!")
        return 7  # returning as FOUR_OF_A_KIND
    elif chances_for_no_pair == 2:  # checking as THREE OF A KIND
        # print("THREE OF A KIND!!!")
        return 3  # returning as THREE_OF_A_KIND
    elif chances_for_no_pair == 3:  # checking for ONE PAIR
        # print("ONE PAIR!!!")
        return 1  # returning as ONE PAIR
    elif chances_for_no_pair == 0 and len(checking_for_pairs) == 1:  # checking for FULL HOUSE
        # print("FULL HOUSE!!!")
        return 6


def checking_card2(card2_suit, card2_number, max_rank_card2, min_rank_card2):
    chances_for_flush = None  # checking for all FLUSH possibilities
    for card in card2_suit:
        check_suit = card2_suit.count(card)
        if check_suit == 5:
            chances_for_flush = True
    if chances_for_flush == True:
        if 14 in card2_number and 13 in card2_number and 12 in card2_number and 11 in card2_number and 10 in card2_number:
            # print("ROYAL FLUSH!!!!")  # returning as ROYAL_FLUSH
            return 9
        elif max_rank_card2 - min_rank_card2 == 4:
            # print("STRAIGHT FLUSH!!!")
            return 8  # returnig STAIGHT_FLUSH
        else:
            # print("FLUSH!!!!")
            return 5  # returning as FLUSH

    chances_for_no_pair = 0  # checking for NO_PAIR
    checking_for_pairs = list()
    for card in card2_number:
        check_number = card2_number.count(card)
        if check_number == 2:
            checking_for_pairs.append(card)
        if check_number == 1:
            chances_for_no_pair += 1
    checking_for_pairs = set(checking_for_pairs)
    if chances_for_no_pair == 5:
        if max_rank_card2 - min_rank_card2 == 4:  # checking for STRAIGHT
            # print("STRAIGHT!!!")
            return 4  # returning as STRAIGHT
        # print("NO PAIR!!!!")
        return 0  # returning as NO_PAIR
    elif chances_for_no_pair == 1 and len(checking_for_pairs) == 2:  # checking for TWO_PAIRS
        # print("TWO PAIRS!!!")
        return 2  # returning as TWO_PAIRS
    elif chances_for_no_pair == 1:  # checking for FOUR_OF_A_KIND
        # print("FOUR OF A KIND!!!")
        return 7  # returning as FOUR_OF_A_KIND
    elif chances_for_no_pair == 2:  # checking as THREE OF A KIND
        # print("THREE OF A KIND!!!")
        return 3  # returning as THREE_OF_A_KIND
    elif chances_for_no_pair == 3:  # checking for ONE PAIR
        # print("ONE PAIR!!!")
        return 1  # returning as ONE PAIR
    elif chances_for_no_pair == 0 and len(checking_for_pairs) == 1:  # checking for FULL HOUSE
        # print("FULL HOUSE!!!")
        return 6


def poker_real(player_one, player_two):  # seperating player cards into suit and number

    p1 = player_one.split(" ")
    card1_number = list()
    card1_suit = list()
    for item in p1:  # assigning each card to seperate numbers and suit
        card1_number.append(item[0])
        card1_suit.append(item[1])

    if "A" or "K" or "Q" or "J" or "T" in card1_number:  # converting all characters in the card to numbers
        card1_number = [14 if rank == "A" else rank for rank in card1_number]  #
        card1_number = [13 if rank == "K" else rank for rank in card1_number]  #
        card1_number = [12 if rank == "Q" else rank for rank in card1_number]  #
        card1_number = [11 if rank == "J" else rank for rank in card1_number]  #
        card1_number = [10 if rank == "T" else rank for rank in card1_number]  #
    card1_number = [int(x) for x in card1_number]
    min_rank_card1 = min(int(x) for x in card1_number)  # finding minimum number
    max_rank_card1 = max(int(x) for x in card1_number)  # findning maximum number

    checking_for_pairs_card1 = list()
    for card in card1_number:
        check_number = card1_number.count(card)
        if check_number == 2:
            checking_for_pairs_card1.append(card)
        elif check_number == 4 or check_number == 3:
            checking_for_duplicate_card1 = card

    p2 = player_two.split(" ")
    card2_number = list()
    card2_suit = list()
    for item in p2:  # assigning each card to separate numbers and suit
        card2_number.append(item[0])
        card2_suit.append(item[1])

    if "A" or "K" or "Q" or "J" or "T" in card2_number:  # converting all characters in the card to numbers
        card2_number = [14 if rank == "A" else rank for rank in card2_number]  #
        card2_number = [13 if rank == "K" else rank for rank in card2_number]  #
        card2_number = [12 if rank == "Q" else rank for rank in card2_number]  #
        card2_number = [11 if rank == "J" else rank for rank in card2_number]  #
        card2_number = [10 if rank == "T" else rank for rank in card2_number]  #
    card2_number = [int(x) for x in card2_number]
    min_rank_card2 = min(int(x) for x in card2_number)  # finding minimum number
    max_rank_card2 = max(int(x) for x in card2_number)  # finding maximum number

    checking_for_pairs_card2 = list()
    for card in card2_number:
        check_number = card2_number.count(card)
        if check_number == 2:
            checking_for_pairs_card2.append(card)
        elif check_number == 4 or check_number == 3:
            checking_for_duplicate_card2 = card

    p1_rank = checking_card1(card1_suit, card1_number, max_rank_card1, min_rank_card1)
    p2_rank = checking_card2(card2_suit, card2_number, max_rank_card2, min_rank_card2)

    if p1_rank > p2_rank:
        return "Player 1 WIN"
    elif p1_rank < p2_rank:
        return "Player 2 WIN"
    elif (p1_rank == 8 and p2_rank == 8) or (p1_rank == 4 and p1_rank == 4) or (p1_rank == 5 and p1_rank == 5) or (p1_rank == 9 and p2_rank == 9):                         #checking condition for STRAIGHT FLUSH tie
        if max_rank_card1 > max_rank_card2:
            return "Player 1 WIN"
        elif max_rank_card1 < max_rank_card2:
            return "Player 2 WIN"
        else:
            while max_rank_card1 == max_rank_card2:
                card2_number.remove(max_rank_card2)
                card1_number.remove(max_rank_card1)
                if len(card1_number) != 0 and len(card2_number) != 0:
                    max_rank_card1 = max(int(x) for x in card1_number)
                    max_rank_card2 = max(int(x) for x in card2_number)
                if max_rank_card1 > max_rank_card2:
                    return "Player 1 WIN"
                elif max_rank_card1 < max_rank_card2:
                    return "Player 2 WIN"
                elif len(card2_number) == 0 and len(card1_number)== 0:
                    break
                else:
                    continue
            return "Tie"
    elif (p1_rank == 6 and p2_rank == 6):
        if checking_for_duplicate_card1 > checking_for_duplicate_card2:
            return "Player 1 WIN"
        elif checking_for_duplicate_card1 < checking_for_duplicate_card2:
            return "Player 2 WIN"
        else:
            max_duplicate_card1 = max(int(x) for x in checking_for_pairs_card1)
            max_duplicate_card2 = max(int(x) for x in checking_for_pairs_card2)

            if max_duplicate_card1 > max_duplicate_card2:
                return "Player 1 WIN"
            elif max_duplicate_card1 < max_duplicate_card2:
                return "Player 2 WIN"
            else:
                return "Tie"
    elif (p1_rank == 3 and p1_rank == 3):
        if checking_for_duplicate_card1 > checking_for_duplicate_card2:
            return "Player 1 WIN"
        elif checking_for_duplicate_card1 < checking_for_duplicate_card2:
            return "Player 2 WIN"
        else:
            card2_number = set(card2_number)
            card1_number = set(card1_number)
            card1_number.remove(checking_for_duplicate_card1)
            card2_number.remove(checking_for_duplicate_card2)
            if card1_number != 0 and card2_number != 0:
                max_card1 = max(int(x) for x in card1_number)
                max_card2 = max(int(x) for x in card2_number)
            if max_card1 > max_card2:
                return "Player 1 WIN"
            elif max_card1 < max_card2:
                return "Player 2 WIN"
            else:
                while max_card1 == max_card2:
                    max_card1 = max(int(x) for x in card1_number)
                    max_card2 = max(int(x) for x in card2_number)
                    card1_number.remove(max_card1)
                    card2_number.remove(max_card2)
                    if max_card1 > max_card2:
                        return "Player 1 WIN"
                    elif max_card1 < max_card2:
                        return "Player 2 WIN"
                    elif len(card1_number) == 0 and len(card2_number) == 0:
                        break
                    else:
                        continue
            return "Tie"
    elif p1_rank == 7 and p2_rank == 7:
        if checking_for_duplicate_card1 > checking_for_duplicate_card2:
            return "Player 1 WIN"
        elif checking_for_duplicate_card1 < checking_for_duplicate_card2:
            return "Player 2 WIN"
        else:
            card2_number = set(card2_number)
            card1_number = set(card1_number)
            card1_number.remove(checking_for_duplicate_card1)
            card2_number.remove(checking_for_duplicate_card2)
            if card1_number !=  0 and card2_number != 0:
                max_card1 = max(int(x) for x in card1_number)
                max_card2 = max(int(x) for x in card2_number)
            if max_card1 > max_card2:
                return "Player 1 WIN"
            elif max_card1 < max_card2:
                return "Player 2 WIN"
            else:
                return "Tie"
    elif (p1_rank == 2 and p2_rank == 2) or (p1_rank == 1 and p2_rank == 1):
        max_duplicate_card1 = max(int(x) for x in checking_for_pairs_card1)
        max_duplicate_card2 = max(int(x) for x in checking_for_pairs_card2)
        if max_duplicate_card1 > max_duplicate_card2:
            return "Player 1 WIN"
        elif max_duplicate_card1 < max_duplicate_card2:
            return "Player 2 WIN"
        else:
            checking_for_pairs_card1 = set(checking_for_pairs_card1)
            checking_for_pairs_card2 = set(checking_for_pairs_card2)
            card1_number = set(card1_number)
            card2_number = set(card2_number)
            if checking_for_pairs_card1 != 0 and checking_for_pairs_card2 != 0:
                max_duplicate_card1 = max(int(x) for x in checking_for_pairs_card1)
                max_duplicate_card2 = max(int(x) for x in checking_for_pairs_card2)
            if max_duplicate_card1 > max_duplicate_card2:
                return "Player 1 WIN"
            elif max_duplicate_card1 < max_duplicate_card2:
                return "Player 2 WIN"
            else:
                while max_duplicate_card1 == max_duplicate_card2:
                    max_duplicate_card1 = max(int(x) for x in checking_for_pairs_card1)
                    max_duplicate_card2 = max(int(x) for x in checking_for_pairs_card2)
                    checking_for_pairs_card1.remove(max_duplicate_card1)
                    checking_for_pairs_card2.remove(max_duplicate_card2)
                    card1_number.remove(max_duplicate_card1)
                    card2_number.remove(max_duplicate_card2)
                    if max_duplicate_card1 > max_duplicate_card2:
                        return "Player 1 WIN"
                    elif max_duplicate_card1 < max_duplicate_card2:
                        return "Player 2 WIN"
                    elif len(checking_for_pairs_card1) == 0 and len(checking_for_pairs_card2) == 0:
                        max_card1 = max(int(x) for x in card1_number)
                        max_card2 = max(int(x) for x in card2_number)
                        if max_card1 > max_card2:
                            return "Player 1 WIN"
                        elif max_card1 < max_card2:
                            return "Player 2 WIN"
                        else:
                            while max_card1 == max_card2:
                                max_card1 = max(int(x) for x in card1_number)
                                max_card2 = max(int(x) for x in card2_number)
                                card1_number.remove(max_card1)
                                card2_number.remove(max_card2)
                                if max_card1 > max_card2:
                                    return "Player 1 WIN"
                                elif max_card1 < max_card2:
                                    return "Player 2 WIN"
                                elif len(card1_number) == 0 and len(card2_number) == 0:
                                    break
                                else:
                                    continue
                            return "Tie"
            return "Tie"
    elif (p1_rank == 0 and p2_rank == 0):
        if max_rank_card1 > max_rank_card2:
            return "Player 1 WIN"
        elif max_rank_card1 < max_rank_card2:
            return "Player 2 WIN"
        else:
            while max_rank_card1 == max_rank_card2:
                card1_number.remove(max_rank_card1)
                card2_number.remove(max_rank_card2)
                if len(card1_number) != 0 and len(card2_number) != 0:
                    max_rank_card1 = max(int(x) for x in card1_number)
                    max_rank_card2 = max(int(x) for x in card2_number)
                if max_rank_card1 > max_rank_card2:
                    return "Player 1 WIN"
                elif max_rank_card1 < max_rank_card2:
                    return "Player 2 WIN"
                elif len(card1_number) == 0 and len(card2_number) == 0:
                    break
                else:
                    continue
            return "Tie"
    else:
        return "Tie"
