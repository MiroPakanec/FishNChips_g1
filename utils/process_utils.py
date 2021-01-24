from utils.preprocessing.AttentionDataGenerator import AttentionDataGenerator
from utils.preprocessing.TestGenerator import TestGenerator

def get_generator(model_config, process_config, kind=""):
    data = process_config['data']
    stride = process_config['stride']
    print(f"*** constructin {kind} generator...")
    return AttentionDataGenerator(
        data, 
        process_config['batch_size'], 
        stride, 
        model_config['encoder_max_length'], 
        model_config['decoder_max_length'])

def get_test_generator(model_config, process_config, kind=""):
    data = process_config['data']
    stride = process_config['stride']
    print(f"*** constructin {kind} generator...")
    return TestGenerator(
        data, 
        process_config['batch_size'], 
        stride, 
        model_config['encoder_max_length'], 
        model_config['decoder_max_length'])