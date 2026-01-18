import os
import pickle
from googleapiclient.discovery import build
def conectar():
    with open('token.pickle', 'rb') as t: return pickle.load(t)
def get_drive(): return build('drive', 'v3', credentials=conectar())
def get_docs(): return build('docs', 'v1', credentials=conectar())
