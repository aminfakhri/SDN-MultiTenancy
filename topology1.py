from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController
from mininet.link import Intf
from time import sleep

# Specify the controller IP
CONTROLLER_IP = '192.168.122.1'

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self):
        s1 = self.addSwitch('s1', dpid='100')
	#tenant1
        a1 = self.addHost('a1', mac="00:00:00:00:00:01", ip="10.1.1.1/24")
        a2 = self.addHost('a2', mac="00:00:00:00:00:02", ip="10.1.1.2/24")
        a7 = self.addHost('a7', mac="00:00:00:00:00:07", ip="10.1.1.7/24")
        a8 = self.addHost('a8', mac="00:00:00:00:00:08", ip="10.1.1.8/24")
	#tenant2
        b1 = self.addHost('b1', mac="00:00:00:00:10:01", ip="172.16.1.1/24")
        b2 = self.addHost('b2', mac="00:00:00:00:10:02", ip="172.16.1.2/24")
        b7 = self.addHost('b7', mac="00:00:00:00:10:07", ip="172.16.1.7/24")
        b8 = self.addHost('b8', mac="00:00:00:00:10:08", ip="172.16.1.8/24")
	#tenant3
        c1 = self.addHost('c1', mac="00:00:00:00:20:01", ip="10.2.1.1/24")
        c2 = self.addHost('c2', mac="00:00:00:00:20:02", ip="10.2.1.2/24")
        c7 = self.addHost('c7', mac="00:00:00:00:20:07", ip="10.2.1.7/24")
        c8 = self.addHost('c8', mac="00:00:00:00:20:08", ip="10.2.1.8/24")
        self.addLink(a1, s1)
        self.addLink(a2, s1)
        self.addLink(a7, s1)
        self.addLink(a8, s1)
        self.addLink(b1, s1)
        self.addLink(b2, s1)
        self.addLink(b7, s1)
        self.addLink(b8, s1)
        self.addLink(c1, s1)
        self.addLink(c2, s1)
        self.addLink(c7, s1)
        self.addLink(c8, s1)

if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip=CONTROLLER_IP)
    net = Mininet(topo=topo, controller=c1)
    net.start()
    sleep(5)
    net.pingAll()
    CLI(net)
    net.stop()
