import getFace as get
import train as tr
import  recognize as rec

# 0表示调用自带相机
model = 0
casade = 'haarcascade_frontalface_alt2.xml'
get.getFace(model=model, cascade=casade)
tr.train(cascade=casade)
rec.recognize(model=model, cascade=casade)