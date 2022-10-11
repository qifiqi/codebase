package ClassObject

class ScalaClass {
  var name:String ="db"
  var age:Int = 15
  def printMe():Unit={println(s"$name,$age")}


}

object text{

  def main(args: Array[String]): Unit = {
    val aa = new ScalaClass()
    aa.printMe()
  }
}
