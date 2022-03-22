#한꺼번에 주석처리 : ctl + /
pocket = ["paper", "cellphon", "money"]
card = True
if "money" not in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("카카오 택시를 불러라")
    else:
        print("걸어라")
