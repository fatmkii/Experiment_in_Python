import pyperclip
import re
import time

clip = pyperclip.paste()
mag = re.match('\w{40}?',clip)
if mag:
    pyperclip.copy('magnet:?xt=urn:btih:'+mag.group())
    print('Now the clip is:', pyperclip.paste())
    time.sleep(0.5)
    pyperclip.copy(clip)
else:
    print('Seems not a Magnetlink')
    time.sleep(0.5)