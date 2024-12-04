def longestprefix (s1):
    if s1 ==[]:
        return""
    if len (s1) ==1:
        return s1[0]
    s1.sort()
    prefix = ""
    longest = s1[0]
    for i in range(len(longest)):
        if s1[len(s1)-1][i]==longest[i]:
            prefix = prefix +s1[len(s1)-1][i]
        else:
            break
    return prefix



