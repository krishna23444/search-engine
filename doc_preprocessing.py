#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
import os

from text_class.Document import Document

def get_docs_list(doc_foldr):
    document_list = []
    for root, _, files in os.walk(doc_foldr):
        for f in files:
            document_list.append(f)
    return document_list


def init_docs(document_list, doc_foldr='data/'):
    doc_id = 0
    documents = []
    for doc in document_list:
        documents.append(Document(doc_id, doc, doc_foldr))
        doc_id += 1
    return documents

if __name__=='__main__':
    document_list = get_docs_list('data/')
    documents = init_docs(document_list)
    for doc in documents:
        doc.to_one_line()
        doc.output_one_line('output/processed_data/')
        doc = []
