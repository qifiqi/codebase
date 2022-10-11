package base

object WordCount {

  def wordCountExercise(): Unit = {
    val word1 = List(
      "hello word","hello Hadoop","hello java","java","hello sb","hello word","hello word","hello python"
    )
//    var aa = word1.flatMap(_.split(" ")).groupBy(w=>w).map(kv=>{(kv._1,kv._2.length)}).toList.sortWith(_._2>_._2)
//    aa.take(3).foreach(kv=>println(kv._1,kv._2))
      word1.flatMap(_.split(" ")).groupBy(w=>w).map(kv=>{(kv._1,kv._2.length)}).toList.sortWith(_._2>_._2).take(3).foreach(kv=>println(kv._1,kv._2))

  }


  def main(args: Array[String]): Unit = {
    wordCountExercise()
  }

}
