import re


class TreeNode(object):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def contains_shiny_gold(self):
        if self.children == []:
            return False

        if any(child.name == "shiny gold" for child in self.children):
            return True

        return any(child.contains_shiny_gold() for child in self.children)


parse_line = re.compile(r"([a-z]+ [a-z]+) bags contain (.*)")


def build_nodes(text):
    nodes = {}
    # print(text)

    for line in text.splitlines():
        # print(line)
        match = parse_line.match(line)

        bag_name = match.group(1)
        nodes[bag_name] = TreeNode(bag_name)
    return nodes


parse_contents = re.compile(r"([a-z]+ [a-z]+) bags{0,1}[.,]")


def build_tree(text, nodes):
    for line in text.splitlines():
        match = parse_line.match(line)

        bag_name = match.group(1)
        # print(match.group(2))
        if match.group(2) == "no other bags.":
            continue
        else:
            contains = parse_contents.findall(match.group(2))
            # print(contains)

            for child_bag in contains:
                nodes[bag_name].add_child(nodes[child_bag])
    return nodes


def count_contains_shiny_gold(nodes):
    return sum([node.contains_shiny_gold() for node in nodes.values()])
