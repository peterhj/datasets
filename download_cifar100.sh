#!/bin/sh
set -eu

mkdir -p cifar100
cd cifar100
curl -O "http://www.cs.toronto.edu/~kriz/cifar-100-binary.tar.gz"
tar -xzkf cifar-100-binary.tar.gz
cp cifar-100-binary/train_batch.bin train.bin
cp cifar-100-binary/test_batch.bin test.bin
