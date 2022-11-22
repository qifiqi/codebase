import org.apache.spark.rdd.RDD
import org.apache.spark.{SparkConf, SparkContext}

object topic_B {

  def main(args: Array[String]): Unit = {
    val SparkConf = new SparkConf().setMaster("local[*]").setAppName("RDD")

    val sc = new SparkContext(SparkConf)

    //读取
    val rdd = sc.textFile("data/query.log")

    //转换格式
    val url_rdd = rdd.map(_.split("\"")(3))

    //过滤-符
    val heng_url = url_rdd.filter(_.equals("-")==false)

    //分割
    val fenge_url = heng_url.map(l=>l.split("\\?")(1))

    //得出关键字
    val gu_url = fenge_url.map(_.split("=")(1))

    //计数
    val ji_url = gu_url.map(d=>(d,1))


    val jl=ji_url.reduceByKey(_+_)
      .sortBy(_._2,ascending = false)
      .take(5)
    jl.foreach(println)


    //    ji_url.foreach(println)
    sc.stop()


  }

}
