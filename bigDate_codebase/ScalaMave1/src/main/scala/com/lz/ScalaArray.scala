package com.lz
import scala.collection.mutable.ArrayBuffer
object ScalaArray {


  def main(args: Array[String]): Unit = {
    val arr1 = new Array[Int](10)
    val arr2 = Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    println(arr1.mkString(","),arr2.mkString(","))

    val bufArr = ArrayBuffer(123, 10)

    bufArr+=12
    println(bufArr.mkString(","))
    bufArr.insert(0,11)
    println(bufArr.mkString(","))


  }



}
