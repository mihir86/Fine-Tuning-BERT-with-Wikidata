# -*- coding: utf-8 -*-
"""Probing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10QROKTDln6gOrpzRW3DFkX96mKVG6v9t
"""

#!pip install transformers

import warnings
warnings.filterwarnings("ignore")
import torch
import tensorflow as tf
import numpy as np
import pandas as pd
from transformers import pipeline
from transformers import AutoModelWithLMHead, AutoTokenizer
from transformers import RobertaTokenizer, TFRobertaForMaskedLM
from transformers import XLNetConfig, XLNetModel
from transformers import XLNetTokenizer, XLNetLMHeadModel
from transformers import AlbertTokenizer, AlbertForMaskedLM
import io

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased")
model = AutoModelWithLMHead.from_pretrained("distilbert-base-cased")

sequence = f"Which is longer, and thus has more [MASK], nut or bolt"

input = tokenizer.encode(sequence, return_tensors="pt")
mask_token_index = torch.where(input == tokenizer.mask_token_id)[1]

token_logits = model(input)[0]
mask_token_logits = token_logits[0, mask_token_index, :]

top_5_tokens = torch.topk(mask_token_logits, 5, dim=1).indices[0].tolist()

for token in top_5_tokens:
    print(sequence.replace(tokenizer.mask_token, tokenizer.decode([token])))

def bertProbing(tokenizer, model) :
    for i in range(1,4):
        d = []
        
        with open(f'{i}.masked_data_width.txt') as f:
            
            for index, line in enumerate(f):

                sequence = line

                input = tokenizer.encode(sequence, return_tensors="pt")
                mask_token_index = torch.where(input == tokenizer.mask_token_id)[1]

                token_logits = model(input)[0]
                mask_token_logits = token_logits[0, mask_token_index, :]

                top_5_tokens = torch.topk(mask_token_logits, 5, dim=1).indices[0].tolist()

                best_token_string = ""
                cnt = 0
                for token in top_5_tokens:
                    best_token_string += tokenizer.decode([token])
                    cnt+=1
                    if cnt!=5:
                        best_token_string += ", "
                    #print(sequence.replace(tokenizer.mask_token, tokenizer.decode([token])))
                d.append([sequence,best_token_string])
                break

        df = pd.DataFrame(d, columns = ['Masked Sentence', 'Prediction'])
        print(df)
        df.to_csv(f'BERT Probing/Probing_List_{i}.csv', encoding="utf-8")

bertProbing(tokenizer, model)
