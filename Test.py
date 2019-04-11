import tensorflow as tf


x = tf.constant(5)
y = tf.constant(6)

result = tf.multiply(x,y)


with tf.Session() as sess:
	print(sess.run(result))