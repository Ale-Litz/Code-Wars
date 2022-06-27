#https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

def longest_consec(strarr, k):
    
    list_emp = []
    
    if (len(strarr) == 0) or (k <= 0) or (k > len(strarr)):
        return ''
    else:
        for i in range(0,len(strarr)):
            for j in range(0,k):
                strarr.append('')
            cnt_n = i
            cnt_t = 0
            txt = ''
            while cnt_t < k:
                txt += strarr[cnt_n]
                cnt_n += 1
                cnt_t += 1
            list_emp.append(txt)
            
    return max(list_emp, key = len)
