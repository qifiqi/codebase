package com.lz

object ScalaTuple {


  def main(args: Array[String]): Unit = {
    val arr1 = Array(1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1)
    val arr2 = Array("Asdf", "Ddds", "ssdf", "ssss", "ssdfff", "cccc", "eeee", "qqqqq")
    val tuple2 = arr1.zip(arr2)
    println(tuple2.mkString(","))
  }


}
