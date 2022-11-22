package test_1

import org.apache.spark.{SparkConf, SparkContext}

object Topic_B {

  def main(args: Array[String]): Unit = {
    val sparkConf = new SparkConf().setMaster("local[*]").setAppName("Topic_B")
    val sc = new SparkContext(sparkConf)

    val data = sc.textFile("data/query.log")

    //    处理数据 ,不要-
    val url = data.map(_.split("\"")(3)).filter(_.equals("-") == false)
    //    找到数据
    val q_data = url.map(_.split("\\?")(1).split("=")(1)).map((_, 1))
    //    分组求和
    val result = q_data.reduceByKey(_ + _).sortBy(_._2).take(5)
    result.foreach(println)
    sc.stop()


  }


}
