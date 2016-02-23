import re
def regexStrip(string, chars='\s'):                 
    if chars != '\s':                               
        chars = '[' + chars + ']'                   
    regexFormat = '^' + chars + '*|' + chars + '*$' 
    stripRegex = re.compile(regexFormat)            
    strippedString = stripRegex.sub('', string)     
    print(strippedString)
    return strippedString

testString = '      Howdy World        '

regexStrip(testString)

