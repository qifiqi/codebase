package DemoOne

import org.apache.spark.rdd.RDD
import org.apache.spark.{SparkConf, SparkContext}

object RDDDemo1 {


  def main(args: Array[String]): Unit = {
//    准备环境
    val sparkConf = new SparkConf()
      .setMaster("local[*]")
      .setAppName("SparkRDD")

    val list1 = List(1,2,3,4,5,6,7,8,9)

//    创建spark上下文对象
    val sc = new SparkContext(sparkConf)
//    创建Rdd,数据来自集合
    var rdd1:RDD[Int] = sc.makeRDD(list1)

//    输出RDD中的内容
    rdd1.collect().foreach(println)

//    关闭环境
    sc.stop()

  }


}
