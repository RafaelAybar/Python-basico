import time
import webbrowser

cuenta_descanso = 0

print("Este programa empieza" +time.ctime() )
for v in range (0, 4):
    time.sleep (10)
    webbrowser.open ("https://www.google.es")
    v = cuenta_descanso + 1

