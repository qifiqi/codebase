package ClassObject

class Bird(val color:String,val bread:String) {
  def fiy(): Unit ={println(s"一只"+color+"的"+bread+"在飞")}
}

class BirdDemo(color:String,bread:String) extends Bird(color, bread){
  def jiao(): Unit ={println(s"一只"+color+"的"+bread+"在叫")}
}

object BirdDemo{
  def main(args: Array[String]): Unit = {
    val bird = new BirdDemo("黑色","老鹰")
    bird.fiy()
    bird.jiao()
  }
}


