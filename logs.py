import logging

logging.basicConfig(filename='logs', level=logging.INFO, filemode='a')

try:
    print(10 / 1)
    logging.info('код работает корректно!')
except Exception as e:
    #logging.error(e) 
    logging.exception(e)   
