from Node import *

yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

yacko.set_link_node(dot)
dot.set_link_node(wacko)

yacko.to_string()
dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()


