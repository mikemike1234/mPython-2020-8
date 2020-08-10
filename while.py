from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getTilePos()
    
    mc.postToChat("我正在看著你x:"+str(x)+"Y:"+str(y)+"Z:"+str(z))
    time.sleep(0.5)