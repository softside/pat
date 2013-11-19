class Bag(object):
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self,target):
        curNode = self._head
        while curNode is not None and curNode.item != target:
            curNode = curNode.next
        return curNode is not None

    def add(self,item):
        newNode = _BagListNode(item)
        newNode.next = self._head
        self._head = newNode
        self._size +=1

    def remove(self,item):
        preNode = None
        curNode = self._head
        while curNode is not None and curNode.item != item:
            preNode = curNode
            curNode = curNode.next
        assert curNode is not None,"The item must be in the bag."
        self._size -=1
        if curNode is self._head:
            self._head = curNode.next
        else:
            preNode.next = curNode.next
        return curNode.item

    def __iter__(self):
        return _BagIterator(self._head)

class _BagListNode(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class _BagIterator:
    def __init__(self,listHead):
        self._curNode = listHead

    def __iter__(self):
        return self

    def next(self):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode.item
            self._curNode = self._curNode.next
            return item
