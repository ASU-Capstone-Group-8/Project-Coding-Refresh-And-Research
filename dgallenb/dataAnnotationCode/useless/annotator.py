# Source: https://medium.com/swlh/data-annotation-using-active-learning-with-python-code-aa5b1fe13608

import tensorflow as tf
from tensorflow import keras

def main():
    for i in range(30):
        print('*'*50)
        model = create_model()
        custom_loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)
        model.compile(optimizer='adam', loss=custom_loss, metrics=['accuracy'])
        model.fit(X, y, epochs=20, batch_size=8, verbose=0)
        uncertain_idx, entropy_avg = max_entropy_acquisition(X_pooled, 100, 20)
        print('Average Entropy: {}'.format(entropy_avg))
        X, y, X_pooled, y_pooled = manage_data(X, y, X_pooled, y_pooled, uncertain_idx)
        print('Iteration Done: {}'.format(i+1))


def manage_data(X, y, X_pooled, y_pooled, idx):
      """
      After every iteration, the uncertain unlabelled data will be given the true labels (in reality the manual annotator will label the data)
      Args:
        X: ndarray, Training Features
        y: ndarray, Training Labels (true)
        X_pooled: ndarray, Unlabelled dataset
        y_pooled: ndarray, True labels of the unlabelled dataset
        idx: ndarray,list, uncertain data index
      Returns:
        Lablled and unlabelled dataset
      """

      pool_mask = np.ones(len(X_pooled), dtype=bool)
      pool_mask[idx] = False
      pool_mask_2 = np.zeros(len(X_pooled), dtype=bool)
      pool_mask_2[idx] = True
      new_training = X_pooled[pool_mask_2]
      new_label = y_pooled[pool_mask_2]
      X_pooled = X_pooled[pool_mask]
      y_pooled = y_pooled[pool_mask]
      X = np.concatenate([X, new_training])
      y = np.concatenate([y, new_label])

      return X, y, X_pooled, y_pooled

def max_entropy_acquisition(X_pool, T, num_query):
      """
      Calculate the entropy of the ensempe of models (by using MC Dropout).
      Get the max entropy and return the index of the data

      Args:
        X_pool: ndarray, Pooled dataset (unlabelled)
        T: int, number of iteration to replicate ensemble model using MC Dropout
        num_query: int, number of datapoints to be returned by the model per itration

      Returns:
        Index points of uncertain dataset
        mean entropy value
      """

      proba_all = np.zeros(shape=(X_pool.shape[0], 10))
      for _ in range(T):
            probas = model.predict(X_pool)
            proba_all += probas
      avg_proba = np.divide(proba_all, T)
      entropy_avg = sp.stats.entropy(avg_proba, base=10, axis=1)
      uncertain_idx = entropy_avg.argsort()[-num_query:][::-1]
      return uncertain_idx, entropy_avg.mean()

def create_model():
      # Input Layer
      input_layer = tf.keras.Input(shape=(64,), name='input_layer') # Feature dimension=64
      input_dropout_layer = tf.keras.layers.Dropout(0.4, name='input_dropout_layer')(input_layer, training=True) #training=True activates MC Dropout

      # Hidden Layer 1
      dense_layer_1 = tf.keras.layers.Dense(256, activation='relu', name='dense_layer_1')(input_dropout_layer)
      dropout_layer_1 = tf.keras.layers.Dropout(0.4, name='dropout_layer_1')(dense_layer_1, training=True)

      # Hidden Layer 2
      dense_layer_2 = tf.keras.layers.Dense(256, activation='relu', name='dense_layer_2')(dropout_layer_1)
      dropout_layer_2 = tf.keras.layers.Dropout(0.4, name='dropout_layer_2')(dense_layer_2, training=True)

      # Hidden Layer 3
      dense_layer_3 = tf.keras.layers.Dense(256, activation='relu', name='dense_layer_3')(dropout_layer_2)
      dropout_layer_3 = tf.keras.layers.Dropout(0.4, name='dropout_layer_3')(dense_layer_3, training=True)

      # Output Layer
      output_layer = tf.keras.layers.Dense(len(digits['target_names']), activation='softmax', name='output_layer')(dropout_layer_3)

      # Model Init
      model = tf.keras.Model(inputs=input_layer, outputs=output_layer, name='Model')

      return model
