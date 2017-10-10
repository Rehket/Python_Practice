

# Time for some Neural Network Practice

# So the main idea here is that we have object called a neuron that accepts some inputs and spits
# out an output based on those inputs. Once we have the output, we check it against the target and adjust the weights
# of the inputs.

from enum import Enum


Direction = Enum('Forward Reverse')
Phase = Enum('Train Test')
Preprocess = Enum('Default Colorization Edges')
Model = Enum('Basic UNET')


class SettingsObject:
    data_location = ''
    batch_size = 1
    load_size = 1
    fine_size = 1
    number_gen_filters = 64
    number_discriminator_filters = 64
    input_image_channels = 3
    output_image_channels = 3
    starting_iterations = 200 # How many epochs do we want...
    learning_rate = 0.0002
    beta_1 = 0.5
    num_training_examples = 100
    flip_images = False
    display_while_training = False
    display_window_id = 10
    display_plot = 'errL1'
    use_gpu = False
    name = ''
    training_direction = Direction.Forward
    preprocess = Preprocess.Default
    loading_threads = 2
    epoch_backup_frequency = 2
    save_latest_epoch_freq = 5000
    print_status_freq = 50
    display_freq = 100
    save_display_frequency = 5000
    continue_training = False
    use_serial_batches = False
    serial_batch_iterator = 2
    model_directory = './models'
    use_cudnn = False
    conditional_gan = True
    use_gan = True
    use_L1 = True
    which_model_discriminator = Model.Basic
    which_model_generator = Model.UNET
    number_discrim_layers = 0
    weight_L1 = 100








