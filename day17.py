#!/usr/bin/env python3
"""Problem - Day 17
Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
    dir
        subdir1
        subdir2
            file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
    dir
        subdir1
            file1.ext
            subsubdir1
        subdir2
            subsubdir2
                file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
Note:
- The name of a file contains at least a period and an extension.
- The name of a directory or sub-directory will not contain a period.
"""
class FSNode():
    def __init__(self, name: str, depth: int, parent=None):
        self.name = name
        self.depth = depth
        if '.' not in self.name:
            self.contents = []
        self.parent = parent

    def addNode(self, name: str, depth: int):
        if depth <= self.depth:
            new_node = self.parent.addNode(name, depth)
            return new_node
        else:
            new_node = FSNode(name, depth, self)
            self.contents.append(new_node)
            return self.contents[-1]

    def findDeepest(self):
        total_len = len(self.name)
        longest_child = {'name': None, 'len': 0}
        try:
            for i in self.contents:
                current_child = i.findDeepest()
                if current_child['len'] > longest_child['len']:
                    longest_child = current_child
        except AttributeError:
            if '.' not in self.name:
                return {'name': '0', 'len': 0}
            return {'name': self.name, 'len': total_len}
        try:
            total_len += 1 + longest_child['len']
            full_path = '/'.join([self.name, longest_child['name']])
        except TypeError:
            full_path = self.name
        if '.' not in full_path:
            return {'name': '0', 'len': 0}
        return {'name': full_path, 'len': total_len}


class FSMap():
    def __init__(self, fsstring: str):
        self.fss = fsstring
        self.fst = None
        self._buildTree()

    def _buildTree(self):
        fsl = [{'name': i.strip('\t'), 'depth': i.count('\t')} for i in self.fss.split('\n')]
        headNode = FSNode(fsl[0]['name'], fsl[0]['depth'])
        self.fst = headNode
        last_node = self.fst
        for node in fsl[1:]:
            last_node = last_node.addNode(node['name'], node['depth'])

    def deepestPath(self):
        deepest = self.fst.findDeepest()
        return deepest['name']


def main():
    fss1 = 'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext'
    fsm1 = FSMap(fss1)
    print(fsm1.deepestPath())
    fss2 = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
    fsm2 = FSMap(fss2)
    print(fsm2.deepestPath())
    fss3 = 'dir\n\tsubdir1\n\t\tsubsubdir1\n\tsubdir2'
    fsm3 = FSMap(fss3)
    print(fsm3.deepestPath())


if __name__ == '__main__':
    main()

