package DemoOne

import org.apache.spark.rdd.RDD
import org.apache.spark.{SparkConf, SparkContext}

object RDDDemo3 {

  def main(args: Array[String]): Unit = {
    System.setProperty("hadoop.home.dir","E:\\modlue\\hadoop-2.7.3\\bin\\winutils.exe")
    val sparkConf = new SparkConf()
      .setMaster("local[*]")
      .setAppName("SparkRDD")


    //    创建spark上下文对象
    val sc = new SparkContext(sparkConf)

    val aa = sc.wholeTextFiles("hdfs://hadoop102:9870/aa.txt")
    aa.collect().foreach(println)

    sc.stop()


  }

}
