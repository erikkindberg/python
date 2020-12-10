

"""
Add depth to the current package stucture (tasks) so that the import statement below works.

restrictions:
1) shallow, deeper, deepest, too_deep should all be folders
2) deepseafish is the following function:

    def deepseafish():
        return "bluop  bluop bluop"

3) deepseafish() should be located in a file called "something_in_the_deep.py"
"""
import sys
sys.path.append('./shallow/deeper/deepest/too_deep')
from something_in_the_deep import deepseafish

def whats_at_the_bottom():
    return deepseafish()


print(whats_at_the_bottom())