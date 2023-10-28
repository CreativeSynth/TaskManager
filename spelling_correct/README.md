# Setup

데이터를 옮기고 실행하는 방법에 대해서 설명해드리겠습니다.

https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=545 이곳에서 데이터를 다운받아서

원천데이터를 압출 해제 합니다.

`글짓기`, `대안제시`, `설명글`, `주장`, `찬성반대` 의 5개 폴더가 있습니다.
현재는 용량상 폴더를 전부 지워놨습니다. 폴더를 전부 옮겨놓고 setup.py를 실행하면 갱신 됩니다.


## 평가 방식

우선 정답에서 가장 바깥의 대괄호 안만 모델의 답으로 처리합니다. 만약 대괄호가 없거나 내부가 너무 짧다면 전체 문장을 사용하고, 대괄호는 삭제합니다.

평가는 아래 두가지 요소를 가지고 점수를 산정합니다.

1. 원본 문장과 달라진 문자의 개수 (편집거리)
2. 원본 문장의 맞춤법 오류 개수 - 바뀐 문장의 맞춤법 오류 개수

맞춤법 오류의 개수는 파이썬 library를 기준으로 합니다.
두가지를 적절히 가중치를 두어 계산합니다.