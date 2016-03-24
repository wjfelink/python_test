__author__ = 'user'
# -*- coding:utf-8 -*-
import PyMysql_db as sqldb
import timeDate
#result_master_order_create
def getDiffData(result_txt_name,table_name,sqltext1,sqltext2,primary_key='',db1='portal_0224',db2='portal_0304'):
    #table_name="master_order"
    #sqltext = "select *  from master_order where master_order_no='20160324104026882095'"
    data = sqldb.getDbData(db=db1,sqltext=sqltext1)
    #sqltext = "select *  from master_order where master_order_no='20160324104026477003'"
    data2 = sqldb.getDbData(db=db2, sqltext=sqltext2)
    print data
    print data2
    with open(result_txt_name, 'ab+') as result:
        #result.truncate()
        result.write("---------------%s---------------\n"%table_name)
        try:
            for order in data:
                if primary_key != "null":
                    primary_key_value = order[primary_key]
                else:
                    primary_key_value = "null"
                for key in order:
                    for order2 in data2:
                        if primary_key_value != "null":
                            primary_key_value2=order2[primary_key]
                            if primary_key_value!=primary_key_value2:
                                continue;
                        for key2 in order2:
                            if key == key2:
                                if (order[key] == order2[key2]):
                                    break
                                else:
                                    print "%s %s %s-%s:%s"%(timeDate.getCurrentDateTime(),db1,table_name,key,order[key])
                                    print "%s %s %s-%s:%s"%(timeDate.getCurrentDateTime(),db2,table_name,key2,order2[key2])
                                    result.write(u"%s %s-%s:  %s %s" % (timeDate.getCurrentDateTime(),db1,table_name,key, order[key]), )
                                    result.write(u"\n%s %s-%s:  %s %s\n" % (timeDate.getCurrentDateTime(),db2,table_name,key2, order2[key2]))
                print "\n"
                result.write(u"\n")
        except Exception as ex:
            print "error",ex.message
        finally:
            result.close()
# if __name__ == '__main__':
#     table_name="order_item"
#     sqltext1="select *  from order_item where fk_master_order_id='47e35de732534ee9846926090230be07'"
#     sqltext2="select *  from order_item where fk_master_order_id='7cee403643714c41b10c96be0ff6fec3'"
#     primary_key="FK_sales_entry_id"
#     getDiffData(table_name,sqltext1,sqltext2,primary_key)