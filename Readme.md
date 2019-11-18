# zxid_generator 

a simple helper to generate zxids, as a aworkaround for [ZOOKEEPER-832](https://issues.apache.org/jira/browse/ZOOKEEPER-832)

## why?
we deploy our entire Solr 8.x.x with/Zookeeper 3.5.x ensemble without persistence of the previous deployment.
As a result we encountered following issue: [ZOOKEEPER-832](https://issues.apache.org/jira/browse/ZOOKEEPER-832)

## how?

`docker run -it --rm -e ZK_HOST=zookeeper.local zxid_generator`

the default zxids to generate is 100...
if you need more add ZXIDS_INCREASE environment variable and set it to a valid integer