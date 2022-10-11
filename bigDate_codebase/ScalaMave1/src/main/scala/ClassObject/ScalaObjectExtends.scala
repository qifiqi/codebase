package ClassObject

class ScalaObjectExtends {

}

class yi{
  private val name="鹰"
  var types = "鹰科"
  def typeShow(): Unit ={
    println(s"我是$types 动物")
  }
}

class banj extends yi{
   val name="sb"
}

object test{

  def main(args: Array[String]): Unit = {
    var banj = new banj()
    banj.typeShow()
  }
}

