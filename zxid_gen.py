from kazoo.client import KazooClient
import os

zk_timeout = 60.0
if "ZK_TIMEOUT" in os.environ:
  zk_timeout = float(os.environ['ZK_TIMEOUT'])

print(os.environ['ZK_HOST'])
zk = KazooClient(hosts=os.environ['ZK_HOST']+':2181',timeout=zk_timeout)
zk.start()

node = "/ZOOKEEPER-832"

if zk.exists(node):
  zk.delete(node, recursive=True)

zxids_increase = 100
if "ZXIDS_INCREASE" in os.environ:
  zxids_increase = int(os.environ['ZXIDS_INCREASE'])

print("adding " + str(zxids_increase) + " zxids...")
# Create zxids
zk.create(node, b"oh no...!")
for x in range(zxids_increase):
  zk.set(node, b"fix me")
else:
  print("Finally finished!")

zk.stop()