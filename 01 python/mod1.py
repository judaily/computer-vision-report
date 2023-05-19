# # mod1.py
# def sum(a,b): # module 안에 있는 함수 정의
#     return a + b

# def safe_sum(a,b): # a type == b type => +
#     if type(a) == type(b):
#         result = sum(a,b)
#     else: # type(a) != type(b)
#         result = '더할수 있는 값이 아닙니다.' 
#         # print('더할수 있는 값이 아닙니다.')
#         # return 
#     return result

def sum(a,b): # module 안에 있는 함수 정의
    return a + b

def safe_sum(a,b): # a type == b type => +
    if type(a) != type(b):
        print('더할수 있는 값이 아닙니다.') 
        return None
    else:
        result = sum(a,b)
    return result

# 실행코드
if __name__ == '__main__':
    print(safe_sum('a',1)) 
    print(safe_sum(1,4))       
    print(sum(10,10.4))