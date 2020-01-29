# 코드 작성규칙
---
## 1. Indentation(들여쓰기)는 무조건 스페이스바 4번으로 통일합니다.
> 연속되는 문장은 괄호(소, 중, 대)를 이용하여 수직 정렬을 하거나 'hanging indent'를 사용합니다.
> 첫번째 줄에는 인수가 오면 안되며 더 많은 들여쓰기를 통해 연속되는 문장임을 확실히 드러냅니다.
> ```python
> example:
> # 구분자(delimeters)를 이용한 정렬
> foo = long_function_name(var_one, var_two,
>                          var_three, var_four)
> 
> # 추가적인 들여쓰기로 나머지 코드를 구분자
> def long_function_name(
>         var_one, var_two, var_three,
>         var_four):
>     print(var_one)
> 
> # 'hanging indent'는 반드시 한 레벨을 추가한다.
> foo = long_function_name(
>     var_one, var_two,
>     var_three, var_four)
> ```
> 여러줄로 표현되는 if문의 경우 명확하게 하기 위해 하단의 방법을 사용한다.
> ```python
> # 주석을 통해 조건문과 실행 코드를 구분자
> if (first_contidion and
>     second_condition):
>     # 두 조건문이 만족되면 아래를 실행
>     do_something()
> ```
> 여러 줄의 생성자의 닫히는 괄호는 마지막 줄의 공백이 아닌 첫번째 문자(요소) 위치에 오거나 마지막 줄에서 생성자가 시작되는 첫번째 열에 위치한다.
> ```python
> my_list = [
>     1, 2, 3,
>     4, 5, 6,
>     ]
> result = some_function_that_takes_arguments(
>     'a', 'b', 'c',
>     'd', 'e', 'f',
>     )
> my_list = [
>     1, 2, 3,
>     4, 5, 6,
> ]
> result = some_function_that_takes_arguments(
>     'a', 'b', 'c',
>     'd', 'e', 'f',
> )
> ```
**들여쓰기는 space가 권장됩니다. 파이참 개발환경의 경우 tap을 사용했을때 자동적으로 스페이스바로 처리하니 크게 신경안쓰셔도 됩니다.**
> 이항연산자의 줄바뀜의 경우 연산자의 앞에서 표현합니다.
> ```python
> income = (gross_wages
>           + taxable_interest
>           + (dividents - qualified_dividends)
>           - ira_deduction
>           - student_loan_interest)
> ```

## 2. 함수 작성시, 함수 def 하단에 docstring(""")을 이용해서 함수에 대한 설명을 작성합니다.
> ```python
> def function(args):
> """
>     입력한 인자로 실행하는 함수이다
>     받아온 인자를 처리해주는 기능을 한다
>     return: 결과값
> """
> ```
> **docstring의 경우에는 반드시 double quote(")를 3개 사용해서 표기해줍니다.**
## 3. 문자열 포맷은 항상 UTF-8을 사용합니다.
## 4. 모듈 import시 반드시 행을 분리해서 선언합니다.
> ```python
> True : import os
>        import sys
> False: import sys, os
> ```
> 그러나 다음과 같은 경우는 허용됩니다.
> ```python
> from subprocess import Popen, PIPE
> ```
> import는 반드시 파일 주석과 Docstring 바로 아래, 그리고 전역변수, 상수 선언부 위에 위치합니다.
## 5. single 혹은 double quote(따옴표)를 사용시, 자유롭게 사용하되 이스케이프 문자(백슬래시 등)사용을 피하고 가독성이 좋도록 적절히 따옴표를 사용하여 주시기 바랍니다.
## 6. Whitespace: 무의미한 공백사용을 피하도록 합니다
> + 괄호(소,중,대)의 양쪽 
> ```python
> True : spam(ham[1], {eggs: 2})
> False: spam( ham[ 1 ], { eggs: 2 } }
> ```
> + 콤마, 세미콜론, 콜론 바로 앞
> ```python
> True : if x == 4: print x, y; x,y = y, x
> False: if x == 4 : print x, y ; x, y = y, x
> ```
> + 슬라이스에서 콜론은 우선순위가 낮은 이항연산자와 유사한 방식으로 사용되며 양쪽에 동일한 공간을 할당해야됩니다. 확장된 슬라이스에서 모든 콜론은 같은 크기의 공간이 할당되어야 합니다. 다만, 피연산자가 누락되었을 경우에는 공백 또한 주지 않습니다.
> ```python
> True:
> ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
> ham[lower:upper], ham[lower:upper:], ham[l;ower::step]
> ham[lower+offset : upper+offet]
> ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
> ham[lower + offset : upper + offset]
>
> False:
> ham[lower + offset:uppser + offset]
> ham[1: 9], ham[1 :9], ham[1:9: 3]
> ham[lower : : upper]
> ham[ : upper]
> ```
> + 함수 호출 시 뒤 인자를 넣기 위한 소괄호의 바로 앞
> ```python
> True : spam(1)
> False: spam (1)
> ```
> + 리스트나 사전의 인덱스나 슬라이스에 사용되는 대괄호의 바로 앞
> ```python
> True : dct['key'] = lst[index]
> False: dec ['key'] = lst [index]
> ```
> + 대입 연산자의 앞뒤는 공백 한칸을 줍니다.
> ```python
> True:
> x = 1
> y = 1
> long_variable = 3
>
> False:
> x             = 1
> y             = 2
> long_variable = 3
> ```
## 7. 기타 유의사항
> + 문장의 마지막에 따라오는 공백을 없게 합니다. 잘 안보이기 때문에 혼란이 생길 수 있습니다. 예로 들어 백슬래시 뒤에 오는 공백이나 줄바꿈은 문장이 이어지는 것을 표현하는 마커역할을 하지 못합니다.
> + 모든 이항연산자(대입, 증감, 비교, 부울) 앞뒤로는 공백을 둡니다.
> + 우선순위가 다른 연산자를 동시에 사용할 경우에는 낮은 순위의 연산자에 공백을 줍니다. 연산자에 공백을 주는건 각자의 판단에 맡기지만, 그러나 절대로 한 칸을 초과하는 공백을 사용하지는 않으며 이항연산자의 양쪽은 같은 공백을 갖도록 합니다.
> ```python
> True:
> i = i + 1
> submitted += 1
> x = x*2 - 1
> hypot2 = x*x + y*y
> c = (a+b) * (a-b)
>
> False:
> i=i+1
> submitted +=1
> x = x * 2 - 1
> hypot2 = x * x + y * y
> c = (a + b) * (a - b)
> ```
> + 키워드 인자나 디폴트 인자에 사용되는 대입연산자는 절대로 공백을 사용하지 않습니다.
> ```python
> True:
> def complex(real, imag=0.0):
>     return magic(r=real, i=imag)
>
> False:
> def complex(real, imag = 0.0):
>     return magic(r = real, i = imag)
> ```
> + function annotation에 사용되는 콜론은 기존의 룰을 따르며, '->'는 양 옆에 공백을 한 칸씩 가집니다.
> ```python
> True:
> def munge(input: AnyStr): ...
> def munge() -> AnyStr: ...
>
> False:
> def munge(input:AnyStr): ...
> def munge()->AnyStr: ...
> ```
> + argument annotation을 디폴트 변수에 사용할때, 기존의 디폴트 변수에 사용할때의 공백 없는 대입연산자완 다르게 대입연산자 앞 뒤에 공백을 한 칸씩 가진다.
> ```python
> True:
> def munge(sep: AnyStr = None): ...
> def munge(input: AnyStr, sep: AnyStr = None, limit=1000):
> False:
> def munge(sep: AnyStr=None): ...
> def munge(input: AnyStr, sep: AnyStr=None, limit = 1000):
> ```

## 8. 주석 관련
주석은 코드가 업데이트 될 때마다 반드시 같이 업데이트 해야 합니다.<br>
주석은 반드시 완전한 문장형태여야 한다. 만약 주석이 구문이거나 한 문장일 경우, 일반적으로 첫 글자는 대문자를 씁니다.<br>

**주석은 반드시 영어로 작성하도록한다.**
> + Inline Comments
> 본 프로젝트에서 인라인 주석은 변수에 대한 짧은 설명 외에는 허용하지 않는다.
> ```python
> True:
> x = x + 1 # Increment x
> exhibition_list = list() # return list
> 
> False:
> def simple_function(x,y): # function for x+y
> if(condition1 or condition2): # execute in condition1 or condition2
> ```
> + 앞서 언급했지만 함수 작성시, 함수 하단에 함수에 대한 설명을 작성합니다.
> ```python
> def function(args):
> """
>     입력한 인자로 실행하는 함수이다
>     받아온 인자를 처리해주는 기능을 한다
>     return: 결과값
> """
> # Last line should only be """ notation
> ```
> **docstring의 경우에는 반드시 double quote(")를 3개 사용해서 표기해줍니다.**

## 9. 변수와 함수 그리고 메소드 이름
(협의후, 추가작성필요)