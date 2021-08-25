
from modules import upbitmod as ubm
from modules import loggermod as lgm
from modules import configmod as cfm
from modules import datasetmod as dsm
from modules import testmod as ttm
lgm.init()
lgm.logmsg('Initlizing logger module finished.','info')
cfm.init()
lgm.logmsg('Initlizling data module finished.','info')

if cfm.isupdated_read()=='1':
    dsm.init()
    lgm.logmsg('Updated coin dataset.','info')
cfm.version_read()
lgm.logmsg('Loading account data finished.','info')
#ubm.init_account()
ttm.trader()
