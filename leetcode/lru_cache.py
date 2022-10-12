'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-11
    * Time : 8:53 p.m.
    * Question :
        Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

        Implement the LRUCache class:

        LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
        int get(int key) Return the value of the key if the key exists, otherwise return -1.
        void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
        If the number of keys exceeds the capacity from this operation, evict the least recently used key.
        The functions get and put must each run in O(1) average time complexity.
    * Example :
        Input
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
        Output
        [null, null, null, 1, null, -1, null, -1, 3, 4]

        Explanation
        LRUCache lRUCache = new LRUCache(2);
        lRUCache.put(1, 1); // cache is {1=1}
        lRUCache.put(2, 2); // cache is {1=1, 2=2}
        lRUCache.get(1);    // return 1
        lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        lRUCache.get(2);    // returns -1 (not found)
        lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        lRUCache.get(1);    // return -1 (not found)
        lRUCache.get(3);    // return 3
        lRUCache.get(4);    // return 4
'''
import sys
class DoubleLinkedList():
    def __init__(self):
        self.key=0
        self.value=0
        self.prev=None
        self.next=None
class LRUCache():
    def add_node(self,node):
        node.prev=self.head
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node
    def remove_node(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
    def move_to_head(self,node):
        self.remove_node(node)
        self.add_node(node)
    def pop(self):
        lst=self.tail.prev
        self.remove_node(lst)
        return lst
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache={}
        self.size=0
        self.head=DoubleLinkedList()
        self.tail=DoubleLinkedList()
        self.head.next=self.tail
        self.tail.prev=self.head
    def get(self,key):
        node=None
        if key in self.cache:
            node=self.cache[key]
            self.move_to_head(node)
            return node.value
        else:
            return -1
    def put(self,key,value):
        node=None
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self.move_to_head(node)
        else:
            node=DoubleLinkedList()
            node.key=key
            node.value=value
            self.cache[key]=node
            self.add_node(node)
            self.size+=1
            if self.size>self.capacity:
                node=self.pop()
                del self.cache[node.key]
                self.size-=1
if __name__=='__main__':
    oper=[sys.stdin.readline().rstrip('\n').split(',')]
    data=[list(x) for x in sys.stdin.readline().rstrip('\n').split(',')]
    lru_cache=None
    if oper[1]=='LRUCache':
        lru_cache=LRUCache((data[0])[0])
        for i in range(1,len(oper)):
            if oper[i]=='get':
                sys.stdout.write(str(lru_cache.get((data[i])[0])))
            elif oper[i]=='put':
                lru_cache.put((data[i])[0],(data[i])[1])
                sys.stdout.write('inserter successufully\n')
    else:
        sys.stdout.write('Not valid operation')

