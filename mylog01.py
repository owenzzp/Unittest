from loguru import logger

logger.info('info')
logger.debug('debug')
logger.warning('warning')
logger.success('success')
logger.error('error')

logger.add('a.txt', format='{time:YYYY-MM-DD hh:mm:ss} | {level} | {message}', level = 'WARNING')

logger.info("这是一条{}的日志".format('error'))