import collections
counter = collections.Counter
class Text:
    text_caller = {}
    def __init__(self, text:str):
        self.text = text
        self.text_counter = counter(text)
        for i in self.text_counter:
            if not i in Text.text_caller:
                Text.text_caller[i] = []
            Text.text_caller[i].append(self)

# 이 클래스 객체를 단위로 글을 관리하면, 선형 탐색 범위를 줄일 수 있다. 
# 물론 하나의 글에 대해서는 효과가 없다. 이미 나눠진 여러 개의 글 중 하나를 찾을 때 유용하다. 
# 이후 선형 탐색은 compare_as_combination.py 또는 difflib 등을 이용. 