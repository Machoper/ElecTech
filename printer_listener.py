import time
import urllib.request, json
from escpos.printer import Usb

starttime = time.time()
p = Usb(0x0456, 0x0808, 0, 0x81, 0x03)

while True:
    with urllib.request.urlopen("http://localhost:8000/printer/?key=electech") as url:
        data = json.loads(url.read().decode())
        for i in data:
            p.text(str(i.get("fields").get("title"))+"\n")
            p.text(str(i.get("fields").get("party"))+"\n")
            p.text(str(i.get("fields").get("running_mate"))+"\n")
            p.text(str(i.get("fields").get("question_text"))+"\n\n\n")

    time.sleep(1.0 - ((time.time() - starttime) % 1.0))
