package test_1

import org.apache.spark.{SparkConf, SparkContext}

object topic_A {


  def main(args: Array[String]): Unit = {
    //    创建环境
    var sparkConf = new SparkConf().setMaster("local[*]").setAppName("Topic_A")
    var sc = new SparkContext(sparkConf)
    //    读取文件
    val data = sc.textFile("data/loudi_weather.csv")
    //     去取出温度和日期
    val map_data = data.map(line => {
      val data = line.split(",")
      (data(0), data(1))
    })
    //    获得最高温最低温
    val temperature_Data = map_data.mapValues(line => {
      val data = line.split("/")
      (data(0).dropRight(1), data(1).dropRight(1))
    })

    //    过滤掉小于0的温度
    val filterSortData = temperature_Data.filter(_._2._2.toInt < 0).sortBy(_._2._2, ascending = false)
    filterSortData.collect().foreach(println)


  }


}
