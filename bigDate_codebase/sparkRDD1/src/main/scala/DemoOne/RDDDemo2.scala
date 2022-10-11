package DemoOne

import org.apache.spark.rdd.RDD
import org.apache.spark.{SparkConf, SparkContext}

object RDDDemo2 {

  def main(args: Array[String]): Unit = {
    val sparkConf = new SparkConf()
      .setMaster("local[*]")
      .setAppName("SparkRDD")


    //    创建spark上下文对象
    val sc = new SparkContext(sparkConf)

    val aa: RDD[String] = sc.textFile("data/aa.txt")
    val cc = aa.collect()
    cc.flatMap(_.split(" ")).groupBy(m=>m).map(kv=>{(kv._1,kv._2.length)}).toList.sortWith(_._2>_._2).foreach(println)

    sc.stop()


  }

}
