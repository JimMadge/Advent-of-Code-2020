import re


class TreeNode(object):
    def __init__(self, name):
        self.name = name
        self.children = []
        self.n_children = []

    def add_child(self, child, number):
        self.children.append(child)
        self.n_children.append(number)

    def contains_shiny_gold(self):
        if self.children == []:
            return False

        if any(child.name == "shiny gold" for child in self.children):
            return True

        return any(child.contains_shiny_gold() for child in self.children)

    def total_children(self):
        if self.children == []:
            return 0

        return (
            sum(self.n_children) +
            sum([number * child.total_children()
                 for number, child in zip(self.n_children, self.children)])
        )


parse_line = re.compile(r"([a-z]+ [a-z]+) bags contain (.*)")


def build_nodes(text):
    nodes = {}

    for line in text.splitlines():
        match = parse_line.match(line)

        bag_name = match.group(1)
        nodes[bag_name] = TreeNode(bag_name)
    return nodes


parse_contents = re.compile(r"(\d) ([a-z]+ [a-z]+) bags{0,1}[.,]")


def build_tree(text, nodes):
    for line in text.splitlines():
        match = parse_line.match(line)

        bag_name = match.group(1)
        if match.group(2) == "no other bags.":
            continue
        else:
            contains = parse_contents.findall(match.group(2))

            for number, child_bag in contains:
                nodes[bag_name].add_child(nodes[child_bag], int(number))
    return nodes


def count_contains_shiny_gold(nodes):
    return sum([node.contains_shiny_gold() for node in nodes.values()])
