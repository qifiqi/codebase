package com.lz

object LianXI {
  def incr(arr:Array[Int],in:Int=>Int):Array[Int]={
    //for循环遍历数据传到in匿名中加一并返回
    for (a<-arr) yield in(a)

  }


  def main(args: Array[String]): Unit = {
    val arrSum:Array[Int] = incr(arr = Array[Int](2, 23, 55, 43, 2, 34, 23, 44, 234), _ + 1)
    val arrSub:Array[Int] = incr(arr = Array[Int](2, 23, 55, 43, 2, 34, 23, 44, 234), _ * 2)
    println(arrSum.mkString(sep = ","))
    println(arrSub.mkString(sep = ","))
  }
}
