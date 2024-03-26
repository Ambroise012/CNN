from matplotlib import pyplot
import tensorflow as tf
# load the model
model = tf.keras.models.load_model('tensorboard.h5',compile='False')
# retrieve weights from the second hidden layer
filters, biases = model.layers[1].get_weights()
# normalize filter values to 0-1 so we can visualize them
f_min, f_max = filters.min(), filters.max()
filters = (filters - f_min) / (f_max - f_min)
# plot first few filters
n_filters, ix = 6, 1
for i in range(n_filters):
 # get the filter
   f = filters[:, :, :, i]
 # plot each channel separately
   for j in range(3):
 # specify subplot and turn of axis
      ax = pyplot.subplot(n_filters, 3, ix)
      ax.set_xticks([])
      ax.set_yticks([])
 # plot filter channel in grayscale
      pyplot.imshow(f[:, :, j], cmap='gray')
      ix += 1
# show the figure
pyplot.show()