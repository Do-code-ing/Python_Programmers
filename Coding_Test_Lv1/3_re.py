new_id = "=.="
import re

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub("[\`\~\!\@\#\$\%\^\&\*\(\)\=\+\[\]\;\'\,\/\}\{\:\<\>\?\"]", "", new_id)
    new_id = re.sub("[.]{2,}",".",new_id)
    if new_id[:1] == ".":
        new_id = new_id[1:]
    if new_id[-1:] == ".":
        new_id = new_id[0:-1]
    if new_id == "":
        new_id = "a"
    if len(new_id) > 15:
        new_id = new_id[0:15]
    if new_id[-1:] == ".":
        new_id = new_id[0:-1]
    while len(new_id) <= 2:
        new_id += new_id[-1:]
    answer = new_id
    return answer

print(solution(new_id))

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub("[^a-z0-9\-_.]", "", new_id) # [^a-z0-9\-_.] ^~것들은 제외하고
    new_id = re.sub("\.+", ".", new_id)
    new_id = re.sub('^[.]|[.]$', '', new_id)
    new_id = "a" if len(new_id) == 0 else new_id[:15]
    new_id = re.sub("[.]$", "", new_id)
    new_id = new_id if len(new_id) > 2 else new_id + "".join([new_id[-1] for i in range(3-len(new_id))])
    answer = new_id
    return answer