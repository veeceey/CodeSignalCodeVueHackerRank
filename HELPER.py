## class url, label, children , those children might have children


##navigation item

class NavigationItem:
    def __init__(self):



# public class NavigationItem {public string Url;public string Label;public List<NavigationItem> Children}


def helper(children):
    if not children:
        return ##base case
    if children:
        print(URL, Label, children )
    for child in children:
        helper(child)
helper(NavigationItem)

[]
#### ({3:[3]})