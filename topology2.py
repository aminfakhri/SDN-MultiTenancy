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
        s2 = self.addSwitch('s2', dpid='200')
	#tenant1
        a3 = self.addHost('a3', mac="00:00:00:00:00:03", ip="10.1.1.3/24")
        a4 = self.addHost('a4', mac="00:00:00:00:00:04", ip="10.1.1.4/24")
        a9 = self.addHost('a9', mac="00:00:00:00:00:09", ip="10.1.1.9/24")
        a10 = self.addHost('a10', mac="00:00:00:00:00:10", ip="10.1.1.10/24")
	#tenant2
        b3 = self.addHost('b3', mac="00:00:00:00:10:03", ip="172.16.1.3/24")
        b4 = self.addHost('b4', mac="00:00:00:00:10:04", ip="172.16.1.4/24")
        b9 = self.addHost('b9', mac="00:00:00:00:10:09", ip="172.16.1.9/24")
        b10 = self.addHost('b10', mac="00:00:00:00:10:10", ip="172.16.1.10/24")
	#tenant3
        c3 = self.addHost('c3', mac="00:00:00:00:20:03", ip="10.2.1.3/24")
        c4 = self.addHost('c4', mac="00:00:00:00:20:04", ip="10.2.1.4/24")
        c9 = self.addHost('c9', mac="00:00:00:00:20:09", ip="10.2.1.9/24") 
        c10 = self.addHost('c10', mac="00:00:00:00:20:10", ip="10.2.1.10/24")
        self.addLink(a3, s2)
        self.addLink(a4, s2)
        self.addLink(a9, s2)
        self.addLink(a10, s2)
        self.addLink(b3, s2)
        self.addLink(b4, s2)
        self.addLink(b9, s2)
        self.addLink(b10, s2)
        self.addLink(c3, s2)
        self.addLink(c4, s2)
        self.addLink(c9, s2)
        self.addLink(c10, s2)

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
