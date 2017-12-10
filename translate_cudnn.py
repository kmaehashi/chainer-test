#!/usr/bin/env python

import sys

def translate_cudnn(cuda, cudnn):
    if cuda == 'cuda70' and cudnn in ['cudnn4']:
        return cudnn
    elif cuda == 'cuda75' and cudnn in ['cudnn5', 'cudnn51', 'cudnn6']:
        return cudnn
    elif cuda == 'cuda80' and cudnn in ['cudnn5', 'cudnn51', 'cudnn6', 'cudnn7']:
        return '{}-cuda8'.format(cudnn)
    elif cuda == 'cuda90' and cudnn in ['cudnn7']:
        return '{}-cuda9'.format(cudnn)
    raise RuntimeError('unsupported CUDA/cuDNN combination')

print(translate_cudnn(sys.argv[1], sys.argv[2]))
