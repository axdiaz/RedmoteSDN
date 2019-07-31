from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.log import setLogLevel
from mininet.link import Link, TCLink


def topology():
    net = Mininet(controller=RemoteController)

    # Add hosts and switches

    h1 = net.addHost('h1', ip="10.0.1.10/24", mac="00:00:00:00:00:01")
    h2 = net.addHost('h2', ip="10.0.2.10/24", mac="00:00:00:00:00:02")

    r1 = net.addHost('r1')

    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    net.addLink(r1, s1)
    net.addLink(r1, s2)
    net.addLink(h1, s1)
    net.addLink(h2, s2)

    net.build()


if __name__ == '__main__':
    setLogLevel('info')

    topology()
