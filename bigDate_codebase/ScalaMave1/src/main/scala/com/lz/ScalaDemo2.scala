package com.lz

object ScalaDemo2 {

  def jc(num:Int): Int ={
    var jc:Int = 1
    for (i<-1 to num) {
      jc *=i
    }
    return jc

  }
  def main(args: Array[String]): Unit = {
    println(jc(10))


  }

}
