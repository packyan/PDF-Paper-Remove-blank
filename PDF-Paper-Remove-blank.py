import pyperclip
def is_Chinese_pdf(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

needed_process_content = pyperclip.paste()
processed_content = ""
lines = needed_process_content.split('\r\n')
last_line = ''        
for index , line  in enumerate(lines):

    is_ch_line = 0
    #print(line[-1])
    #print(line)
    if(is_Chinese_pdf(line)):
       #chinese line remove space
       line = line.strip()
       is_ch_line = 1
       #print('ch')
    if(len(line) <= 2):
        processed_content += line
        #print("5")
        continue
    #小标题
    if(line[0].isdigit() and line[1]=='.'):
        processed_content += '\n\n' + line + '\n\n'
        continue    
    #段落
    if(index > 0 and lines[index-1][-1]== '.' and  line[0].isupper()):
        processed_content += "\n \n" + line + ' '
        #print('s')
        continue
    if(is_ch_line == 0 and line[-1] == '-'):
        processed_content += line
        #print("2")
    elif(line[-1] == '.' or line[-1] != '。' ):
        #print("3")
        processed_content += line + ('' if(is_ch_line) else ' ' )
        #print(line)
    else:
        processed_content += line
        #print("4")
#write to cpoyboard
pyperclip.copy(processed_content)
