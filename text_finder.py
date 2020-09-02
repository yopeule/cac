import compare_as_combination
import text_caller

t = text_caller.Text
tc = t.text_caller

cac = compare_as_combination

def create_text(s):
    if type(s) == str:
        t(s)
    elif type(s) == list:
        for i in s:
            create_text(i)
    else:
        pass

# compare_as_combination.

def find_text(s:str):
    sset = set()
    s_counter = cac.counter(s)
    for si in s:
        sset.update(tc[si])
    mylist = []
    for mystr in sset:
        mystr_counter = cac.counter(mystr.text)
        if cac.is_sub_counter(s_counter, mystr_counter):
            mylist.append((mystr.text, cac.sub_counter_size_ratio(s_counter, mystr_counter)))
    
    def k(o):
        return o[1]
    mylist.sort(key=k, reverse=True)
    return mylist