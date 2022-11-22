import org.apache.spark.{SparkConf, SparkContext}

object topic_A {

  def main(args: Array[String]): Unit = {
    //    创建环境
    val SparkConf = new SparkConf().setMaster("local[*]").setAppName("RDD")

    val sc = new SparkContext(SparkConf)

    //读取
    val rdd = sc.textFile("data/loudi_weather.csv")

    //    3.分割出日期和温度
    val map_rdd = rdd.map(line => {
      val data = line.split(",")
      (data(0), data(1)) // 0是日期,1是温度
    })

    // 4.取出最高温和最低温
    val wendu_rdd = map_rdd.mapValues(str => {
      val data = str.split("/")
      (data(0).dropRight(1), data(1).dropRight(1)) // 从右侧去除27℃,15℃-> 27,15

    })
    //    过滤出零下的温度和日期
    val filter_Rdd = wendu_rdd.filter(line => {
      line._2._2.toInt < 0
    })
    //    按照最低温度排序,降序排序
    val reustl = filter_Rdd.sortBy(_._2._2, ascending = false)

    reustl.collect().foreach(println)
  }


}
