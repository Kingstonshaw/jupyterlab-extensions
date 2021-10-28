import numpy as np
import argparse
import logging

def main():
    
    # intitialize logging
    logging.basicConfig(format='%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    logger = logging.getLogger("main")
    logger.setLevel(logging.INFO)
    
    # Setup the Argument parsing
    parser = argparse.ArgumentParser(prog='script', description='Script to execute Jupyter Notebooks')

    # Parse input arguments from WIPP format: '--PARAMETER VALUE'
    parser.add_argument('--inputImages', dest='input_collection', type=str, help='Input Images', required=True)
    parser.add_argument('--configParam', dest='config_param', type=float, help='Configuration parameter value', required=False)
    parser.add_argument('--outputCollection', dest='output_collection', type=str, help='output collection', required=True)
    
    args = parser.parse_args()
    
    logger.info('Arguments:')
    logger.info(f'Input collection: {args.input_collection}')
    logger.info(f'Configuration parameter: {args.config_param}')
    logger.info(f'Output collection: {args.output_collection}')
    logger.info(f'Random number generated with numpy: {np.random.rand()*args.config_param}')

if __name__ == "__main__":
    main()