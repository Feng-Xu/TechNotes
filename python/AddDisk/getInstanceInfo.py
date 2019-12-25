# coding=utf-8

import baseInfo
from math import ceil
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest

def _get_instance_id(item):
    return item.get('InstanceId')


# 进行主机名的匹配，取出实例信息
def _get_special_info(item, hostname):
    instanceName = item.get('InstanceName')
    if instanceName == hostname:
        return item.get('InstanceId'), item.get('RegionId'), item.get('ZoneId')


# 分页取出所有实例
# 指定查询区域，默认北京
def get_page_instances(pageNumber, regionid = 'cn-beijing'):
    request = DescribeInstancesRequest()
    request.add_query_param('RegionId', regionid)
    # 设置分页大小为100，默认是10
    request.set_PageSize(100)
    request.set_PageNumber(pageNumber)
    response = baseInfo.send_request(request)

    if response is not None:
        return response.get('Instances').get('Instance')


# 取出特定主机的信息
def get_instance_info(hostname, regionid='cn-beijing'):
    request = DescribeInstancesRequest()
    request.add_query_param('RegionId', regionid)
    response = baseInfo.send_request(request)
    # 获取数据总条数，设置分页大小
    totalCount = response.get('TotalCount')
    # 向上取整
    pageNuber = ceil(totalCount / 100)
    for i in range(1, pageNuber+1):
        pageInstancesList = get_page_instances(i, regionid)
        print(type(pageInstancesList))
        if pageInstancesList is not None:
            for instance in pageInstancesList:
                result_info = _get_special_info(instance, hostname)
                if result_info is not None:
                    return result_info


# 推荐使用这个方法
# 获取指定区域的指定主机
# 指定查询区域，默认北京
def get_special_instance(hostname, regionid='cn-beijing'):
    request = DescribeInstancesRequest()
    request.add_query_param('RegionId', regionid)
    request.set_InstanceName(hostname)
    response = baseInfo.send_request(request)
    if response is not None:
        instances = response.get('Instances').get('Instance')
        #baseInfo.logger.info(instances)
        if len(instances) == 1:
            instanceInfo = instances[0].get('InstanceName'), instances[0].get('InstanceId'), instances[0].get('RegionId'), instances[0].get('ZoneId')
            baseInfo.logger.info("实例信息：%s", instanceInfo)
            return instanceInfo
        elif len(instances) > 1:
            baseInfo.logger.error("%s 中主机名有重名", regionid)
            return 0
        else:
            baseInfo.logger.error("%s 没有该主机", regionid)
            return 0
    else:
        baseInfo.logger.error("查询主机失败")
        return 0


if __name__ == '__main__':
    baseInfo.logger.info("Get Instances Info")
    #print(get_instance_info('l-test-xufeng1.ops.dev.ali.dm', 'cn-beijing'))
    print(get_special_instance('l-test-xufeng1.ops.qd.ali.dm', 'cn-beijing'))