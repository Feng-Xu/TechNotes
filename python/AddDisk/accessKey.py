#  coding=utf-8
import logging
import json
from aliyunsdkcore import client
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526.DescribeRegionsRequest import DescribeRegionsRequest

# configuration the log output formatter, if you want to save the output to file,
# append ",filename='ecs_invoke.log'" after datefmt.
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

clt = client.AcsClient('', '', 'cn-beijing')

# send open api request
def _send_request(request):
    request.set_accept_format('json')
    try:
        response_str = clt.do_action_with_exception(request)
        logging.info(response_str)
        response_detail = json.loads(response_str)
        return response_detail
    except Exception as e:
        logging.error(e)

def _print_region_id(item):
    region_id = item.get("RegionId")
    return region_id

def hello_aliyun_regions():
    request = DescribeRegionsRequest()
    response = _send_request(request)
    if response is not None:
        #logging.info(response)
        region_list = response.get('Regions').get('Region')
        #logging.info(region_list)
        # 断言变量不为空
        assert response is not None
        assert region_list is not None
        result = list(map(_print_region_id, region_list))
        logging.info("region list: %s", result)

def _get_instance_id(item):
    return item.get('InstanceId')

# 获取指定区域的主机list
def list_instance(regionid):
    request = DescribeInstancesRequest()
    # 指定查询区域，默认北京
    if regionid is None:
        regionid = cn-beijing
    request.add_query_param('RegionId', regionid)
    response = _send_request(request)
    if response is not None:
        instance_list = response.get('Instances').get('Instance')
        #result = list(map(_get_instance_id, instance_list))
        #logging.info("instances list: %s",result)
        return instance_list

def get_instance_id(regionid, hostname):
    instances_list = list_instance(regionid)
    if instances_list is not None:
        logging.info(instances_list)

if __name__ == '__main__':
    logging.info("hello Aliyun openApi!")
    #hello_aliyun_regions()
    #list_instance()
    get_instance_id('cn-beijing', 'l-test-xufeng1.ops.dev.ali.dm')
