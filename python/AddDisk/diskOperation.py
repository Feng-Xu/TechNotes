# coding=utf-8

import json
import time
import baseInfo
import getInstanceInfo
from aliyunsdkecs.request.v20140526.CreateDiskRequest import CreateDiskRequest
from aliyunsdkecs.request.v20140526.AttachDiskRequest import AttachDiskRequest
from aliyunsdkecs.request.v20140526.ModifyDiskChargeTypeRequest import ModifyDiskChargeTypeRequest


# 创建磁盘
def createDisk(instanceInfo, size, diskCategory):
    createDiskRequest = CreateDiskRequest()
    createDiskRequest.add_query_param('RegionId', instanceInfo[2])
    createDiskRequest.set_ZoneId(instanceInfo[3])
    createDiskRequest.set_Size(size)
    createDiskRequest.set_DiskCategory(diskCategory)
    createDiskRequest.set_DiskName(instanceInfo[0])
    response = baseInfo.send_request(createDiskRequest)
    baseInfo.logger.info('创建磁盘返回信息： %s', response)
    # 添加创建磁盘状态
    if response is not None:
        baseInfo.logger.info("创建磁盘 %s 成功。", response.get('DiskId'))
        response['status'] = 1
        # 转化为json返回
        response_json = json.dumps(response)
        return response_json
    else:
        response = {}
        response['status'] = 0
        response_json = json.dumps(response)
        return response_json


# 更改磁盘付费类型,默认修改为包年包月
def modify_disk_charge_type(disk_id_list, instance_info, disk_charge_type='PrePaid'):
    if disk_charge_type == 'PrePaid':
        charge_type = '包年包月'
    else:
        charge_type = '按量付费'

    modify_disk_chargetype = ModifyDiskChargeTypeRequest()
    modify_disk_chargetype.set_DiskIds(disk_id_list)
    modify_disk_chargetype.set_InstanceId(instance_info[1])
    modify_disk_chargetype.add_query_param('RegionId', instance_info[2])
    modify_disk_chargetype.set_DiskChargeType(disk_charge_type)
    response = baseInfo.send_request(modify_disk_chargetype)
    baseInfo.logger.info("更改付费类型结果：%s", response)
    if response is not None:
        baseInfo.logger.info("磁盘 %s 更改磁盘付费类型成功：%s", disk_id_list, charge_type)
        response['status'] = 1
        response_json = json.dumps(response)
        return response_json
    else:
        response = {}
        response['status'] = 0
        response_json = json.dumps(response)
        return response_json


# 挂载磁盘到实例
def attachDisk(instanceId, diskId):
    attachDiskRequest = AttachDiskRequest()
    attachDiskRequest.set_InstanceId(instanceId)
    attachDiskRequest.set_DiskId(diskId)
    response = baseInfo.send_request(attachDiskRequest)
    if response is not None:
        baseInfo.logger.info("向实例 %s 挂载磁盘 %s 成功!", instanceId, diskId)
        response['status'] = 1
        response_json = json.dumps(response)
        return response_json
    else:
        response = {}
        response['status'] = 0
        response_json = json.dumps(response)
        return response_json


# 通过ssh远程获取disk列表
def get_disk_list(ssh_result):
    disk_list = []
    for x in ssh_result[1].readlines():
        if x.find('Disk /dev') != -1:
            # print(x, end='')
            disk_list.append(x.split(':')[0].split()[1])
    return disk_list


if __name__ == '__main__':
    baseInfo.logger.info("Create & attach Disk!")
    instanceInfo = getInstanceInfo.get_special_instance('l-test-xufeng1.ops.dev.ali.dm', 'cn-beijing')
    #result = ('l-test-xufeng1.ops.dev.ali.dm', 'i-2zea6ctqde8i2jx5v84z', 'cn-beijing', 'cn-beijing-c')
    # 多个磁盘创建并挂载
    disk_num = 1
    for i in range(disk_num):
        createDiskResult = createDisk(instanceInfo, 100, 'cloud_efficiency')
        # 创建磁盘成功，则挂载磁盘
        if json.loads(createDiskResult).get('status') == 1:
            attachDisk(instanceInfo[1], json.loads(createDiskResult).get('DiskId'))
            # 将磁盘ID转化成list
            disk_list = json.loads(createDiskResult).get('DiskId').split(',')
            # 等待10s，等待挂盘操作
            time.sleep(10)
            #modify_result = modify_disk_charge_type(disk_list, instanceInfo)
        else:
            baseInfo.logger.error("磁盘创建失败。")

