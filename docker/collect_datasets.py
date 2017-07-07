import chainer.datasets as D

def collect(name, func):
    print('Collecting {} dataset...'.format(name))
    func()

collect('MNIST', D.get_mnist)
collect('CIFAR-10', D.get_cifar10)
collect('CIFAR-100', D.get_cifar100)
print('Done!')
