import org.apache.spark.{SparkConf, SparkContext}

object RddDemo1 {


  def main(args: Array[String]): Unit = {
    //    1.搭建环境
    val sparkConf = new SparkConf()
      .setMaster("local[*]") // 创建环境,local表示本地环境 * 表示线程数没有就是单线程,这里是最大
      .setAppName("RDD") // 自己这个app 的名字
//    创建上下文集合
    val sc = new SparkContext(sparkConf)
    // 3. 使用集合创建RDD
    val rdd  = sc.parallelize(List(1,2,3,4,5,6,7,8))
    val rdd1  = sc.makeRDD(Array(1,2,3,4,8))
//      输出rdd中的数据
    rdd.collect().foreach(println)
    rdd1.collect().foreach(println)
//    关闭
    sc.stop()

  }




}
