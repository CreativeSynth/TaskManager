number_dic_ko = ("", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구")
place_value1_ko = ("", "십", "백", "천")
place_value2_ko = ("", "만", "억", "조", "경")

def split_number(number, n):
    """number를 n자리씩 끊어서 리스트로 반환한다."""
    res = []
    div = 10**n
    while number > 0:
        number, remainder = divmod(number, div)
        res.append(remainder)
    return res

def num2kr(number, delimiter):
    """10000 미만의 수를 한글로 변환한다.
       delimiter가 ''이면 1을 무조건 '일'로 바꾼다."""
    if number == 0:
        return "영"
    
    res = ""
    flag = ""
    if number < 0:
        flag = "마이너스 "
        number = -number
    for place, digit in enumerate(split_number(number, 1)):
        if not digit:
            continue
        if delimiter and digit == 1 and place != 0:
            num = ""
        else:
            num = number_dic_ko[digit]
        res = num + place_value1_ko[place] + res
    return flag + res

