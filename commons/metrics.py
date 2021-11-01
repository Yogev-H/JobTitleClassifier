#!/usr/bin/env python
# coding: utf-8

# In[1]:

from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score


def evaluate(y_true, y_pred, average='weighted'):
    precision = precision_score(y_true, y_pred, average=average)
    recall = recall_score(y_true, y_pred, average=average)
    f1 = f1_score(y_true, y_pred, average=average)
    accuracy = accuracy_score(y_true, y_pred)
    
    scores = {
        'precision': '{:.2f}'.format(precision),
        'recall': '{:.2f}'.format(recall),
        'f1': '{:.2f}'.format(f1),
        'accuracy': '{:.2f}'.format(accuracy)
    }
    return scores
