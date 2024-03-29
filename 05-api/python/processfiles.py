# Usage:
# spark-submit  processfiles.py  <files to process>
# spark-submit  --master spark://localhost:7077 processfiles.py  <files to process>

# Multiple files can be specified

#e.g:
#- with 4G executor memory and turning off verbose logging
#   spark-submit  --master spark://localhost:7077 --executor-memory 4g   --driver-class-path logging/    processfiles.py  /data/text/twinkle/1G.data
#

import sys
import time
from pyspark.sql import SparkSession

if len(sys.argv) < 2:
    sys.exit("need file(s) to load")

## TODO 1: Give a name
spark = SparkSession.builder.appName("Process Files -- MYNAME").getOrCreate()

print('### Spark UI available on port : ' + spark.sparkContext.uiWebUrl.split(':')[2])

for file in sys.argv[1:]:
    ## TODO-2 : read a file as dataset
    ## hint : spark.read.text(file)
    f = ???(file)

    t1 = time.perf_counter()
    ## TODO-3 : Count the number of lines
    ## Hint : count
    count = f.???()
    t2 = time.perf_counter()

    print("### {}: count:  {:,} ,  time took:  {:,.2f} ms".format(file, count, (t2-t1)*1000))

    # end of for loop


# line = input('### Hit Ctrl+C to terminate the program...')

print("Press Enter to continue...")

scanner = spark.sparkContext._gateway.jvm.java.util.Scanner
sys_in = getattr(spark.sparkContext._gateway.jvm.java.lang.System, 'in')
result = scanner(sys_in).nextLine()

spark.stop()  # close the session
