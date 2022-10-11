package com.lz

object ScalaOperation {




  def Operation(fun:(Int,Int)=>Int,numA:Int,numB:Int):Int ={
    fun(numA,numB)
  }

  def main(args: Array[String]): Unit = {
    val sum = (a: Int, b: Int) => a + b
    val sub = (a: Int, b: Int) => a - b
    val mul = (a: Int, b: Int) => a * b
    val div = (a: Int, b: Int) => a / b

    println(Operation(sum,8,2))
    println(Operation(sub,8,2))
    println(Operation(mul,8,2))
    println(Operation(div,8,2))
    println(Operation(_+_,8,2))
    println(Operation(_-_,8,2))
    println(Operation(_*_,8,2))
    println(Operation(_/_,8,2))

  }

}
