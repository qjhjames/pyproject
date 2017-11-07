#import tensorflow as tf
#
#a = tf.constant([-1.0, 2.0])
#with tf.Session() as sess:
# b = tf.nn.relu(a)
# print sess.run(b)


from itertools import product
for x,y,z in product(['a','b','c'],['d','e','f'],['m','n']):

    print(x,y,z)





