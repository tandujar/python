# \r\n -> CRLF (Windows)
# \n -> LF (Linux | Mac)

#apenas um exemplo que posso colocar qq coisa mas ele vai entender o \n para mudar a linha também se estiver junto
#por padrao o \n para dar quebrar a linha (enter) já é implicito no print
print(12, 34, 1011, sep="-", end='##\n') 
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')