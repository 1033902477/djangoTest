# !/usr/bin/env python3
# _*_ coding=utf-8 _*_
# author: liuqing
# dateTime: 2021/3/7 14:14

class Comparison:

    def valueCheck(self, actualValues: dict, expectValues: dict):
        #  取预期中的一个值
        try:
            for key in expectValues:
                print('key:', key)
                # 判断key所对应的value是否为字典
                if isinstance(expectValues[key], dict):
                    # 如果最后字典是一个空，则返回False
                    if Comparison().valueCheck(expectValues=expectValues[key], actualValues=actualValues[key]) is False:
                        return False
                # 判断key所对应的value是否为列表
                elif isinstance(expectValues[key], list):
                    # 枚举出列表中数据的索引与值
                    for expectListIndex, expectListValues in enumerate(expectValues[key]):
                        for actualListIndex, actualListValues in enumerate(actualValues[key]):
                            # 如实这个期望的值时一个列表的形式，则直接进行对比
                            if expectListIndex == actualListIndex:
                                if isinstance(expectListValues, list):
                                    if str(expectValues[key][expectListIndex]) == str(actualValues[key][actualListIndex]):
                                        break
                                    else:
                                        return Exception('expectValues != actualValues'+ str(expectValues[key]) + str(actualValues))
                                elif isinstance(expectListValues, dict):
                                    # 进入递归
                                    Comparison().valueCheck(expectValues=expectValues[key][expectListIndex], actualValues=actualValues[key][actualListIndex])
                                else:
                                    # 如果不是列表或者其他，可以直接进行对比
                                    if str(expectValues[key][expectListIndex]) == str(actualValues[key][actualListIndex]):
                                        break
                                    else:
                                        return Exception('expectValues != actualValues'+ str(expectValues[key]) + str(actualValues))
                else:
                    if expectValues[key] == actualValues[key]:
                        continue
                    else:
                        return Exception('expectValues != actualValues'+ str(expectValues[key]) + str(actualValues))
            return 0
        except KeyError as e:
            print(e)
            return 1

        except Exception as e:
            print(e)
            return 1