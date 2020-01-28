
Journer
============
> Journer은 약 4주간 진행하는 사이드 프로젝트입니다.

혼자 여행하는 인구의 비율이 늘어남에 따라서 동행을 구하는 비율도 증가했습니다.
우리의 프로젝트는 여기에 초점을 맞춰서 더 간편하고 더 안전하게 동행을 구할 수 있게 도와줄 수 있는 플랫폼을 개발하고자합니다.

작가 다비드 르 브르통의
##### “걸어서 떠나는 사람은 익명 속으로 미끄러져 들어가는 것을 즐기고 함께 길을 가는 동행이나 길에서 만난 사람들 외에는 더 이상 그 어느 누구를 위해서도 존재하지 않는 입장이 된 것을 즐긴다.”
라는 말에 공감하며 이 프로젝트가 당신의 여행에 이정표가 될 수 있기를 바랍니다.


## 파일 정보

### /sample1
<pre>
</pre>

### /sample2
<pre>
</pre>



## 사용언어
* (Python)
* ()
* ()

## 데이터 출처

코드 작성규칙
============
1. Indentation(들여쓰기)는 무조건 스페이스바 4번으로 통일합니다.
2. 함수 작성시, 함수 def 하단에 docstring(""")을 이용해서 함수에 대한 설명을 작성합니다.
> ```python
> def function(args):
> """
>     입력한 인자로 실행하는 함수이다
>     받아온 인자를 처리해주는 기능을 한다
>     return: 결과값
> """
> ```
> **docstring의 경우에는 반드시 double quote(")를 3개 사용해서 표기해줍니다.**
3. 문자열 포맷은 항상 UTF-8을 사용합니다.
4. 모듈 import시 반드시 행을 분리해서 선언합니다.
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
5. single 혹은 double quote(따옴표)를 사용시, 자유롭게 사용하되 이스케이프 문자(백슬래시 등)사용을 피하고 가독성이 좋도록 적절히 따옴표를 사용하여 주시기 바랍니다.
6. Whitespace: 무의미한 공백사용을 피하도록 합니다
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
7. 기타 유의사항
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
> 
