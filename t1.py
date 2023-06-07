import tensorflow as tf

# Prepare to feed input, i.e. feed_dict and placeholders
w1 = tf.placeholder(tf.float32, name="w1")
w2 = tf.placeholder(tf.float32, name="w2")
b1 = tf.Variable(2.0,dtype=tf.float32, name="bias")
feed_dict = {'w1': 4.0, 'w2': 8.0}

# Define a test operation that we will restore
w3 = w1 + w2
w4 = tf.multiply(w3, b1, name="op_to_restore")
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# Create a saver object which will save all the variables
saver = tf.train.Saver()

# Run the operation by feeding input
result = sess.run(w4, {w1:feed_dict['w1'], w2:feed_dict['w2']})
print(result)
# Prints 24 which is sum of (w1+w2)*b1

# Now, save the graph
tf.train.write_graph(sess.graph_def, "./", "test.pb", as_text=False)
saver.save(sess, './my_test_model', global_step=1000)