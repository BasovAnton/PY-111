"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
# import networkx as nx

root = {
    "key":8,
    "value": 8,
    "left": {
        "key": 3,
        "value": 3,
        "left": None,
        "right": None
    },
    "right": {
        "key": 10,
        "value": 10,
        "left": None,
        "right": None
    },
}


class BinarySearchTree:
    @staticmethod
    def _create_node(key, value, left = None, right = None):

        return {
            "key": key,
            "value": value,
            "left": left,
            "right": right
        }

    def __init__(self):
        self.root = None

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree

        :param key: key from pair (key is used for positioning node in the tree)
        :param value: value associated with key
        :return: None
        """
        if self.root is None:
            self.root = self._create_node(key, value)
        else:
            current_node = self.root
            while True:
                current_key = current_node["key"]
                if key > current_key:
                    # правое
                    right_node = current_node["right"]
                    if right_node is None:
                        current_node["right"] = self._create_node(key, value)
                        break
                    current_node = current_node["right"]
                else:
                    left_node = current_node["left"]
                    if left_node is None:
                        current_node["left"] = self._create_node(key, value)
                        break
                    else:
                        current_node = current_node["left"]

        return None

    def remove(self, key: int) -> Optional[Tuple[int, Any]]:
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """
        print(key)
        return None

    def find(self, key: int) -> Optional[Any]:
        """
        Find value by given key in the BST
        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """

        def _find(current_node: Optional[dict]):
            if current_node is None:  # базовый случай
                raise KeyError
            current_key = current_node["key"]
            if current_key == key:
                return current_node["value"]

            next_node = current_node["left"] if key < current_key else current_node["right"]
            return _find(next_node)

        return _find(self.root)

    def clear(self) -> None:
        """
        Clear the tree

        :return: None
        """
        return None
