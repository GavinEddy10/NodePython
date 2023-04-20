class Node:

    # could add link node value in none
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def get_value(self):
        return self.value

    def get_link_node(self):
        return self.link_node

    def set_link_node(self, link_node):
        self.link_node = link_node

    def to_string(self, null=None):
        if self.get_link_node() != null:
            print("{value: " + str(self.value) + ", link_node: " + str(self.link_node.get_value()) + "}")
