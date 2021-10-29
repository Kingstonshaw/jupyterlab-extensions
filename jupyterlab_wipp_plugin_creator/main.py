import os
from time import ctime
from pathlib import Path
import argparse
import logging

import numpy as np

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
    
    script_path = Path(__file__).parent

    logger.info(f'script path:{script_path}')
    
    logger.info('Arguments:')
    logger.info(f'Input collection: {args.input_collection}')
    logger.info(f'Configuration parameter: {args.config_param}')
    logger.info(f'Output collection: {args.output_collection}')
    logger.info(f'Random number generated with numpy: {np.random.rand()*args.config_param}')
    allFiles = os.listdir(args.input_collection)

# statistics on files present in args.input_collection which should automatically be the full path

    fileSizeArr = []
    measure = 'MB'

    logger.info(f'Files information in "{args.input_collection}":')
    for filepath in allFiles:
        split_tup = os.path.splitext(filepath)
        filepath = os.path.join(args.input_collection, filepath)
        fileSize = os.path.getsize(filepath)//(1024*1024)
        fileSizeArr.append(fileSize)
        logger.info(f'name:{split_tup[0]}, type: {split_tup[1]}, size: {fileSize} MB, created: {ctime(os.path.getmtime(filepath))}, last modified: {ctime(os.path.getctime(filepath))}')
    fileSizeArr.sort()
    collectionSize = sum(fileSizeArr)

    if collectionSize >= 1024:
        collectionSize = collectionSize//1024
        measure = 'GB'

    logger.info(f'Collection size is {collectionSize} {measure}. Average file size: {collectionSize//len(fileSizeArr)} MB, Max file size: {fileSizeArr[-1]} MB, Min file size: {fileSizeArr[0]} MB, Median file size: {fileSizeArr[len(fileSizeArr)//2]} MB')
        # logger.info(f'name:{split_tup[0]} type: {Path(file).suffix}, size:{os.path.getsize(file)}, creation time:{os.path.getmtime(file)}, modification time:{os.path.getctime(file)}')

if __name__ == "__main__":
    main()