# -*- coding: utf-8 -*-
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel

class MyTopo(Topo):
    "Topologia customizada com multiplos switches e hosts."

    def __init__(self):
        "Cria a topologia customizada."

        # Inicializa a topologia
        Topo.__init__(self)

        # Adiciona hosts
        h1 = self.addHost('h1', mac='00:00:00:00:00:01')
        h2 = self.addHost('h2', mac='00:00:00:00:00:02')
        h3 = self.addHost('h3', mac='00:00:00:00:00:03')
        h4 = self.addHost('h4', mac='00:00:00:00:00:04')
        h5 = self.addHost('h5', mac='00:00:00:00:00:05')
        h6 = self.addHost('h6', mac='00:00:00:00:00:06')
        h7 = self.addHost('h7', mac='00:00:00:00:00:07')

        # Adiciona switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')

        # Conectando hosts aos switches
        self.addLink(h1, s2)
        self.addLink(h2, s6)
        self.addLink(h3, s6)
        self.addLink(h4, s5)
        self.addLink(h5, s4)
        self.addLink(h6, s3)
        self.addLink(h7, s7)

        # Conectando switches entre si
        self.addLink(s1, s2)
        self.addLink(s2, s4)
        self.addLink(s3, s4)
        self.addLink(s4, s5)
        self.addLink(s5, s6)
        self.addLink(s3, s7)

def run_topology():
    topo = MyTopo()
    net = Mininet(topo=topo, controller=Controller)
    net.start()

    # Teste de conectividade
    net.pingAll()

    # Inicia o CLI para testes adicionais
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run_topology()
