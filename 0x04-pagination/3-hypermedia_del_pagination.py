#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''Returns a dictionary with index, next index, page_size and data'''
        assert isinstance(index, int)
        assert index <= list(self.__indexed_dataset.keys())[-1]
        aux_iterator = iter(self.__indexed_dataset.values())
        for _ in range(0, index):
            next(aux_iterator)
        data = [next(aux_iterator) for _ in range(page_size)]
        aux_iterator = iter(self.__indexed_dataset.keys())
        for _ in range(0, (index * page_size)):
            next_index = next(aux_iterator)
        ret_dict = {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
        return ret_dict
