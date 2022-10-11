package com.lz

import scala.io.StdIn

object ScalaDemo1 {

  def gg_dd(): Unit = {


    var sum = 1
    while (true) {
      val a = scala.util.Random.nextInt(100)
      println("请输入一个数字")
      val sc = StdIn.readInt()

      if (sc > a) {
        println("您输入的数字大于随机数")
        println("您猜测" + sum + "次")
      } else if (sc < a) {
        println("您输入的数字小于随机数")
        println("您猜测" + sum + "次")
      } else {
        println("您输入的等于随机数")
        println("您猜测" + sum + "次")
        return
      }


      sum = sum + 1
    }


  }

  def times_table(): Unit = {
    for (i <- 1 to 9; j <- 1 to i) {
      print(i + "" + "*" + j + "=" + i * j + " ")

      if (i == j) {
        println()

      }

    }
  }

  def aa(): Unit = {
//    for (i <- 1 to (9)) {
//      for (j <- 1 to (9 - i)) {
//        print(" ")
//
//      }
//      for (k <- 1 to (2 * i - 1)) {
//        print("*")
//      }
//      println()
//    }
    for (i<-1 to 9){
      val a = 9 - i
      val b = 2 * i - 1
      println(" "*a+"*"*b)
    }
    for (i<- 1 to 8 reverse){
      val a = 9 - i
      val b = 2 * i - 1
      println(" "*a+"*"*b)
    }


    for (i<-1 to 9){
      val a = 9 - i
      val b = 2 * i - 1
      println(" "*a+"*"*b)
    }
    for (i<- 8 to 1 by -1){
      val a = 9 - i
      val b = 2 * i - 1
      println(" "*a+"*"*b)
    }






  }

  def main(args: Array[String]): Unit = {
    //    gg_dd()
    times_table()
    aa()

  }

}