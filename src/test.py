import tensorflow as tf
print("You are using TensorFlow version", tf.__version__)




if tf.test.gpu_device_name():

    print('Default GPU Device:{}'.format(tf.test.gpu_device_name()))

else:

   print("Please install GPU version of TF")

