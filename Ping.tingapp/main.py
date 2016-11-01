import tingbot
from tingbot import *
import subprocess as sp

address = "4.2.2.2"

@every(seconds=1)
def loop():
    screen.fill(color='black')
    
    res = sp.Popen(['ping', '-c1', address], stdout=sp.PIPE, stderr=sp.PIPE)
    
    out, err = res.communicate()
    print out
    
        
    screen.text(
        out,
        xy=(10,10),
        align='topleft',
        color=(46, 204, 113),
        font_size=14,
        max_width=300
    )
tingbot.run()