import re

def solution(files):
    
    files = sorted(files, key=lambda str : int(re.search('\d+',str).group()))
    files = sorted(files, key=lambda str : re.match('^\D+',str.upper()).group())
    return files        

solution(	["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])