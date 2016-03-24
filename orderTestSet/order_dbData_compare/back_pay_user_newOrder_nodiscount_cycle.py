# -*- coding:utf-8 -*-
import orderTestSet.utils.db_operate as mysql_db
import json
def getDiffData():
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')
    result_txt_name='result_order_create'
    with open(result_txt_name, 'ab+') as result:
        result.truncate()
    with open("1.txt") as f:
        try:
            input_data=json.loads(f.read())
            for data in input_data:
                for i in range(0,data["table_nums"],1):
                    #获取表名
                    table_names=data["table_name"].split(',')
                    if len(table_names)==1:
                        table_name=table_names[0]
                    else:
                        table_name=table_names[i]
                    #获取查询主键Id
                    table_search_id_names=data["table_search_id_name"].split(',')
                    if len(table_search_id_names)==1:
                        table_search_id_name=table_search_id_names[0]
                    else:
                        table_search_id_name=table_search_id_names[i]
                    #获取新库查询主键Id值
                    new_table_search_id_values=data["new_table_search_id_value"].split(',')
                    if len(new_table_search_id_values)==1:
                        new_table_search_id_value=new_table_search_id_values[0]
                    else:
                        new_table_search_id_value=new_table_search_id_values[i]
                    #获取旧库查询主键Id值
                    old_table_search_id_values=data["old_table_search_id_value"].split(',')
                    if len(old_table_search_id_values)==1:
                        old_table_search_id_value=old_table_search_id_values[0]
                    else:
                        old_table_search_id_value=old_table_search_id_values[i]

                    sqltext1="select *  from %s where %s='%s'"%(table_name,table_search_id_name,new_table_search_id_value)
                    sqltext2="select *  from %s where %s='%s'"%(table_name,table_search_id_name,old_table_search_id_value)
                    #获取查询结果主键Id
                    result_primary_keys=data["result_primary_key"].split(',')
                    if len(result_primary_keys)==1:
                        result_primary_key=result_primary_keys[0]
                    else:
                        result_primary_key=result_primary_keys[i]
                    print table_name,sqltext1,sqltext2,result_primary_key,data["new_db_name"],data["old_db_name"]
                    mysql_db.getDiffData(result_txt_name,table_name,sqltext1,sqltext2,primary_key=result_primary_key,db1=data["new_db_name"],db2=data["old_db_name"])
        except Exception as  ex:
            print ex.message

if __name__=="__main__":
    getDiffData()