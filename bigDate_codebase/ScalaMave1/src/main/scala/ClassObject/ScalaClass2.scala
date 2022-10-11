package ClassObject

class ScalaClass2(val num1: Int, val num2: Int, val f: String) {
  def aa(): Unit = {
//    this(num1, num2, f)
    if (f == "+") {
      println(s"$num1$f$num2=" + (num1 + num2))
    } else if (f == "-") {
      println(s"$num1$f$num2=" + (num1 - num2))
    } else if (f == "/") {
      println(s"$num1$f$num2=" + (num1 / num2))
    } else if (f == "*") {
      println(s"$num1$f$num2=" + (num1 * num2))
    } else {
      println("没有哦")
    }
  }
}

object ScalaClass2 {
  def main(args: Array[String]): Unit = {
    new ScalaClass2(10, 5, "+").aa()
    new ScalaClass2(10, 5, "-").aa()
    new ScalaClass2(10, 5, "/").aa()
    new ScalaClass2(10, 5, "*").aa()

  }
}
